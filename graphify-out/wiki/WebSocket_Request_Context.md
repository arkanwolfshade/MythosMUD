# WebSocket Request Context

> 32 nodes

## Key Concepts

- **UnequipCommand** (22 connections) — `server/models/command_inventory.py`
- **test_unequip_command_validate_slot_empty_string()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_unequip_command_validate_search_term_empty_string()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_unequip_command_validate_requirements_neither_provided()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_unequip_command_with_slot()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_unequip_command_with_search_term()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_unequip_command_with_both()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_unequip_command_validate_slot_strips()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_unequip_command_validate_slot_whitespace_only()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_unequip_command_validate_search_term_strips()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_unequip_command_validate_search_term_whitespace_only()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_unequip_command_validate_requirements_slot_provided()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_unequip_command_validate_requirements_search_term_provided()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **.validate_slot()** (2 connections) — `server/models/command_inventory.py`
- **.validate_search_term()** (2 connections) — `server/models/command_inventory.py`
- **.validate_unequip_requirements()** (2 connections) — `server/models/command_inventory.py`
- **Command for unequipping an item back to inventory.** (1 connections) — `server/models/command_inventory.py`
- **Strip and normalize slot name.** (1 connections) — `server/models/command_inventory.py`
- **Strip and validate search term.** (1 connections) — `server/models/command_inventory.py`
- **Ensure either slot or search_term is provided.** (1 connections) — `server/models/command_inventory.py`
- **Test UnequipCommand can be created with slot.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test UnequipCommand can be created with search_term.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test UnequipCommand can be created with both slot and search_term.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test UnequipCommand strips whitespace from slot.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test UnequipCommand cannot accept empty slot (fails min_length before validator)** (1 connections) — `server/tests/unit/models/test_command_inventory.py`
- *... and 7 more nodes in this community*

## Relationships

- [Admin Summon Command](Admin_Summon_Command.md) (14 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (3 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (1 shared connections)
- [Emote Schema Validator](Emote_Schema_Validator.md) (1 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (1 shared connections)
- [Chat Rate Limiter](Chat_Rate_Limiter.md) (1 shared connections)

## Source Files

- `server/models/command_inventory.py`
- `server/tests/unit/models/test_command_inventory.py`

## Audit Trail

- EXTRACTED: 78 (94%)
- INFERRED: 5 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*