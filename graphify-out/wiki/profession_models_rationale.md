# profession models rationale

> 447 nodes

## Key Concepts

- **PlayerLeftRoom** (57 connections) — `server/events/event_types.py`
- **RealTimeEventHandler** (44 connections) — `server/realtime/event_handler.py`
- **PlayerEventHandlerUtils** (42 connections) — `server/realtime/player_event_handlers_utils.py`
- **test_event_handler.py** (41 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **PlayerDPUpdated** (39 connections) — `server/events/event_types.py`
- **event_handler.py** (35 connections) — `server/realtime/event_handler.py`
- **PlayerXPAwardEvent** (35 connections) — `server/services/player_combat_service.py`
- **test_player_event_handlers.py** (33 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_player_event_handlers_state.py** (33 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **MessageBuilder** (26 connections) — `server/realtime/message_builders.py`
- **player_event_handlers.py** (26 connections) — `server/realtime/player_event_handlers.py`
- **PlayerEventHandler** (26 connections) — `server/realtime/player_event_handlers.py`
- **NPCEventHandler** (25 connections) — `server/realtime/npc_event_handlers.py`
- **player_event_handlers_state.py** (23 connections) — `server/realtime/player_event_handlers_state.py`
- **RoomOccupantManager** (22 connections) — `server/realtime/room_occupant_manager.py`
- **conftest.py** (22 connections) — `server/tests/unit/realtime/conftest.py`
- **PlayerRespawnedEvent** (20 connections) — `server/events/event_types.py`
- **PlayerDiedEvent** (19 connections) — `server/events/event_types.py`
- **player_event_handlers_room.py** (17 connections) — `server/realtime/player_event_handlers_room.py`
- **PlayerDPDecayEvent** (16 connections) — `server/events/event_types.py`
- **player_event_handlers_utils.py** (16 connections) — `server/realtime/player_event_handlers_utils.py`
- **PlayerDeliriumRespawnedEvent** (15 connections) — `server/events/event_types.py`
- **test_message_builders.py** (15 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_player_event_handlers_room_left.py** (15 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **PlayerStateEventHandler** (14 connections) — `server/realtime/player_event_handlers_state.py`
- *... and 422 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (84 shared connections)
- [party service game](party_service_game.md) (21 shared connections)
- [message nats handler](message_nats_handler.md) (14 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (14 shared connections)
- [NATS Messaging](NATS_Messaging.md) (13 shared connections)
- [player service game](player_service_game.md) (10 shared connections)
- [player room realtime](player_room_realtime.md) (10 shared connections)
- [schemas players profession](schemas_players_profession.md) (10 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (9 shared connections)
- [combat services messaging](combat_services_messaging.md) (8 shared connections)
- [Room Broadcast](Room_Broadcast.md) (7 shared connections)
- [command service commands](command_service_commands.md) (6 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/npc_event_handlers.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_room.py`
- `server/realtime/player_event_handlers_state.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/realtime/player_name_utils.py`
- `server/realtime/room_occupant_manager.py`
- `server/services/player_combat_service.py`
- `server/services/room_sync_service.py`
- `server/tests/unit/realtime/conftest.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_message_builders.py`
- `server/tests/unit/realtime/test_player_event_handlers.py`
- `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 1490 (93%)
- INFERRED: 116 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*