# async_load_zone_configurations

> 27 nodes

## Key Concepts

- **async_load_zone_configurations()** (13 connections) — `server/npc/zone_config_loader.py`
- **_empty_zone_load_result()** (13 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **asyncio** (11 connections)
- **test_async_load_zone_configurations_converts_url()** (6 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_passes_search_path_for_mythos_e2e()** (6 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_subzone_rows()** (6 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_zone_rows()** (6 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_zone_rows_json_strings()** (6 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_closes_connection()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_error()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_no_database_url()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_success()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_subzone_rows_empty()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_zone_rows_empty()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **MonkeyPatch** (2 connections)
- **Async helper to load zone configurations from PostgreSQL database.** (1 connections) — `server/npc/zone_config_loader.py`
- **Test process_zone_rows() handles empty result.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test process_zone_rows() parses JSON string fields.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test process_subzone_rows() processes subzone rows.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test process_subzone_rows() handles empty result.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test async_load_zone_configurations() loads configurations successfully.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test async_load_zone_configurations() converts SQLAlchemy URL format.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Regression: zones/subzones live in schema mythos_e2e; raw asyncpg must set…** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test async_load_zone_configurations() raises error when DATABASE_URL not set.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test async_load_zone_configurations() handles database errors.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- *... and 2 more nodes in this community*

## Relationships

- [test_zone_config_loader.py](test_zone_config_loader.py.md) (13 shared connections)
- [zone_config_loader.py](zone_config_loader.py.md) (10 shared connections)
- [NPCDefinition](NPCDefinition.md) (3 shared connections)
- [npc_database.py](npc_database.py.md) (1 shared connections)

## Source Files

- `server/npc/zone_config_loader.py`
- `server/tests/unit/npc/test_zone_config_loader.py`

## Audit Trail

- EXTRACTED: 65 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*