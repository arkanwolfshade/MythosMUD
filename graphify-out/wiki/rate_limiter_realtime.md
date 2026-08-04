# rate limiter realtime

> 50 nodes

## Key Concepts

- **register_default_reactions_for_npc()** (15 connections) — `server/npc/npc_default_reactions.py`
- **npc_config_parsing.py** (14 connections) — `server/npc/npc_config_parsing.py`
- **.__init__()** (11 connections) — `server/npc/npc_base.py`
- **test_npc_default_reactions.py** (9 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **to_int_or_default()** (7 connections) — `server/npc/npc_config_parsing.py`
- **get_combat_stats_dict()** (7 connections) — `server/npc/npc_config_parsing.py`
- **.npc_attacked_retaliation()** (6 connections) — `server/npc/event_reaction_system.py`
- **._register_reactions_and_chat_name()** (5 connections) — `server/npc/npc_base.py`
- **normalize_determination_points()** (5 connections) — `server/npc/npc_config_parsing.py`
- **parse_behavior_config()** (5 connections) — `server/npc/npc_config_parsing.py`
- **_safe_stat_int()** (5 connections) — `server/npc/npc_config_parsing.py`
- **._safe_get()** (4 connections) — `server/npc/npc_base.py`
- **._apply_definition_attributes()** (4 connections) — `server/npc/npc_base.py`
- **parse_stats()** (4 connections) — `server/npc/npc_config_parsing.py`
- **parse_ai_config()** (4 connections) — `server/npc/npc_config_parsing.py`
- **_compute_max_dp()** (4 connections) — `server/npc/npc_config_parsing.py`
- **test_npc_attacked_retaliation_template()** (4 connections) — `server/tests/unit/npc/test_event_reaction_speech.py`
- **._setup_base_behavior_rules()** (3 connections) — `server/npc/npc_base.py`
- **._safe_stat_int()** (3 connections) — `server/npc/npc_base.py`
- **.get_combat_stats()** (3 connections) — `server/npc/npc_base.py`
- **apply_dp_from_source()** (3 connections) — `server/npc/npc_config_parsing.py`
- **apply_idle_movement_defaults()** (3 connections) — `server/npc/npc_config_parsing.py`
- **test_register_passive_mob_reactions()** (2 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **test_register_shopkeeper_reactions()** (2 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **test_register_aggressive_mob_retaliation_only()** (2 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- *... and 25 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (16 shared connections)
- [Error Conversion](Error_Conversion.md) (8 shared connections)
- [services nats service](services_nats_service.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [behavior engine npc](behavior_engine_npc.md) (1 shared connections)
- [quest chat game](quest_chat_game.md) (1 shared connections)

## Source Files

- `server/npc/event_reaction_system.py`
- `server/npc/npc_base.py`
- `server/npc/npc_config_parsing.py`
- `server/npc/npc_default_reactions.py`
- `server/tests/unit/npc/test_event_reaction_speech.py`
- `server/tests/unit/npc/test_npc_default_reactions.py`

## Audit Trail

- EXTRACTED: 161 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*