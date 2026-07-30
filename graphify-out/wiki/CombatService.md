# CombatService

> 419 nodes

## Key Concepts

- **TargetMatch** (122 connections) — `server/schemas/shared/target_resolution.py`
- **PlayerCombatService** (78 connections) — `server/services/player_combat_service.py`
- **CombatCommandHandler** (54 connections) — `server/commands/combat_handler.py`
- **TargetResolutionService** (53 connections) — `server/services/target_resolution_service.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **TargetResolutionResult** (39 connections) — `server/schemas/shared/target_resolution.py`
- **test_combat_handler.py** (37 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_player_combat_service.py** (37 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **player_combat_service.py** (35 connections) — `server/services/player_combat_service.py`
- **TargetType** (31 connections) — `server/schemas/shared/target_resolution.py`
- **CombatValidator** (28 connections) — `server/validators/combat_validator.py`
- **target_resolution_service.py** (27 connections) — `server/services/target_resolution_service.py`
- **test_target_resolution_service.py** (27 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **CombatCommandHandlerExtras** (25 connections) — `server/commands/combat_handler.py`
- **combat_loader.py** (25 connections) — `server/commands/combat_loader.py`
- **spell_targeting.py** (25 connections) — `server/game/magic/spell_targeting.py`
- **_handler_with_persistence()** (20 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **combat.py** (19 connections) — `server/commands/combat.py`
- **get_combat_command_handler()** (19 connections) — `server/commands/combat_loader.py`
- **AppWithState** (17 connections) — `server/commands/combat_app_protocols.py`
- **_NpcWithLife** (17 connections) — `server/commands/combat_handler.py`
- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **UUID** (15 connections)
- **PlayerCombatState** (14 connections) — `server/services/player_combat_service.py`
- **TargetMetadata** (12 connections) — `server/schemas/shared/target_metadata.py`
- *... and 394 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (55 shared connections)
- [message handler factory](message_handler_factory.md) (29 shared connections)
- [Player Position Service](Player_Position_Service.md) (22 shared connections)
- [test player event handlers room](test_player_event_handlers_room.md) (21 shared connections)
- [Player](Player.md) (17 shared connections)
- [parse jsonb column()](parse_jsonb_column%28%29.md) (17 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (16 shared connections)
- [.end combat()](end_combat%28%29.md) (16 shared connections)
- [Any](Any.md) (15 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (12 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (11 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (11 shared connections)

## Source Files

- `server/commands/combat.py`
- `server/commands/combat_app_protocols.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_loader.py`
- `server/game/magic/spell_targeting.py`
- `server/realtime/connection_manager.py`
- `server/schemas/shared/target_metadata.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/player_combat_service.py`
- `server/services/player_combat_service_support.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/commands/test_flee_command.py`
- `server/tests/unit/schemas/test_target_resolution.py`
- `server/tests/unit/services/test_player_combat_service.py`
- `server/tests/unit/services/test_target_resolution_service.py`
- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 1631 (90%)
- INFERRED: 176 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*