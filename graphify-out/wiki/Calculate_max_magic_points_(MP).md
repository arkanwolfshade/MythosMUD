# Calculate max magic points (MP)

> 4 nodes

## Key Concepts

- **._save_player_after_consume()** (5 connections) — `server/game/quest/quest_service.py`
- **.save_player()** (3 connections) — `server/game/magic/spell_effect_types.py`
- **Persist player after spell mutations.** (1 connections) — `server/game/magic/spell_effect_types.py`
- **Persist player after collect_n consumption when async_persistence is wired.** (1 connections) — `server/game/quest/quest_service.py`

## Relationships

- [QuestCompleted](QuestCompleted.md) (3 shared connections)
- [.end combat()](end_combat%28%29.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effect_types.py`
- `server/game/quest/quest_service.py`

## Audit Trail

- EXTRACTED: 8 (80%)
- INFERRED: 2 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*