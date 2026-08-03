# look helpers commands

> 165 nodes

## Key Concepts

- **test_look_player.py** (32 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_look_helpers.py** (30 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **look_player.py** (23 connections) — `server/commands/look_player.py`
- **_format_player_look_display()** (23 connections) — `server/commands/look_player.py`
- **test_look_helpers_functions.py** (23 connections) — `server/tests/unit/commands/test_look_helpers_functions.py`
- **_get_health_label()** (17 connections) — `server/commands/look_helpers.py`
- **_get_lucidity_label()** (17 connections) — `server/commands/look_helpers.py`
- **_select_target_player()** (17 connections) — `server/commands/look_player.py`
- **look_helpers.py** (16 connections) — `server/commands/look_helpers.py`
- **_handle_player_look()** (13 connections) — `server/commands/look_player.py`
- **_try_lookup_player_implicit()** (12 connections) — `server/commands/look_player.py`
- **test_look_player_helpers.py** (12 connections) — `server/tests/unit/commands/test_look_player_helpers.py`
- **_parse_instance_number()** (11 connections) — `server/commands/look_helpers.py`
- **_get_visible_equipment()** (11 connections) — `server/commands/look_helpers.py`
- **_get_players_in_room()** (11 connections) — `server/commands/look_player.py`
- **_get_wearable_container_service()** (9 connections) — `server/commands/look_helpers.py`
- **_find_matching_players()** (9 connections) — `server/commands/look_player.py`
- **Any** (6 connections)
- **Any** (4 connections)
- **test_parse_instance_number_hyphen_syntax()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_parse_instance_number_space_syntax()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_parse_instance_number_no_instance()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_parse_instance_number_multiple_spaces()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_get_health_label_healthy()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **test_get_health_label_wounded()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- *... and 140 more nodes in this community*

## Relationships

- [look command commands](look_command_commands.md) (14 shared connections)
- [grace period disconnect](grace_period_disconnect.md) (6 shared connections)
- [NATS Messaging](NATS_Messaging.md) (4 shared connections)
- [player look commands](player_look_commands.md) (4 shared connections)
- [DI Container Format](DI_Container_Format.md) (3 shared connections)
- [Inventory Equip](Inventory_Equip.md) (3 shared connections)
- [grace period login](grace_period_login.md) (3 shared connections)
- [room look commands](room_look_commands.md) (3 shared connections)

## Source Files

- `server/commands/look_helpers.py`
- `server/commands/look_player.py`
- `server/tests/unit/commands/test_look_helpers.py`
- `server/tests/unit/commands/test_look_helpers_functions.py`
- `server/tests/unit/commands/test_look_player.py`
- `server/tests/unit/commands/test_look_player_helpers.py`

## Audit Trail

- EXTRACTED: 568 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*