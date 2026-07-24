#!/usr/bin/env python3
"""Validate canonical skills, service manifests, and generated adapters."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED_TOOLS = {
    "list_curriculum",
    "search_materials",
    "read_material",
    "get_index_status",
}


def load_json(path: Path, errors: list[str]) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"{path.relative_to(ROOT)}: {error}")
        return {}


def frontmatter_name(path: Path, errors: list[str]) -> str | None:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as error:
        errors.append(f"{path.relative_to(ROOT)}: {error}")
        return None
    match = re.match(r"^---\n(?P<body>.*?)\n---\n", text, re.DOTALL)
    if not match:
        errors.append(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
        return None
    fields = {}
    for line in match.group("body").splitlines():
        key, separator, value = line.partition(":")
        if separator:
            fields[key.strip()] = value.strip()
    if not fields.get("description"):
        errors.append(f"{path.relative_to(ROOT)}: missing description")
    return fields.get("name")


def validate() -> list[str]:
    errors: list[str] = []
    catalog = load_json(ROOT / "catalog.json", errors)
    marketplace = load_json(ROOT / "marketplace.json", errors)
    if not catalog:
        return errors
    if catalog.get("schemaVersion") != 1:
        errors.append("catalog.json: schemaVersion must be 1")

    service_entries = catalog.get("services", [])
    services = {entry.get("id"): entry for entry in service_entries}
    skill_names: set[str] = set()

    for skill in catalog.get("skills", []):
        name = skill.get("name", "")
        if not NAME_PATTERN.fullmatch(name):
            errors.append(f"catalog.json: invalid skill name {name!r}")
        if name in skill_names:
            errors.append(f"catalog.json: duplicate skill {name}")
        skill_names.add(name)
        expected_path = f"skills/{name}"
        if skill.get("path") != expected_path:
            errors.append(f"catalog.json: {name} path must be {expected_path}")
        skill_file = ROOT / expected_path / "SKILL.md"
        if frontmatter_name(skill_file, errors) != name:
            errors.append(f"{skill_file.relative_to(ROOT)}: name must be {name}")
        if skill.get("service") and skill["service"] not in services:
            errors.append(f"catalog.json: {name} references unknown service")
        adapters = set(skill.get("adapters", []))
        if adapters != {"codex", "claude", "cursor"}:
            errors.append(f"catalog.json: {name} must declare all supported adapters")

    for service_id, entry in services.items():
        manifest = load_json(ROOT / entry.get("manifest", ""), errors)
        if manifest.get("id") != service_id:
            errors.append(f"service {service_id}: manifest id mismatch")
        if manifest.get("access") != "read-only":
            errors.append(f"service {service_id}: access must be read-only")
        tool_names = {tool.get("name") for tool in manifest.get("tools", [])}
        if service_id == "openscied-library" and tool_names != REQUIRED_TOOLS:
            errors.append("openscied-library: tool contract differs from required tools")
        security = manifest.get("security", {})
        for forbidden in ("absolutePaths", "arbitraryFileReads", "binaryDownloads", "mutationTools"):
            if security.get(forbidden) is not False:
                errors.append(f"service {service_id}: {forbidden} must be false")

    marketplace_plugins = marketplace.get("plugins", [])
    marketplace_names = [plugin.get("name") for plugin in marketplace_plugins]
    if marketplace_names != [skill["name"] for skill in catalog.get("skills", [])]:
        errors.append("marketplace.json: entries must match catalog skill order")
    for plugin in marketplace_plugins:
        name = plugin.get("name")
        expected_source = f"./adapters/codex/{name}"
        if plugin.get("source", {}).get("path") != expected_source:
            errors.append(f"marketplace.json: {name} must use {expected_source}")
        if not (ROOT / expected_source.removeprefix("./")).is_dir():
            errors.append(f"marketplace.json: source for {name} does not exist")
        policy = plugin.get("policy", {})
        if policy.get("installation") != "AVAILABLE":
            errors.append(f"marketplace.json: {name} must be AVAILABLE")
        if policy.get("authentication") != "ON_INSTALL":
            errors.append(f"marketplace.json: {name} must authenticate ON_INSTALL")

    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts/build_adapters.py"), "--check"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode:
        errors.extend(line for line in result.stdout.splitlines() if line)
        errors.extend(line for line in result.stderr.splitlines() if line)
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print("Catalog, skills, services, and adapters are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
