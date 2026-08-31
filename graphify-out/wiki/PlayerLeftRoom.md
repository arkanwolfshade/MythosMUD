# PlayerLeftRoom

> 77 nodes

## Key Concepts

- **PlayerLeftRoom** (49 connections) — `server/events/event_types.py`
- **test_quest_events.py** (17 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_player_event_handlers_room_left.py** (16 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **subscribe_quest_events()** (15 connections) — `server/game/quest/quest_events.py`
- **quest_events.py** (15 connections) — `server/game/quest/quest_events.py`
- **asyncio** (11 connections)
- **_make_on_player_entered()** (8 connections) — `server/game/quest/quest_events.py`
- **_make_on_npc_died()** (7 connections) — `server/game/quest/quest_events.py`
- **_make_on_player_left()** (6 connections) — `server/game/quest/quest_events.py`
- **test_npc_died_no_killer_skips()** (5 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_npc_died_records_kill_for_player_killer()** (5 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_player_entered_invalid_player_id_skips()** (5 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_player_entered_starts_quest_by_room_trigger()** (5 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_player_left_records_exit_activity()** (5 connections) — `server/tests/unit/game/test_quest_events.py`
- **asyncio** (5 connections)
- **_entity_id_for_quest_offer()** (4 connections) — `server/game/quest/quest_events.py`
- **_parse_player_id()** (4 connections) — `server/game/quest/quest_events.py`
- **test_handle_player_left_disconnecting()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **test_handle_player_left_error_handling()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **test_handle_player_left_no_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **test_handle_player_left_no_player_info()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **test_handle_player_left_success()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **Any** (4 connections)
- **._handle_player_left_room()** (3 connections) — `server/npc/spawning_service.py`
- **._handle_player_left()** (3 connections) — `server/realtime/event_handler.py`
- *... and 52 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (23 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (11 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (7 shared connections)
- [MessageBuilder](MessageBuilder.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_player_event_handlers.py](test_player_event_handlers.py.md) (3 shared connections)
- [test_event_reaction_speech.py](test_event_reaction_speech.py.md) (2 shared connections)
- [test_follow_service.py](test_follow_service.py.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [Room](Room.md) (1 shared connections)
- [RoomEventHandler](RoomEventHandler.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/quest/quest_events.py`
- `server/npc/spawning_service.py`
- `server/realtime/event_handler.py`
- `server/realtime/player_event_handlers_room.py`
- `server/tests/unit/game/test_quest_events.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_player_event_handlers_room_left.py`

## Audit Trail

- EXTRACTED: 153 (86%)
- INFERRED: 25 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*