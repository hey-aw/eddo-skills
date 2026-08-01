# Eddo Instructional Skills

Reusable instructional expertise, packaged as agent skills and plugins.

## Install Pacing Coach

In the Codex marketplace UI, add this GitHub source URL:

`https://github.com/hey-aw/eddo-skills`

Codex will load the repo marketplace from `.agents/plugins/marketplace.json`. Choose **Eddo Instructional Skills**, then install **Pacing Coach**.

The equivalent CLI route is:

```sh
codex plugin marketplace add https://github.com/hey-aw/eddo-skills --ref main
codex plugin add pacing-coach@eddo-skills
```

Start a new task after installation so the skill is available.

## Available now

### Pacing Coach

Pacing Coach packages Val's complete four-phase OpenSciEd pacing workflow. It helps teachers and instructional leaders:

- Count real instructional days
- Sketch unit durations from source guidance
- Map units onto a school calendar
- Deep-dive Unit 1 while protecting inquiry and sensemaking

The plugin is self-contained and has no MCP or hosted-service dependency. Its complete source lives at `plugins/pacing-coach`.

## OpenSciEd pack status

The previously published `openscied` beta combined Pacing Coach with an MCP-backed Resource Finder. Its marketplace entry is retained as `NOT_AVAILABLE` so the published identity and source history remain explicit, but it is not currently offered for installation from `main`.

The beta source remains under `plugins/openscied` while Resource Finder continues on a feature branch. The pack can return to `AVAILABLE` after both Pacing Coach and Resource Finder are release-ready and verified together.

## Release policy

- Treat `main` as the published release channel.
- List only mature plugins as `AVAILABLE`.
- Develop new skills and packs on feature branches until they are ready to publish.
- Preserve or explicitly mark previously published packages unavailable instead of silently deleting them.

## Add a new skill

Each skill lives in its own `plugins/<skill-name>` directory and includes a `.codex-plugin/plugin.json` manifest plus its `skills/` content. Add the new plugin to the canonical `.agents/plugins/marketplace.json` catalog to make it installable from the repository URL. Keep the root `marketplace.json` compatibility mirror synchronized.
