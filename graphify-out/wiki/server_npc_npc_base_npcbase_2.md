# server npc npc base npcbase

> 12 nodes

## Key Concepts

- **get_combat_stats_dict()** (7 connections) — `server/npc/npc_config_parsing.py`
- **to_int_or_default()** (7 connections) — `server/npc/npc_config_parsing.py`
- **_safe_stat_int()** (5 connections) — `server/npc/npc_config_parsing.py`
- **_compute_max_dp()** (4 connections) — `server/npc/npc_config_parsing.py`
- **.get_combat_stats()** (3 connections) — `server/npc/npc_base.py`
- **._safe_stat_int()** (3 connections) — `server/npc/npc_base.py`
- **Return stats[key] as int, or default if missing/None.** (1 connections) — `server/npc/npc_base.py`
- **Return current_dp, max_dp, dexterity for CombatParticipantData.** (1 connections) — `server/npc/npc_base.py`
- **Return stats[key] as int, or default if missing/None.** (1 connections) — `server/npc/npc_config_parsing.py`
- **Compute max_dp from stats when max_dp/max_hp not explicitly set.** (1 connections) — `server/npc/npc_config_parsing.py`
- **Return current_dp, max_dp, dexterity for CombatParticipantData.** (1 connections) — `server/npc/npc_config_parsing.py`
- **Coerce value to int; return default if not numeric.** (1 connections) — `server/npc/npc_config_parsing.py`

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (3 shared connections)
- [server events event bus](server_events_event_bus.md) (2 shared connections)

## Source Files

- `server/npc/npc_base.py`
- `server/npc/npc_config_parsing.py`

## Audit Trail

- EXTRACTED: 22 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*