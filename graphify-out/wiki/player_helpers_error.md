# player helpers error

> 18 nodes

## Key Concepts

- **inventory_display_helpers.py** (13 connections) — `server/commands/inventory_display_helpers.py`
- **render_inventory()** (12 connections) — `server/commands/inventory_display_helpers.py`
- **build_inventory_lines()** (8 connections) — `server/commands/inventory_display_helpers.py`
- **build_equipped_lines()** (8 connections) — `server/commands/inventory_display_helpers.py`
- **Any** (7 connections)
- **get_equipped_item_identifiers()** (6 connections) — `server/commands/inventory_display_helpers.py`
- **test_get_equipped_item_identifiers()** (2 connections) — `server/tests/unit/commands/test_inventory_display_helpers.py`
- **test_build_inventory_lines_empty()** (2 connections) — `server/tests/unit/commands/test_inventory_display_helpers.py`
- **test_build_inventory_lines_with_item()** (2 connections) — `server/tests/unit/commands/test_inventory_display_helpers.py`
- **test_build_equipped_lines_empty()** (2 connections) — `server/tests/unit/commands/test_inventory_display_helpers.py`
- **test_build_equipped_lines_with_container_items()** (2 connections) — `server/tests/unit/commands/test_inventory_display_helpers.py`
- **test_render_inventory_capacity_line()** (2 connections) — `server/tests/unit/commands/test_inventory_display_helpers.py`
- **test_render_inventory_full_flow()** (2 connections) — `server/tests/unit/commands/test_inventory_display_helpers.py`
- **Display and rendering helpers for inventory commands.** (1 connections) — `server/commands/inventory_display_helpers.py`
- **Get sets of equipped item IDs and instance IDs for efficient lookup.** (1 connections) — `server/commands/inventory_display_helpers.py`
- **Build inventory display lines.** (1 connections) — `server/commands/inventory_display_helpers.py`
- **Build equipped items display lines.** (1 connections) — `server/commands/inventory_display_helpers.py`
- **Render inventory display with equipped items and container contents.** (1 connections) — `server/commands/inventory_display_helpers.py`

## Relationships

- [commands inventory helpers](commands_inventory_helpers.md) (21 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [subzone realtime nats](subzone_realtime_nats.md) (1 shared connections)
- [commands inventory command](commands_inventory_command.md) (1 shared connections)
- [realtime real time](realtime_real_time.md) (1 shared connections)

## Source Files

- `server/commands/inventory_display_helpers.py`
- `server/tests/unit/commands/test_inventory_display_helpers.py`

## Audit Trail

- EXTRACTED: 73 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*