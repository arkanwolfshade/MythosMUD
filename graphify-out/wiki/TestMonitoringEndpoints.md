# TestMonitoringEndpoints

> 37 nodes · cohesion 0.13

## Key Concepts

- **test_inventory_use_command.py** (24 connections) — `server/tests/unit/commands/test_inventory_use_command.py`
- **handle_use_command()** (14 connections) — `server/commands/inventory_use_command.py`
- **EffectProbe** (13 connections) — `server/tests/unit/commands/test_inventory_use_command.py`
- **FakePlayer** (12 connections) — `server/tests/unit/commands/test_inventory_use_command.py`
- **_use()** (10 connections) — `server/tests/unit/commands/test_inventory_use_command.py`
- **_resolve_usable_or_error()** (9 connections) — `server/commands/inventory_use_command.py`
- **ItemEffectResult** (9 connections) — `server/game/items/item_effects.py`
- **SimpleNamespace** (9 connections)
- **test_a_refused_effect_keeps_the_item()** (8 connections) — `server/tests/unit/commands/test_inventory_use_command.py`
- **test_unresolvable_selectors_report_what_is_missing()** (8 connections) — `server/tests/unit/commands/test_inventory_use_command.py`
- **asyncio** (7 connections)
- **test_a_failed_save_restores_the_inventory_but_the_effect_stands()** (7 connections) — `server/tests/unit/commands/test_inventory_use_command.py`
- **test_unusable_items_are_not_spent()** (7 connections) — `server/tests/unit/commands/test_inventory_use_command.py`
- **test_use_by_index_removes_the_last_item_from_the_stack()** (7 connections) — `server/tests/unit/commands/test_inventory_use_command.py`
- **test_use_decrements_a_stack_and_reports_to_player_and_room()** (7 connections) — `server/tests/unit/commands/test_inventory_use_command.py`
- **effect()** (6 connections) — `server/tests/unit/commands/test_inventory_use_command.py`
- **_stack()** (6 connections) — `server/tests/unit/commands/test_inventory_use_command.py`
- **request_obj()** (5 connections) — `server/tests/unit/commands/test_inventory_use_command.py`
- **test_player_resolution_errors_are_passed_through()** (4 connections) — `server/tests/unit/commands/test_inventory_use_command.py`
- **.__call__()** (3 connections) — `server/tests/unit/commands/test_inventory_use_command.py`
- **_prototype()** (3 connections) — `server/tests/unit/commands/test_inventory_use_command.py`
- **CommandResponse** (2 connections)
- **Player** (2 connections)
- **.__init__()** (2 connections) — `server/tests/unit/commands/test_inventory_use_command.py`
- **fixture** (2 connections)
- *... and 12 more nodes in this community*

## Relationships

- [items/catalog_dml.py](items-catalog_dml.py.md) (11 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (7 shared connections)
- [test_room_sync_service.py](test_room_sync_service.py.md) (3 shared connections)
- [command_parser.py](command_parser.py.md) (2 shared connections)
- [test_command_alias.py](test_command_alias.py.md) (1 shared connections)
- [run_flee_effect](run_flee_effect.md) (1 shared connections)

## Source Files

- `server/commands/inventory_use_command.py`
- `server/game/items/item_effects.py`
- `server/tests/unit/commands/test_inventory_use_command.py`

## Audit Trail

- EXTRACTED: 107 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*