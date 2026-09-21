# CombatCommandHandler

> 257 nodes

## Key Concepts

- **CombatCommandHandler** (51 connections) — `server/commands/combat_handler.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **TargetType** (45 connections) — `server/schemas/shared/target_resolution.py`
- **test_combat_handler.py** (39 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **combat_taunt.py** (34 connections) — `server/commands/combat_taunt.py`
- **TauntCommandHandler** (27 connections) — `server/commands/combat_taunt.py`
- **CombatValidator** (26 connections) — `server/validators/combat_validator.py`
- **combat_attack.py** (25 connections) — `server/commands/combat_attack.py`
- **_handler_with_persistence()** (22 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_combat_taunt.py** (21 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_combat_attack.py** (19 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **get_current_tick()** (16 connections) — `server/app/game_tick_counter.py`
- **AppWithState** (15 connections) — `server/commands/combat_app_protocols.py`
- **asyncio** (14 connections)
- **run_handle_taunt_command()** (13 connections) — `server/commands/combat_taunt.py`
- **_validate_taunt_context()** (12 connections) — `server/commands/combat_taunt.py`
- **target_resolution.py** (12 connections) — `server/schemas/shared/target_resolution.py`
- **run_handle_attack_command()** (11 connections) — `server/commands/combat_attack.py`
- **.__init__()** (11 connections) — `server/commands/combat_handler.py`
- **_apply_taunt_and_maybe_broadcast()** (11 connections) — `server/commands/combat_taunt.py`
- **asyncio** (11 connections)
- **_execute_phantom_combat_action()** (10 connections) — `server/commands/combat_attack.py`
- **_resolve_combat_damage()** (9 connections) — `server/commands/combat_attack.py`
- **_resolve_taunt_combat_and_participant()** (9 connections) — `server/commands/combat_taunt.py`
- **_as_app_with_state()** (9 connections) — `server/tests/unit/commands/test_combat_handler.py`
- *... and 232 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (22 shared connections)
- [get_config](get_config.md) (19 shared connections)
- [TargetResolutionResult](TargetResolutionResult.md) (13 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [combat_loader.py](combat_loader.py.md) (12 shared connections)
- [CombatService](CombatService.md) (10 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (9 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (9 shared connections)
- [AliasStorage](AliasStorage.md) (7 shared connections)
- [CombatInstance](CombatInstance.md) (7 shared connections)
- [CombatParticipant](CombatParticipant.md) (7 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (6 shared connections)

## Source Files

- `server/app/game_tick_counter.py`
- `server/commands/combat_app_protocols.py`
- `server/commands/combat_attack.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_taunt.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/commands/test_combat_attack.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/commands/test_combat_taunt.py`
- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 600 (90%)
- INFERRED: 63 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*