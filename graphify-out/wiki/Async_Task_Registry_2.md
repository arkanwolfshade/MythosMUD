# Async Task Registry

> 99 nodes

## Key Concepts

- **test_inventory_helpers.py** (38 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **equipment_helpers.py** (28 connections) — `server/commands/equipment_helpers.py`
- **inventory_item_matching.py** (22 connections) — `server/commands/inventory_item_matching.py`
- **match_room_drop_by_name()** (19 connections) — `server/commands/inventory_item_matching.py`
- **normalize_slot_name()** (19 connections) — `server/commands/inventory_item_matching.py`
- **match_equipped_item_by_name()** (18 connections) — `server/commands/inventory_item_matching.py`
- **match_inventory_item_by_name()** (16 connections) — `server/commands/inventory_item_matching.py`
- **test_inventory_commands_helpers.py** (13 connections) — `server/tests/unit/commands/test_inventory_commands_helpers.py`
- **resolve_unequip_slot()** (8 connections) — `server/commands/equipment_helpers.py`
- **build_equipped_candidates()** (5 connections) — `server/commands/inventory_item_matching.py`
- **extract_item_identifier()** (4 connections) — `server/commands/inventory_item_matching.py`
- **build_drop_candidates()** (4 connections) — `server/commands/inventory_item_matching.py`
- **match_exact_drop()** (4 connections) — `server/commands/inventory_item_matching.py`
- **match_prefix_drop()** (4 connections) — `server/commands/inventory_item_matching.py`
- **match_substring_drop()** (4 connections) — `server/commands/inventory_item_matching.py`
- **build_inventory_candidates()** (4 connections) — `server/commands/inventory_item_matching.py`
- **_try_resolve_unequip_by_search()** (3 connections) — `server/commands/equipment_helpers.py`
- **clean_item_value()** (3 connections) — `server/commands/inventory_item_matching.py`
- **search_exact_match()** (3 connections) — `server/commands/inventory_item_matching.py`
- **search_prefix_match()** (3 connections) — `server/commands/inventory_item_matching.py`
- **search_substring_match()** (3 connections) — `server/commands/inventory_item_matching.py`
- **test_match_room_drop_by_name_exact()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_helpers.py`
- **test_match_room_drop_by_name_not_found()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_helpers.py`
- **test_match_inventory_item_by_name_exact()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_helpers.py`
- **test_match_inventory_item_by_name_not_found()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_helpers.py`
- *... and 74 more nodes in this community*

## Relationships

- [Character Creation Service](Character_Creation_Service.md) (23 shared connections)
- [NPC Room Event Handlers](NPC_Room_Event_Handlers.md) (6 shared connections)
- [Whisper Remediation Plan](Whisper_Remediation_Plan.md) (5 shared connections)
- [NPC Database Sessions](NPC_Database_Sessions.md) (4 shared connections)
- [Chat Service Whispers](Chat_Service_Whispers.md) (3 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (1 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (1 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_item_matching.py`
- `server/tests/unit/commands/test_inventory_commands_helpers.py`
- `server/tests/unit/commands/test_inventory_helpers.py`

## Audit Trail

- EXTRACTED: 361 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*