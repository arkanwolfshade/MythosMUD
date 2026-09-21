# test_message_filtering.py

> 159 nodes

## Key Concepts

- **test_message_filtering.py** (41 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **MessageFilteringHelper** (32 connections) — `server/realtime/message_filtering.py`
- **format_message_content()** (19 connections) — `server/realtime/message_formatters.py`
- **nats_message_handler_broadcast.py** (18 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **message_filtering.py** (16 connections) — `server/realtime/message_filtering.py`
- **test_message_formatters.py** (16 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **asyncio** (15 connections)
- **BroadcastFilterContext** (11 connections) — `server/realtime/message_filtering.py`
- **test_message_filtering_helpers.py** (10 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **message_formatters.py** (9 connections) — `server/realtime/message_formatters.py`
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
- **test_format_message_content_nats_error()** (4 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **.compare_canonical_rooms()** (3 connections) — `server/realtime/message_filtering.py`
- *... and 134 more nodes in this community*

## Relationships

- [NATSRetryHandler](NATSRetryHandler.md) (16 shared connections)
- [NATSError](NATSError.md) (11 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [apply_communication_dampening](apply_communication_dampening.md) (3 shared connections)
- [UserManager](UserManager.md) (2 shared connections)
- [user_manager.py](user_manager.py.md) (2 shared connections)
- [command_service.py](command_service.py.md) (1 shared connections)
- [PlayerGuidFormatter](PlayerGuidFormatter.md) (1 shared connections)
- [DatabaseManager](DatabaseManager.md) (1 shared connections)
- [LucidityService](LucidityService.md) (1 shared connections)

## Source Files

- `server/realtime/message_filtering.py`
- `server/realtime/message_formatters.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/tests/unit/realtime/test_message_filtering.py`
- `server/tests/unit/realtime/test_message_filtering_helpers.py`
- `server/tests/unit/realtime/test_message_formatters.py`

## Audit Trail

- EXTRACTED: 246 (94%)
- INFERRED: 15 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*