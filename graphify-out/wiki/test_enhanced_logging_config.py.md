# test_enhanced_logging_config.py

> 33 nodes

## Key Concepts

- **test_enhanced_logging_config.py** (20 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **configure_enhanced_structlog()** (13 connections) — `server/structured_logging/enhanced_logging_config.py`
- **setup_enhanced_logging()** (11 connections) — `server/structured_logging/enhanced_logging_config.py`
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
- **MonkeyPatch** (4 connections)
- **_reset_logging_state()** (3 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Path** (3 connections)
- **.__init__()** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **BoundLogger** (1 connections)
- **fixture** (1 connections)
- **Set up enhanced logging configuration with MDC and security features. Args:…** (1 connections) — `server/structured_logging/enhanced_logging_config.py`
- **Set third-party loggers to avoid ERROR noise in errors.log (e.g. NATS…** (1 connections) — `server/structured_logging/enhanced_logging_config.py`
- **Configure enhanced Structlog with MDC, security, and performance features.…** (1 connections) — `server/structured_logging/enhanced_logging_config.py`
- **Unit tests for enhanced_logging_config helpers. Covers log_exception_once…** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **The disabled branch still configures structlog but must not touch uvicorn or…** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- *... and 8 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (9 shared connections)
- [logging_file_setup.py](logging_file_setup.py.md) (7 shared connections)
- [test_logging_processors.py](test_logging_processors.py.md) (4 shared connections)
- [PlayerDeathService](PlayerDeathService.md) (3 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (1 shared connections)
- [test_logging_utilities.py](test_logging_utilities.py.md) (1 shared connections)
- [test_logging_handlers.py](test_logging_handlers.py.md) (1 shared connections)
- [factory.py](factory.py.md) (1 shared connections)

## Source Files

- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`

## Audit Trail

- EXTRACTED: 72 (92%)
- INFERRED: 6 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*