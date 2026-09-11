# LoggingConfig

> 45 nodes

## Key Concepts

- **LoggingConfig** (25 connections) — `server/config/models/security_logging.py`
- **test_enhanced_logging_config.py** (20 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **configure_enhanced_structlog()** (13 connections) — `server/structured_logging/enhanced_logging_config.py`
- **setup_enhanced_logging()** (11 connections) — `server/structured_logging/enhanced_logging_config.py`
- **security_logging.py** (10 connections) — `server/config/models/security_logging.py`
- **_StubBoundLogger** (7 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_as_bound_logger()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_configure_enhanced_structlog_configures_file_logging_when_enabled()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_log_exception_once_logged_exception_uses_mark_logged()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_setup_enhanced_logging_enabled_configures_uvicorn_and_sets_state()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_enabled_config()** (5 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_configure_enhanced_structlog_skips_file_logging_when_disabled()** (5 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_log_exception_once_plain_exception_sets_flag_and_skips_repeat()** (5 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_setup_enhanced_logging_disabled_skips_uvicorn_and_state()** (5 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_configure_third_party_log_levels()** (4 connections) — `server/structured_logging/enhanced_logging_config.py`
- **_disabled_config()** (4 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **field_validator** (4 connections)
- **MonkeyPatch** (4 connections)
- **.validate_environment()** (3 connections) — `server/config/models/security_logging.py`
- **.validate_admin_password()** (3 connections) — `server/config/models/security_logging.py`
- **_reset_logging_state()** (3 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Path** (3 connections)
- **.validate_format()** (2 connections) — `server/config/models/security_logging.py`
- **.validate_level()** (2 connections) — `server/config/models/security_logging.py`
- **BaseSettings** (2 connections)
- *... and 20 more nodes in this community*

## Relationships

- [logging_file_setup.py](logging_file_setup.py.md) (13 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [NATSService](NATSService.md) (8 shared connections)
- [test_logging_processors.py](test_logging_processors.py.md) (4 shared connections)
- [PlayerDeathService](PlayerDeathService.md) (3 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (1 shared connections)
- [test_logging_utilities.py](test_logging_utilities.py.md) (1 shared connections)
- [test_logging_handlers.py](test_logging_handlers.py.md) (1 shared connections)

## Source Files

- `server/config/models/security_logging.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`

## Audit Trail

- EXTRACTED: 100 (88%)
- INFERRED: 14 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*