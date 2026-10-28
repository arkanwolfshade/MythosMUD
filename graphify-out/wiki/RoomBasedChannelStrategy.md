# RoomBasedChannelStrategy

> 12 nodes · cohesion 0.23

## Key Concepts

- **test_command_use.py** (15 connections) — `server/tests/unit/models/test_command_use.py`
- **UseCommand** (13 connections) — `server/models/command_inventory.py`
- **test_use_command_rejects_non_positive_index()** (3 connections) — `server/tests/unit/models/test_command_use.py`
- **test_use_command_type_is_use()** (3 connections) — `server/tests/unit/models/test_command_use.py`
- **test_use_has_help_text_naming_its_aliases()** (3 connections) — `server/tests/unit/models/test_command_use.py`
- **test_command_factory_builds_use_command()** (2 connections) — `server/tests/unit/models/test_command_use.py`
- **test_use_command_accepts_index_or_name()** (2 connections) — `server/tests/unit/models/test_command_use.py`
- **test_use_command_requires_a_selector()** (2 connections) — `server/tests/unit/models/test_command_use.py`
- **test_use_command_strips_the_search_term()** (2 connections) — `server/tests/unit/models/test_command_use.py`
- **Command for using a consumable item from inventory (also reached via…** (1 connections) — `server/models/command_inventory.py`
- **parametrize** (1 connections)
- **Unit tests for UseCommand and its wiring into the command factory and help…** (1 connections) — `server/tests/unit/models/test_command_use.py`

## Relationships

- [ContainerComponent](ContainerComponent.md) (8 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [test_communication_commands_flows.py](test_communication_commands_flows.py.md) (2 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (2 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (1 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (1 shared connections)

## Source Files

- `server/models/command_inventory.py`
- `server/tests/unit/models/test_command_use.py`

## Audit Trail

- EXTRACTED: 25 (76%)
- INFERRED: 8 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*