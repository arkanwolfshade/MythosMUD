# server events event types playerleftroom

> 93 nodes

## Key Concepts

- **PlayerLeftRoom** (44 connections) — `server/events/event_types.py`
- **test_quest_events.py** (17 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_player_event_handlers_room_left.py** (16 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **subscribe_quest_events()** (15 connections) — `server/game/quest/quest_events.py`
- **quest_events.py** (15 connections) — `server/game/quest/quest_events.py`
- **test_message_builders.py** (15 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **asyncio** (11 connections)
- **connection_event_helpers.py** (10 connections) — `server/realtime/connection_event_helpers.py`
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
- *... and 68 more nodes in this community*

## Relationships

- [server events event bus](server_events_event_bus.md) (13 shared connections)
- [server events event types playerenteredroom](server_events_event_types_playerenteredroom.md) (11 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (10 shared connections)
- [server realtime event handler py](server_realtime_event_handler_py.md) (7 shared connections)
- [server tests unit realtime test](server_tests_unit_realtime_test.md) (6 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (3 shared connections)
- [server app lifespan event subscriptions](server_app_lifespan_event_subscriptions.md) (3 shared connections)
- [attributeerror](attributeerror.md) (3 shared connections)
- [server npc population control npcpopulationcontroller](server_npc_population_control_npcpopulationcontroller.md) (2 shared connections)
- [server app lifespan startup create](server_app_lifespan_startup_create.md) (2 shared connections)
- [characterinfo](characterinfo.md) (2 shared connections)
- [server models npc npcdefinition is](server_models_npc_npcdefinition_is.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/quest/quest_events.py`
- `server/npc/spawning_service.py`
- `server/realtime/connection_event_helpers.py`
- `server/realtime/event_handler.py`
- `server/tests/unit/game/test_quest_events.py`
- `server/tests/unit/realtime/test_message_builders.py`
- `server/tests/unit/realtime/test_player_event_handlers_room_left.py`

## Audit Trail

- EXTRACTED: 176 (85%)
- INFERRED: 32 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*