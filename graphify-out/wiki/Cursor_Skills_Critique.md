# Cursor Skills Critique

> 12 nodes

## Key Concepts

- **DropCommand** (12 connections) — `server/models/command_inventory.py`
- **test_drop_command_index_validation_min()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_drop_command_quantity_validation_min()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_drop_command_missing_index()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_drop_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_drop_command_with_quantity()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Command for dropping items from inventory into the room.** (1 connections) — `server/models/command_inventory.py`
- **Test DropCommand requires index.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test DropCommand can have optional quantity.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test DropCommand validates index is >= 1.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test DropCommand validates quantity is >= 1.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test DropCommand requires index.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`

## Relationships

- [Admin Summon Command](Admin_Summon_Command.md) (7 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (3 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (1 shared connections)
- [Emote Schema Validator](Emote_Schema_Validator.md) (1 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (1 shared connections)
- [Calendar NPC Schedule](Calendar_NPC_Schedule.md) (1 shared connections)

## Source Files

- `server/models/command_inventory.py`
- `server/tests/unit/models/test_command_inventory.py`

## Audit Trail

- EXTRACTED: 31 (86%)
- INFERRED: 5 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*