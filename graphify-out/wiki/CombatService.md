# CombatService

> 158 nodes

## Key Concepts

- **CombatCommandHandler** (54 connections) — `server/commands/combat_handler.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **TargetResolutionResult** (39 connections) — `server/schemas/shared/target_resolution.py`
- **test_combat_handler.py** (37 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **CombatCommandHandlerExtras** (25 connections) — `server/commands/combat_handler.py`
- **combat_loader.py** (25 connections) — `server/commands/combat_loader.py`
- **_handler_with_persistence()** (20 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **combat.py** (19 connections) — `server/commands/combat.py`
- **get_combat_command_handler()** (19 connections) — `server/commands/combat_loader.py`
- **AppWithState** (17 connections) — `server/commands/combat_app_protocols.py`
- **_NpcWithLife** (17 connections) — `server/commands/combat_handler.py`
- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **TargetMetadata** (12 connections) — `server/schemas/shared/target_metadata.py`
- **target_resolution.py** (11 connections) — `server/schemas/shared/target_resolution.py`
- **_AppStatePersistence** (10 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_AppWithPersistence** (10 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **handle_attack_command()** (9 connections) — `server/commands/combat_loader.py`
- **_app_from_request()** (8 connections) — `server/commands/combat_loader.py`
- **handle_punch_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_kick_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_strike_command()** (8 connections) — `server/commands/combat_loader.py`
- **_CmdType** (8 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_as_app_with_state()** (8 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **combat_app_protocols.py** (6 connections) — `server/commands/combat_app_protocols.py`
- **Any** (6 connections)
- *... and 133 more nodes in this community*

## Relationships

- [.end combat()](end_combat%28%29.md) (25 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (17 shared connections)
- [test magic commands](test_magic_commands.md) (15 shared connections)
- [test command service](test_command_service.md) (14 shared connections)
- [combat](combat.md) (12 shared connections)
- [. init ()](_init_%28%29.md) (12 shared connections)
- [Player](Player.md) (10 shared connections)
- [test flee command](test_flee_command.md) (9 shared connections)
- [combat flee](combat_flee.md) (8 shared connections)
- [test player event handlers room](test_player_event_handlers_room.md) (8 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (6 shared connections)
- [login grace period](login_grace_period.md) (6 shared connections)

## Source Files

- `server/commands/combat.py`
- `server/commands/combat_app_protocols.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_loader.py`
- `server/schemas/shared/target_metadata.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/commands/test_flee_command.py`
- `server/tests/unit/schemas/test_target_resolution.py`

## Audit Trail

- EXTRACTED: 618 (85%)
- INFERRED: 111 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*