# Eddo Instructional Skills

Reusable instructional expertise packaged as platform-agnostic Agent Skills.

## Included skills

### Pacing Coach

Val's four-phase OpenSciEd pacing workshop helps teachers and instructional leaders count real instructional days, estimate and map units, and create a practical Unit 1 plan that protects inquiry and sensemaking.

Source: [`skills/pacing-coach`](skills/pacing-coach)

Try:

- Help me count the real instructional days in my school calendar.
- Map my OpenSciEd units across the year.
- Build a practical Unit 1 pacing plan with flex days.

### OpenSciEd Resource Finder

Searches an authenticated, read-only OpenSciEd library; retrieves bounded evidence; and supports grounded comparisons and synthesis with stable citations.

Source: [`skills/openscied-resource-finder`](skills/openscied-resource-finder)

Try:

- Find the teacher materials and slides for Grade 7 Unit 2.
- Compare how two lessons introduce their key models.
- Find assessment evidence for this unit and summarize what it measures.

## Architecture

- `skills/` is the canonical source for every Agent Skill.
- `services/` contains platform-neutral MCP service contracts.
- `adapters/` contains generated host-specific packages.
- `plugins/` remains a generated compatibility path for existing Codex links.
- `catalog.json` describes skills, authors, capabilities, service dependencies, and supported adapters.

The OpenSciEd Resource Finder combines a private filesystem index with a read-only MCP interface. The filesystem approach is efficient for corpus ingestion and deterministic indexing. MCP provides authenticated, typed, bounded access without distributing the corpus or exposing host paths.

## Install

Hosts that implement the Agent Skills convention can consume a directory under `skills/` directly. MCP-capable hosts must also configure services declared by the skill in `catalog.json`.

Codex users can add this repository as a plugin marketplace and install entries from `marketplace.json`. Claude and Cursor adapter packages are generated under their respective `adapters/` directories.

For OpenSciEd Resource Finder, configure:

- `EDDO_OPENSCIED_MCP_URL`: HTTPS endpoint for the deployed service
- `EDDO_OPENSCIED_MCP_TOKEN`: Eddo bearer token

## Contribute

Add canonical content under `skills/<skill-name>/SKILL.md`, register it in `catalog.json`, then run:

```bash
python3 scripts/build_adapters.py
python3 scripts/validate_catalog.py
python3 -m unittest discover -s tests
```

Do not edit generated adapter or compatibility files directly.
