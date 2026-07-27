# Ground and Rescue Commands

> 59 nodes · cohesion 0.05

## Key Concepts

- **handle_ground_command()** (30 connections) — `server/commands/rescue_commands.py`
- **test_rescue_commands.py** (21 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **handle_rescue_command()** (12 connections) — `server/commands/rescue_commands.py`
- **Test handle_read_command() handles missing persistence.** (8 connections) — `server/tests/unit/commands/test_read_command.py`
- **_apply_grounding_adjustment()** (7 connections) — `server/commands/rescue_commands.py`
- **Test handle_read_command() handles missing target.** (7 connections) — `server/tests/unit/commands/test_read_command.py`
- **Any** (7 connections) — `server/commands/rescue_commands.py`
- **_normalize_player_ids()** (5 connections) — `server/commands/rescue_commands.py`
- **_send_grounding_failure_events()** (5 connections) — `server/commands/rescue_commands.py`
- **_send_grounding_success_events()** (5 connections) — `server/commands/rescue_commands.py`
- **_validate_ground_context()** (5 connections) — `server/commands/rescue_commands.py`
- **UUID** (5 connections) — `server/commands/rescue_commands.py`
- **_get_ground_services()** (4 connections) — `server/commands/rescue_commands.py`
- **_send_grounding_channeling_events()** (4 connections) — `server/commands/rescue_commands.py`
- **_validate_ground_target()** (4 connections) — `server/commands/rescue_commands.py`
- **test_handle_equip_command_no_target()** (4 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **test_handle_unequip_command_no_target()** (4 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **test_handle_logout_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_logout_commands.py`
- **test_handle_ground_command()** (3 connections) — `server/tests/unit/commands/test_position_commands.py`
- **Test handle_ground_command() handles rescuer not found.** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_apply_lucidity_error()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_different_rooms()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_lucidity_record_not_found()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_no_rescuer_room()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- *... and 34 more nodes in this community*

## Relationships

- [[Alias Expansion Logic]] (15 shared connections)
- [[Inventory Test Support]] (5 shared connections)
- [[Lucidity Rescue Helpers]] (3 shared connections)
- [[Logout and Quit Commands]] (3 shared connections)
- [[Command Helper Utilities]] (2 shared connections)
- [[Admin Summon Command]] (2 shared connections)
- [[Spellbook Read Command]] (2 shared connections)
- [[Rest Command Flow]] (2 shared connections)
- [[Lucidity State Models]] (1 shared connections)
- [[NPC Admin API]] (1 shared connections)
- [[Services Rescue Service]] (1 shared connections)
- [[Commands Teach Command]] (1 shared connections)

## Source Files

- `server/commands/rescue_commands.py`
- `server/tests/unit/commands/test_inventory_commands.py`
- `server/tests/unit/commands/test_logout_commands.py`
- `server/tests/unit/commands/test_position_commands.py`
- `server/tests/unit/commands/test_read_command.py`
- `server/tests/unit/commands/test_rescue_commands.py`

## Audit Trail

- EXTRACTED: 216 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
