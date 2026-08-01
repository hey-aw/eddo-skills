# OpenSciEd beta

Status: preserved but not currently available for installation from the `main` marketplace.

This previously published beta combined two complementary educator workflows:

- **Pacing Coach:** Val's complete four-phase process for turning a real school calendar into a practical, adaptable OpenSciEd pacing plan.
- **Resource Finder:** structured grade, unit, lesson, and artifact navigation backed by cited, bounded excerpts from the OpenSciEd curriculum library.

The standalone `pacing-coach` plugin is the current published release.

## Availability

The `openscied` marketplace entry is retained with `policy.installation: NOT_AVAILABLE` to preserve the beta's identity and source history. Resource Finder development continues separately. This pack can return to `AVAILABLE` after both included workflows are release-ready and verified together.

## What the MCP connection does

The plugin connects to:

`https://openscied-library-mcp.vercel.app/mcp`

The preserved beta used a public, anonymous, read-only connection. The package contains no credentials and configures no request headers. Its available operations are limited to:

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
