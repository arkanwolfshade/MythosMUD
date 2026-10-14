# LoggingConfig

> 42 nodes

## Key Concepts

- **LoggingConfig** (30 connections) — `server/config/models/security_logging.py`
- **test_enhanced_logging_config.py** (20 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **configure_enhanced_structlog()** (14 connections) — `server/structured_logging/enhanced_logging_config.py`
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
- **_disabled_config()** (4 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **MonkeyPatch** (4 connections)
- **test_logging_config_rotation_backup_count_default()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_logging_config_rotation_backup_count_override()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **_reset_logging_state()** (3 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Path** (3 connections)
- **BaseSettings** (2 connections)
- **.error()** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **.__init__()** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Processor** (1 connections)
- **BoundLogger** (1 connections)
- *... and 17 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (13 shared connections)
- [logging_file_setup.py](logging_file_setup.py.md) (12 shared connections)
- [NATSService](NATSService.md) (6 shared connections)
- [ValueError](ValueError.md) (4 shared connections)
- [test_logging_processors.py](test_logging_processors.py.md) (4 shared connections)
- [test_config_models.py](test_config_models.py.md) (3 shared connections)
- [PlayerDeathService](PlayerDeathService.md) (3 shared connections)
- [test_logging_utilities.py](test_logging_utilities.py.md) (1 shared connections)

## Source Files

- `server/config/models/security_logging.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/config/test_config_models.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`

## Audit Trail

- EXTRACTED: 91 (85%)
- INFERRED: 16 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*