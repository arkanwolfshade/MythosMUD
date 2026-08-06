# commands inventory helpers

> 23 nodes

## Key Concepts

- **test_inventory_display_helpers.py** (25 connections) — `server/tests/unit/commands/test_inventory_display_helpers.py`
- **format_metadata()** (20 connections) — `server/commands/inventory_display_helpers.py`
- **filter_non_equipped_inventory()** (8 connections) — `server/commands/inventory_display_helpers.py`
- **build_container_metadata()** (8 connections) — `server/commands/inventory_display_helpers.py`
- **test_format_metadata_none()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **test_format_metadata_simple()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **test_format_metadata_complex()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **test_format_metadata_empty()** (2 connections) — `server/tests/unit/commands/test_inventory_display_helpers.py`
- **test_format_metadata_sorted_keys()** (2 connections) — `server/tests/unit/commands/test_inventory_display_helpers.py`
- **test_format_metadata_nested_dict()** (2 connections) — `server/tests/unit/commands/test_inventory_display_helpers.py`
- **test_format_metadata_exception_returns_empty()** (2 connections) — `server/tests/unit/commands/test_inventory_display_helpers.py`
- **test_filter_non_equipped_inventory()** (2 connections) — `server/tests/unit/commands/test_inventory_display_helpers.py`
- **test_filter_keeps_non_equipped_items()** (2 connections) — `server/tests/unit/commands/test_inventory_display_helpers.py`
- **test_build_container_metadata_without_contents()** (2 connections) — `server/tests/unit/commands/test_inventory_display_helpers.py`
- **test_build_container_metadata_with_contents()** (2 connections) — `server/tests/unit/commands/test_inventory_display_helpers.py`
- **test_filter_equipped_by_item_id()** (2 connections) — `server/tests/unit/commands/test_inventory_display_helpers.py`
- **Format metadata for display.** (1 connections) — `server/commands/inventory_display_helpers.py`
- **Filter out equipped items and container items from inventory.** (1 connections) — `server/commands/inventory_display_helpers.py`
- **Build and format metadata for equipped item with container.** (1 connections) — `server/commands/inventory_display_helpers.py`
- **Unit tests for inventory display helpers.** (1 connections) — `server/tests/unit/commands/test_inventory_display_helpers.py`
- **Test _format_metadata with None.** (1 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **Test format_metadata with simple metadata.** (1 connections) — `server/tests/unit/commands/test_inventory_helpers.py`
- **Test format_metadata with complex metadata.** (1 connections) — `server/tests/unit/commands/test_inventory_helpers.py`

## Relationships

- [player helpers error](player_helpers_error.md) (21 shared connections)
- [subzone realtime nats](subzone_realtime_nats.md) (4 shared connections)
- [commands inventory command](commands_inventory_command.md) (4 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [tsconfig app DOM](tsconfig_app_DOM.md) (1 shared connections)

## Source Files

- `server/commands/inventory_display_helpers.py`
- `server/tests/unit/commands/test_inventory_display_helpers.py`
- `server/tests/unit/commands/test_inventory_helpers.py`

## Audit Trail

- EXTRACTED: 95 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*