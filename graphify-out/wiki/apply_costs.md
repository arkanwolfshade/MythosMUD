# .apply_costs

> 6 nodes · cohesion 0.33

## Key Concepts

- **.apply_costs()** (5 connections) — `server/game/magic/spell_costs.py`
- **.restore_mp()** (4 connections) — `server/game/magic/spell_costs.py`
- **UUID** (3 connections)
- **Any** (1 connections)
- **Restore magic points to a player.          Args:             player_id: Player I** (1 connections) — `server/game/magic/spell_costs.py`
- **Apply spell costs (MP and lucidity if Mythos).          Args:             player** (1 connections) — `server/game/magic/spell_costs.py`

## Relationships

- [CombatService](CombatService.md) (3 shared connections)
- [TargetMatch](TargetMatch.md) (1 shared connections)
- [send_game_event](send_game_event.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_costs.py`

## Audit Trail

- EXTRACTED: 15 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*