# Cache and NPC Cache

> 54 nodes

## Key Concepts

- **test_look_helpers.py** (30 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **_parse_instance_number()** (11 connections) — `server/commands/look_helpers.py`
- **test_parse_instance_number_hyphen_syntax()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_parse_instance_number_space_syntax()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_parse_instance_number_no_instance()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_parse_instance_number_multiple_spaces()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_get_health_label_healthy()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_get_health_label_wounded()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_get_health_label_critical()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_get_health_label_mortally_wounded()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_get_health_label_no_max_dp()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_get_health_label_zero_max_dp()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_get_lucidity_label_lucid()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_get_lucidity_label_disturbed()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_get_lucidity_label_unstable()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_get_lucidity_label_mad()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_get_lucidity_label_no_lucidity()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_get_visible_equipment_no_equipment()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_get_visible_equipment_with_equipment()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_is_direction_cardinal()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_is_direction_abbreviation()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_is_direction_not_direction()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_get_wearable_container_service_initializes()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_get_wearable_container_service_no_persistence()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_parse_instance_number_hyphen_syntax()** (3 connections) — `server/tests/unit/commands/test_look_helpers_functions.py`
- *... and 29 more nodes in this community*

## Relationships

- [Look Player Command](Look_Player_Command.md) (25 shared connections)
- [Commands Command Look](Commands_Command_Look.md) (4 shared connections)

## Source Files

- `server/commands/look_helpers.py`
- `server/tests/unit/commands/test_look_helpers.py`
- `server/tests/unit/commands/test_look_helpers_functions.py`

## Audit Trail

- EXTRACTED: 143 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*