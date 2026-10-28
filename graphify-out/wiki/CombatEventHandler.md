# CombatEventHandler

> 42 nodes · cohesion 0.06

## Key Concepts

- **ValidationRule** (10 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- **ValidationError** (8 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- **.validate()** (6 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- **.validate_room()** (5 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **base_rule.py** (5 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- **Path** (4 connections)
- **.__init__()** (4 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **._load_schema()** (4 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **.validate_room_file()** (4 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **.validate_subzone_config()** (4 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **.validate_zone_config()** (4 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **.validate_room_database()** (3 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **.create_error()** (3 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- **.create_warning()** (3 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- **rules/__init__.py** (3 connections) — `tools/room_toolkit/room_validator/rules/__init__.py`
- **ABC** (2 connections)
- **.__init__()** (2 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- **.__str__()** (2 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- **.to_dict()** (2 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- **._filter_rooms_by_zone()** (2 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- **.get_rule_info()** (2 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- **.__init__()** (2 connections) — `tools/room_toolkit/room_validator/rules/base_rule.py`
- **Validate a room file against the schema. Args: file_path: Path to the room JSON…** (1 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **Validate all rooms in a database against the schema. Args: room_database:…** (1 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **Validate a sub-zone configuration against its schema. Args: config_data: Sub-…** (1 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- *... and 17 more nodes in this community*

## Relationships

- [ScheduleEntry](ScheduleEntry.md) (7 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)

## Source Files

- `tools/room_toolkit/room_validator/core/schema_validator.py`
- `tools/room_toolkit/room_validator/rules/__init__.py`
- `tools/room_toolkit/room_validator/rules/base_rule.py`

## Audit Trail

- EXTRACTED: 52 (93%)
- INFERRED: 4 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*