# container main rationale

> 2 nodes

## Key Concepts

- **.save_player()** (3 connections) — `server/game/magic/spell_effect_types.py`
- **Persist player after spell mutations.** (1 connections) — `server/game/magic/spell_effect_types.py`

## Relationships

- [spell game magic](spell_game_magic.md) (1 shared connections)
- [quest game service](quest_game_service.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effect_types.py`

## Audit Trail

- EXTRACTED: 3 (75%)
- INFERRED: 1 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*