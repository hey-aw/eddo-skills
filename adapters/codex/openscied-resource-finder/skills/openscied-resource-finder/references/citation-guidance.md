# Citation guidance

Use the title and `citation_uri` returned by the service for every curriculum-specific claim.

## Required form

Prefer a compact inline citation:

```text
The lesson introduces particle motion through a modeling task (Grade 6 Unit 1 Teacher Edition, openscied://materials/abc123#page=14).
```

When several claims rely on one excerpt, cite the paragraph once. When claims come from different artifacts or locators, cite each source separately.

## Evidence rules

- Treat returned excerpts as source evidence.
- Identify comparisons, recommendations, and conclusions as synthesis when they are not stated directly in a source.
- Preserve distinctions between teacher materials, student materials, assessments, answer keys, and slides.
- If an excerpt is truncated, follow `next_locator` only when the missing continuation is necessary.
- If a citation URI is absent or malformed, name the source but state that a stable citation is unavailable.
- Never convert a service-side citation URI into a guessed web URL or local path.
