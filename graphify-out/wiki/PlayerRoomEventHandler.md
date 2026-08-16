# PlayerRoomEventHandler

> 68 nodes

## Key Concepts

- **PlayerRoomEventHandler** (30 connections) — `server/realtime/player_event_handlers_room.py`
- **player_event_handlers_room.py** (28 connections) — `server/realtime/player_event_handlers_room.py`
- **UUID** (15 connections)
- **PlayerRoomEventHandlerDeps** (12 connections) — `server/realtime/player_event_handlers_room.py`
- **_as_map()** (10 connections) — `server/realtime/player_event_handlers_room.py`
- **.handle_player_entered()** (10 connections) — `server/realtime/player_event_handlers_room.py`
- **_snapshot_payload()** (10 connections) — `server/realtime/player_event_handlers_room.py`
- **OccupantsUpdateFn** (9 connections) — `server/realtime/player_event_handlers_room.py`
- **RoomConnectionManager** (9 connections) — `server/realtime/player_event_handlers_room.py`
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
- **Protocol** (6 connections)
- **_NamedRoom** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **_as_occupant_snap()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.log_player_movement()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- *... and 43 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (23 shared connections)
- [realtime/conftest.py](realtime-conftest.py.md) (5 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (5 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (5 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (4 shared connections)
- [build_event](build_event.md) (4 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (3 shared connections)
- [test_room_sync_service.py](test_room_sync_service.py.md) (1 shared connections)
- [player_event_handlers_respawn.py](player_event_handlers_respawn.py.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_room.py`

## Audit Trail

- EXTRACTED: 169 (91%)
- INFERRED: 16 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*