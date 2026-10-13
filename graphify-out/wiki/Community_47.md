# Community 47

> 130 nodes

## Key Concepts

- **test_message_filtering.py** (38 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **MessageFilteringHelper** (31 connections) — `server/realtime/message_filtering.py`
- **nats_message_handler.py** (31 connections) — `server/realtime/nats_message_handler.py`
- **user_manager.py** (22 connections) — `server/services/user_manager.py`
- **nats_message_handler_base.py** (20 connections) — `server/realtime/nats_message_handler_base.py`
- **message_filtering.py** (15 connections) — `server/realtime/message_filtering.py`
- **nats_message_handler_broadcast.py** (15 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **asyncio** (13 connections)
- **BroadcastFilterContext** (11 connections) — `server/realtime/message_filtering.py`
- **nats_message_handler_subscriptions.py** (10 connections) — `server/realtime/nats_message_handler_subscriptions.py`
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
- *... and 105 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (21 shared connections)
- [Community 85](Community_85.md) (6 shared connections)
- [Community 417](Community_417.md) (5 shared connections)
- [Community 63](Community_63.md) (5 shared connections)
- [Community 41](Community_41.md) (5 shared connections)
- [Community 1169](Community_1169.md) (4 shared connections)
- [Community 805](Community_805.md) (3 shared connections)
- [Community 137](Community_137.md) (3 shared connections)
- [Community 140](Community_140.md) (3 shared connections)
- [Community 312](Community_312.md) (3 shared connections)
- [Community 328](Community_328.md) (2 shared connections)
- [Community 265](Community_265.md) (2 shared connections)

## Source Files

- `server/realtime/message_filtering.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/nats_message_handler_base.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/realtime/nats_message_handler_subscriptions.py`
- `server/services/user_manager.py`
- `server/tests/unit/realtime/test_message_filtering.py`
- `server/tests/unit/realtime/test_message_filtering_helpers.py`

## Audit Trail

- EXTRACTED: 252 (95%)
- INFERRED: 13 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*