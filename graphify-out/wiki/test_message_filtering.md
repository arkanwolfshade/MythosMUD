# test message filtering

> 48 nodes

## Key Concepts

- **test_message_filtering.py** (26 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **message_filtering_helper()** (3 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **mock_connection_manager()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_message_filtering_helper_init()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_collect_room_targets()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_collect_room_targets_empty()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_preload_receiver_mute_data()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_preload_receiver_mute_data_excludes_sender()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_collect_room_targets_with_canonical_id()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_extract_chat_event_info()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_should_apply_mute_check_sensitive_channel()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_should_apply_mute_check_non_sensitive_channel()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_compare_canonical_rooms_same()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_compare_canonical_rooms_different()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_get_player_room_from_online_players()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_get_player_room_from_online_players_not_found()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_get_player_room_from_persistence()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_get_player_room_from_persistence_not_found()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_is_player_in_room_true()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_is_player_in_room_false()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_is_player_muted_by_receiver()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_is_player_muted_by_receiver_not_muted()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_get_user_manager_custom()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_get_user_manager_global()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **Unit tests for message filtering.  Tests the MessageFilteringHelper class.** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- *... and 23 more nodes in this community*

## Relationships

- [circuit breaker](circuit_breaker.md) (3 shared connections)

## Source Files

- `server/tests/unit/realtime/test_message_filtering.py`

## Audit Trail

- EXTRACTED: 97 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*