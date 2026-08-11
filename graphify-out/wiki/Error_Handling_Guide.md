# Error Handling Guide

> 25 nodes

## Key Concepts

- **_find_item_in_equipped()** (17 connections) — `server/commands/look_item.py`
- **_handle_item_look()** (17 connections) — `server/commands/look_item.py`
- **_try_lookup_item_implicit()** (15 connections) — `server/commands/look_item.py`
- **look_item.py** (14 connections) — `server/commands/look_item.py`
- **_check_item_in_location()** (13 connections) — `server/commands/look_item.py`
- **_get_item_description_from_prototype()** (12 connections) — `server/commands/look_item.py`
- **_check_equipped_item()** (10 connections) — `server/commands/look_item.py`
- **Any** (8 connections)
- **test_get_item_description_from_prototype_fallback_no_prototype()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_item_in_location_not_found()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_handle_item_look_not_found()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_handle_item_look_look_in_skips_equipped()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_find_item_in_equipped_by_prototype_id()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **Item look functionality for MythosMUD.  This module handles looking at items, in** (1 connections) — `server/commands/look_item.py`
- **Find an item in equipped items by name or prototype_id.      Args:         equip** (1 connections) — `server/commands/look_item.py`
- **Get item description from prototype registry.      Returns:         Formatted re** (1 connections) — `server/commands/look_item.py`
- **Check if item found in a location and return formatted result.** (1 connections) — `server/commands/look_item.py`
- **Check if item is equipped and return formatted result.** (1 connections) — `server/commands/look_item.py`
- **Handle looking at a specific item.** (1 connections) — `server/commands/look_item.py`
- **Try to find and display an item in implicit lookup.** (1 connections) — `server/commands/look_item.py`
- **Test getting item description with fallback name when prototype doesn't exist.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test checking item in location when item not found.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test handling item look when item not found.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test handling item look with look_in flag skips equipped items.** (1 connections) — `server/tests/unit/commands/test_look_item.py`
- **Test finding item in equipped by prototype_id.** (1 connections) — `server/tests/unit/commands/test_look_item.py`

## Relationships

- [Test Modernization Plan](Test_Modernization_Plan.md) (27 shared connections)
- [Command Request App State](Command_Request_App_State.md) (9 shared connections)
- [Commands Command Look](Commands_Command_Look.md) (5 shared connections)
- [Structured Error Logging Tasks](Structured_Error_Logging_Tasks.md) (4 shared connections)
- [Chat Service Whispers](Chat_Service_Whispers.md) (4 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Commands Container Inventory](Commands_Container_Inventory.md) (1 shared connections)
- [Logging Structured Processors](Logging_Structured_Processors.md) (1 shared connections)
- [E 2 E Bugs Found](E_2_E_Bugs_Found.md) (1 shared connections)
- [Room Toolkit Validator](Room_Toolkit_Validator.md) (1 shared connections)
- [Command Commands Validation](Command_Commands_Validation.md) (1 shared connections)
- [Api Players Quests](Api_Players_Quests.md) (1 shared connections)

## Source Files

- `server/commands/look_item.py`
- `server/tests/unit/commands/test_look_item.py`

## Audit Trail

- EXTRACTED: 133 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*