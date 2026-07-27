# User Manager Mute Tests

> 129 nodes · cohesion 0.02

## Key Concepts

- **test_user_manager.py** (70 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test is_player_muted() returns True when player is muted.** (4 connections) — `server/tests/unit/services/test_user_manager.py`
- **user_manager()** (3 connections) — `server/tests/unit/services/test_user_manager.py`
- **mock_data_dir()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test is_globally_muted() returns True when player is globally muted.** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test can_send_message() returns False when channel is muted.** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test get_player_mutes() returns player mutes.** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test load_player_mutes() handles invalid JSON.** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_add_admin_no_container()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_add_admin_no_container_duplicate()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_add_admin_no_persistence()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_add_admin_player_not_found()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_add_admin_success()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_can_send_message_channel_muted()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_can_send_message_globally_muted()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_can_send_message_player_muted()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_can_send_message_true()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_cleanup_expired_mutes()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_cleanup_player_mutes_no_delete_file()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_cleanup_player_mutes_with_delete_file()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_get_player_mute_file()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_get_player_mutes()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_get_player_mutes_empty()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_get_player_mutes_with_mutes()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_get_who_muted_player()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- *... and 104 more nodes in this community*

## Relationships

- [[Player Mute Persistence]] (2 shared connections)
- [[Rate Limiter Service]] (1 shared connections)

## Source Files

- `server/tests/unit/services/test_user_manager.py`

## Audit Trail

- EXTRACTED: 273 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
