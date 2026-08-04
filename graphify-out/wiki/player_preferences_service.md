# player preferences service

> 82 nodes

## Key Concepts

- **test_player_preferences_service.py** (59 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_create_player_preferences_success()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_create_player_preferences_already_exists()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_get_player_preferences_not_found()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_update_default_channel_success()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_update_default_channel_not_found()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_mute_channel_success()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_mute_channel_already_muted()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_unmute_channel_success()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_get_muted_channels_not_found()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_is_channel_muted_true()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_is_channel_muted_false()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_delete_player_preferences_success()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_delete_player_preferences_not_found()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_delete_player_preferences_database_error()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_mute_channel_database_error()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_is_channel_muted_not_found()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **mock_session()** (2 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **sample_player_id()** (2 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_is_valid_player_id_uuid()** (2 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_is_valid_player_id_string()** (2 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_is_valid_player_id_invalid_string()** (2 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_is_valid_player_id_empty()** (2 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_is_valid_channel_valid()** (2 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_is_valid_channel_invalid()** (2 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- *... and 57 more nodes in this community*

## Relationships

- [player requests schemas](player_requests_schemas.md) (17 shared connections)
- [room infrastructure persistence](room_infrastructure_persistence.md) (8 shared connections)
- [infrastructure persistence room](infrastructure_persistence_room.md) (4 shared connections)
- [commands rescue rationale](commands_rescue_rationale.md) (3 shared connections)
- [combat models rationale](combat_models_rationale.md) (1 shared connections)
- [npc combat service](npc_combat_service.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_player_preferences_service.py`

## Audit Trail

- EXTRACTED: 180 (92%)
- INFERRED: 16 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*