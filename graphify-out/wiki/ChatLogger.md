# chatlogger

> 85 nodes

## Key Concepts

- **PlayerEventHandler** (26 connections) — `server/realtime/player_event_handlers.py`
- **realtime/conftest.py** (22 connections) — `server/tests/unit/realtime/conftest.py`
- **fixture** (15 connections)
- **OccupantsUpdateFn** (9 connections) — `server/realtime/player_event_handlers_room.py`
- **.__init__()** (9 connections) — `server/realtime/player_event_handlers.py`
- **PlayerRoomEventHandlerDeps** (8 connections) — `server/realtime/player_event_handlers_room.py`
- **RoomChatLogger** (6 connections) — `server/realtime/player_event_handlers_room.py`
- **._initialize_handlers()** (6 connections) — `server/realtime/player_event_handlers.py`
- **Protocol** (6 connections)
- **_NamedRoom** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **player_room_event_handler()** (5 connections) — `server/tests/unit/realtime/conftest.py`
- **.get_room_state_event()** (4 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_entered()** (4 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_left()** (4 connections) — `server/realtime/player_event_handlers.py`
- **mock_utils()** (4 connections) — `server/tests/unit/realtime/conftest.py`
- **_RoomPersistence** (3 connections) — `server/realtime/player_event_handlers_room.py`
- **.handle_player_delirium_respawned()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_died()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_dp_decay()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_respawned()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_xp_awarded()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.send_occupants_snapshot_to_player()** (3 connections) — `server/realtime/player_event_handlers.py`
- **mock_chat_logger()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **mock_connection_manager()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **mock_logger()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- *... and 60 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (15 shared connections)
- [occupantsnap](occupantsnap.md) (11 shared connections)
- [server realtime event handler py](server_realtime_event_handler_py.md) (2 shared connections)
- [server tests unit realtime test](server_tests_unit_realtime_test.md) (2 shared connections)
- [baseevent](baseevent.md) (2 shared connections)
- [playerdpupdated](playerdpupdated.md) (1 shared connections)
- [playercombatservice](playercombatservice.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)
- [server realtime event handlers](server_realtime_event_handlers.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_room.py`
- `server/tests/unit/realtime/conftest.py`

## Audit Trail

- EXTRACTED: 128 (90%)
- INFERRED: 15 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*