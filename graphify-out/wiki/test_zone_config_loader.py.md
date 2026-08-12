# test_zone_config_loader.py

> 29 nodes

## Key Concepts

- **test_zone_config_loader.py** (35 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **async_load_zone_configurations()** (13 connections) — `server/npc/zone_config_loader.py`
- **_empty_zone_load_result()** (13 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **asyncio** (11 connections)
- **test_async_load_zone_configurations_converts_url()** (6 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_passes_search_path_for_mythos_e2e()** (6 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_closes_connection()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_error()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_no_database_url()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_success()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_subzone_rows()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_subzone_rows_empty()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_zone_rows()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_zone_rows_empty()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_zone_rows_json_strings()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **MonkeyPatch** (2 connections)
- **Async helper to load zone configurations from PostgreSQL database.** (1 connections) — `server/npc/zone_config_loader.py`
- **Unit tests for zone configuration loader. Tests the zone_config_loader module…** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test process_zone_rows() handles empty result.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test process_zone_rows() parses JSON string fields.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test process_subzone_rows() processes subzone rows.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test process_subzone_rows() handles empty result.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test async_load_zone_configurations() loads configurations successfully.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test async_load_zone_configurations() converts SQLAlchemy URL format.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Regression: zones/subzones live in schema mythos_e2e; raw asyncpg must set…** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- *... and 4 more nodes in this community*

## Relationships

- [zone_config_loader.py](zone_config_loader.py.md) (15 shared connections)
- [parse_json_field](parse_json_field.md) (6 shared connections)
- [extract_zone_name](extract_zone_name.md) (5 shared connections)
- [load_zone_configurations](load_zone_configurations.md) (4 shared connections)
- [HolidayService](HolidayService.md) (1 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (1 shared connections)

## Source Files

- `server/npc/zone_config_loader.py`
- `server/tests/unit/npc/test_zone_config_loader.py`

## Audit Trail

- EXTRACTED: 88 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*