# ZoneConfiguration

> 135 nodes · cohesion 0.03

## Key Concepts

- **player_event_handlers.py** (41 connections) — `server/realtime/player_event_handlers.py`
- **PlayerRoomEventHandler** (34 connections) — `server/realtime/player_event_handlers_room.py`
- **PlayerEventHandler** (32 connections) — `server/realtime/player_event_handlers.py`
- **player_event_handlers_room.py** (31 connections) — `server/realtime/player_event_handlers_room.py`
- **realtime/conftest.py** (23 connections) — `server/tests/unit/realtime/conftest.py`
- **UUID** (17 connections)
- **fixture** (15 connections)
- **PlayerRoomEventHandlerDeps** (12 connections) — `server/realtime/player_event_handlers_room.py`
- **.__init__()** (10 connections) — `server/realtime/player_event_handlers.py`
- **_as_map()** (10 connections) — `server/realtime/player_event_handlers_room.py`
- **.handle_player_entered()** (10 connections) — `server/realtime/player_event_handlers_room.py`
- **JsonMap** (10 connections)
- **RoomConnectionManager** (10 connections) — `server/realtime/player_event_handlers_room.py`
- **_snapshot_payload()** (10 connections) — `server/realtime/player_event_handlers_room.py`
- **OccupantsUpdateFn** (9 connections) — `server/realtime/player_event_handlers_room.py`
- **._initialize_handlers()** (8 connections) — `server/realtime/player_event_handlers.py`
- **._build_room_update_data()** (8 connections) — `server/realtime/player_event_handlers_room.py`
- **.handle_player_left()** (8 connections) — `server/realtime/player_event_handlers_room.py`
- **._prepare_room_data()** (8 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_occupants_snapshot_to_player()** (8 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_update_to_player()** (8 connections) — `server/realtime/player_event_handlers_room.py`
- **_NamedRoom** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.get_room_state_event()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_state_to_player()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_updates_to_entering_player()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- *... and 110 more nodes in this community*

## Relationships

- [ConnectionManager](ConnectionManager.md) (22 shared connections)
- [look_container.py](look_container.py.md) (14 shared connections)
- [BaseEvent](BaseEvent.md) (12 shared connections)
- [Room](Room.md) (8 shared connections)
- [Communities (355 total, 223 thin omitted)](Communities_355_total,_223_thin_omitted.md) (8 shared connections)
- [ChatHistoryPanel.tsx](ChatHistoryPanel.tsx.md) (8 shared connections)
- [deque](deque.md) (5 shared connections)
- [asyncio](asyncio.md) (3 shared connections)
- [test_rate_limiter_utils.py](test_rate_limiter_utils.py.md) (3 shared connections)
- [.publish_with_pool](publish_with_pool.md) (3 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (2 shared connections)
- [test_command_admin.py](test_command_admin.py.md) (2 shared connections)

## Source Files

- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_room.py`
- `server/tests/unit/realtime/conftest.py`

## Audit Trail

- EXTRACTED: 313 (92%)
- INFERRED: 29 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*