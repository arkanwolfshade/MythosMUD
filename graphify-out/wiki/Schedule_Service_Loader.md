# Schedule Service Loader

> 6 nodes · cohesion 0.33

## Key Concepts

- **.apply_costs()** (5 connections) — `server/game/magic/spell_costs.py`
- **.restore_mp()** (4 connections) — `server/game/magic/spell_costs.py`
- **UUID** (3 connections)
- **Any** (1 connections)
- **Restore magic points to a player.          Args:             player_id: Player I** (1 connections) — `server/game/magic/spell_costs.py`
- **Apply spell costs (MP and lucidity if Mythos).          Args:             player** (1 connections) — `server/game/magic/spell_costs.py`

## Relationships

- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (3 shared connections)
- [Game Magic Spell](Game_Magic_Spell.md) (1 shared connections)
- [NPC Combat Handler Tests](NPC_Combat_Handler_Tests.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_costs.py`

## Audit Trail

- EXTRACTED: 15 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*