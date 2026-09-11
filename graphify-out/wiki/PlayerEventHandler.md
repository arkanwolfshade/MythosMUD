# PlayerEventHandler

> 129 nodes

## Key Concepts

- **PlayerEventHandler** (32 connections) — `server/realtime/player_event_handlers.py`
- **PlayerRoomEventHandler** (30 connections) — `server/realtime/player_event_handlers_room.py`
- **player_event_handlers_room.py** (28 connections) — `server/realtime/player_event_handlers_room.py`
- **realtime/conftest.py** (23 connections) — `server/tests/unit/realtime/conftest.py`
- **UUID** (16 connections)
- **fixture** (15 connections)
- **PlayerRoomEventHandlerDeps** (12 connections) — `server/realtime/player_event_handlers_room.py`
- **RoomConnectionManager** (10 connections) — `server/realtime/player_event_handlers_room.py`
- **.__init__()** (10 connections) — `server/realtime/player_event_handlers.py`
- **_as_map()** (10 connections) — `server/realtime/player_event_handlers_room.py`
- **.handle_player_entered()** (10 connections) — `server/realtime/player_event_handlers_room.py`
- **_snapshot_payload()** (10 connections) — `server/realtime/player_event_handlers_room.py`
- **OccupantsUpdateFn** (9 connections) — `server/realtime/player_event_handlers_room.py`
- **JsonMap** (9 connections)
- **._initialize_handlers()** (8 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_left()** (8 connections) — `server/realtime/player_event_handlers_room.py`
- **._prepare_room_data()** (8 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_occupants_snapshot_to_player()** (8 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_update_to_player()** (8 connections) — `server/realtime/player_event_handlers_room.py`
- **.get_room_state_event()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_state_to_player()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_updates_to_entering_player()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **RoomChatLogger** (6 connections) — `server/realtime/player_event_handlers_room.py`
- **._log_occupants_info()** (6 connections) — `server/realtime/player_event_handlers_room.py`
- **.query_room_occupants_snapshot()** (6 connections) — `server/realtime/player_event_handlers_room.py`
- *... and 104 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (18 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (12 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (10 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (7 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (6 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (5 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (4 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (3 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_room.py`
- `server/tests/unit/realtime/conftest.py`

## Audit Trail

- EXTRACTED: 267 (91%)
- INFERRED: 28 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*