from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_builder():
    spec = importlib.util.spec_from_file_location(
        "build_adapters", ROOT / "scripts" / "build_adapters.py"
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CatalogTests(unittest.TestCase):
    def test_catalog_is_platform_neutral(self) -> None:
        catalog = json.loads((ROOT / "catalog.json").read_text())
        for skill in catalog["skills"]:
            self.assertTrue(skill["path"].startswith("skills/"))
            self.assertNotIn("codex", skill["path"])

    def test_generator_is_deterministic(self) -> None:
        builder = load_builder()
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            builder.generate_into(Path(first))
            builder.generate_into(Path(second))
            self.assertEqual([], builder.compare_trees(Path(first), Path(second)))

    def test_compatibility_plugin_matches_canonical_skill(self) -> None:
        catalog = json.loads((ROOT / "catalog.json").read_text())
        for skill in catalog["skills"]:
            name = skill["name"]
            canonical = ROOT / skill["path"] / "SKILL.md"
            compatibility = ROOT / "plugins" / name / "skills" / name / "SKILL.md"
            self.assertEqual(canonical.read_bytes(), compatibility.read_bytes())

    def test_marketplace_uses_generated_codex_adapters(self) -> None:
        catalog = json.loads((ROOT / "catalog.json").read_text())
        marketplace = json.loads((ROOT / "marketplace.json").read_text())
        self.assertEqual(
            [skill["name"] for skill in catalog["skills"]],
            [plugin["name"] for plugin in marketplace["plugins"]],
        )
        for plugin in marketplace["plugins"]:
            self.assertEqual(
                f"./adapters/codex/{plugin['name']}",
                plugin["source"]["path"],
            )

    def test_service_is_read_only(self) -> None:
        service = json.loads(
            (ROOT / "services" / "openscied-library" / "mcp.json").read_text()
        )
        self.assertEqual("read-only", service["access"])
        self.assertFalse(service["security"]["mutationTools"])
        self.assertEqual(
            {
                "list_curriculum",
                "search_materials",
                "read_material",
                "get_index_status",
            },
            {tool["name"] for tool in service["tools"]},
        )

    def test_validation_command(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/validate_catalog.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
