# .__init__

> 20 nodes

## Key Concepts

- **.__init__()** (11 connections) — `server/npc/npc_base.py`
- **normalize_determination_points()** (5 connections) — `server/npc/npc_config_parsing.py`
- **parse_behavior_config()** (5 connections) — `server/npc/npc_config_parsing.py`
- **._apply_definition_attributes()** (4 connections) — `server/npc/npc_base.py`
- **._safe_get()** (4 connections) — `server/npc/npc_base.py`
- **parse_ai_config()** (4 connections) — `server/npc/npc_config_parsing.py`
- **parse_stats()** (4 connections) — `server/npc/npc_config_parsing.py`
- **._setup_base_behavior_rules()** (3 connections) — `server/npc/npc_base.py`
- **apply_dp_from_source()** (3 connections) — `server/npc/npc_config_parsing.py`
- **apply_idle_movement_defaults()** (3 connections) — `server/npc/npc_config_parsing.py`
- **Get attribute from obj with default to avoid lazy-loading issues.** (1 connections) — `server/npc/npc_base.py`
- **Set npc_type, name, current_room, spawn_room_id from definition.** (1 connections) — `server/npc/npc_base.py`
- **Setup base behavior rules common to all NPCs.** (1 connections) — `server/npc/npc_base.py`
- **Initialize the NPC base class.** (1 connections) — `server/npc/npc_base.py`
- **Parse stats from JSON string. Returns default stats on parse error.** (1 connections) — `server/npc/npc_config_parsing.py`
- **Set determination_points from source_key; optionally set max_dp. Returns True…** (1 connections) — `server/npc/npc_config_parsing.py`
- **Ensure stats has determination_points; support hp/dp backward compat. Mutates…** (1 connections) — `server/npc/npc_config_parsing.py`
- **Apply default idle movement config based on NPC type. Mutates config.** (1 connections) — `server/npc/npc_config_parsing.py`
- **Parse behavior configuration from JSON string. Applies idle movement defaults.** (1 connections) — `server/npc/npc_config_parsing.py`
- **Parse AI integration configuration from JSON string.** (1 connections) — `server/npc/npc_config_parsing.py`

## Relationships

- [NPCDefinition](NPCDefinition.md) (9 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [BehaviorEngine](BehaviorEngine.md) (1 shared connections)

## Source Files

- `server/npc/npc_base.py`
- `server/npc/npc_config_parsing.py`

## Audit Trail

- EXTRACTED: 36 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*