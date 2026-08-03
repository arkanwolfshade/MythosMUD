# npc combat service

> 51 nodes

## Key Concepts

- **Result** (54 connections) — `scripts/run_test_ci.py`
- **test_create_player_preferences_success()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_create_player_preferences_with_string_id()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_create_player_preferences_already_exists()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_get_player_preferences_success()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_get_player_preferences_not_found()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_update_default_channel_success()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_update_default_channel_not_found()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_mute_channel_success()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_mute_channel_already_muted()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_unmute_channel_success()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_unmute_channel_not_muted()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_get_muted_channels_success()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_get_muted_channels_not_found()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_is_channel_muted_true()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_is_channel_muted_false()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_delete_player_preferences_success()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_delete_player_preferences_not_found()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_delete_player_preferences_database_error()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_update_default_channel_database_error()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_mute_channel_not_found()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_unmute_channel_not_found()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_unmute_channel_database_error()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_mute_channel_database_error()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **test_is_channel_muted_not_found()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- *... and 26 more nodes in this community*

## Relationships

- [player preferences service](player_preferences_service.md) (24 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (14 shared connections)
- [player service game](player_service_game.md) (11 shared connections)
- [correct patterns examples](correct_patterns_examples.md) (1 shared connections)
- [examples migration logging](examples_migration_logging.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)

## Source Files

- `scripts/run_test_ci.py`
- `server/tests/unit/services/test_player_preferences_service.py`

## Audit Trail

- EXTRACTED: 77 (51%)
- INFERRED: 75 (49%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*