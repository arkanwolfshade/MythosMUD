# NPCCombatIntegrationBase

> 401 nodes

## Key Concepts

- **PlayerEventHandlerUtils** (42 connections) — `server/realtime/player_event_handlers_utils.py`
- **PlayerXPAwardEvent** (35 connections) — `server/services/player_combat_service.py`
- **test_player_event_handlers_respawn.py** (34 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **player_event_handlers_respawn.py** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **PlayerRespawnEventHandler** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **test_player_event_handlers.py** (33 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_player_event_handlers_state.py** (33 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **PlayerRoomEventHandler** (30 connections) — `server/realtime/player_event_handlers_room.py`
- **player_event_handlers.py** (26 connections) — `server/realtime/player_event_handlers.py`
- **PlayerEventHandler** (26 connections) — `server/realtime/player_event_handlers.py`
- **MessageBuilder** (22 connections) — `server/realtime/message_builders.py`
- **RoomOccupantManager** (22 connections) — `server/realtime/room_occupant_manager.py`
- **conftest.py** (22 connections) — `server/tests/unit/realtime/conftest.py`
- **PlayerRespawnedEvent** (19 connections) — `server/events/event_types.py`
- **player_event_handlers_room.py** (17 connections) — `server/realtime/player_event_handlers_room.py`
- **player_event_handlers_utils.py** (16 connections) — `server/realtime/player_event_handlers_utils.py`
- **PlayerStateEventHandler** (14 connections) — `server/realtime/player_event_handlers_state.py`
- **RespawnPlayerEventPayload** (13 connections) — `server/realtime/player_event_handlers_respawn.py`
- **UUID** (12 connections)
- **UUID** (11 connections)
- **Any** (10 connections)
- **Any** (9 connections)
- **.get_player_data_for_respawn()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_respawned()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._extract_occupant_names()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- *... and 376 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (76 shared connections)
- [Player](Player.md) (19 shared connections)
- [UUID](UUID.md) (14 shared connections)
- [container websocket events](container_websocket_events.md) (10 shared connections)
- [Any](Any.md) (8 shared connections)
- [connection manager api](connection_manager_api.md) (8 shared connections)
- [clean command input()](clean_command_input%28%29.md) (6 shared connections)
- [. init ()](_init_%28%29.md) (5 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (5 shared connections)
- [combat initialization](combat_initialization.md) (4 shared connections)
- [test npc event handlers](test_npc_event_handlers.md) (3 shared connections)
- [test room occupant manager](test_room_occupant_manager.md) (3 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/player_event_handlers_room.py`
- `server/realtime/player_event_handlers_state.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/realtime/room_occupant_manager.py`
- `server/services/player_combat_service.py`
- `server/tests/unit/realtime/conftest.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_player_event_handlers.py`
- `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`

## Audit Trail

- EXTRACTED: 1296 (96%)
- INFERRED: 56 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*