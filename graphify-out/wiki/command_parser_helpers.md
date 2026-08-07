# command parser helpers

> 51 nodes

## Key Concepts

- **MessageFilteringHelper** (25 connections) — `server/realtime/message_filtering.py`
- **NATSMessageHandler** (24 connections) — `server/realtime/nats_message_handler.py`
- **test_message_filtering_helpers.py** (10 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **.is_player_in_room()** (7 connections) — `server/realtime/message_filtering.py`
- **.__init__()** (7 connections) — `server/realtime/nats_message_handler.py`
- **.check_player_mute_status()** (6 connections) — `server/realtime/message_filtering.py`
- **.filter_target_players()** (6 connections) — `server/realtime/message_filtering.py`
- **Any** (4 connections)
- **.is_player_muted_by_receiver()** (4 connections) — `server/realtime/message_filtering.py`
- **.is_player_muted_by_receiver_with_user_manager()** (4 connections) — `server/realtime/message_filtering.py`
- **.__init__()** (3 connections) — `server/realtime/message_filtering.py`
- **._get_user_manager()** (3 connections) — `server/realtime/message_filtering.py`
- **.extract_chat_event_info()** (3 connections) — `server/realtime/message_filtering.py`
- **.should_apply_mute_check()** (3 connections) — `server/realtime/message_filtering.py`
- **.compare_canonical_rooms()** (3 connections) — `server/realtime/message_filtering.py`
- **.get_player_room_from_online_players()** (3 connections) — `server/realtime/message_filtering.py`
- **.get_player_room_from_persistence()** (3 connections) — `server/realtime/message_filtering.py`
- **nats_message_handler()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **message_filtering_helper()** (3 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **.collect_room_targets()** (2 connections) — `server/realtime/message_filtering.py`
- **mock_connection_manager()** (2 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **test_extract_chat_event_info()** (2 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **test_should_apply_mute_check()** (2 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **test_compare_canonical_rooms()** (2 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **test_get_player_room_from_online_players()** (2 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- *... and 26 more nodes in this community*

## Relationships

- [game chat service](game_chat_service.md) (10 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (7 shared connections)
- [nats services service](nats_services_service.md) (3 shared connections)
- [command commands handler](command_commands_handler.md) (2 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (2 shared connections)
- [inventory schemas schema](inventory_schemas_schema.md) (2 shared connections)
- [follow game service](follow_game_service.md) (2 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (2 shared connections)
- [profession models rationale](profession_models_rationale.md) (2 shared connections)
- [message filtering realtime](message_filtering_realtime.md) (1 shared connections)
- [command factories create](command_factories_create.md) (1 shared connections)
- [Room Broadcast](Room_Broadcast.md) (1 shared connections)

## Source Files

- `server/realtime/message_filtering.py`
- `server/realtime/nats_message_handler.py`
- `server/tests/unit/realtime/conftest.py`
- `server/tests/unit/realtime/test_message_filtering_helpers.py`

## Audit Trail

- EXTRACTED: 147 (90%)
- INFERRED: 16 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*