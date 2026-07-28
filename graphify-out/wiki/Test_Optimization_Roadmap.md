# Test Optimization Roadmap

> 30 nodes · cohesion 0.08

## Key Concepts

- **npc_config_parsing.py** (14 connections) — `server/npc/npc_config_parsing.py`
- **.__init__()** (11 connections) — `server/npc/npc_base.py`
- **get_combat_stats_dict()** (7 connections) — `server/npc/npc_config_parsing.py`
- **to_int_or_default()** (7 connections) — `server/npc/npc_config_parsing.py`
- **normalize_determination_points()** (5 connections) — `server/npc/npc_config_parsing.py`
- **parse_behavior_config()** (5 connections) — `server/npc/npc_config_parsing.py`
- **_safe_stat_int()** (5 connections) — `server/npc/npc_config_parsing.py`
- **._apply_definition_attributes()** (4 connections) — `server/npc/npc_base.py`
- **._safe_get()** (4 connections) — `server/npc/npc_base.py`
- **_compute_max_dp()** (4 connections) — `server/npc/npc_config_parsing.py`
- **parse_ai_config()** (4 connections) — `server/npc/npc_config_parsing.py`
- **parse_stats()** (4 connections) — `server/npc/npc_config_parsing.py`
- **.get_combat_stats()** (3 connections) — `server/npc/npc_base.py`
- **._safe_stat_int()** (3 connections) — `server/npc/npc_base.py`
- **._setup_base_behavior_rules()** (3 connections) — `server/npc/npc_base.py`
- **apply_dp_from_source()** (3 connections) — `server/npc/npc_config_parsing.py`
- **apply_idle_movement_defaults()** (3 connections) — `server/npc/npc_config_parsing.py`
- **Set npc_type, name, current_room, spawn_room_id from definition.** (1 connections) — `server/npc/npc_base.py`
- **Get current NPC stats.** (1 connections) — `server/npc/npc_base.py`
- **Parsing and normalization of NPC config (stats, behavior, AI) to keep npc_base N** (1 connections) — `server/npc/npc_config_parsing.py`
- **Return stats[key] as int, or default if missing/None.** (1 connections) — `server/npc/npc_config_parsing.py`
- **Compute max_dp from stats when max_dp/max_hp not explicitly set.** (1 connections) — `server/npc/npc_config_parsing.py`
- **Return current_dp, max_dp, dexterity for CombatParticipantData.** (1 connections) — `server/npc/npc_config_parsing.py`
- **Parse stats from JSON string. Returns default stats on parse error.** (1 connections) — `server/npc/npc_config_parsing.py`
- **Set determination_points from source_key; optionally set max_dp. Returns True if** (1 connections) — `server/npc/npc_config_parsing.py`
- *... and 5 more nodes in this community*

## Relationships

- [Character Creation API](Character_Creation_API.md) (8 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (7 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [NPC Definition Schemas](NPC_Definition_Schemas.md) (1 shared connections)

## Source Files

- `server/npc/npc_base.py`
- `server/npc/npc_config_parsing.py`

## Audit Trail

- EXTRACTED: 102 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*