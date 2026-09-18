# Community 756

> 22 nodes

## Key Concepts

- **npc_config_parsing.py** (14 connections) — `server/npc/npc_config_parsing.py`
- **get_combat_stats_dict()** (5 connections) — `server/npc/npc_config_parsing.py`
- **_safe_stat_int()** (5 connections) — `server/npc/npc_config_parsing.py`
- **_compute_max_dp()** (4 connections) — `server/npc/npc_config_parsing.py`
- **to_int_or_default()** (4 connections) — `server/npc/npc_config_parsing.py`
- **apply_dp_from_source()** (3 connections) — `server/npc/npc_config_parsing.py`
- **apply_idle_movement_defaults()** (3 connections) — `server/npc/npc_config_parsing.py`
- **normalize_determination_points()** (3 connections) — `server/npc/npc_config_parsing.py`
- **parse_behavior_config()** (3 connections) — `server/npc/npc_config_parsing.py`
- **parse_ai_config()** (2 connections) — `server/npc/npc_config_parsing.py`
- **parse_stats()** (2 connections) — `server/npc/npc_config_parsing.py`
- **Parsing and normalization of NPC config (stats, behavior, AI) to keep npc_base…** (1 connections) — `server/npc/npc_config_parsing.py`
- **Return stats[key] as int, or default if missing/None.** (1 connections) — `server/npc/npc_config_parsing.py`
- **Compute max_dp from stats when max_dp/max_hp not explicitly set.** (1 connections) — `server/npc/npc_config_parsing.py`
- **Return current_dp, max_dp, dexterity for CombatParticipantData.** (1 connections) — `server/npc/npc_config_parsing.py`
- **Parse stats from JSON string. Returns default stats on parse error.** (1 connections) — `server/npc/npc_config_parsing.py`
- **Set determination_points from source_key; optionally set max_dp. Returns True…** (1 connections) — `server/npc/npc_config_parsing.py`
- **Ensure stats has determination_points; support hp/dp backward compat. Mutates…** (1 connections) — `server/npc/npc_config_parsing.py`
- **Apply default idle movement config based on NPC type. Mutates config.** (1 connections) — `server/npc/npc_config_parsing.py`
- **Parse behavior configuration from JSON string. Applies idle movement defaults.** (1 connections) — `server/npc/npc_config_parsing.py`
- **Parse AI integration configuration from JSON string.** (1 connections) — `server/npc/npc_config_parsing.py`
- **Coerce value to int; return default if not numeric.** (1 connections) — `server/npc/npc_config_parsing.py`

## Relationships

- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (2 shared connections)
- [Community 635](Community_635.md) (1 shared connections)

## Source Files

- `server/npc/npc_config_parsing.py`

## Audit Trail

- EXTRACTED: 31 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*