# container main rationale

> 4 nodes

## Key Concepts

- **._save_player_after_consume()** (5 connections) — `server/game/quest/quest_service.py`
- **.save_player()** (3 connections) — `server/game/magic/spell_effect_types.py`
- **Persist player after spell mutations.** (1 connections) — `server/game/magic/spell_effect_types.py`
- **Persist player after collect_n consumption when async_persistence is wired.** (1 connections) — `server/game/quest/quest_service.py`

## Relationships

- [quest game service](quest_game_service.md) (2 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (1 shared connections)
- [quest service game](quest_service_game.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effect_types.py`
- `server/game/quest/quest_service.py`

## Audit Trail

- EXTRACTED: 8 (80%)
- INFERRED: 2 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*