# container inventory display

> 16 nodes

## Key Concepts

- **container_helpers_inventory_display.py** (17 connections) — `server/commands/container_helpers_inventory_display.py`
- **_apply_container_component_to_slot()** (8 connections) — `server/commands/container_helpers_inventory_display.py`
- **get_container_data_for_inventory()** (7 connections) — `server/commands/container_helpers_inventory_display.py`
- **match_container_to_slot()** (6 connections) — `server/commands/container_helpers_inventory_display.py`
- **_inventory_stack_to_display_dict()** (4 connections) — `server/commands/container_helpers_inventory_display.py`
- **update_equipped_with_container_info()** (4 connections) — `server/commands/container_helpers_inventory_display.py`
- **_component_metadata()** (3 connections) — `server/commands/container_helpers_inventory_display.py`
- **_equipped_matches_container_metadata()** (2 connections) — `server/commands/container_helpers_inventory_display.py`
- **_lock_state_as_str()** (2 connections) — `server/commands/container_helpers_inventory_display.py`
- **InventoryStack** (1 connections)
- **Player** (1 connections)
- **Container display helpers for inventory UI (wearable contents, slot matching).** (1 connections) — `server/commands/container_helpers_inventory_display.py`
- **Shallow-copy a wearable stack into a plain dict for equipped-view metadata.** (1 connections) — `server/commands/container_helpers_inventory_display.py`
- **Match a container component to an equipped slot. Returns slot name or None.** (1 connections) — `server/commands/container_helpers_inventory_display.py`
- **Get container contents, capacities, and lock states for equipped containers.** (1 connections) — `server/commands/container_helpers_inventory_display.py`
- **Update equipped items' metadata to include container information.** (1 connections) — `server/commands/container_helpers_inventory_display.py`

## Relationships

- [container inventory helpers](container_inventory_helpers.md) (4 shared connections)
- [commands inventory command](commands_inventory_command.md) (3 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (3 shared connections)
- [commands inventory pickup](commands_inventory_pickup.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)
- [world models rationale](world_models_rationale.md) (1 shared connections)
- [combat models rationale](combat_models_rationale.md) (1 shared connections)
- [caching lru cache](caching_lru_cache.md) (1 shared connections)

## Source Files

- `server/commands/container_helpers_inventory_display.py`

## Audit Trail

- EXTRACTED: 56 (93%)
- INFERRED: 4 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*