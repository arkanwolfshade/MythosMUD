# test_message_filtering.py

> 123 nodes

## Key Concepts

- **test_message_filtering.py** (39 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **MessageFilteringHelper** (31 connections) — `server/realtime/message_filtering.py`
- **message_filtering.py** (16 connections) — `server/realtime/message_filtering.py`
- **asyncio** (13 connections)
- **BroadcastFilterContext** (11 connections) — `server/realtime/message_filtering.py`
- **test_message_filtering_helpers.py** (10 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **.check_player_mute_status()** (6 connections) — `server/realtime/message_filtering.py`
- **.is_player_in_room()** (6 connections) — `server/realtime/message_filtering.py`
- **._should_include_target()** (6 connections) — `server/realtime/message_filtering.py`
- **._debug_dump_receiver_mute_cache()** (5 connections) — `server/realtime/message_filtering.py`
- **.filter_target_players()** (5 connections) — `server/realtime/message_filtering.py`
- **test_filter_target_players_includes_allowed_player()** (5 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_filter_target_players_skips_mute_check_for_non_sensitive_channel()** (5 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **.get_player_room_from_online_players()** (4 connections) — `server/realtime/message_filtering.py`
- **.get_player_room_from_persistence()** (4 connections) — `server/realtime/message_filtering.py`
- **.is_player_muted_by_receiver()** (4 connections) — `server/realtime/message_filtering.py`
- **.is_player_muted_by_receiver_with_user_manager()** (4 connections) — `server/realtime/message_filtering.py`
- **message_filtering_helper()** (4 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **message_filtering_helper()** (4 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **.compare_canonical_rooms()** (3 connections) — `server/realtime/message_filtering.py`
- **.extract_chat_event_info()** (3 connections) — `server/realtime/message_filtering.py`
- **._get_user_manager()** (3 connections) — `server/realtime/message_filtering.py`
- **.__init__()** (3 connections) — `server/realtime/message_filtering.py`
- **._room_id_from_player_info()** (3 connections) — `server/realtime/message_filtering.py`
- **.should_apply_mute_check()** (3 connections) — `server/realtime/message_filtering.py`
- *... and 98 more nodes in this community*

## Relationships

- [NATSRetryHandler](NATSRetryHandler.md) (12 shared connections)
- [NATSError](NATSError.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [player_presence_tracker.py](player_presence_tracker.py.md) (1 shared connections)
- [UserManager](UserManager.md) (1 shared connections)

## Source Files

- `server/realtime/message_filtering.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/tests/unit/realtime/test_message_filtering.py`
- `server/tests/unit/realtime/test_message_filtering_helpers.py`

## Audit Trail

- EXTRACTED: 172 (92%)
- INFERRED: 14 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*