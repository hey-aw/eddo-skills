#!/usr/bin/env python3
"""Generate client adapters from the platform-neutral Eddo skill catalog."""

from __future__ import annotations

import argparse
import json
import shutil
import tempfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
GENERATED_ROOTS = (
    Path("adapters/codex"),
    Path("adapters/claude"),
    Path("adapters/cursor"),
    Path("plugins"),
)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def copy_skill(source: Path, destination: Path) -> None:
    shutil.copytree(source, destination)


def mcp_config(service: dict[str, Any]) -> dict[str, Any]:
    service_id = service["id"]
    url_env = service["transport"]["urlEnvironmentVariable"]
    token_env = service["authentication"]["tokenEnvironmentVariable"]
    return {
        "mcpServers": {
            service_id: {
                "type": "http",
                "url": f"${{{url_env}}}",
                "headers": {"Authorization": f"Bearer ${{{token_env}}}"},
            }
        }
    }


def plugin_manifest(skill: dict[str, Any], has_service: bool) -> dict[str, Any]:
    manifest: dict[str, Any] = {
        "name": skill["name"],
        "version": "0.1.0",
        "description": skill["description"],
        "author": {"name": skill["author"]},
        "skills": "./skills/",
        "interface": {
            "displayName": skill["displayName"],
            "shortDescription": skill["shortDescription"],
            "longDescription": skill["longDescription"],
            "developerName": skill["author"],
            "category": skill["category"],
            "capabilities": skill["capabilities"],
            "defaultPrompt": skill["defaultPrompt"],
        },
    }
    if has_service:
        manifest["mcpServers"] = "./.mcp.json"
    return manifest


def generate_into(root: Path) -> None:
    catalog = load_json(ROOT / "catalog.json")
    services = {
        item["id"]: load_json(ROOT / item["manifest"])
        for item in catalog.get("services", [])
    }

    for generated_root in GENERATED_ROOTS:
        (root / generated_root).mkdir(parents=True, exist_ok=True)

    for skill in catalog["skills"]:
        name = skill["name"]
        canonical = ROOT / skill["path"]
        service = services.get(skill.get("service"))

        for base in (Path("adapters/codex"), Path("plugins")):
            plugin_root = root / base / name
            copy_skill(canonical, plugin_root / "skills" / name)
            write_json(
                plugin_root / ".codex-plugin" / "plugin.json",
                plugin_manifest(skill, service is not None),
            )
            if service:
                write_json(plugin_root / ".mcp.json", mcp_config(service))

        claude_root = root / "adapters/claude" / name
        copy_skill(canonical, claude_root / "skills" / name)
        if service:
            write_json(claude_root / ".mcp.json", mcp_config(service))

        cursor_root = root / "adapters/cursor" / name
        copy_skill(canonical, cursor_root / "skills" / name)
        if service:
            write_json(cursor_root / ".cursor" / "mcp.json", mcp_config(service))


def compare_trees(expected: Path, actual: Path) -> list[str]:
    problems: list[str] = []
    for generated_root in GENERATED_ROOTS:
        expected_root = expected / generated_root
        actual_root = actual / generated_root
        expected_files = {
            path.relative_to(expected_root)
            for path in expected_root.rglob("*")
            if path.is_file()
        }
        actual_files = {
            path.relative_to(actual_root)
            for path in actual_root.rglob("*")
            if path.is_file()
        }
        for path in sorted(expected_files - actual_files):
            problems.append(f"missing generated file: {generated_root / path}")
        for path in sorted(actual_files - expected_files):
            problems.append(f"unexpected generated file: {generated_root / path}")
        for path in sorted(expected_files & actual_files):
            if (expected_root / path).read_bytes() != (actual_root / path).read_bytes():
                problems.append(f"stale generated file: {generated_root / path}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check committed adapters without changing them.",
    )
    args = parser.parse_args()

    if args.check:
        with tempfile.TemporaryDirectory() as directory:
            expected = Path(directory)
            generate_into(expected)
            problems = compare_trees(expected, ROOT)
        if problems:
            print("\n".join(problems))
            return 1
        print("Generated adapters are current.")
        return 0

    for generated_root in GENERATED_ROOTS:
        target = ROOT / generated_root
        if target.exists():
            shutil.rmtree(target)
    generate_into(ROOT)
    print("Generated Codex, Claude, Cursor, and compatibility adapters.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
