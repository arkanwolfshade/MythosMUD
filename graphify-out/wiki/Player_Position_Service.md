# Player Position Service

> 293 nodes

## Key Concepts

- **CombatCommandHandler** (54 connections) — `server/commands/combat_handler.py`
- **TargetResolutionService** (50 connections) — `server/services/target_resolution_service.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **TargetResolutionResult** (39 connections) — `server/schemas/shared/target_resolution.py`
- **test_combat_handler.py** (37 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **CombatValidator** (28 connections) — `server/validators/combat_validator.py`
- **target_resolution_service.py** (27 connections) — `server/services/target_resolution_service.py`
- **test_target_resolution_service.py** (27 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **CombatCommandHandlerExtras** (25 connections) — `server/commands/combat_handler.py`
- **combat_loader.py** (25 connections) — `server/commands/combat_loader.py`
- **_handler_with_persistence()** (20 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **combat.py** (19 connections) — `server/commands/combat.py`
- **get_combat_command_handler()** (19 connections) — `server/commands/combat_loader.py`
- **AppWithState** (17 connections) — `server/commands/combat_app_protocols.py`
- **_NpcWithLife** (17 connections) — `server/commands/combat_handler.py`
- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **TargetMetadata** (12 connections) — `server/schemas/shared/target_metadata.py`
- **.__init__()** (11 connections) — `server/commands/combat_handler.py`
- **_AppStatePersistence** (10 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_AppWithPersistence** (10 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **handle_attack_command()** (9 connections) — `server/commands/combat_loader.py`
- **.resolve_target()** (9 connections) — `server/services/target_resolution_service.py`
- **_app_from_request()** (8 connections) — `server/commands/combat_loader.py`
- **handle_punch_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_kick_command()** (8 connections) — `server/commands/combat_loader.py`
- *... and 268 more nodes in this community*

## Relationships

- [Any](Any.md) (38 shared connections)
- [Spell Targeting](Spell_Targeting.md) (31 shared connections)
- [combat taunt](combat_taunt.md) (16 shared connections)
- [combat flee](combat_flee.md) (11 shared connections)
- [Connection Manager](Connection_Manager.md) (11 shared connections)
- [.initialize()](initialize%28%29.md) (10 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (10 shared connections)
- [.set player combat service()](set_player_combat_service%28%29.md) (10 shared connections)
- [test flee command](test_flee_command.md) (9 shared connections)
- [. init ()](_init_%28%29.md) (9 shared connections)
- [main()](main%28%29.md) (8 shared connections)
- [follow commands](follow_commands.md) (8 shared connections)

## Source Files

- `server/commands/combat.py`
- `server/commands/combat_app_protocols.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_loader.py`
- `server/schemas/shared/target_metadata.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/commands/test_flee_command.py`
- `server/tests/unit/schemas/test_target_resolution.py`
- `server/tests/unit/services/test_target_resolution_service.py`
- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 1055 (89%)
- INFERRED: 130 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*