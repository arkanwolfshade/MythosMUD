# inventory mutation guard

> 42 nodes

## Key Concepts

- **PlayerRoomEventHandler** (30 connections) — `server/realtime/player_event_handlers_room.py`
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
- **Handles room-related player events (entered, left, occupants).** (1 connections) — `server/realtime/player_event_handlers_room.py`
- **Initialize room event handler.          Args:             connection_manager: Co** (1 connections) — `server/realtime/player_event_handlers_room.py`
- **Log player movement for AI processing.          Args:             player_id: The** (1 connections) — `server/realtime/player_event_handlers_room.py`
- *... and 17 more nodes in this community*

## Relationships

- [event bus events](event_bus_events.md) (5 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (3 shared connections)
- [realtime monitoring performance](realtime_monitoring_performance.md) (2 shared connections)
- [schedule services service](schedule_services_service.md) (2 shared connections)
- [player_event_handler_utils](player_event_handler_utils.md) (2 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (2 shared connections)
- [realtime messaging message](realtime_messaging_message.md) (2 shared connections)
- [room look commands](room_look_commands.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_room.py`

## Audit Trail

- EXTRACTED: 170 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*