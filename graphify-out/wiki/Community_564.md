# Community 564

> 30 nodes

## Key Concepts

- **test_enhanced_logging_config.py** (19 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **setup_enhanced_logging()** (11 connections) — `server/structured_logging/enhanced_logging_config.py`
- **configure_enhanced_structlog()** (10 connections) — `server/structured_logging/enhanced_logging_config.py`
- **test_configure_enhanced_structlog_configures_file_logging_when_enabled()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_setup_enhanced_logging_enabled_configures_uvicorn_and_sets_state()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_log_enhanced_logging_configured()** (5 connections) — `server/structured_logging/enhanced_logging_config.py`
- **_enabled_config()** (5 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_configure_enhanced_structlog_skips_file_logging_when_disabled()** (5 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_setup_enhanced_logging_disabled_skips_uvicorn_and_state()** (5 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_configure_structlog_with_fallback()** (4 connections) — `server/structured_logging/enhanced_logging_config.py`
- **_configure_third_party_log_levels()** (4 connections) — `server/structured_logging/enhanced_logging_config.py`
- **_disabled_config()** (4 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **MonkeyPatch** (4 connections)
- **_reset_logging_state()** (3 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **LoggingConfig** (3 connections)
- **Path** (3 connections)
- **LoggingConfig** (2 connections)
- **Processor** (1 connections)
- **fixture** (1 connections)
- **Configure structlog with the enhanced pipeline, falling back to a basic one on…** (1 connections) — `server/structured_logging/enhanced_logging_config.py`
- **Emit the one-time confirmation log that enhanced error logging is active.** (1 connections) — `server/structured_logging/enhanced_logging_config.py`
- **Set up enhanced logging configuration with MDC and security features. Args:…** (1 connections) — `server/structured_logging/enhanced_logging_config.py`
- **Set third-party loggers to avoid ERROR noise in errors.log (e.g. NATS…** (1 connections) — `server/structured_logging/enhanced_logging_config.py`
- **Configure enhanced Structlog with MDC, security, and performance features.…** (1 connections) — `server/structured_logging/enhanced_logging_config.py`
- **Unit tests for enhanced_logging_config helpers. Covers log_exception_once…** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- *... and 5 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (8 shared connections)
- [Community 454](Community_454.md) (5 shared connections)
- [Community 200](Community_200.md) (2 shared connections)
- [Community 186](Community_186.md) (1 shared connections)
- [Community 107](Community_107.md) (1 shared connections)
- [Auth Dependencies & Users](Auth_Dependencies_&_Users.md) (1 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (1 shared connections)

## Source Files

- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`

## Audit Trail

- EXTRACTED: 66 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*