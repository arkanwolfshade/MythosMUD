# models npc rationale

> 17 nodes

## Key Concepts

- **parse_json_field()** (11 connections) — `server/npc/zone_config_loader.py`
- **_store_subzone_row()** (9 connections) — `server/npc/zone_config_loader.py`
- **parse_zone_special_rules()** (6 connections) — `server/npc/zone_config_loader.py`
- **test_parse_json_field_none()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_parse_json_field_string()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_parse_json_field_dict()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_parse_json_field_list()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_parse_json_field_invalid_json()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Record** (1 connections)
- **Parse a JSON field from database, handling both dict/list and string formats.** (1 connections) — `server/npc/zone_config_loader.py`
- **Parse a zone special_rules field from the database.** (1 connections) — `server/npc/zone_config_loader.py`
- **Build and store one subzone configuration from a database row.** (1 connections) — `server/npc/zone_config_loader.py`
- **Test parse_json_field() returns default when None.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test parse_json_field() parses JSON string.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test parse_json_field() returns dict as-is.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test parse_json_field() returns list as-is.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test parse_json_field() raises error on invalid JSON string.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`

## Relationships

- [spell game magic](spell_game_magic.md) (10 shared connections)
- [container events rationale](container_events_rationale.md) (5 shared connections)
- [validator room toolkit](validator_room_toolkit.md) (1 shared connections)

## Source Files

- `server/npc/zone_config_loader.py`
- `server/tests/unit/npc/test_zone_config_loader.py`

## Audit Trail

- EXTRACTED: 50 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*