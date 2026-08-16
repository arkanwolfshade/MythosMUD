# CombatCommandHandler

> 77 nodes

## Key Concepts

- **CombatCommandHandler** (51 connections) — `server/commands/combat_handler.py`
- **test_flee_command.py** (29 connections) — `server/tests/unit/commands/test_flee_command.py`
- **FleeHandlerDeps** (10 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_request_with_persistence()** (10 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_no_exits_returns_no_escape()** (9 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_roll_fails_returns_failure_and_uses_action()** (9 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_roll_succeeds_returns_success()** (9 connections) — `server/tests/unit/commands/test_flee_command.py`
- **.get_player_and_room()** (6 connections) — `server/commands/combat_handler.py`
- **handler()** (6 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_make_participant()** (6 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_standing_player_id()** (6 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_not_in_combat_returns_message()** (6 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_not_standing_forces_stand_and_returns_message()** (6 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_get_combat_command_handler_includes_flee()** (6 connections) — `server/tests/unit/commands/test_flee_command.py`
- **._get_persistence_from_app()** (5 connections) — `server/commands/combat_handler.py`
- **.handle_attack_command()** (5 connections) — `server/commands/combat_handler.py`
- **.handle_taunt_command()** (5 connections) — `server/commands/combat_handler.py`
- **.resolve_combat_target()** (5 connections) — `server/commands/combat_handler.py`
- **._validate_combat_target_match()** (5 connections) — `server/commands/combat_handler.py`
- **asyncio** (5 connections)
- **.extract_combat_command_data()** (4 connections) — `server/commands/combat_handler.py`
- **.get_npc_instance()** (4 connections) — `server/commands/combat_handler.py`
- **.handle_flee_command()** (4 connections) — `server/commands/combat_handler.py`
- **flee_handler_deps()** (4 connections) — `server/tests/unit/commands/test_flee_command.py`
- **Any** (4 connections)
- *... and 52 more nodes in this community*

## Relationships

- [combat_loader.py](combat_loader.py.md) (9 shared connections)
- [CombatInstance](CombatInstance.md) (7 shared connections)
- [test_combat_handler.py](test_combat_handler.py.md) (4 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (4 shared connections)
- [AliasStorage](AliasStorage.md) (4 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (4 shared connections)
- [server/models/game.py](server-models-game.py.md) (3 shared connections)
- [TargetMatch](TargetMatch.md) (3 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (2 shared connections)
- [CombatValidator](CombatValidator.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [CombatParticipant](CombatParticipant.md) (2 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/tests/unit/commands/test_flee_command.py`

## Audit Trail

- EXTRACTED: 152 (86%)
- INFERRED: 24 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*