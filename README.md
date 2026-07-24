# Eddo Instructional Skills

Reusable instructional expertise, packaged as agent skills and plugins.

## Install the collection

Add this repository as a plugin marketplace in an agent that supports Codex-style plugin marketplaces, then install any skill listed in `marketplace.json`.

## Included skills

### Pacing Coach

Val's four-phase OpenSciEd pacing workshop. It helps teachers and instructional leaders count real instructional days, estimate and map units, and create a practical Unit 1 plan that protects inquiry and sensemaking.

The complete source lives at `plugins/pacing-coach`.

## Add a new skill

Each skill lives in its own `plugins/<skill-name>` directory and includes a `.codex-plugin/plugin.json` manifest plus its `skills/` content. Add the new plugin to `marketplace.json` to make it discoverable.
