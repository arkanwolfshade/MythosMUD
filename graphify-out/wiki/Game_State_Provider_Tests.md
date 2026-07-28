# Game State Provider Tests

> 34 nodes · cohesion 0.06

## Key Concepts

- **test_message_filtering.py** (26 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_collect_room_targets()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_collect_room_targets_empty()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_collect_room_targets_with_canonical_id()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_compare_canonical_rooms_same()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_extract_chat_event_info()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_get_player_room_from_online_players()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_get_player_room_from_online_players_not_found()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_get_player_room_from_persistence()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_get_player_room_from_persistence_not_found()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_get_user_manager_global()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_is_player_in_room_false()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_is_player_in_room_true()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_message_filtering_helper_init()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_preload_receiver_mute_data()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_should_apply_mute_check_non_sensitive_channel()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_should_apply_mute_check_sensitive_channel()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **Unit tests for message filtering.  Tests the MessageFilteringHelper class.** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **Test should_apply_mute_check() returns True for sensitive channels.** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **Test should_apply_mute_check() returns False for non-sensitive channels.** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **Test compare_canonical_rooms() returns True for same rooms.** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **Test get_player_room_from_online_players() returns player room.** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **Test get_player_room_from_online_players() returns None when player not found.** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **Test get_player_room_from_persistence() returns player room.** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **Test get_player_room_from_persistence() returns None when player not found.** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- *... and 9 more nodes in this community*

## Relationships

- [Playwright Remediation Plan](Playwright_Remediation_Plan.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [Migration Verification](Migration_Verification.md) (1 shared connections)
- [Persistence Async Migration](Persistence_Async_Migration.md) (1 shared connections)
- [Game Quest Service](Game_Quest_Service.md) (1 shared connections)
- [Refactoring Summary](Refactoring_Summary.md) (1 shared connections)
- [E 2 E Remaining Work](E_2_E_Remaining_Work.md) (1 shared connections)
- [Npc Idle Movement](Npc_Idle_Movement.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_message_filtering.py`

## Audit Trail

- EXTRACTED: 75 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*