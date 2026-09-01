# CombatCommandHandler

> 386 nodes

## Key Concepts

- **CombatCommandHandler** (51 connections) — `server/commands/combat_handler.py`
- **TargetResolutionService** (51 connections) — `server/services/target_resolution_service.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **TargetType** (45 connections) — `server/schemas/shared/target_resolution.py`
- **test_target_resolution_service.py** (43 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_combat_handler.py** (40 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **TargetResolutionResult** (36 connections) — `server/schemas/shared/target_resolution.py`
- **combat_taunt.py** (34 connections) — `server/commands/combat_taunt.py`
- **target_resolution_service.py** (29 connections) — `server/services/target_resolution_service.py`
- **TauntCommandHandler** (27 connections) — `server/commands/combat_taunt.py`
- **combat_attack.py** (25 connections) — `server/commands/combat_attack.py`
- **_handler_with_persistence()** (22 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_combat_taunt.py** (22 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **asyncio** (21 connections)
- **test_combat_attack.py** (20 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **schemas/shared/__init__.py** (16 connections) — `server/schemas/shared/__init__.py`
- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **AppWithState** (15 connections) — `server/commands/combat_app_protocols.py`
- **TargetMetadata** (15 connections) — `server/schemas/shared/target_metadata.py`
- **asyncio** (14 connections)
- **run_handle_taunt_command()** (13 connections) — `server/commands/combat_taunt.py`
- **target_resolution.py** (13 connections) — `server/schemas/shared/target_resolution.py`
- **_validate_taunt_context()** (12 connections) — `server/commands/combat_taunt.py`
- **run_handle_attack_command()** (11 connections) — `server/commands/combat_attack.py`
- **_apply_taunt_and_maybe_broadcast()** (11 connections) — `server/commands/combat_taunt.py`
- *... and 361 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (53 shared connections)
- [CombatParticipant](CombatParticipant.md) (15 shared connections)
- [CombatService](CombatService.md) (13 shared connections)
- [combat_loader.py](combat_loader.py.md) (11 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (11 shared connections)
- [SpellEffectType](SpellEffectType.md) (9 shared connections)
- [CombatInstance](CombatInstance.md) (8 shared connections)
- [AliasStorage](AliasStorage.md) (7 shared connections)
- [EventBus](EventBus.md) (7 shared connections)
- [test_party_commands.py](test_party_commands.py.md) (7 shared connections)
- [SpellEffects](SpellEffects.md) (7 shared connections)
- [get_logger](get_logger.md) (7 shared connections)

## Source Files

- `server/commands/combat_app_protocols.py`
- `server/commands/combat_attack.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_taunt.py`
- `server/schemas/shared/__init__.py`
- `server/schemas/shared/target_metadata.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/commands/test_combat_attack.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/commands/test_combat_taunt.py`
- `server/tests/unit/schemas/test_target_resolution.py`
- `server/tests/unit/services/test_target_resolution_service.py`

## Audit Trail

- EXTRACTED: 853 (92%)
- INFERRED: 79 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*