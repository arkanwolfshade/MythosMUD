---
name: mythosmud-adr-authoring
description: Create or update Architecture Decision Records in docs/architecture/decisions/: Status, Context, Decision, Alternatives Considered, Consequences. Use when documenting an architectural decision, adding an ADR, or when the user mentions ADR or architecture decision.
---

# MythosMUD ADR Authoring

## Location

- **Directory:** `docs/architecture/decisions/`
- **Filename:** `ADR-NNN-kebab-title.md` (e.g. `ADR-009-event-serialization-format.md`)
- **Index:** Update the table in [docs/architecture/decisions/README.md](../../docs/architecture/decisions/README.md) when adding a new ADR.

## Structure

Each ADR must include:

| Section | Content |
|---------|---------|
| **Status** | One of: Proposed, Accepted, Deprecated, Superseded |
| **Context** | Situation and forces driving the decision |
| **Decision** | The chosen approach |
| **Alternatives Considered** | Other options evaluated |
| **Consequences** | Positive, negative, and neutral outcomes |

## Template

```markdown
# ADR-NNN: Short Title

**Status:** Proposed | Accepted | Deprecated | Superseded
**Date:** YYYY-MM-DD

## Context

[What situation and forces led to this decision?]

## Decision

[What was decided?]

## Alternatives Considered

[What other options were evaluated and why they were not chosen?]

## Consequences

[Positive, negative, and neutral outcomes.]
```

## Index Update

When adding a new ADR, add a row to the table in `docs/architecture/decisions/README.md`:

| ADR | Title | Status | Date |
|-----|-------|--------|------|
| [ADR-NNN](ADR-NNN-kebab-title.md) | Short Title | Accepted | YYYY-MM-DD |

Use the next sequential number (e.g. after ADR-008 use ADR-009).

## Reference

- Format and index: [docs/architecture/decisions/README.md](../../docs/architecture/decisions/README.md)
- Existing ADRs: [docs/architecture/decisions/](../../docs/architecture/decisions/) (for style and numbering)
