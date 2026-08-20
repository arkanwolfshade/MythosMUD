# LoggingConfig

> 15 nodes

## Key Concepts

- **LoggingConfig** (10 connections) — `server/config/models/security_logging.py`
- **SecurityConfig** (7 connections) — `server/config/models/security_logging.py`
- **field_validator** (4 connections)
- **.to_legacy_dict()** (3 connections) — `server/config/models/security_logging.py`
- **.validate_environment()** (3 connections) — `server/config/models/security_logging.py`
- **.validate_admin_password()** (3 connections) — `server/config/models/security_logging.py`
- **.validate_format()** (2 connections) — `server/config/models/security_logging.py`
- **.validate_level()** (2 connections) — `server/config/models/security_logging.py`
- **BaseSettings** (2 connections)
- **Any** (1 connections)
- **Security-sensitive configuration.** (1 connections) — `server/config/models/security_logging.py`
- **Validate admin password strength (production only).** (1 connections) — `server/config/models/security_logging.py`
- **Logging configuration.** (1 connections) — `server/config/models/security_logging.py`
- **Validate logging environment.** (1 connections) — `server/config/models/security_logging.py`
- **Convert to legacy logging config dict format for backward compatibility.…** (1 connections) — `server/config/models/security_logging.py`

## Relationships

- [config/models/__init__.py](config-models-__init__.py.md) (4 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [AppConfig](AppConfig.md) (2 shared connections)

## Source Files

- `server/config/models/security_logging.py`

## Audit Trail

- EXTRACTED: 23 (92%)
- INFERRED: 2 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*