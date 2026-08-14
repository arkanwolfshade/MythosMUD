# async_load_zone_configurations

> 17 nodes

## Key Concepts

- **async_load_zone_configurations()** (13 connections) — `server/npc/zone_config_loader.py`
- **_empty_zone_load_result()** (13 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **asyncio** (11 connections)
- **test_async_load_zone_configurations_converts_url()** (6 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_passes_search_path_for_mythos_e2e()** (6 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_closes_connection()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_error()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_no_database_url()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_success()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **MonkeyPatch** (2 connections)
- **Async helper to load zone configurations from PostgreSQL database.** (1 connections) — `server/npc/zone_config_loader.py`
- **Test async_load_zone_configurations() loads configurations successfully.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test async_load_zone_configurations() converts SQLAlchemy URL format.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Regression: zones/subzones live in schema mythos_e2e; raw asyncpg must set…** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test async_load_zone_configurations() raises error when DATABASE_URL not set.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test async_load_zone_configurations() handles database errors.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test async_load_zone_configurations() closes connection.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`

## Relationships

- [test_zone_config_loader.py](test_zone_config_loader.py.md) (8 shared connections)
- [process_zone_rows](process_zone_rows.md) (7 shared connections)
- [process_subzone_rows](process_subzone_rows.md) (5 shared connections)
- [zone_config_loader.py](zone_config_loader.py.md) (3 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/npc/zone_config_loader.py`
- `server/tests/unit/npc/test_zone_config_loader.py`

## Audit Trail

- EXTRACTED: 51 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*