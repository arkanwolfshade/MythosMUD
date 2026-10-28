# HeaderBar.tsx

> 46 nodes · cohesion 0.07

## Key Concepts

- **CombatCommandFactory** (29 connections) — `server/utils/command_factories_combat.py`
- **test_command_factories_combat.py** (14 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **.__init__()** (9 connections) — `server/utils/command_factories.py`
- **.create_attack_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **.create_kick_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **.create_punch_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **.create_strike_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **.create_taunt_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **test_create_attack_command()** (4 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_attack_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_flee_command()** (4 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_kick_command()** (4 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_kick_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_punch_command()** (4 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_punch_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_strike_command()** (4 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_strike_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_taunt_command()** (4 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_taunt_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **.create_assist_command()** (4 connections) — `server/utils/command_factories_combat.py`
- **.create_flee_command()** (4 connections) — `server/utils/command_factories_combat.py`
- **.create_protect_command()** (4 connections) — `server/utils/command_factories_combat.py`
- **test_the_factory_builds_an_assist_command_with_or_without_a_name()** (3 connections) — `server/tests/unit/commands/test_assist_wiring.py`
- **test_the_factory_builds_a_protect_command_with_or_without_a_name()** (3 connections) — `server/tests/unit/commands/test_protect_wiring.py`
- **Unit tests for combat command factories. Tests the CombatCommandFactory class…** (1 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- *... and 21 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (7 shared connections)
- [CommandFactory](CommandFactory.md) (4 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (2 shared connections)
- [useMythosAppState.ts](useMythosAppState.ts.md) (1 shared connections)
- [PrototypeRegistry](PrototypeRegistry.md) (1 shared connections)
- [command_service.py](command_service.py.md) (1 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (1 shared connections)
- [test_message_filtering.py](test_message_filtering.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_assist_wiring.py`
- `server/tests/unit/commands/test_protect_wiring.py`
- `server/tests/unit/utils/test_command_factories_combat.py`
- `server/utils/command_factories.py`
- `server/utils/command_factories_combat.py`

## Audit Trail

- EXTRACTED: 78 (85%)
- INFERRED: 14 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*