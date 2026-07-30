# HealthMonitor

> 33 nodes

## Key Concepts

- **test_zone_config_loader.py** (35 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **process_zone_rows()** (13 connections) — `server/npc/zone_config_loader.py`
- **async_load_zone_configurations()** (13 connections) — `server/npc/zone_config_loader.py`
- **_empty_zone_load_result()** (13 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
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
- **Process zone rows from database and populate zone configurations.      Args:** (1 connections) — `server/npc/zone_config_loader.py`
- **Process subzone rows from database and populate subzone configurations.      Arg** (1 connections) — `server/npc/zone_config_loader.py`
- **Async helper to load zone configurations from PostgreSQL database.** (1 connections) — `server/npc/zone_config_loader.py`
- **Unit tests for zone configuration loader.  Tests the zone_config_loader module f** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test process_zone_rows() processes zone rows.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test process_zone_rows() handles empty result.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test process_zone_rows() parses JSON string fields.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- *... and 8 more nodes in this community*

## Relationships

- [memory lifespan coordinator](memory_lifespan_coordinator.md) (12 shared connections)
- [.apply dp change()](apply_dp_change%28%29.md) (7 shared connections)
- [src/**/*.spec](src-__-_.spec.md) (6 shared connections)
- [Represents the configuration for a](Represents_the_configuration_for_a.md) (4 shared connections)
- [MutableHeaders](MutableHeaders.md) (4 shared connections)
- [rate overrides](rate_overrides.md) (1 shared connections)

## Source Files

- `server/npc/zone_config_loader.py`
- `server/tests/unit/npc/test_zone_config_loader.py`

## Audit Trail

- EXTRACTED: 148 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*