# Commands Container Inventory

> 18 nodes · cohesion 0.18

## Key Concepts

- **container_helpers_inventory.py** (31 connections) — `server/commands/container_helpers_inventory.py`
- **container_helpers_inventory_display.py** (17 connections) — `server/commands/container_helpers_inventory_display.py`
- **get_container_data_for_inventory()** (8 connections) — `server/commands/container_helpers_inventory_display.py`
- **_apply_container_component_to_slot()** (6 connections) — `server/commands/container_helpers_inventory_display.py`
- **match_container_to_slot()** (6 connections) — `server/commands/container_helpers_inventory_display.py`
- **_inventory_stack_to_display_dict()** (4 connections) — `server/commands/container_helpers_inventory_display.py`
- **update_equipped_with_container_info()** (4 connections) — `server/commands/container_helpers_inventory_display.py`
- **_component_metadata()** (3 connections) — `server/commands/container_helpers_inventory_display.py`
- **_equipped_matches_container_metadata()** (2 connections) — `server/commands/container_helpers_inventory_display.py`
- **_lock_state_as_str()** (2 connections) — `server/commands/container_helpers_inventory_display.py`
- **Container display helpers for inventory UI (wearable contents, slot matching).** (1 connections) — `server/commands/container_helpers_inventory_display.py`
- **Get container contents, capacities, and lock states for equipped containers.** (1 connections) — `server/commands/container_helpers_inventory_display.py`
- **Shallow-copy a wearable stack into a plain dict for equipped-view metadata.** (1 connections) — `server/commands/container_helpers_inventory_display.py`
- **Update equipped items' metadata to include container information.** (1 connections) — `server/commands/container_helpers_inventory_display.py`
- **Match a container component to an equipped slot. Returns slot name or None.** (1 connections) — `server/commands/container_helpers_inventory_display.py`
- **Container-related helper functions for inventory commands (facade re-exports).** (1 connections) — `server/commands/container_helpers_inventory.py`
- **InventoryStack** (1 connections) — `server/commands/container_helpers_inventory_display.py`
- **Player** (1 connections) — `server/commands/container_helpers_inventory_display.py`

## Relationships

- [[Container Inventory Finders]] (12 shared connections)
- [[Container Inventory Ops]] (11 shared connections)
- [[Admin Summon Command]] (7 shared connections)
- [[Inventory Service Helpers]] (4 shared connections)
- [[NPC Admin API]] (1 shared connections)
- [[SQLAlchemy Model Base]] (1 shared connections)
- [[Player Domain Model]] (1 shared connections)

## Source Files

- `server/commands/container_helpers_inventory.py`
- `server/commands/container_helpers_inventory_display.py`

## Audit Trail

- EXTRACTED: 89 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
