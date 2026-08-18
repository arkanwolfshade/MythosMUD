# PlayerLeftRoom

> 94 nodes

## Key Concepts

- **PlayerLeftRoom** (49 connections) — `server/events/event_types.py`
- **test_quest_events.py** (17 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_player_event_handlers_room_left.py** (16 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **subscribe_quest_events()** (15 connections) — `server/game/quest/quest_events.py`
- **quest_events.py** (15 connections) — `server/game/quest/quest_events.py`
- **test_message_builders.py** (15 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **asyncio** (11 connections)
- **_make_on_player_entered()** (8 connections) — `server/game/quest/quest_events.py`
- **_builder()** (8 connections) — `server/tests/unit/realtime/test_message_builders.py`
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
- **test_create_player_entered_message()** (4 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_create_player_left_message()** (4 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_handle_player_left_disconnecting()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **test_handle_player_left_error_handling()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **test_handle_player_left_no_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **test_handle_player_left_no_player_info()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- *... and 69 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (24 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (15 shared connections)
- [test_event_handler.py](test_event_handler.py.md) (6 shared connections)
- [test_lifecycle_periodic.py](test_lifecycle_periodic.py.md) (6 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_lifespan_event_subscriptions.py](test_lifespan_event_subscriptions.py.md) (3 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [Room](Room.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/quest/quest_events.py`
- `server/npc/spawning_service.py`
- `server/realtime/event_handler.py`
- `server/realtime/player_event_handlers_room.py`
- `server/tests/unit/game/test_quest_events.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/realtime/test_message_builders.py`
- `server/tests/unit/realtime/test_player_event_handlers_room_left.py`

## Audit Trail

- EXTRACTED: 183 (88%)
- INFERRED: 25 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*