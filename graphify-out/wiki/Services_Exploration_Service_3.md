# Services Exploration Service

> 4 nodes

## Key Concepts

- **._send_spell_completion_message()** (6 connections) — `server/game/magic/magic_service.py`
- **.send_spell_execution_notifications()** (5 connections) — `server/game/magic/magic_service.py`
- **Send notifications after spell execution (completion messages and healing events** (1 connections) — `server/game/magic/magic_service.py`
- **Send spell completion message to player.** (1 connections) — `server/game/magic/magic_service.py`

## Relationships

- [Security Headers Middleware](Security_Headers_Middleware.md) (6 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (1 shared connections)

## Source Files

- `server/game/magic/magic_service.py`

## Audit Trail

- EXTRACTED: 13 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*