# Eddo Instructional Skills

Reusable instructional expertise, packaged as agent skills and plugins.

## Install the collection

Add `https://github.com/hey-aw/eddo-skills` as a plugin marketplace in Codex, then install a plugin listed in `marketplace.json`. Start a new task after installation so its skills and tools are available.

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

Each skill lives in its own `plugins/<skill-name>` directory and includes a `.codex-plugin/plugin.json` manifest plus its `skills/` content. Add the new plugin to `marketplace.json` to make it discoverable.
