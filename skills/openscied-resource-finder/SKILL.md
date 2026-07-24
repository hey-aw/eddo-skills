---
name: openscied-resource-finder
description: Find, compare, and synthesize OpenSciEd curriculum materials through the read-only OpenSciEd Library MCP service. Use for requests about grades, units, lessons, teacher editions, slides, assessments, answer keys, or related curriculum artifacts.
---

# OpenSciEd Resource Finder

Use the connected `openscied-library` MCP service as the evidence source. The service is read-only and may not contain every OpenSciEd resource.

## Workflow

1. Call `get_index_status` when freshness or coverage matters. Report stale, partial, or failed coverage.
2. Call `list_curriculum` for browsing and `search_materials` for a specific question.
3. Narrow broad searches by grade, unit, lesson, material kind, or extension. Ask the user only when different interpretations would materially change the result.
4. Call `read_material` only for the most relevant results and retrieve the smallest excerpts needed.
5. Answer from the retrieved evidence. Clearly label inferences and unresolved gaps.

Follow [citation guidance](references/citation-guidance.md) whenever material evidence appears in the answer.

## Boundaries

- Never claim access to materials that the service did not return.
- Never invent curriculum details or citations.
- Never request arbitrary filesystem paths, raw Drive identifiers, credentials, or unrestricted binary downloads.
- Never synchronize Drive, refresh the index, modify files, or publish content.
- If the MCP service is unavailable, explain that the host needs the `openscied-library` service configured. Do not substitute an unverified local corpus.
