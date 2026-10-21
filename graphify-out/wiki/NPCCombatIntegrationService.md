# NPCCombatIntegrationService

> 217 nodes · cohesion 0.02

## Key Concepts

- **ValidationError** (325 connections) — `server/exceptions.py`
- **InventoryCommandFactory** (98 connections) — `server/utils/command_factories_inventory.py`
- **test_command_factories_inventory.py** (70 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_command_factories_inventory_helpers.py** (22 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **.create_get_command()** (20 connections) — `server/utils/command_factories_inventory.py`
- **.create_pickup_command()** (19 connections) — `server/utils/command_factories_inventory.py`
- **.create_put_command()** (19 connections) — `server/utils/command_factories_inventory.py`
- **command_factories_inventory.py** (17 connections) — `server/utils/command_factories_inventory.py`
- **.create_equip_command()** (16 connections) — `server/utils/command_factories_inventory.py`
- **.create_unequip_command()** (14 connections) — `server/utils/command_factories_inventory.py`
- **MythosValidationError** (10 connections)
- **.create_drop_command()** (9 connections) — `server/utils/command_factories_inventory.py`
- **WithdrawCommand** (7 connections) — `server/models/command_inventory.py`
- **.create_use_command()** (7 connections) — `server/utils/command_factories_inventory.py`
- **parametrize** (6 connections)
- **test_create_get_command_separator_needs_both_sides()** (6 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_put_command_separator_needs_both_sides()** (6 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_use_command_rejects_missing_or_zero_selector()** (6 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_deposit_and_withdraw_share_item_and_quantity_parsing()** (6 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **.create_inventory_command()** (6 connections) — `server/utils/command_factories_inventory.py`
- **_pop_trailing_quantity()** (6 connections) — `server/utils/command_factories_inventory.py`
- **_split_item_container()** (6 connections) — `server/utils/command_factories_inventory.py`
- **test_create_drop_command_invalid_index()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_inventory_command_with_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_pickup_command_invalid_index()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- *... and 192 more nodes in this community*

## Relationships

- [SecureBaseModel](SecureBaseModel.md) (44 shared connections)
- [CommandFactory](CommandFactory.md) (29 shared connections)
- [AttributeError](AttributeError.md) (23 shared connections)
- [test_message_filtering.py](test_message_filtering.py.md) (19 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (17 shared connections)
- [PrototypeRegistry](PrototypeRegistry.md) (16 shared connections)
- [command_service.py](command_service.py.md) (15 shared connections)
- [MemoryProfiler](MemoryProfiler.md) (11 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (9 shared connections)
- [resolve_lazy_attr](resolve_lazy_attr.md) (9 shared connections)
- [ContainerComponent](ContainerComponent.md) (9 shared connections)
- [test_communication_commands_flows.py](test_communication_commands_flows.py.md) (9 shared connections)

## Source Files

- `server/exceptions.py`
- `server/game/profession_service.py`
- `server/models/command_inventory.py`
- `server/tests/unit/commands/test_command_service.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/utils/test_command_factories_inventory.py`
- `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- `server/tests/unit/utils/test_command_parser.py`
- `server/tests/unit/utils/test_command_processor.py`
- `server/utils/command_factories_inventory.py`

## Audit Trail

- EXTRACTED: 484 (63%)
- INFERRED: 289 (37%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*