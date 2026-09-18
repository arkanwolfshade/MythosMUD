# Community 390

> 45 nodes

## Key Concepts

- **LoggingConfig** (27 connections) — `server/config/models/security_logging.py`
- **test_enhanced_logging_config.py** (19 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **setup_enhanced_logging()** (11 connections) — `server/structured_logging/enhanced_logging_config.py`
- **security_logging.py** (10 connections) — `server/config/models/security_logging.py`
- **configure_enhanced_structlog()** (9 connections) — `server/structured_logging/enhanced_logging_config.py`
- **_StubBoundLogger** (7 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_as_bound_logger()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_configure_enhanced_structlog_configures_file_logging_when_enabled()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_setup_enhanced_logging_enabled_configures_uvicorn_and_sets_state()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_enabled_config()** (5 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_configure_enhanced_structlog_skips_file_logging_when_disabled()** (5 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_log_exception_once_logged_exception_uses_mark_logged()** (5 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
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

- [Community 225](Community_225.md) (12 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (10 shared connections)
- [AppConfig Composite Settings](AppConfig_Composite_Settings.md) (8 shared connections)
- [Community 504](Community_504.md) (3 shared connections)
- [Community 309](Community_309.md) (2 shared connections)
- [Community 189](Community_189.md) (2 shared connections)
- [Community 57](Community_57.md) (1 shared connections)
- [Community 201](Community_201.md) (1 shared connections)
- [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md) (1 shared connections)

## Source Files

- `server/config/models/security_logging.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`

## Audit Trail

- EXTRACTED: 98 (89%)
- INFERRED: 12 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*