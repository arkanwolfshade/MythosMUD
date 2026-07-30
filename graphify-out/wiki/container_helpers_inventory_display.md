# container helpers inventory display

> 21 nodes

## Key Concepts

- **container_helpers_inventory_display.py** (17 connections) — `server/commands/container_helpers_inventory_display.py`
- **handle_inventory_command()** (14 connections) — `server/commands/inventory_commands.py`
- **_apply_container_component_to_slot()** (8 connections) — `server/commands/container_helpers_inventory_display.py`
- **get_container_data_for_inventory()** (7 connections) — `server/commands/container_helpers_inventory_display.py`
- **match_container_to_slot()** (6 connections) — `server/commands/container_helpers_inventory_display.py`
- **_inventory_stack_to_display_dict()** (4 connections) — `server/commands/container_helpers_inventory_display.py`
- **update_equipped_with_container_info()** (4 connections) — `server/commands/container_helpers_inventory_display.py`
- **_component_metadata()** (3 connections) — `server/commands/container_helpers_inventory_display.py`
- **test_handle_inventory_command()** (3 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **_equipped_matches_container_metadata()** (2 connections) — `server/commands/container_helpers_inventory_display.py`
- **_lock_state_as_str()** (2 connections) — `server/commands/container_helpers_inventory_display.py`
- **InventoryStack** (1 connections)
- **Player** (1 connections)
- **Container display helpers for inventory UI (wearable contents, slot matching).** (1 connections) — `server/commands/container_helpers_inventory_display.py`
- **Shallow-copy a wearable stack into a plain dict for equipped-view metadata.** (1 connections) — `server/commands/container_helpers_inventory_display.py`
- **Match a container component to an equipped slot. Returns slot name or None.** (1 connections) — `server/commands/container_helpers_inventory_display.py`
- **Get container contents, capacities, and lock states for equipped containers.** (1 connections) — `server/commands/container_helpers_inventory_display.py`
- **Update equipped items' metadata to include container information.** (1 connections) — `server/commands/container_helpers_inventory_display.py`
- **CommandResponse** (1 connections)
- **Display the player's inventory and equipped items, including container contents.** (1 connections) — `server/commands/inventory_commands.py`
- **Test handle_inventory_command() displays inventory.** (1 connections) — `server/tests/unit/commands/test_inventory_commands.py`

## Relationships

- [test resolve state no app()](test_resolve_state_no_app%28%29.md) (5 shared connections)
- [container helpers inventory](container_helpers_inventory.md) (4 shared connections)
- [Lock](Lock.md) (3 shared connections)
- [handle pickup command()](handle_pickup_command%28%29.md) (3 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (1 shared connections)
- [init](init.md) (1 shared connections)
- [test magic commands](test_magic_commands.md) (1 shared connections)
- [websocket handler app state](websocket_handler_app_state.md) (1 shared connections)
- [DropResolved](DropResolved.md) (1 shared connections)
- [Player Position Service](Player_Position_Service.md) (1 shared connections)
- [Base](Base.md) (1 shared connections)

## Source Files

- `server/commands/container_helpers_inventory_display.py`
- `server/commands/inventory_commands.py`
- `server/tests/unit/commands/test_inventory_commands.py`

## Audit Trail

- EXTRACTED: 73 (91%)
- INFERRED: 7 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*