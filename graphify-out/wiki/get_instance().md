# .get instance()

> 46 nodes

## Key Concepts

- **PlayerRoomEventHandler** (30 connections) — `server/realtime/player_event_handlers_room.py`
- **RoomOccupantManager** (22 connections) — `server/realtime/room_occupant_manager.py`
- **player_event_handlers_room.py** (17 connections) — `server/realtime/player_event_handlers_room.py`
- **UUID** (12 connections)
- **Any** (10 connections)
- **.handle_player_entered()** (9 connections) — `server/realtime/player_event_handlers_room.py`
- **.__init__()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_occupants_snapshot_to_player()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_updates_to_entering_player()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.handle_player_left()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **._prepare_room_data()** (6 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_update_to_player()** (6 connections) — `server/realtime/player_event_handlers_room.py`
- **.log_player_movement()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **._send_room_name_message()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **._log_occupants_info()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.query_room_occupants_snapshot()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_state_to_player()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.get_room_state_event()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.broadcast_player_entered_message()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **.subscribe_player_to_room()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **.build_room_occupants_message()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **._process_player_entered_event()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **.unsubscribe_player_from_room()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **.broadcast_player_left_message()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **Room-related player event handlers.  This module handles player room entry/exit** (1 connections) — `server/realtime/player_event_handlers_room.py`
- *... and 21 more nodes in this community*

## Relationships

- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (11 shared connections)
- [world](world.md) (6 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (5 shared connections)
- [NPCEventHandler](NPCEventHandler.md) (4 shared connections)
- [connection statistics](connection_statistics.md) (4 shared connections)
- [.validate player name field()](validate_player_name_field%28%29.md) (3 shared connections)
- [PlayerChannelPreferences](PlayerChannelPreferences.md) (3 shared connections)
- [test room occupant manager](test_room_occupant_manager.md) (3 shared connections)
- [circuit breaker](circuit_breaker.md) (2 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (2 shared connections)
- [UUID](UUID.md) (1 shared connections)
- [occupant formatter](occupant_formatter.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_room.py`
- `server/realtime/room_occupant_manager.py`

## Audit Trail

- EXTRACTED: 203 (94%)
- INFERRED: 13 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*