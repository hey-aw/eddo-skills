# Eddo Instructional Skills

Reusable instructional expertise, packaged as agent skills and plugins.

## Install the collection

In the Codex marketplace UI, add this GitHub source URL:

`https://github.com/hey-aw/eddo-skills`

Codex will load the repo marketplace from `.agents/plugins/marketplace.json`. Choose **Eddo Instructional Skills**, then install **OpenSciEd** (recommended) or **Pacing Coach**.

The equivalent CLI route is:

```sh
codex plugin marketplace add https://github.com/hey-aw/eddo-skills --ref main
codex plugin add openscied@eddo-skills
```

Start a new task after installation so the selected plugin's skills and tools are available.

## Recommended OpenSciEd install

### OpenSciEd

The `openscied` plugin is the default educator installation. It combines:

- Val's complete four-phase Pacing Coach workflow
- OpenSciEd Resource Finder with a preconfigured connection to the public, read-only OpenSciEd Library MCP beta

Resource Finder supports structured grade, unit, lesson, and material navigation; bounded source reads; curriculum citations; and explicit guardrails for teacher control, inquiry, sensemaking, and lesson coherence.

The complete package lives at `plugins/openscied`.

## Standalone install

### Pacing Coach

Install `pacing-coach` separately when you want Val's pacing workflow without the curriculum-library connection. It helps teachers and instructional leaders count real instructional days, estimate and map units, and create a practical Unit 1 plan that protects inquiry and sensemaking.

The complete source lives at `plugins/pacing-coach`.

## Public beta access model

The combined plugin connects anonymously to `https://openscied-library-mcp.vercel.app/mcp`. The service exposes only bounded browse, search, excerpt-read, and index-status operations. The plugin includes no credentials and no write, synchronization, refresh, upload, or publishing capabilities.

## Add a new skill

Each skill lives in its own `plugins/<skill-name>` directory and includes a `.codex-plugin/plugin.json` manifest plus its `skills/` content. Add the new plugin to the canonical `.agents/plugins/marketplace.json` catalog to make it installable from the repository URL. Keep the root `marketplace.json` compatibility mirror synchronized.
