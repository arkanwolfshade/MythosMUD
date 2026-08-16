# CombatValidator

> 41 nodes

## Key Concepts

- **CombatValidator** (26 connections) — `server/validators/combat_validator.py`
- **.__init__()** (11 connections) — `server/commands/combat_handler.py`
- **._get_random_error_message()** (8 connections) — `server/validators/combat_validator.py`
- **.validate_combat_command()** (7 connections) — `server/validators/combat_validator.py`
- **combat_validator.py** (7 connections) — `server/validators/combat_validator.py`
- **combat_validator()** (4 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **._is_rate_limited()** (4 connections) — `server/validators/combat_validator.py`
- **Any** (4 connections)
- **._contains_suspicious_patterns()** (3 connections) — `server/validators/combat_validator.py`
- **.get_combat_status_message()** (3 connections) — `server/validators/combat_validator.py`
- **.__init__()** (3 connections) — `server/validators/combat_validator.py`
- **._is_valid_target_name()** (3 connections) — `server/validators/combat_validator.py`
- **.validate_attack_strength()** (3 connections) — `server/validators/combat_validator.py`
- **.validate_can_attack_target()** (3 connections) — `server/validators/combat_validator.py`
- **.validate_combat_state()** (3 connections) — `server/validators/combat_validator.py`
- **.validate_target_alive()** (3 connections) — `server/validators/combat_validator.py`
- **.validate_target_exists()** (3 connections) — `server/validators/combat_validator.py`
- **.get_combat_death_message()** (2 connections) — `server/validators/combat_validator.py`
- **.get_combat_help_message()** (2 connections) — `server/validators/combat_validator.py`
- **.get_combat_result_message()** (2 connections) — `server/validators/combat_validator.py`
- **.get_combat_victory_message()** (2 connections) — `server/validators/combat_validator.py`
- **fixture** (1 connections)
- **Create a CombatValidator instance.** (1 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **Combat command validation with thematic error messages. This module provides…** (1 connections) — `server/validators/combat_validator.py`
- **Enhanced combat command validator with thematic error messages. Provides…** (1 connections) — `server/validators/combat_validator.py`
- *... and 16 more nodes in this community*

## Relationships

- [test_combat_validator.py](test_combat_validator.py.md) (6 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (2 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (1 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [combat_loader.py](combat_loader.py.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [CombatInstance](CombatInstance.md) (1 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (1 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/tests/unit/validators/test_combat_validator.py`
- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 69 (93%)
- INFERRED: 5 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*