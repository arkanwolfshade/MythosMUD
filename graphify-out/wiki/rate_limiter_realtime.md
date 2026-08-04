# rate limiter realtime

> 34 nodes

## Key Concepts

- **register_default_reactions_for_npc()** (15 connections) — `server/npc/npc_default_reactions.py`
- **.__init__()** (11 connections) — `server/npc/npc_base.py`
- **npc_default_reactions.py** (10 connections) — `server/npc/npc_default_reactions.py`
- **test_npc_default_reactions.py** (9 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **._register_reactions_and_chat_name()** (5 connections) — `server/npc/npc_base.py`
- **normalize_determination_points()** (5 connections) — `server/npc/npc_config_parsing.py`
- **parse_behavior_config()** (5 connections) — `server/npc/npc_config_parsing.py`
- **._safe_get()** (4 connections) — `server/npc/npc_base.py`
- **._apply_definition_attributes()** (4 connections) — `server/npc/npc_base.py`
- **parse_stats()** (4 connections) — `server/npc/npc_config_parsing.py`
- **parse_ai_config()** (4 connections) — `server/npc/npc_config_parsing.py`
- **._setup_base_behavior_rules()** (3 connections) — `server/npc/npc_base.py`
- **apply_dp_from_source()** (3 connections) — `server/npc/npc_config_parsing.py`
- **apply_idle_movement_defaults()** (3 connections) — `server/npc/npc_config_parsing.py`
- **test_register_passive_mob_reactions()** (2 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **test_register_shopkeeper_reactions()** (2 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **test_register_aggressive_mob_retaliation_only()** (2 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **test_register_unknown_type_no_reactions()** (2 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **test_register_shopkeeper_logs_debug()** (2 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **test_register_handles_import_error()** (2 connections) — `server/tests/unit/npc/test_npc_default_reactions.py`
- **Initialize the NPC base class.** (1 connections) — `server/npc/npc_base.py`
- **Register default reactions, room context, and chat display name.** (1 connections) — `server/npc/npc_base.py`
- **Get attribute from obj with default to avoid lazy-loading issues.** (1 connections) — `server/npc/npc_base.py`
- **Set npc_type, name, current_room, spawn_room_id from definition.** (1 connections) — `server/npc/npc_base.py`
- **Setup base behavior rules common to all NPCs.** (1 connections) — `server/npc/npc_base.py`
- *... and 9 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (12 shared connections)
- [Loot Generation](Loot_Generation.md) (8 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (7 shared connections)
- [lucidity active service](lucidity_active_service.md) (1 shared connections)
- [quest chat game](quest_chat_game.md) (1 shared connections)

## Source Files

- `server/npc/npc_base.py`
- `server/npc/npc_config_parsing.py`
- `server/npc/npc_default_reactions.py`
- `server/tests/unit/npc/test_npc_default_reactions.py`

## Audit Trail

- EXTRACTED: 111 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*