# Distributed Event Bus

> 389 nodes

## Key Concepts

- **ConnectionManager** (170 connections) — `server/realtime/connection_manager.py`
- **build_event()** (117 connections) — `server/realtime/envelope.py`
- **UUID** (41 connections)
- **Any** (40 connections)
- **nats_message_handler.py** (39 connections) — `server/realtime/nats_message_handler.py`
- **AttributeError** (38 connections)
- **websocket_room_updates.py** (32 connections) — `server/realtime/websocket_room_updates.py`
- **test_websocket_room_updates.py** (32 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **envelope.py** (28 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (28 connections) — `server/tests/unit/realtime/test_envelope.py`
- **event_handlers.py** (23 connections) — `server/realtime/event_handlers.py`
- **broadcast_room_update()** (23 connections) — `server/realtime/websocket_room_updates.py`
- **EventHandler** (22 connections) — `server/realtime/event_handlers.py`
- **websocket_handler_connection.py** (17 connections) — `server/realtime/websocket_handler_connection.py`
- **build_room_update_event()** (13 connections) — `server/realtime/websocket_room_updates.py`
- **get_player_occupants()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **get_npc_occupants_from_lifecycle_manager()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **get_npc_occupants_fallback()** (9 connections) — `server/realtime/websocket_room_updates.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **_send_combat_participant_updates()** (8 connections) — `server/realtime/event_handlers.py`
- **get_next_sequence_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **_EventBusPublishPort** (7 connections) — `server/realtime/event_handlers.py`
- **_publish_npc_died_to_event_bus()** (7 connections) — `server/realtime/event_handlers.py`
- **_npc_died_broadcast_and_bridge()** (7 connections) — `server/realtime/event_handlers.py`
- **cleanup_websocket_connection()** (7 connections) — `server/realtime/websocket_handler_connection.py`
- *... and 364 more nodes in this community*

## Relationships

- [Room Occupant Events](Room_Occupant_Events.md) (77 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (23 shared connections)
- [Pydantic Error Handlers](Pydantic_Error_Handlers.md) (13 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (13 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (11 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (10 shared connections)
- [NATS Message Broker](NATS_Message_Broker.md) (10 shared connections)
- [Combat Command Helpers](Combat_Command_Helpers.md) (10 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (9 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (9 shared connections)
- [Combat Turn Processor](Combat_Turn_Processor.md) (8 shared connections)
- [Message Broadcaster Core](Message_Broadcaster_Core.md) (8 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/envelope.py`
- `server/realtime/event_handlers.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/websocket_handler_connection.py`
- `server/realtime/websocket_room_updates.py`
- `server/tests/unit/realtime/test_envelope.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`
- `server/tests/unit/realtime/test_room_occupant_manager.py`
- `server/tests/unit/realtime/test_websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- `server/tests/unit/services/test_npc_instance_service.py`
- `server/tests/unit/services/test_room_sync_service.py`

## Audit Trail

- EXTRACTED: 1469 (94%)
- INFERRED: 100 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*