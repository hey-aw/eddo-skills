# OpenSciEd

One installation for two complementary educator workflows:

- **Pacing Coach:** Val's complete four-phase process for turning a real school calendar into a practical, adaptable OpenSciEd pacing plan.
- **Resource Finder:** structured grade, unit, lesson, and artifact navigation backed by cited, bounded excerpts from the OpenSciEd curriculum library.

The original `pacing-coach` plugin remains available as a separate installation for people who only want Val's pacing workflow.

## Install

Add `https://github.com/hey-aw/eddo-skills` as a plugin marketplace in Codex, then install the `openscied` plugin. Start a new task after installation so both skills and the MCP connection are available.

## What the MCP connection does

The plugin connects to:

`https://openscied-library-mcp.vercel.app/mcp`

This is a public, anonymous, read-only beta. The package contains no credentials and configures no request headers. Its available operations are limited to:

- Browse curriculum metadata with optional grade and unit filters
- Search with structured grade, unit, lesson, material-kind, and extension filters
- Read a bounded excerpt by opaque material ID and locator
- Report index version, build time, document count, and failures

The hosted library is a snapshot and may be incomplete. Resource Finder requires citations for curriculum-specific claims, retrieves only the excerpts needed, reports coverage gaps, and never modifies or publishes curriculum content.

## Suggested requests

- "Browse Grade 7 units and help me locate the teacher materials for Unit 2."
- "Find the relevant Grade 6 Unit 1 lesson evidence for this instructional question and cite it."
- "Use Pacing Coach to build a year plan, then check the library for cited Unit 1 context."

## Instructional boundaries

The skills preserve teacher control and distinguish retrieved source evidence from the assistant's synthesis. Any proposed pacing change must name assumptions and tradeoffs. Recommendations should protect inquiry, sensemaking, lesson coherence, and the distinct roles of teacher materials, student materials, assessments, and answer keys.
