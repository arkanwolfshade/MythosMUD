# Test Modernization Plan

> 40 nodes

## Key Concepts

- **test_look_item.py** (55 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_find_item_in_equipped_success()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_get_item_description_from_prototype_success()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_get_item_description_from_prototype_fallback()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_item_in_location_with_location_name()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_item_in_location_no_prototype()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_equipped_item_success()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_handle_item_look_in_inventory()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_handle_item_look_in_equipped()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_try_lookup_item_implicit_in_room_drops()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_get_item_description_from_prototype_with_item_id()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_get_item_description_from_prototype_exception_handling()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_item_in_location_fallback_name()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_handle_item_look_with_instance_number()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_try_lookup_item_implicit_in_equipped()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_try_lookup_item_implicit_player_no_get_equipped_items()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **mock_prototype_registry()** (2 connections) — `server/tests/unit/commands/test_look_item.py`
- **sample_room_drop()** (2 connections) — `server/tests/unit/commands/test_look_item.py`
- **sample_inventory_item()** (2 connections) — `server/tests/unit/commands/test_look_item.py`
- **sample_equipped_item()** (2 connections) — `server/tests/unit/commands/test_look_item.py`
- **Unit tests for item look functionality.  Tests the helper functions for looking** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Create a mock prototype registry.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Create a sample room drop item.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Create a sample inventory item.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Create a sample equipped item.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- *... and 15 more nodes in this community*

## Relationships

- [Error Handling Guide](Error_Handling_Guide.md) (27 shared connections)
- [Chat Service Whispers](Chat_Service_Whispers.md) (8 shared connections)
- [Structured Error Logging Tasks](Structured_Error_Logging_Tasks.md) (5 shared connections)
- [Command Commands Validation](Command_Commands_Validation.md) (1 shared connections)
- [Api Players Quests](Api_Players_Quests.md) (1 shared connections)
- [Room Toolkit Validator](Room_Toolkit_Validator.md) (1 shared connections)
- [Commands Container Inventory](Commands_Container_Inventory.md) (1 shared connections)
- [Logging Structured Processors](Logging_Structured_Processors.md) (1 shared connections)
- [E 2 E Bugs Found](E_2_E_Bugs_Found.md) (1 shared connections)
- [Archive Npc Duplication](Archive_Npc_Duplication.md) (1 shared connections)
- [Error Logging Implementation](Error_Logging_Implementation.md) (1 shared connections)
- [Archive Room Hierarchy](Archive_Room_Hierarchy.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_look_item.py`

## Audit Trail

- EXTRACTED: 128 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*