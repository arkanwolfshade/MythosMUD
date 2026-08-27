# Hardening Dimensions

> 14 nodes

## Key Concepts

- **asyncio** (13 connections)
- **test_is_player_in_room_true()** (3 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_preload_receiver_mute_data()** (3 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_preload_receiver_mute_data_excludes_sender()** (3 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_check_player_mute_status_patched_and_emote()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_filter_target_players_room_and_mute()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_get_player_room_from_persistence_mock_player()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_get_player_room_from_persistence_no_layer()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_is_player_in_room_error_returns_false()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_is_player_in_room_via_persistence()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_is_player_muted_with_user_manager_async_paths()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **Test is_player_in_room() returns True when player is in room.** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **Test preload_receiver_mute_data() preloads mute data.** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **Test preload_receiver_mute_data() excludes sender from targets.** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`

## Relationships

- [MythosMUD Testing Strategy (Greenfield Suite)](MythosMUD_Testing_Strategy_Greenfield_Suite.md) (10 shared connections)
- [](unnamed.md) (3 shared connections)

## Source Files

- `server/tests/unit/realtime/test_message_filtering.py`

## Audit Trail

- EXTRACTED: 26 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*