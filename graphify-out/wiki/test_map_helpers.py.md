# test_map_helpers.py

> 46 nodes · cohesion 0.07

## Key Concepts

- **LoggingConfig** (30 connections) — `server/config/models/security_logging.py`
- **test_enhanced_logging_config.py** (20 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **configure_enhanced_structlog()** (14 connections) — `server/structured_logging/enhanced_logging_config.py`
- **setup_enhanced_logging()** (11 connections) — `server/structured_logging/enhanced_logging_config.py`
- **_StubBoundLogger** (7 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_as_bound_logger()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_configure_enhanced_structlog_configures_file_logging_when_enabled()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_log_exception_once_logged_exception_uses_mark_logged()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_log_exception_once_plain_exception_sets_flag_and_skips_repeat()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_setup_enhanced_logging_enabled_configures_uvicorn_and_sets_state()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_log_enhanced_logging_configured()** (5 connections) — `server/structured_logging/enhanced_logging_config.py`
- **_enabled_config()** (5 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_configure_enhanced_structlog_skips_file_logging_when_disabled()** (5 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_setup_enhanced_logging_disabled_skips_uvicorn_and_state()** (5 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_configure_structlog_with_fallback()** (4 connections) — `server/structured_logging/enhanced_logging_config.py`
- **_configure_third_party_log_levels()** (4 connections) — `server/structured_logging/enhanced_logging_config.py`
- **_disabled_config()** (4 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **MonkeyPatch** (4 connections)
- **test_logging_config_rotation_backup_count_default()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_logging_config_rotation_backup_count_override()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **Path** (3 connections)
- **_reset_logging_state()** (3 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **BaseSettings** (2 connections)
- **Processor** (1 connections)
- **Logging configuration.** (1 connections) — `server/config/models/security_logging.py`
- *... and 21 more nodes in this community*

## Relationships

- [Room](Room.md) (17 shared connections)
- [GameClientV2.tsx](GameClientV2.tsx.md) (12 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (4 shared connections)
- [LootAllRequest](LootAllRequest.md) (4 shared connections)
- [AttributeError](AttributeError.md) (3 shared connections)
- [test_lifecycle_respawn.py](test_lifecycle_respawn.py.md) (3 shared connections)
- [test_windows_safe_rotation.py](test_windows_safe_rotation.py.md) (1 shared connections)
- [CatalogPage.tsx](CatalogPage.tsx.md) (1 shared connections)
- [test_status_commands.py](test_status_commands.py.md) (1 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (1 shared connections)

## Source Files

- `server/config/models/security_logging.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/config/test_config_models.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`

## Audit Trail

- EXTRACTED: 100 (86%)
- INFERRED: 16 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*