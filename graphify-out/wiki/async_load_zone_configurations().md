# async load zone configurations()

> 34 nodes

## Key Concepts

- **test_zone_config_loader.py** (35 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **process_zone_rows()** (13 connections) — `server/npc/zone_config_loader.py`
- **async_load_zone_configurations()** (13 connections) — `server/npc/zone_config_loader.py`
- **_empty_zone_load_result()** (13 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **ZoneLoadResult** (12 connections) — `server/npc/zone_config_loader.py`
- **process_subzone_rows()** (9 connections) — `server/npc/zone_config_loader.py`
- **test_process_zone_rows()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_subzone_rows()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_converts_url()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_passes_search_path_for_mythos_e2e()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_zone_rows_empty()** (4 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_zone_rows_json_strings()** (4 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_subzone_rows_empty()** (4 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_success()** (4 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_no_database_url()** (4 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_error()** (4 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_closes_connection()** (4 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Connection** (2 connections)
- **MonkeyPatch** (2 connections)
- **Test process_zone_rows() handles empty result.** (2 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Result of loading zone and sub-zone configs from PostgreSQL.** (1 connections) — `server/npc/zone_config_loader.py`
- **Process zone rows from database and populate zone configurations.      Args:** (1 connections) — `server/npc/zone_config_loader.py`
- **Process subzone rows from database and populate subzone configurations.      Arg** (1 connections) — `server/npc/zone_config_loader.py`
- **Async helper to load zone configurations from PostgreSQL database.** (1 connections) — `server/npc/zone_config_loader.py`
- **Unit tests for zone configuration loader.  Tests the zone_config_loader module f** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- *... and 9 more nodes in this community*

## Relationships

- [TypedDict](TypedDict.md) (12 shared connections)
- [parse json field()](parse_json_field%28%29.md) (7 shared connections)
- [extract zone name()](extract_zone_name%28%29.md) (6 shared connections)
- [Represents the configuration for a](Represents_the_configuration_for_a.md) (5 shared connections)
- [load zone configurations()](load_zone_configurations%28%29.md) (4 shared connections)
- [get asyncpg server settings for](get_asyncpg_server_settings_for.md) (1 shared connections)

## Source Files

- `server/npc/zone_config_loader.py`
- `server/tests/unit/npc/test_zone_config_loader.py`

## Audit Trail

- EXTRACTED: 158 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*