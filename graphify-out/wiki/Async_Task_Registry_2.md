# Async Task Registry

> 117 nodes

## Key Concepts

- **test_inventory_helpers.py** (38 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **match_room_drop_by_name()** (19 connections) — `server/commands/inventory_item_matching.py`
- **match_equipped_item_by_name()** (18 connections) — `server/commands/inventory_item_matching.py`
- **match_inventory_item_by_name()** (16 connections) — `server/commands/inventory_item_matching.py`
- **format_metadata()** (15 connections) — `server/commands/inventory_display_helpers.py`
- **test_inventory_commands_helpers.py** (13 connections) — `server/tests/unit/commands/test_inventory_commands_helpers.py`
- **inventory_display_helpers.py** (12 connections) — `server/commands/inventory_display_helpers.py`
- **render_inventory()** (9 connections) — `server/commands/inventory_display_helpers.py`
- **Any** (7 connections)
- **test_inventory_commands_format_helpers.py** (6 connections) — `server/tests/unit/commands/test_inventory_commands_format_helpers.py`
- **build_inventory_lines()** (5 connections) — `server/commands/inventory_display_helpers.py`
- **build_container_metadata()** (5 connections) — `server/commands/inventory_display_helpers.py`
- **build_equipped_lines()** (5 connections) — `server/commands/inventory_display_helpers.py`
- **get_equipped_item_identifiers()** (4 connections) — `server/commands/inventory_display_helpers.py`
- **filter_non_equipped_inventory()** (4 connections) — `server/commands/inventory_display_helpers.py`
- **match_exact_drop()** (4 connections) — `server/commands/inventory_item_matching.py`
- **match_prefix_drop()** (4 connections) — `server/commands/inventory_item_matching.py`
- **match_substring_drop()** (4 connections) — `server/commands/inventory_item_matching.py`
- **search_exact_match()** (3 connections) — `server/commands/inventory_item_matching.py`
- **search_prefix_match()** (3 connections) — `server/commands/inventory_item_matching.py`
- **search_substring_match()** (3 connections) — `server/commands/inventory_item_matching.py`
- **test_format_metadata_empty()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_format_helpers.py`
- **test_format_metadata_simple()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_format_helpers.py`
- **test_format_metadata_nested_dict()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_format_helpers.py`
- **test_match_room_drop_by_name_exact()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_helpers.py`
- *... and 92 more nodes in this community*

## Relationships

- [Character Creation Service](Character_Creation_Service.md) (27 shared connections)
- [Spell Effect Protocols](Spell_Effect_Protocols.md) (4 shared connections)
- [Container Sync Remediation](Container_Sync_Remediation.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Admin NPC Schemas](Admin_NPC_Schemas.md) (1 shared connections)
- [FastAPI Auth Integration](FastAPI_Auth_Integration.md) (1 shared connections)

## Source Files

- `server/commands/inventory_display_helpers.py`
- `server/commands/inventory_item_matching.py`
- `server/tests/unit/commands/test_inventory_commands_format_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_helpers.py`
- `server/tests/unit/commands/test_inventory_helpers.py`

## Audit Trail

- EXTRACTED: 369 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*