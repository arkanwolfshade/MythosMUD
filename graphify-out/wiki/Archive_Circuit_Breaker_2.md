# Archive Circuit Breaker

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
- [Services Lucidity Repository](Services_Lucidity_Repository.md) (9 shared connections)
- [Commands Command Look](Commands_Command_Look.md) (5 shared connections)
- [Nats Anti Patterns](Nats_Anti_Patterns.md) (4 shared connections)
- [E2E Suite Overview](E2E_Suite_Overview.md) (4 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Archive Combat Health](Archive_Combat_Health.md) (2 shared connections)
- [Cursor Agents Readme](Cursor_Agents_Readme.md) (1 shared connections)
- [test_setup_session_tracking_no_session_id](test_setup_session_tracking_no_session_id.md) (1 shared connections)
- [test_setup_connection_metadata_no_session_token](test_setup_connection_metadata_no_session_token.md) (1 shared connections)
- [CleanupContext](CleanupContext.md) (1 shared connections)
- [test_setup_player_and_room_no_player](test_setup_player_and_room_no_player.md) (1 shared connections)

## Source Files

- `server/commands/look_item.py`
- `server/tests/unit/commands/test_look_item.py`

## Audit Trail

- EXTRACTED: 133 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*