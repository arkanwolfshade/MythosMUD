# player death service

> 127 nodes

## Key Concepts

- **test_player_death_service.py** (52 connections) — `server/tests/unit/services/test_player_death_service.py`
- **PlayerDeathService** (28 connections) — `server/services/player_death_service.py`
- **PlayerDiedEvent** (19 connections) — `server/events/event_types.py`
- **player_death_service.py** (19 connections) — `server/services/player_death_service.py`
- **log_exception_once()** (15 connections) — `server/structured_logging/enhanced_logging_config.py`
- **.handle_player_death()** (10 connections) — `server/services/player_death_service.py`
- **_send_player_death_notification()** (7 connections) — `server/realtime/player_event_handlers_state.py`
- **combat_service_types.py** (7 connections) — `server/services/combat_service_types.py`
- **.process_mortally_wounded_tick()** (7 connections) — `server/services/player_death_service.py`
- **._publish_death_event()** (7 connections) — `server/services/player_death_service.py`
- **.get_dead_players()** (6 connections) — `server/services/player_death_service.py`
- **UUID** (6 connections)
- **.get_mortally_wounded_players()** (5 connections) — `server/services/player_death_service.py`
- **._ensure_player_posture_lying()** (5 connections) — `server/services/player_death_service.py`
- **._clear_player_combat_state()** (5 connections) — `server/services/player_death_service.py`
- **.handle_player_died()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **AsyncSession** (4 connections)
- **._get_room_name_for_death()** (4 connections) — `server/services/player_death_service.py`
- **._handle_player_died()** (3 connections) — `server/realtime/event_handler.py`
- **.__init__()** (3 connections) — `server/services/player_death_service.py`
- **Any** (3 connections)
- **Player** (3 connections)
- **test_event_handler_handle_player_died()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **player_death_service()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **player_death_service_no_dependencies()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- *... and 102 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (13 shared connections)
- [world models rationale](world_models_rationale.md) (10 shared connections)
- [models npc rationale](models_npc_rationale.md) (7 shared connections)
- [NATS Messaging](NATS_Messaging.md) (5 shared connections)
- [combat models rationale](combat_models_rationale.md) (5 shared connections)
- [NPC Combat](NPC_Combat.md) (4 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (4 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (3 shared connections)
- [exceptions rationale error](exceptions_rationale_error.md) (3 shared connections)
- [item models rationale](item_models_rationale.md) (2 shared connections)
- [command service commands](command_service_commands.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/event_handler.py`
- `server/realtime/player_event_handlers_state.py`
- `server/services/combat_service_types.py`
- `server/services/player_death_service.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 356 (95%)
- INFERRED: 20 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*