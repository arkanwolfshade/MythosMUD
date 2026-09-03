# Test Player Event Handlers Room

> 74 nodes

## Key Concepts

- **PlayerEnteredRoom** (77 connections) — `server/events/event_types.py`
- **test_player_event_handlers_room.py** (38 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **asyncio** (33 connections)
- **test_handle_player_entered_error_handling()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_handle_player_entered_no_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_handle_player_entered_no_player_info()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_handle_player_entered_success()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_process_player_entered_event_no_player_info()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_process_player_entered_event_no_room_id()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_process_player_entered_event_success()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_handle_player_entered_room()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_broadcast_player_entered_message()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_broadcast_player_entered_message_no_room_id()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_build_room_occupants_message()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_log_player_movement_error_handling()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_log_player_movement_joined()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_log_player_movement_left()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_log_player_movement_no_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_log_player_movement_no_room()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_prepare_room_data_with_to_dict()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_prepare_room_data_without_to_dict()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_query_room_occupants_snapshot()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_send_occupants_snapshot_to_player_error_handling()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_send_occupants_snapshot_to_player_no_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_send_occupants_snapshot_to_player_string_id()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- *... and 49 more nodes in this community*

## Relationships

- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (16 shared connections)
- [Test Quest Events](Test_Quest_Events.md) (7 shared connections)
- [Test Event Handler](Test_Event_Handler.md) (6 shared connections)
- [NPC Behavior & Spawning](NPC_Behavior_&_Spawning.md) (5 shared connections)
- [Test Follow Service](Test_Follow_Service.md) (5 shared connections)
- [Player Event Handlers Room](Player_Event_Handlers_Room.md) (4 shared connections)
- [Test Player Event Handlers](Test_Player_Event_Handlers.md) (4 shared connections)
- [Message Builders](Message_Builders.md) (3 shared connections)
- [Event Serialization](Event_Serialization.md) (2 shared connections)
- [Follow Movement](Follow_Movement.md) (2 shared connections)
- [Test Follow Flow](Test_Follow_Flow.md) (2 shared connections)
- [Test Population Control](Test_Population_Control.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/realtime/test_player_event_handlers_room.py`

## Audit Trail

- EXTRACTED: 158 (86%)
- INFERRED: 25 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*