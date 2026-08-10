# Structured Concurrency Patterns

> 2 nodes

## Key Concepts

- **.save_player()** (3 connections) — `server/game/magic/spell_effect_types.py`
- **Persist player after spell mutations.** (1 connections) — `server/game/magic/spell_effect_types.py`

## Relationships

- [Combat Attack Service](Combat_Attack_Service.md) (1 shared connections)
- [Quest Service Core](Quest_Service_Core.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effect_types.py`

## Audit Trail

- EXTRACTED: 3 (75%)
- INFERRED: 1 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*