# test_user_manager.py

> 26 nodes

## Key Concepts

- **test_user_manager.py** (72 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_can_send_message_channel_muted()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_can_send_message_player_muted()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_cleanup_expired_mutes()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_is_admin_sync_false()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_is_channel_muted_true()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_is_globally_muted_true()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_is_player_muted_true()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_load_player_mutes_invalid_uuid_in_data()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_mute_global_success()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_normalize_to_uuid_string()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_save_player_mutes_serialization_error()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_unmute_channel_not_muted()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **Unit tests for user manager service. Tests the UserManager class.** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test unmute_channel() when channel is not muted.** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test mute_global() successfully globally mutes a player.** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test is_player_muted() returns True when player is muted.** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test is_channel_muted() returns True when channel is muted.** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test is_globally_muted() returns True when player is globally muted.** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test can_send_message() behavior when target player is muted.** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test can_send_message() returns False when channel is muted.** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test _cleanup_expired_mutes() cleans up expired mutes.** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test load_player_mutes() handles invalid UUID in data.** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test _normalize_to_uuid() with string UUID.** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test save_player_mutes() handles serialization error.** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- *... and 1 more nodes in this community*

## Relationships

- [asyncio](asyncio.md) (16 shared connections)
- [user_manager](user_manager.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [UserManager](UserManager.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [test_unmute_player_not_muted](test_unmute_player_not_muted.md) (1 shared connections)
- [test_mute_channel_success](test_mute_channel_success.md) (1 shared connections)
- [test_mute_channel_already_muted](test_mute_channel_already_muted.md) (1 shared connections)
- [test_unmute_channel_success](test_unmute_channel_success.md) (1 shared connections)
- [test_mute_global_admin_immune](test_mute_global_admin_immune.md) (1 shared connections)
- [test_unmute_global_success](test_unmute_global_success.md) (1 shared connections)
- [test_unmute_global_not_muted](test_unmute_global_not_muted.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_user_manager.py`

## Audit Trail

- EXTRACTED: 84 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*