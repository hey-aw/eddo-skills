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

Before calculating availability, gather the teacher's schedule model and ask them to confirm your summary:

- Course span: full year, semester, trimester, quarter, or another term, with the actual course start and end dates.
- Meeting pattern: daily, a fixed number of classes per week, alternating A/B days, a rotating cycle, or another block design.
- Typical class length and any recurring shortened days, double periods, or lab blocks.
- Schedule changes by term, grading period, or day of the week.

Ask how the teacher wants class meetings translated into pacing days for the year map. Let the teacher provide a local rule. If they want a recommendation, offer a simple starting point:

- For daily standard periods, count one class meeting as one pacing day.
- For a 90-minute block against a 45-minute middle-school recommendation, count one block as two pacing days for rough unit allocation, rounding the required meetings up.
- For a mixed or rotating schedule, either use one simple local rule or map class meetings directly on the calendar.

Summarize the model and the chosen rule in a compact form such as `semester, alternating A/B blocks, 3-4 meetings/week, 1 block = 2 pacing days for rough allocation`. Ask the teacher to correct or replace the rule before continuing. Treat the teacher's confirmed convention as authoritative for the planning draft.

Collect the school year start and end dates, non-instructional days, breaks, testing windows, professional-development days, and any regular schedule disruptions.

Calculate the available class meetings or pacing days inside the confirmed course term, using the teacher's rule. Keep school-calendar days distinct from days when this course actually meets, and list every exclusion used. Do not create a minute-by-minute ledger unless the teacher specifically asks for one. If details are missing, give a provisional range and clearly label it as an assumption.

### Phase 2: Sketch the units

Identify the course or grade band. Ask the teacher to confirm whether they expect to follow the standard OpenSciEd unit sequence or a district or locally defined sequence. Treat the teacher's confirmation as authoritative for the planning draft.

Offer to look up an official district-published sequence in parallel. If the teacher accepts:

- Use only official district and OpenSciEd sources, and name and link the sources used.
- Compare published guidance with the teacher's confirmed sequence without silently overriding the teacher.
- Surface conflicting district guidance or the absence of a published district sequence.

Label the sequence as confirmed when the teacher confirms it. If confirmation is still pending, use the standard OpenSciEd sequence only as a clearly labeled provisional assumption.

Read [references/unit-lengths.md](references/unit-lengths.md) and use its embedded table as the primary pacing reference for OpenSciEd `Recommended Days`. Preserve the source notes and provisional labels in that reference. Do not require external lookup before using a value from the embedded table.

Offer optional verification when the teacher wants a current or unit-specific check:

1. Retrieve the relevant Unit Overview or Quick Start Guide through the public, read-only OpenSciEd MCP server.
2. Consult the relevant guidance on the official OpenSciEd website.

The public MCP server is a convenience layer for bounded access to curriculum materials, not a substitute for verification against the official source. When verification is requested, identify and cite the source used. If a verified value conflicts with the embedded table, surface the conflict and ask the teacher which value to use; do not silently overwrite it.

For a non-OpenSciEd unit, use and cite the timeline in the relevant curriculum guide. If the embedded reference does not cover a unit and no verification route yields clear guidance, leave the value unresolved or label it explicitly as provisional and state its basis; do not substitute a generic grade-band guess.

Translate source recommendations into the teacher's schedule with the confirmed pacing-day rule:

1. Keep the source `Recommended Days` visible. The bundled middle-school values assume 45-minute classes; elementary values are school-calendar spans. Do not assign the same meaning to an undefined high-school or non-OpenSciEd day.
2. Apply the teacher's rule and express the result in class meetings or pacing days. For example, under the suggested block rule, `37 recommended days ≈ 19 block meetings`.
3. Keep the calculation at this day-and-meeting level unless the teacher asks for more detail.
4. Treat the equivalency as a rough year-map recommendation, not permission to combine or omit lessons. Validate what actually fits within a meeting during the Phase 4 unit deep dive.

Build a year-long planning table with these columns:

| Unit Name / Topic | Recommended Days | Adjustment (+/-) | Predicted Days | Actual Days (Finalized) |
| --- | ---: | ---: | ---: | ---: |

Enter the source value and status in `Recommended Days`. When the pacing-day rule changes the number of meetings, show the concise translation, such as `37 recommended days ≈ 19 block meetings`, and state that `Adjustment (+/-)`, `Predicted Days`, and `Actual Days (Finalized)` use class meetings as their working unit. Keep teacher or local changes separate in `Adjustment (+/-)` and calculate `Predicted Days` from the translated recommendation plus the adjustment. Do not rewrite a curriculum recommendation to absorb a local adjustment. Leave `Actual Days (Finalized)` open until Phase 3.

Total the predicted class meetings, then compare them with the available course meetings established in Phase 1. Show the gap or buffer explicitly. If the curriculum total exceeds the available schedule, work with the teacher to distribute the necessary provisional reductions thoughtfully across units rather than hiding the mismatch or concentrating all reductions in one place. Record every reduction in `Adjustment (+/-)`.

Treat the table as a sketch. Carry its reductions and pressure points into Phases 3 and 4, where calendar fit and unit-specific guidance can test whether they are workable.

### Phase 3: Map dates and constraints

Using `Predicted Days` under the confirmed pacing-day rule, pencil each unit's estimated end date onto the Phase 1 calendar. Place instruction only on dates when the course meets, including the correct side of an A/B or rotating schedule.

Look for calendar awkwardness around breaks, testing windows, grading periods, and local events. Adjust targets when needed so a unit reaches a sensible stopping point, and avoid starting a new unit immediately before a long break.

After checking the full calendar, finalize each unit's allocation in `Actual Days (Finalized)`. Compare the finalized class-meeting total with the Phase 1 available meetings. Ask whether the resulting pace feels sustainable for the teacher and students. If it does not, revisit the adjustments with the teacher before treating the map as settled.

Adjust a plan that does not fit in this order:

1. Recheck the course term, meeting cadence, exclusions, and chosen pacing-day rule.
2. Move unit boundaries around breaks, testing windows, and term transitions without changing instructional time unnecessarily.
3. Rebalance buffers and flex days across units while preserving a sustainable cadence.
4. If reductions remain necessary, use each Unit Overview's official shortening guidance and the Quick Start Guide's Summative Assessment Moments before proposing lesson changes.
5. Present the revised tradeoffs to the teacher, ask for confirmation, and record approved changes in `Adjustment (+/-)` and `Predicted Days`.

### Phase 4: Deep-dive Unit 1

Use the Unit Storyline to map the class meetings needed for each lesson onto the calendar.

For block schedules, use the Storyline and lesson structure to decide which activities can share a meeting. Do not pack two lessons into one block based on minutes alone; protect investigations, discussion, sensemaking, and assessment moments.

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
- Confirmed schedule model, including classes per week or cycle, typical class length, course term, block or rotation design, and the teacher-approved pacing-day rule
- Available course meetings or pacing days, exclusions, and any provisional assumptions
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
