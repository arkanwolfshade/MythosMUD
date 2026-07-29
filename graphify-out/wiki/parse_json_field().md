# parse json field()

> 12 nodes

## Key Concepts

- **parse_json_field()** (11 connections) — `server/npc/zone_config_loader.py`
- **test_parse_json_field_none()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_parse_json_field_string()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_parse_json_field_dict()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_parse_json_field_list()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_parse_json_field_invalid_json()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Parse a JSON field from database, handling both dict/list and string formats.** (1 connections) — `server/npc/zone_config_loader.py`
- **Test parse_json_field() returns default when None.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test parse_json_field() parses JSON string.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test parse_json_field() returns dict as-is.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test parse_json_field() returns list as-is.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test parse_json_field() raises error on invalid JSON string.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`

## Relationships

- [async load zone configurations()](async_load_zone_configurations%28%29.md) (7 shared connections)
- [TypedDict](TypedDict.md) (3 shared connections)

## Source Files

- `server/npc/zone_config_loader.py`
- `server/tests/unit/npc/test_zone_config_loader.py`

## Audit Trail

- EXTRACTED: 32 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*