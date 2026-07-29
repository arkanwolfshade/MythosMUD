# . init ()

> 51 nodes

## Key Concepts

- **MessageFilteringHelper** (23 connections) — `server/realtime/message_filtering.py`
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
- **.preload_receiver_mute_data()** (3 connections) — `server/realtime/message_filtering.py`
- **.extract_chat_event_info()** (3 connections) — `server/realtime/message_filtering.py`
- **.should_apply_mute_check()** (3 connections) — `server/realtime/message_filtering.py`
- **.compare_canonical_rooms()** (3 connections) — `server/realtime/message_filtering.py`
- **.get_player_room_from_online_players()** (3 connections) — `server/realtime/message_filtering.py`
- **.get_player_room_from_persistence()** (3 connections) — `server/realtime/message_filtering.py`
- **._is_player_muted_by_receiver()** (3 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **message_filtering_helper()** (3 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **.collect_room_targets()** (2 connections) — `server/realtime/message_filtering.py`
- **mock_connection_manager()** (2 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **test_extract_chat_event_info()** (2 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **test_should_apply_mute_check()** (2 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **test_compare_canonical_rooms()** (2 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **test_get_player_room_from_online_players()** (2 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- *... and 26 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (4 shared connections)
- [message filtering](message_filtering.md) (2 shared connections)
- [Any](Any.md) (2 shared connections)
- [test message filtering](test_message_filtering.md) (2 shared connections)
- [UUID](UUID.md) (1 shared connections)
- [circuit breaker](circuit_breaker.md) (1 shared connections)
- [DeadLetterMessage](DeadLetterMessage.md) (1 shared connections)
- [as event data dict()](as_event_data_dict%28%29.md) (1 shared connections)
- [nats retry handler](nats_retry_handler.md) (1 shared connections)
- [message formatters](message_formatters.md) (1 shared connections)

## Source Files

- `server/realtime/message_filtering.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/tests/unit/realtime/test_message_filtering_helpers.py`

## Audit Trail

- EXTRACTED: 133 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*