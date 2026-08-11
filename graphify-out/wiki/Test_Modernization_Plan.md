# Test Modernization Plan

> 95 nodes

## Key Concepts

- **test_look_item.py** (55 connections) — `server/tests/unit/commands/test_look_item.py`
- **_find_item_in_inventory()** (18 connections) — `server/commands/look_item.py`
- **_find_item_in_equipped()** (17 connections) — `server/commands/look_item.py`
- **_handle_item_look()** (17 connections) — `server/commands/look_item.py`
- **_try_lookup_item_implicit()** (15 connections) — `server/commands/look_item.py`
- **look_item.py** (14 connections) — `server/commands/look_item.py`
- **_check_item_in_location()** (13 connections) — `server/commands/look_item.py`
- **_get_item_description_from_prototype()** (12 connections) — `server/commands/look_item.py`
- **_check_equipped_item()** (10 connections) — `server/commands/look_item.py`
- **Any** (8 connections)
- **test_find_item_in_inventory_success()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_find_item_in_inventory_not_found()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_find_item_in_equipped_success()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_find_item_in_equipped_not_found()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_get_item_description_from_prototype_success()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_get_item_description_from_prototype_no_registry()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_get_item_description_from_prototype_no_prototype_id()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_get_item_description_from_prototype_fallback()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_get_item_description_from_prototype_fallback_no_prototype()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_item_in_location_success()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_item_in_location_with_location_name()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_item_in_location_not_found()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_item_in_location_no_prototype()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_equipped_item_success()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- **test_check_equipped_item_not_found()** (3 connections) — `server/tests/unit/commands/test_look_item.py`
- *... and 70 more nodes in this community*

## Relationships

- [Chat Service Whispers](Chat_Service_Whispers.md) (29 shared connections)
- [Commands Command Look](Commands_Command_Look.md) (5 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)

## Source Files

- `server/commands/look_item.py`
- `server/tests/unit/commands/test_look_item.py`

## Audit Trail

- EXTRACTED: 336 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*