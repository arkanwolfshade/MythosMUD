# test_message_filtering.py

> 12 nodes

## Key Concepts

- **test_message_filtering.py** (36 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_collect_room_targets()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_collect_room_targets_empty()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_get_user_manager_global()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_is_player_muted_by_receiver()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_is_player_muted_by_receiver_exception()** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_is_player_muted_global_mute_and_admin()** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **Unit tests for message filtering. Tests the MessageFilteringHelper class.** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **Test is_player_muted_by_receiver() checks mute status.** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **Test _get_user_manager() returns global user manager when custom not set.** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **Test collect_room_targets() returns subscribed players.** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **Test collect_room_targets() returns empty set when no subscribers.** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`

## Relationships

- [asyncio](asyncio.md) (10 shared connections)
- [message_filtering_helper](message_filtering_helper.md) (2 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (1 shared connections)
- [NATSError](NATSError.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [test_should_apply_mute_check_sensitive_channel](test_should_apply_mute_check_sensitive_channel.md) (1 shared connections)
- [test_should_apply_mute_check_non_sensitive_channel](test_should_apply_mute_check_non_sensitive_channel.md) (1 shared connections)
- [test_compare_canonical_rooms_same](test_compare_canonical_rooms_same.md) (1 shared connections)
- [test_compare_canonical_rooms_different](test_compare_canonical_rooms_different.md) (1 shared connections)
- [test_get_player_room_from_online_players](test_get_player_room_from_online_players.md) (1 shared connections)
- [test_get_player_room_from_online_players_not_found](test_get_player_room_from_online_players_not_found.md) (1 shared connections)
- [test_get_player_room_from_persistence_not_found](test_get_player_room_from_persistence_not_found.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_message_filtering.py`

## Audit Trail

- EXTRACTED: 40 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*