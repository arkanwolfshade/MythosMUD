# rate limiter realtime

> 117 nodes

## Key Concepts

- **NPCBase** (83 connections) — `server/npc/npc_base.py`
- **npc_config_parsing.py** (14 connections) — `server/npc/npc_config_parsing.py`
- **.__init__()** (11 connections) — `server/npc/npc_base.py`
- **CommunicationIntegrationProtocol** (10 connections) — `server/npc/npc_protocols.py`
- **to_int_or_default()** (7 connections) — `server/npc/npc_config_parsing.py`
- **get_combat_stats_dict()** (7 connections) — `server/npc/npc_config_parsing.py`
- **register_npc_display_name()** (7 connections) — `server/npc/npc_display_names.py`
- **CombatIntegrationProtocol** (7 connections) — `server/npc/npc_protocols.py`
- **._handle_npc_death()** (6 connections) — `server/npc/npc_base.py`
- **._register_reactions_and_chat_name()** (5 connections) — `server/npc/npc_base.py`
- **.take_damage()** (5 connections) — `server/npc/npc_base.py`
- **.move_to_room()** (5 connections) — `server/npc/npc_base.py`
- **normalize_determination_points()** (5 connections) — `server/npc/npc_config_parsing.py`
- **parse_behavior_config()** (5 connections) — `server/npc/npc_config_parsing.py`
- **_safe_stat_int()** (5 connections) — `server/npc/npc_config_parsing.py`
- **npc_display_names.py** (5 connections) — `server/npc/npc_display_names.py`
- **._safe_get()** (4 connections) — `server/npc/npc_base.py`
- **._apply_definition_attributes()** (4 connections) — `server/npc/npc_base.py`
- **._publish_damage_event()** (4 connections) — `server/npc/npc_base.py`
- **._schedule_end_combat_if_npc_died()** (4 connections) — `server/npc/npc_base.py`
- **.heal()** (4 connections) — `server/npc/npc_base.py`
- **.speak()** (4 connections) — `server/npc/npc_base.py`
- **.listen()** (4 connections) — `server/npc/npc_base.py`
- **.execute_behavior()** (4 connections) — `server/npc/npc_base.py`
- **parse_stats()** (4 connections) — `server/npc/npc_config_parsing.py`
- *... and 92 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (38 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (6 shared connections)
- [quest chat game](quest_chat_game.md) (5 shared connections)
- [commands logout helpers](commands_logout_helpers.md) (4 shared connections)
- [item models rationale](item_models_rationale.md) (4 shared connections)
- [behavior engine npc](behavior_engine_npc.md) (3 shared connections)
- [lucidity event services](lucidity_event_services.md) (2 shared connections)
- [combat services rationale](combat_services_rationale.md) (2 shared connections)
- [target resolution service](target_resolution_service.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [room realtime occupant](room_realtime_occupant.md) (1 shared connections)
- [message queue realtime](message_queue_realtime.md) (1 shared connections)

## Source Files

- `server/npc/npc_base.py`
- `server/npc/npc_config_parsing.py`
- `server/npc/npc_display_names.py`
- `server/npc/npc_protocols.py`
- `server/npc/spawning_models.py`

## Audit Trail

- EXTRACTED: 345 (93%)
- INFERRED: 24 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*