# Look Item Commands

> 25 nodes · cohesion 0.12

## Key Concepts

- **_find_item_in_equipped()** (17 connections) — `server/commands/look_item.py`
- **_handle_item_look()** (17 connections) — `server/commands/look_item.py`
- **_try_lookup_item_implicit()** (15 connections) — `server/commands/look_item.py`
- **look_item.py** (14 connections) — `server/commands/look_item.py`
- **_check_item_in_location()** (13 connections) — `server/commands/look_item.py`
- **_get_item_description_from_prototype()** (12 connections) — `server/commands/look_item.py`
- **_check_equipped_item()** (10 connections) — `server/commands/look_item.py`
- **Any** (8 connections)
- **test_check_item_in_location_not_found()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_find_item_in_equipped_by_prototype_id()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_get_item_description_from_prototype_fallback_no_prototype()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_handle_item_look_look_in_skips_equipped()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_handle_item_look_not_found()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
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

- [Character Selection Screens](Character_Selection_Screens.md) (27 shared connections)
- [Player State Command Factory](Player_State_Command_Factory.md) (9 shared connections)
- [Async Persistence Core](Async_Persistence_Core.md) (5 shared connections)
- [Async Code Audit](Async_Code_Audit.md) (4 shared connections)
- [Memory Leak Metrics Tests](Memory_Leak_Metrics_Tests.md) (4 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Development 5 Scripts](Development_5_Scripts.md) (1 shared connections)
- [Commands Admin Shutdown](Commands_Admin_Shutdown.md) (1 shared connections)
- [Cursor Skills Arrange](Cursor_Skills_Arrange.md) (1 shared connections)
- [Review Code Postgresql](Review_Code_Postgresql.md) (1 shared connections)
- [Archive Refactoring Project](Archive_Refactoring_Project.md) (1 shared connections)
- [Error Logging Archive](Error_Logging_Archive.md) (1 shared connections)

## Source Files

- `server/commands/look_item.py`
- `server/tests/unit/commands/test_look_item.py`

## Audit Trail

- EXTRACTED: 133 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*