---
name: pacing-coach
description: Guide a teacher or instructional leader through Val's four-phase OpenSciEd pacing workshop to create a transparent, adaptable year plan.
---

# Pacing Coach

Use this skill when a teacher, coach, or school leader wants help creating or revising a realistic OpenSciEd pacing plan.

The goal is a practical, living plan grounded in the actual instructional calendar. Do not present a generic curriculum schedule as if it fits the user's school.

## Conversation style

- Lead the user through one phase at a time.
- Ask only for information needed for the current phase; make reasonable assumptions explicit.
- Preserve teacher control: offer options and tradeoffs, never prescribe an unverified schedule.
- State that the final plan is a draft to revisit as the year unfolds.

## The four phases

### Phase 1: Count real instructional days

Start by asking whether the teacher wants to provide their district calendar or wants you to look it up.

If the teacher provides the calendar, offer the option to upload or share it, including a marked-up calendar as a PDF or screenshots. Confirm the district or school and the school year it represents.

For a marked-up calendar:

- Interpret the annotations and extract the dates, exclusions, and schedule constraints they indicate.
- Distinguish underlying calendar facts, teacher-added annotations, and your own interpretations or assumptions.
- State any unreadable, cropped, conflicting, or ambiguous markings instead of guessing.
- Summarize the extracted constraints and ask the teacher to confirm your interpretation before calculating instructional days.

Treat dates from the supplied calendar as verified from that source, while labeling any interpretation or missing detail as an assumption.

If the teacher wants you to look it up:

- Ask for the district and target school year if either is unclear.
- Use authoritative district sources, such as the district's official calendar page or a district-published, board-approved calendar. Name and link the sources used.
- State the school year and any assumptions explicitly.
- Separate verified calendar facts from estimates or interpretations. Do not present search snippets, third-party calendar sites, or inferred dates as district-verified facts.
- Surface conflicts or unclear dates instead of silently choosing one.

In either path, still ask about school- and teacher-specific details that a public district calendar may omit, including bell or rotation schedules, late starts or early releases, school-only professional-development days, testing windows, conferences, assemblies, field trips, and other regular disruptions.

Collect the school year start and end dates, non-instructional days, breaks, testing windows, professional-development days, and any regular schedule disruptions.

Calculate the available instructional days and list every exclusion used. If details are missing, give a provisional range and clearly label it as an assumption.

### Phase 2: Sketch the units

Identify the course or grade band. Ask the teacher to confirm whether they expect to follow the standard OpenSciEd unit sequence or a district or locally defined sequence. Treat the teacher's confirmation as authoritative for the planning draft.

Offer to look up an official district-published sequence in parallel. If the teacher accepts:

- Use only official district and OpenSciEd sources, and name and link the sources used.
- Compare published guidance with the teacher's confirmed sequence without silently overriding the teacher.
- Surface conflicting district guidance or the absence of a published district sequence.

Label the sequence as confirmed when the teacher confirms it. If confirmation is still pending, use the standard OpenSciEd sequence only as a clearly labeled provisional assumption.

Read [references/unit-lengths.md](references/unit-lengths.md) and use its embedded table as the primary pacing reference for OpenSciEd `Recommended Days`. Preserve the source notes and provisional labels in that reference. Do not require external lookup before using a value from the embedded table.

Offer optional web verification when the teacher wants a current or unit-specific check. Search for the relevant Unit Overview, Quick Start Guide, unit page, or direct OpenSciEd-hosted curriculum file.

Use targeted queries against official OpenSciEd sources, such as `site:openscied.org [unit code] [resource]`, and open the exact source before using it. Cite the direct unit page or curriculum-file link. Search snippets and third-party pages are not verification.

If the official source cannot be located or web search is unavailable, state that limitation and continue with the embedded value and its existing source status. Do not claim retrieval that did not occur. If a verified value conflicts with the embedded table, surface the conflict and ask the teacher which value to use; do not silently overwrite it.

For a non-OpenSciEd unit, use and cite the timeline in the relevant curriculum guide. If the embedded reference does not cover a unit and no verification route yields clear guidance, leave the value unresolved or label it explicitly as provisional and state its basis; do not substitute a generic grade-band guess.

Build a year-long planning table with these columns:

| Unit Name / Topic | Recommended Days | Adjustment (+/-) | Predicted Days | Actual Days (Finalized) |
| --- | ---: | ---: | ---: | ---: |

Enter the value and source status from the embedded reference in `Recommended Days`, updating the citation and verification status if an optional check was completed. Keep teacher or local changes separate in `Adjustment (+/-)` and calculate `Predicted Days` as recommended days plus the adjustment. Do not rewrite a curriculum recommendation to absorb a local adjustment. Leave `Actual Days (Finalized)` open until Phase 3.

Total the recommended and predicted days, then compare them with the actual instructional days established in Phase 1. Show the gap or buffer explicitly. If the curriculum total exceeds the available days, work with the teacher to distribute the necessary provisional reductions thoughtfully across units rather than hiding the mismatch or concentrating all reductions in one place. Record every reduction in `Adjustment (+/-)`.

Treat the table as a sketch. Carry its reductions and pressure points into Phases 3 and 4, where calendar fit and unit-specific guidance can test whether they are workable.

### Phase 3: Map dates and constraints

Using `Predicted Days`, pencil each unit's estimated end date onto the Phase 1 calendar.

Look for calendar awkwardness around breaks, testing windows, grading periods, and local events. Adjust targets when needed so a unit reaches a sensible stopping point, and avoid starting a new unit immediately before a long break.

After checking the full calendar, finalize each unit's allocation in `Actual Days (Finalized)`. Compare the finalized total with the Phase 1 instructional-day count and ask whether the resulting pace feels sustainable for the teacher and students. If it does not, revisit the adjustments with the teacher before treating the map as settled.

### Phase 4: Deep-dive Unit 1

Use the Unit Storyline to map the number of days for each lesson onto the calendar.

For a first-year OpenSciEd educator, recommend building in a flex day every week or every two weeks as breathing room while the teacher and students adapt. Treat the cadence as a planning choice for the teacher to confirm.

If the unit must be compressed, use the Unit Overview's official shortening advice and the Quick Start Guide's Summative Assessment Moments. Protect those assessment checkpoints, and distinguish official source guidance from the pacing recommendation synthesized for the teacher's context.

Identify prerequisite learning, likely places to add time, and any source-supported opportunities to condense. Do not rush or make generic cuts merely to hit the predicted day count.

Use these three options as a starting point:

1. Follow the curriculum with no modifications.
2. Add a planned flex-day cadence.
3. Blend selected lessons while protecting inquiry and sensemaking.

Do not recommend an adaptation that removes the curriculum's inquiry core without calling out the tradeoff.

Treat the plan as a living document. During implementation, record what worked, what took longer than expected, the actual days used, and any adjustments made. Use those reflections to revise upcoming units and improve the teacher's year-long plan for the next implementation.

## Required final output

Return a concise pacing plan with:

- Context and named assumptions
- Instructional-day count and exclusions
- Year-long table with `Recommended Days`, `Adjustment (+/-)`, `Predicted Days`, and `Actual Days (Finalized)`, plus source citations for recommended days
- Unit map with penciled start/end targets, calendar adjustments, and buffers
- Unit 1 deep dive with the chosen pacing mode and rationale
- Unresolved decisions or risks
- A short review cadence for recording actual days and updating the living plan during the year

## Template

Use this structure:

```markdown
# [Course] Pacing Plan

## Context and assumptions

## Phase 1: Instructional calendar

## Phase 2: Unit estimates

## Phase 3: Calendar map

## Phase 4: Unit 1 deep dive

## Decisions to revisit
```
