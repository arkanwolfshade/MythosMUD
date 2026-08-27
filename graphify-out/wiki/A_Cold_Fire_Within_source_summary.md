# A Cold Fire Within (source summary)

> 6 nodes

## Key Concepts

- **.get_combat_stats()** (4 connections) — `server/npc/combat_integration.py`
- **._get_player_combat_stats()** (4 connections) — `server/npc/combat_integration.py`
- **._normalize_npc_stats()** (3 connections) — `server/npc/combat_integration.py`
- **Get combat stats for a player.** (1 connections) — `server/npc/combat_integration.py`
- **Normalize NPC stats to include 'hp' for backward compatibility.** (1 connections) — `server/npc/combat_integration.py`
- **Get combat-relevant stats for an entity. Args: entity_id: ID of the entity…** (1 connections) — `server/npc/combat_integration.py`

## Relationships

- [test_movement_monitor.py](test_movement_monitor.py.md) (3 shared connections)
- [TestGracefulDegradation](TestGracefulDegradation.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration.py`

## Audit Trail

- EXTRACTED: 9 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*