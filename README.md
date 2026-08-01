# Eddo Community Skills

Reusable instructional expertise, packaged as agent skills and plugins.

## Install the community marketplace

In the Codex marketplace UI, add this GitHub source URL:

`https://github.com/eddo-ai/eddo-skills`

Codex will load the repo marketplace from `.agents/plugins/marketplace.json`. Install **OpenSciEd Educator** for the complete public role or **Pacing Coach** for pacing alone.

The equivalent CLI route is:

```sh
codex plugin marketplace add https://github.com/eddo-ai/eddo-skills --ref main
codex plugin add eddo-openscied-educator@eddo-skills
```

Start a new task after installation so the skill is available.

## Available roles

### OpenSciEd Educator

OpenSciEd Educator combines Pacing Coach with the public, read-only OpenSciEd Resource Finder. It supports focused teacher requests for exact resources and lessons, remembered activities, materials and lab preparation, summaries, DQB and discussion preparation, differentiation, substitute and first-year support, terminology, assessment and rubric guidance, and faithful student-instruction rewrites.

Curriculum claims require stable archive citations and verified, shareable public OpenSciEd source pages. The skill never exposes private Drive identifiers, local paths, index internals, or other non-public archive inputs.

### Pacing Coach

Pacing Coach packages Val's complete four-phase OpenSciEd pacing workflow. It helps teachers and instructional leaders:

- Count real instructional days
- Sketch unit durations from source guidance
- Map units onto a school calendar
- Deep-dive Unit 1 while protecting inquiry and sensemaking

The plugin is self-contained and has no MCP or hosted-service dependency. Its complete source lives at `plugins/pacing-coach`.

## Legacy OpenSciEd pack

The previously published `openscied` beta is retained as `NOT_AVAILABLE` so its identity and source history remain explicit. `eddo-openscied-educator` is its role-based, release-validated replacement.

## Release policy

- Treat `main` as the published release channel.
- List only mature plugins as `AVAILABLE`.
- Develop new skills and packs on feature branches until they are ready to publish.
- Preserve or explicitly mark previously published packages unavailable instead of silently deleting them.

## Add a new skill

Canonical skill source lives under `skills/<skill-name>`. Role membership is declared in `catalog/roles.json`; run `python3 scripts/package_plugins.py` to build self-contained plugin copies. Add the plugin to `.agents/plugins/marketplace.json`, keep new entries unavailable until verified, and keep the root compatibility mirror synchronized.
