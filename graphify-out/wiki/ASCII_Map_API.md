# ASCII Map API

> 34 nodes

## Key Concepts

- **npc_config_parsing.py** (14 connections) — `server/npc/npc_config_parsing.py`
- **.__init__()** (11 connections) — `server/npc/npc_base.py`
- **to_int_or_default()** (7 connections) — `server/npc/npc_config_parsing.py`
- **get_combat_stats_dict()** (7 connections) — `server/npc/npc_config_parsing.py`
- **normalize_determination_points()** (5 connections) — `server/npc/npc_config_parsing.py`
- **parse_behavior_config()** (5 connections) — `server/npc/npc_config_parsing.py`
- **_safe_stat_int()** (5 connections) — `server/npc/npc_config_parsing.py`
- **._safe_get()** (4 connections) — `server/npc/npc_base.py`
- **._apply_definition_attributes()** (4 connections) — `server/npc/npc_base.py`
- **parse_stats()** (4 connections) — `server/npc/npc_config_parsing.py`
- **parse_ai_config()** (4 connections) — `server/npc/npc_config_parsing.py`
- **_compute_max_dp()** (4 connections) — `server/npc/npc_config_parsing.py`
- **._setup_base_behavior_rules()** (3 connections) — `server/npc/npc_base.py`
- **._safe_stat_int()** (3 connections) — `server/npc/npc_base.py`
- **.get_combat_stats()** (3 connections) — `server/npc/npc_base.py`
- **apply_dp_from_source()** (3 connections) — `server/npc/npc_config_parsing.py`
- **apply_idle_movement_defaults()** (3 connections) — `server/npc/npc_config_parsing.py`
- **Initialize the NPC base class.** (1 connections) — `server/npc/npc_base.py`
- **Get attribute from obj with default to avoid lazy-loading issues.** (1 connections) — `server/npc/npc_base.py`
- **Set npc_type, name, current_room, spawn_room_id from definition.** (1 connections) — `server/npc/npc_base.py`
- **Setup base behavior rules common to all NPCs.** (1 connections) — `server/npc/npc_base.py`
- **Return stats[key] as int, or default if missing/None.** (1 connections) — `server/npc/npc_base.py`
- **Return current_dp, max_dp, dexterity for CombatParticipantData.** (1 connections) — `server/npc/npc_base.py`
- **Parsing and normalization of NPC config (stats, behavior, AI) to keep npc_base N** (1 connections) — `server/npc/npc_config_parsing.py`
- **Parse stats from JSON string. Returns default stats on parse error.** (1 connections) — `server/npc/npc_config_parsing.py`
- *... and 9 more nodes in this community*

## Relationships

- [Realtime Service Bundle](Realtime_Service_Bundle.md) (8 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (7 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [WebSocket Message Handlers](WebSocket_Message_Handlers.md) (1 shared connections)

## Source Files

- `server/npc/npc_base.py`
- `server/npc/npc_config_parsing.py`

## Audit Trail

- EXTRACTED: 106 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*