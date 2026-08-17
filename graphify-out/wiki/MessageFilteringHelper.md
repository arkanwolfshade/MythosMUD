# MessageFilteringHelper

> 50 nodes

## Key Concepts

- **MessageFilteringHelper** (25 connections) — `server/realtime/message_filtering.py`
- **test_message_filtering_helpers.py** (11 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **.check_player_mute_status()** (6 connections) — `server/realtime/message_filtering.py`
- **.filter_target_players()** (6 connections) — `server/realtime/message_filtering.py`
- **.is_player_in_room()** (6 connections) — `server/realtime/message_filtering.py`
- **message_filtering_helper()** (4 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **Any** (4 connections)
- **.compare_canonical_rooms()** (3 connections) — `server/realtime/message_filtering.py`
- **.extract_chat_event_info()** (3 connections) — `server/realtime/message_filtering.py`
- **.get_player_room_from_online_players()** (3 connections) — `server/realtime/message_filtering.py`
- **.get_player_room_from_persistence()** (3 connections) — `server/realtime/message_filtering.py`
- **._get_user_manager()** (3 connections) — `server/realtime/message_filtering.py`
- **.__init__()** (3 connections) — `server/realtime/message_filtering.py`
- **.is_player_muted_by_receiver()** (3 connections) — `server/realtime/message_filtering.py`
- **.is_player_muted_by_receiver_with_user_manager()** (3 connections) — `server/realtime/message_filtering.py`
- **.should_apply_mute_check()** (3 connections) — `server/realtime/message_filtering.py`
- **._is_player_muted_by_receiver()** (3 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **mock_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **.collect_room_targets()** (2 connections) — `server/realtime/message_filtering.py`
- **.preload_receiver_mute_data()** (2 connections) — `server/realtime/message_filtering.py`
- **test_compare_canonical_rooms()** (2 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **test_extract_chat_event_info()** (2 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **test_get_player_room_from_online_players()** (2 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **test_get_player_room_from_online_players_not_found()** (2 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **test_should_apply_mute_check()** (2 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- *... and 25 more nodes in this community*

## Relationships

- [NATSError](NATSError.md) (5 shared connections)
- [NATSMessageHandler](NATSMessageHandler.md) (2 shared connections)
- [test_message_filtering.py](test_message_filtering.py.md) (2 shared connections)
- [NATSMessageBroadcastMixin](NATSMessageBroadcastMixin.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/message_filtering.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/tests/unit/realtime/test_message_filtering_helpers.py`

## Audit Trail

- EXTRACTED: 68 (93%)
- INFERRED: 5 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*