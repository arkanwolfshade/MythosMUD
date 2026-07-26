# container_helpers_inventory_display.py

> 14 nodes · cohesion 0.22

## Key Concepts

- **container_helpers_inventory_display.py** (17 connections) — `server/commands/container_helpers_inventory_display.py`
- **_apply_container_component_to_slot()** (8 connections) — `server/commands/container_helpers_inventory_display.py`
- **get_container_data_for_inventory()** (7 connections) — `server/commands/container_helpers_inventory_display.py`
- **match_container_to_slot()** (6 connections) — `server/commands/container_helpers_inventory_display.py`
- **_inventory_stack_to_display_dict()** (4 connections) — `server/commands/container_helpers_inventory_display.py`
- **_component_metadata()** (3 connections) — `server/commands/container_helpers_inventory_display.py`
- **_equipped_matches_container_metadata()** (2 connections) — `server/commands/container_helpers_inventory_display.py`
- **_lock_state_as_str()** (2 connections) — `server/commands/container_helpers_inventory_display.py`
- **InventoryStack** (1 connections)
- **Player** (1 connections)
- **Container display helpers for inventory UI (wearable contents, slot matching).** (1 connections) — `server/commands/container_helpers_inventory_display.py`
- **Get container contents, capacities, and lock states for equipped containers.** (1 connections) — `server/commands/container_helpers_inventory_display.py`
- **Shallow-copy a wearable stack into a plain dict for equipped-view metadata.** (1 connections) — `server/commands/container_helpers_inventory_display.py`
- **Match a container component to an equipped slot. Returns slot name or None.** (1 connections) — `server/commands/container_helpers_inventory_display.py`

## Relationships

- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (4 shared connections)
- [__init__.py](__init__.py.md) (4 shared connections)
- [Player](Player.md) (2 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [LRUCache](LRUCache.md) (1 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)

## Source Files

- `server/commands/container_helpers_inventory_display.py`

## Audit Trail

- EXTRACTED: 52 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*