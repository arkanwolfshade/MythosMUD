# Async Persistence Delegates

> 54 nodes

## Key Concepts

- **test_player_preferences_service.py** (59 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **preferences_service()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_get_player_preferences_success()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_update_default_channel_success()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_mute_channel_success()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_get_muted_channels_success()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_is_channel_muted_false()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_delete_player_preferences_not_found()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_mute_channel_not_found()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_unmute_channel_database_error()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_mute_channel_database_error()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_is_channel_muted_not_found()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **mock_session()** (2 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **sample_player_id()** (2 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_preferences_service_initialization()** (2 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_is_valid_player_id_uuid()** (2 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_is_valid_player_id_string()** (2 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_is_valid_channel_valid()** (2 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_is_valid_json_array_valid()** (2 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_is_valid_json_array_invalid()** (2 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_create_player_preferences_invalid_id()** (2 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_is_channel_muted_invalid_channel()** (2 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_unmute_channel_invalid_id()** (2 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_get_muted_channels_invalid_id()** (2 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_is_channel_muted_invalid_id()** (2 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- *... and 29 more nodes in this community*

## Relationships

- [Combat Command Handler](Combat_Command_Handler.md) (11 shared connections)
- [Client ASCII Map API](Client_ASCII_Map_API.md) (3 shared connections)
- [Quality Audit Report](Quality_Audit_Report.md) (2 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (1 shared connections)
- [test_create_player_preferences_already_exists](test_create_player_preferences_already_exists.md) (1 shared connections)
- [test_create_player_preferences_success](test_create_player_preferences_success.md) (1 shared connections)
- [test_create_player_preferences_with_string_id](test_create_player_preferences_with_string_id.md) (1 shared connections)
- [test_delete_player_preferences_database_error](test_delete_player_preferences_database_error.md) (1 shared connections)
- [test_delete_player_preferences_invalid_id](test_delete_player_preferences_invalid_id.md) (1 shared connections)
- [test_delete_player_preferences_success](test_delete_player_preferences_success.md) (1 shared connections)
- [test_get_muted_channels_not_found](test_get_muted_channels_not_found.md) (1 shared connections)
- [test_get_player_preferences_database_error](test_get_player_preferences_database_error.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_player_preferences_service.py`

## Audit Trail

- EXTRACTED: 139 (93%)
- INFERRED: 10 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*