# Async Task Registry

> 109 nodes

## Key Concepts

- **test_inventory_helpers.py** (38 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **inventory_item_matching.py** (22 connections) — `server/commands/inventory_item_matching.py`
- **match_room_drop_by_name()** (19 connections) — `server/commands/inventory_item_matching.py`
- **normalize_slot_name()** (19 connections) — `server/commands/inventory_item_matching.py`
- **match_equipped_item_by_name()** (18 connections) — `server/commands/inventory_item_matching.py`
- **match_inventory_item_by_name()** (16 connections) — `server/commands/inventory_item_matching.py`
- **test_inventory_commands_helpers.py** (13 connections) — `server/tests/unit/commands/test_inventory_commands_helpers.py`
- **inventory_command_prototype.py** (12 connections) — `server/commands/inventory_command_prototype.py`
- **infer_equip_slot_from_prototype()** (9 connections) — `server/commands/inventory_command_prototype.py`
- **build_equipped_candidates()** (5 connections) — `server/commands/inventory_item_matching.py`
- **prototype_registry_from_request()** (4 connections) — `server/commands/inventory_command_prototype.py`
- **prototype_from_registry()** (4 connections) — `server/commands/inventory_command_prototype.py`
- **extract_item_identifier()** (4 connections) — `server/commands/inventory_item_matching.py`
- **build_drop_candidates()** (4 connections) — `server/commands/inventory_item_matching.py`
- **match_exact_drop()** (4 connections) — `server/commands/inventory_item_matching.py`
- **match_prefix_drop()** (4 connections) — `server/commands/inventory_item_matching.py`
- **match_substring_drop()** (4 connections) — `server/commands/inventory_item_matching.py`
- **build_inventory_candidates()** (4 connections) — `server/commands/inventory_item_matching.py`
- **_first_normalized_wear_slot()** (3 connections) — `server/commands/inventory_command_prototype.py`
- **clean_item_value()** (3 connections) — `server/commands/inventory_item_matching.py`
- **search_exact_match()** (3 connections) — `server/commands/inventory_item_matching.py`
- **search_prefix_match()** (3 connections) — `server/commands/inventory_item_matching.py`
- **search_substring_match()** (3 connections) — `server/commands/inventory_item_matching.py`
- **test_match_room_drop_by_name_exact()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_helpers.py`
- **test_match_room_drop_by_name_not_found()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_helpers.py`
- *... and 84 more nodes in this community*

## Relationships

- [WebSocket Auth Integration](WebSocket_Auth_Integration.md) (12 shared connections)
- [Spell Effect Protocols](Spell_Effect_Protocols.md) (7 shared connections)
- [Admin Command Models](Admin_Command_Models.md) (6 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (4 shared connections)
- [Upgrade Archive Dependency](Upgrade_Archive_Dependency.md) (1 shared connections)
- [Npc Services Combat](Npc_Services_Combat.md) (1 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (1 shared connections)
- [NATS Subject Admin API](NATS_Subject_Admin_API.md) (1 shared connections)
- [Container Sync Remediation](Container_Sync_Remediation.md) (1 shared connections)

## Source Files

- `server/commands/inventory_command_prototype.py`
- `server/commands/inventory_item_matching.py`
- `server/tests/unit/commands/test_inventory_commands_helpers.py`
- `server/tests/unit/commands/test_inventory_helpers.py`

## Audit Trail

- EXTRACTED: 366 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*