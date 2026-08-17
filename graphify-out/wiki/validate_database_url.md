# .validate_database_url

> 7 nodes

## Key Concepts

- **.validate_database_url()** (3 connections) — `server/config/models/server_db.py`
- **.validate_pool_config()** (3 connections) — `server/config/models/server_db.py`
- **.validate_port()** (3 connections) — `server/config/models/server_db.py`
- **field_validator** (3 connections)
- **Validate port is in valid range.** (1 connections) — `server/config/models/server_db.py`
- **Validate database URL format - PostgreSQL only.** (1 connections) — `server/config/models/server_db.py`
- **Validate pool configuration values are positive.** (1 connections) — `server/config/models/server_db.py`

## Relationships

- [config/models/__init__.py](config-models-__init__.py.md) (2 shared connections)
- [test_config_models.py](test_config_models.py.md) (1 shared connections)

## Source Files

- `server/config/models/server_db.py`

## Audit Trail

- EXTRACTED: 9 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*