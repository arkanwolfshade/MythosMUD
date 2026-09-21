# LoggingConfig

> 56 nodes

## Key Concepts

- **LoggingConfig** (29 connections) — `server/config/models/security_logging.py`
- **test_enhanced_logging_config.py** (20 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **configure_enhanced_structlog()** (14 connections) — `server/structured_logging/enhanced_logging_config.py`
- **setup_enhanced_logging()** (11 connections) — `server/structured_logging/enhanced_logging_config.py`
- **security_logging.py** (10 connections) — `server/config/models/security_logging.py`
- **SecurityConfig** (7 connections) — `server/config/models/security_logging.py`
- **_StubBoundLogger** (7 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_as_bound_logger()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_configure_enhanced_structlog_configures_file_logging_when_enabled()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_log_exception_once_logged_exception_uses_mark_logged()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_setup_enhanced_logging_enabled_configures_uvicorn_and_sets_state()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_log_enhanced_logging_configured()** (5 connections) — `server/structured_logging/enhanced_logging_config.py`
- **_enabled_config()** (5 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_configure_enhanced_structlog_skips_file_logging_when_disabled()** (5 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_log_exception_once_plain_exception_sets_flag_and_skips_repeat()** (5 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_setup_enhanced_logging_disabled_skips_uvicorn_and_state()** (5 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_configure_structlog_with_fallback()** (4 connections) — `server/structured_logging/enhanced_logging_config.py`
- **_configure_third_party_log_levels()** (4 connections) — `server/structured_logging/enhanced_logging_config.py`
- **_disabled_config()** (4 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **field_validator** (4 connections)
- **MonkeyPatch** (4 connections)
- **.validate_environment()** (3 connections) — `server/config/models/security_logging.py`
- **.validate_admin_password()** (3 connections) — `server/config/models/security_logging.py`
- **test_logging_config_rotation_backup_count_default()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_logging_config_rotation_backup_count_override()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- *... and 31 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (17 shared connections)
- [logging_file_setup.py](logging_file_setup.py.md) (12 shared connections)
- [test_logging_processors.py](test_logging_processors.py.md) (4 shared connections)
- [test_config_models.py](test_config_models.py.md) (3 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (3 shared connections)
- [test_player_death_service.py](test_player_death_service.py.md) (3 shared connections)
- [test_logging_utilities.py](test_logging_utilities.py.md) (2 shared connections)
- [AppConfig](AppConfig.md) (2 shared connections)
- [MythosChronicle](MythosChronicle.md) (1 shared connections)
- [test_logging_handlers.py](test_logging_handlers.py.md) (1 shared connections)
- [factory.py](factory.py.md) (1 shared connections)

## Source Files

- `server/config/models/security_logging.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/config/test_config_models.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`

## Audit Trail

- EXTRACTED: 117 (88%)
- INFERRED: 16 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*