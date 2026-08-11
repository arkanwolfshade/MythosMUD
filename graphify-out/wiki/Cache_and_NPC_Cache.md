# Cache and NPC Cache

> 88 nodes

## Key Concepts

- **test_look_helpers.py** (30 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_look_helpers_functions.py** (23 connections) — `server/tests/unit/commands/test_look_helpers_functions.py`
- **_get_health_label()** (17 connections) — `server/commands/look_helpers.py`
- **_parse_instance_number()** (11 connections) — `server/commands/look_helpers.py`
- **_is_direction()** (11 connections) — `server/commands/look_helpers.py`
- **_get_wearable_container_service()** (9 connections) — `server/commands/look_helpers.py`
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
- *... and 63 more nodes in this community*

## Relationships

- [Look Player Command](Look_Player_Command.md) (28 shared connections)
- [Server Process Termination](Server_Process_Termination.md) (2 shared connections)
- [Commands Command Look](Commands_Command_Look.md) (2 shared connections)
- [Exploration Command Factories](Exploration_Command_Factories.md) (1 shared connections)

## Source Files

- `server/commands/look_helpers.py`
- `server/tests/unit/commands/test_look_helpers.py`
- `server/tests/unit/commands/test_look_helpers_functions.py`

## Audit Trail

- EXTRACTED: 259 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*