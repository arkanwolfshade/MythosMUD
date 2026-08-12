# Magic Service Bundle

> 191 nodes

## Key Concepts

- **CombatCommandHandler** (54 connections) — `server/commands/combat_handler.py`
- **test_combat_handler.py** (37 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_flee_command.py** (28 connections) — `server/tests/unit/commands/test_flee_command.py`
- **CombatValidator** (28 connections) — `server/validators/combat_validator.py`
- **CombatCommandHandlerExtras** (25 connections) — `server/commands/combat_handler.py`
- **combat_loader.py** (25 connections) — `server/commands/combat_loader.py`
- **_handler_with_persistence()** (20 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **combat.py** (19 connections) — `server/commands/combat.py`
- **get_combat_command_handler()** (19 connections) — `server/commands/combat_loader.py`
- **.event_bus()** (12 connections) — `server/realtime/connection_manager.py`
- **.__init__()** (11 connections) — `server/commands/combat_handler.py`
- **_AppStatePersistence** (10 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_AppWithPersistence** (10 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **FleeHandlerDeps** (10 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_request_with_persistence()** (10 connections) — `server/tests/unit/commands/test_flee_command.py`
- **handle_attack_command()** (9 connections) — `server/commands/combat_loader.py`
- **_app_from_request()** (8 connections) — `server/commands/combat_loader.py`
- **handle_punch_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_kick_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_strike_command()** (8 connections) — `server/commands/combat_loader.py`
- **_CmdType** (8 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_as_app_with_state()** (8 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_flee_no_exits_returns_no_escape()** (8 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_roll_fails_returns_failure_and_uses_action()** (8 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_roll_succeeds_returns_success()** (8 connections) — `server/tests/unit/commands/test_flee_command.py`
- *... and 166 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (15 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (15 shared connections)
- [Look Command Helpers](Look_Command_Helpers.md) (15 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (14 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (8 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (8 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (8 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (7 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (6 shared connections)
- [Player Service Tests](Player_Service_Tests.md) (6 shared connections)
- [Quest Instance Repository](Quest_Instance_Repository.md) (4 shared connections)
- [Container Open Events](Container_Open_Events.md) (4 shared connections)

## Source Files

- `server/commands/combat.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_loader.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/commands/test_flee_command.py`
- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 683 (89%)
- INFERRED: 88 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*