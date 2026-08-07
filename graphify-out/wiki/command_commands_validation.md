# command commands validation

> 5 nodes

## Key Concepts

- **.__init__()** (4 connections) — `server/services/npc_combat_rewards.py`
- **.calculate_xp_reward()** (3 connections) — `server/services/npc_combat_rewards.py`
- **Any** (2 connections)
- **Initialize the rewards manager.          Args:             async_persistence: As** (1 connections) — `server/services/npc_combat_rewards.py`
- **Calculate XP reward from NPC definition.          Args:             npc_definiti** (1 connections) — `server/services/npc_combat_rewards.py`

## Relationships

- [player event realtime](player_event_realtime.md) (2 shared connections)
- [add used user](add_used_user.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_rewards.py`

## Audit Trail

- EXTRACTED: 11 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*