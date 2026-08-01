#!/usr/bin/env python3
"""Build or verify self-contained role plugin skill bundles."""

from __future__ import annotations

import argparse
import filecmp
import json
import shutil
from pathlib import Path


IGNORED_NAMES = {".DS_Store", "__pycache__"}


def ignored(_path: str, names: list[str]) -> set[str]:
    return {name for name in names if name in IGNORED_NAMES or name.endswith(".pyc")}


def directories_match(source: Path, packaged: Path) -> bool:
    if not packaged.is_dir():
        return False
    comparison = filecmp.dircmp(source, packaged, ignore=list(IGNORED_NAMES))
    if comparison.left_only or comparison.right_only or comparison.funny_files:
        return False
    for filename in comparison.common_files:
        if filename.endswith(".pyc"):
            continue
        if not filecmp.cmp(source / filename, packaged / filename, shallow=False):
            return False
    return all(
        directories_match(source / child, packaged / child)
        for child in comparison.common_dirs
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    config = json.loads((root / "catalog" / "roles.json").read_text())
    source_root = root / config.get("sourceRoot", "skills")
    failures: list[str] = []

    for plugin_name, plugin_config in config["plugins"].items():
        target_root = root / "plugins" / plugin_name / "skills"
        if args.check:
            for skill_name in plugin_config["skills"]:
                if not directories_match(
                    source_root / skill_name, target_root / skill_name
                ):
                    failures.append(f"{plugin_name}: stale {skill_name}")
            packaged_names = {
                path.name for path in target_root.iterdir() if path.is_dir()
            } if target_root.is_dir() else set()
            expected_names = set(plugin_config["skills"])
            for extra in sorted(packaged_names - expected_names):
                failures.append(f"{plugin_name}: unexpected {extra}")
            continue

        if target_root.exists():
            shutil.rmtree(target_root)
        target_root.mkdir(parents=True)
        for skill_name in plugin_config["skills"]:
            source = source_root / skill_name
            if not (source / "SKILL.md").is_file():
                raise SystemExit(f"Missing canonical skill: {source}")
            shutil.copytree(source, target_root / skill_name, ignore=ignored)

    if failures:
        print("\n".join(failures))
        return 1
    print("Plugin skill packages are current.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
