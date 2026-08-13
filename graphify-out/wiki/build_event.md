# build_event

> 118 nodes

## Key Concepts

- **build_event()** (117 connections) — `server/realtime/envelope.py`
- **nats_message_handler.py** (39 connections) — `server/realtime/nats_message_handler.py`
- **envelope.py** (28 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (28 connections) — `server/tests/unit/realtime/test_envelope.py`
- **event_handlers.py** (23 connections) — `server/realtime/event_handlers.py`
- **EventHandler** (22 connections) — `server/realtime/event_handlers.py`
- **_npc_died_broadcast_and_bridge()** (7 connections) — `server/realtime/event_handlers.py`
- **_send_combat_participant_updates()** (7 connections) — `server/realtime/event_handlers.py`
- **UUIDEncoder** (6 connections) — `server/realtime/envelope.py`
- **_EventBusPublishPort** (6 connections) — `server/realtime/event_handlers.py`
- **utc_now_z()** (6 connections) — `server/realtime/envelope.py`
- **_as_event_data_dict()** (6 connections) — `server/realtime/event_handlers.py`
- **.handle_event_message()** (5 connections) — `server/realtime/event_handlers.py`
- **_publish_npc_died_to_event_bus()** (5 connections) — `server/realtime/event_handlers.py`
- **_refresh_room_after_npc_death()** (5 connections) — `server/realtime/event_handlers.py`
- **_SupportsEventSequence** (4 connections) — `server/realtime/envelope.py`
- **.handle_player_entered_room()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **.handle_player_left_room()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **test_handle_npc_took_damage_flattens_event_data_for_websocket()** (4 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **test_event_handlers_combat.py** (4 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **_get_next_global_sequence()** (3 connections) — `server/realtime/envelope.py`
- **.get_event_handler_map()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_combat_ended_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_combat_started_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_attacked_event()** (3 connections) — `server/realtime/event_handlers.py`
- *... and 93 more nodes in this community*

## Relationships

- [CombatMessagingService](CombatMessagingService.md) (15 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (13 shared connections)
- [event_types.py](event_types.py.md) (12 shared connections)
- [ConnectionManager](ConnectionManager.md) (10 shared connections)
- [connection_manager.py](connection_manager.py.md) (8 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [AttributeError](AttributeError.md) (6 shared connections)
- [NATSMessageHandler](NATSMessageHandler.md) (5 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (5 shared connections)
- [admin_teleport_commands.py](admin_teleport_commands.py.md) (4 shared connections)
- [rest_countdown_task.py](rest_countdown_task.py.md) (4 shared connections)
- [send_game_event](send_game_event.md) (4 shared connections)

## Source Files

- `server/realtime/envelope.py`
- `server/realtime/event_handlers.py`
- `server/realtime/integration/room_event_handler.py`
- `server/realtime/nats_message_handler.py`
- `server/tests/unit/realtime/test_envelope.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`

## Audit Trail

- EXTRACTED: 329 (99%)
- INFERRED: 5 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*