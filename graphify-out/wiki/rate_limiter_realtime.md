# rate limiter realtime

> 40 nodes

## Key Concepts

- **npc_config_parsing.py** (14 connections) — `server/npc/npc_config_parsing.py`
- **.__init__()** (11 connections) — `server/npc/npc_base.py`
- **to_int_or_default()** (7 connections) — `server/npc/npc_config_parsing.py`
- **get_combat_stats_dict()** (7 connections) — `server/npc/npc_config_parsing.py`
- **._register_reactions_and_chat_name()** (5 connections) — `server/npc/npc_base.py`
- **normalize_determination_points()** (5 connections) — `server/npc/npc_config_parsing.py`
- **parse_behavior_config()** (5 connections) — `server/npc/npc_config_parsing.py`
- **_safe_stat_int()** (5 connections) — `server/npc/npc_config_parsing.py`
- **._safe_get()** (4 connections) — `server/npc/npc_base.py`
- **._apply_definition_attributes()** (4 connections) — `server/npc/npc_base.py`
- **.heal()** (4 connections) — `server/npc/npc_base.py`
- **parse_stats()** (4 connections) — `server/npc/npc_config_parsing.py`
- **parse_ai_config()** (4 connections) — `server/npc/npc_config_parsing.py`
- **_compute_max_dp()** (4 connections) — `server/npc/npc_config_parsing.py`
- **._setup_base_behavior_rules()** (3 connections) — `server/npc/npc_base.py`
- **._safe_stat_int()** (3 connections) — `server/npc/npc_base.py`
- **.get_combat_stats()** (3 connections) — `server/npc/npc_base.py`
- **._sync_dp_stats()** (3 connections) — `server/npc/npc_base.py`
- **apply_dp_from_source()** (3 connections) — `server/npc/npc_config_parsing.py`
- **apply_idle_movement_defaults()** (3 connections) — `server/npc/npc_config_parsing.py`
- **Initialize the NPC base class.** (1 connections) — `server/npc/npc_base.py`
- **Register default reactions, room context, and chat display name.** (1 connections) — `server/npc/npc_base.py`
- **Get attribute from obj with default to avoid lazy-loading issues.** (1 connections) — `server/npc/npc_base.py`
- **Set npc_type, name, current_room, spawn_room_id from definition.** (1 connections) — `server/npc/npc_base.py`
- **Setup base behavior rules common to all NPCs.** (1 connections) — `server/npc/npc_base.py`
- *... and 15 more nodes in this community*

## Relationships

- [NATS Messaging](NATS_Messaging.md) (10 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (9 shared connections)
- [npc behavior engine](npc_behavior_engine.md) (1 shared connections)
- [quest chat game](quest_chat_game.md) (1 shared connections)

## Source Files

- `server/npc/npc_base.py`
- `server/npc/npc_config_parsing.py`

## Audit Trail

- EXTRACTED: 121 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*