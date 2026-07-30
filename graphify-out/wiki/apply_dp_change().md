# .apply dp change()

> 32 nodes

## Key Concepts

- **test_zone_config_loader.py** (35 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **parse_json_field()** (11 connections) — `server/npc/zone_config_loader.py`
- **extract_zone_name()** (9 connections) — `server/npc/zone_config_loader.py`
- **load_zone_configurations()** (9 connections) — `server/npc/zone_config_loader.py`
- **test_parse_json_field_none()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_parse_json_field_string()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_parse_json_field_dict()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_parse_json_field_list()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_parse_json_field_invalid_json()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_extract_zone_name_with_slash()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_extract_zone_name_no_slash()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_extract_zone_name_multiple_slashes()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_extract_zone_name_empty()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_load_zone_configurations_success()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_load_zone_configurations_merges_zone_and_subzone()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_load_zone_configurations_error()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Parse a JSON field from database, handling both dict/list and string formats.** (1 connections) — `server/npc/zone_config_loader.py`
- **Extract zone name from stable_id (format: 'plane/zone').      Args:         stab** (1 connections) — `server/npc/zone_config_loader.py`
- **Load zone and sub-zone configurations from PostgreSQL database.      Returns:** (1 connections) — `server/npc/zone_config_loader.py`
- **Unit tests for zone configuration loader.  Tests the zone_config_loader module f** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test parse_json_field() returns default when None.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test parse_json_field() parses JSON string.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test parse_json_field() returns dict as-is.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test parse_json_field() returns list as-is.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test parse_json_field() raises error on invalid JSON string.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- *... and 7 more nodes in this community*

## Relationships

- [HealthMonitor](HealthMonitor.md) (14 shared connections)
- [memory lifespan coordinator](memory_lifespan_coordinator.md) (9 shared connections)
- [datetime](datetime.md) (3 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (2 shared connections)
- [Represents the configuration for a](Represents_the_configuration_for_a.md) (2 shared connections)

## Source Files

- `server/npc/zone_config_loader.py`
- `server/tests/unit/npc/test_zone_config_loader.py`

## Audit Trail

- EXTRACTED: 116 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*