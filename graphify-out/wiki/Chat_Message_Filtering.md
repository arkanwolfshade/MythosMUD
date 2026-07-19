# Chat Message Filtering

> 93 nodes · cohesion 0.03

## Key Concepts

- **MessageFilteringHelper** (25 connections) — `server/realtime/message_filtering.py`
- **test_message_filtering.py** (25 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_message_filtering_helpers.py** (9 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **.filter_target_players()** (6 connections) — `server/realtime/message_filtering.py`
- **.is_player_in_room()** (6 connections) — `server/realtime/message_filtering.py`
- **.check_player_mute_status()** (5 connections) — `server/realtime/message_filtering.py`
- **Any** (4 connections) — `server/realtime/message_filtering.py`
- **.compare_canonical_rooms()** (3 connections) — `server/realtime/message_filtering.py`
- **.extract_chat_event_info()** (3 connections) — `server/realtime/message_filtering.py`
- **.get_player_room_from_online_players()** (3 connections) — `server/realtime/message_filtering.py`
- **.get_player_room_from_persistence()** (3 connections) — `server/realtime/message_filtering.py`
- **._get_user_manager()** (3 connections) — `server/realtime/message_filtering.py`
- **.__init__()** (3 connections) — `server/realtime/message_filtering.py`
- **.is_player_muted_by_receiver()** (3 connections) — `server/realtime/message_filtering.py`
- **.is_player_muted_by_receiver_with_user_manager()** (3 connections) — `server/realtime/message_filtering.py`
- **.should_apply_mute_check()** (3 connections) — `server/realtime/message_filtering.py`
- **message_filtering_helper()** (3 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **message_filtering_helper()** (3 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **.collect_room_targets()** (2 connections) — `server/realtime/message_filtering.py`
- **.preload_receiver_mute_data()** (2 connections) — `server/realtime/message_filtering.py`
- **mock_connection_manager()** (2 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **test_compare_canonical_rooms()** (2 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **test_extract_chat_event_info()** (2 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **test_get_player_room_from_online_players()** (2 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **test_get_player_room_from_online_players_not_found()** (2 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- *... and 68 more nodes in this community*

## Relationships

- [[NATS Chat Broadcasting]] (3 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[Circuit Breaker Core]] (1 shared connections)

## Source Files

- `server/realtime/message_filtering.py`
- `server/tests/unit/realtime/test_message_filtering.py`
- `server/tests/unit/realtime/test_message_filtering_helpers.py`

## Audit Trail

- EXTRACTED: 217 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
