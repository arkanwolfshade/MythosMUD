# Character Creation E2E

> 34 nodes

## Key Concepts

- **EquipCommand** (23 connections) — `server/models/command_inventory.py`
- **test_equip_command_validate_search_term_empty_string()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_equip_command_validate_requirements_neither_provided()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_equip_command_validate_slot_empty_string()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_equip_command_validate_slot_whitespace_only()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_equip_command_index_validation_min()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_equip_command_search_term_max_length()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_equip_command_target_slot_max_length()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_equip_command_with_index()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_equip_command_with_search_term()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_equip_command_with_target_slot()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_equip_command_validate_search_term_strips()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_equip_command_validate_search_term_whitespace_only()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_equip_command_validate_slot_strips()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **.validate_search_term()** (2 connections) — `server/models/command_inventory.py`
- **.validate_equip_requirements()** (2 connections) — `server/models/command_inventory.py`
- **.validate_slot()** (2 connections) — `server/models/command_inventory.py`
- **Command for equipping an item from inventory.** (1 connections) — `server/models/command_inventory.py`
- **Strip and validate search term.** (1 connections) — `server/models/command_inventory.py`
- **Ensure either index or search_term is provided.** (1 connections) — `server/models/command_inventory.py`
- **Validate target slot value.          Args:             value: The target slot va** (1 connections) — `server/models/command_inventory.py`
- **Test EquipCommand can be created with index.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test EquipCommand can be created with search_term.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test EquipCommand can have optional target_slot.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test EquipCommand strips whitespace from search_term.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`
- *... and 9 more nodes in this community*

## Relationships

- [Admin Summon Command](Admin_Summon_Command.md) (15 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (7 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (1 shared connections)
- [Emote Schema Validator](Emote_Schema_Validator.md) (1 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (1 shared connections)
- [Base Command Models](Base_Command_Models.md) (1 shared connections)

## Source Files

- `server/models/command_inventory.py`
- `server/tests/unit/models/test_command_inventory.py`

## Audit Trail

- EXTRACTED: 83 (90%)
- INFERRED: 9 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*