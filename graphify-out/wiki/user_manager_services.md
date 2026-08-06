# user manager services

> 110 nodes

## Key Concepts

- **test_user_manager.py** (71 connections) — `server/tests/unit/services/test_user_manager.py`
- **mock_data_dir()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_user_manager_init()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_normalize_to_uuid_uuid()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_normalize_to_uuid_string()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_is_admin_sync_true()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_mute_player_success()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_mute_player_admin_immune()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_unmute_player_success()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_mute_channel_success()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_unmute_channel_not_muted()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_mute_global_admin_immune()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_unmute_global_success()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_unmute_global_not_muted()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_is_player_muted_false()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_is_player_muted_async_true()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_is_player_muted_async_false()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_is_globally_muted_false()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_can_send_message_true()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_can_send_message_player_muted()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_can_send_message_channel_muted()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_can_send_message_globally_muted()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_get_player_mutes()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_is_player_muted_by_others_true()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_is_player_muted_by_others_false()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- *... and 85 more nodes in this community*

## Relationships

- [room infrastructure persistence](room_infrastructure_persistence.md) (9 shared connections)
- [infrastructure persistence room](infrastructure_persistence_room.md) (4 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (1 shared connections)
- [services user manager](services_user_manager.md) (1 shared connections)
- [realtime monitoring performance](realtime_monitoring_performance.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_user_manager.py`

## Audit Trail

- EXTRACTED: 234 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*