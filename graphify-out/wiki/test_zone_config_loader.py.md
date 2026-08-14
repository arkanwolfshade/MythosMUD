# test_zone_config_loader.py

> 20 nodes

## Key Concepts

- **test_zone_config_loader.py** (35 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **parse_json_field()** (11 connections) — `server/npc/zone_config_loader.py`
- **test_load_zone_configurations_error()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_load_zone_configurations_merges_zone_and_subzone()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_load_zone_configurations_success()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_parse_json_field_dict()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_parse_json_field_invalid_json()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_parse_json_field_list()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_parse_json_field_none()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_parse_json_field_string()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Parse a JSON field from database, handling both dict/list and string formats.…** (1 connections) — `server/npc/zone_config_loader.py`
- **Unit tests for zone configuration loader. Tests the zone_config_loader module…** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test load_zone_configurations() loads configurations.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test load_zone_configurations() merges zone and subzone configs.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test parse_json_field() returns default when None.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test load_zone_configurations() raises RuntimeError on failure.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test parse_json_field() parses JSON string.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test parse_json_field() returns dict as-is.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test parse_json_field() returns list as-is.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test parse_json_field() raises error on invalid JSON string.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`

## Relationships

- [async_load_zone_configurations](async_load_zone_configurations.md) (8 shared connections)
- [zone_config_loader.py](zone_config_loader.py.md) (5 shared connections)
- [process_zone_rows](process_zone_rows.md) (5 shared connections)
- [extract_zone_name](extract_zone_name.md) (5 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (4 shared connections)
- [process_subzone_rows](process_subzone_rows.md) (3 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (2 shared connections)

## Source Files

- `server/npc/zone_config_loader.py`
- `server/tests/unit/npc/test_zone_config_loader.py`

## Audit Trail

- EXTRACTED: 56 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*