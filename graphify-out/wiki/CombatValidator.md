# CombatValidator

> 28 nodes

## Key Concepts

- **CombatValidator** (26 connections) — `server/validators/combat_validator.py`
- **._get_random_error_message()** (8 connections) — `server/validators/combat_validator.py`
- **test_validate_can_attack_target_different_party_allows()** (3 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_can_attack_target_no_party_service_allows()** (3 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_can_attack_target_same_party_blocks()** (3 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **.validate_attack_strength()** (3 connections) — `server/validators/combat_validator.py`
- **.validate_can_attack_target()** (3 connections) — `server/validators/combat_validator.py`
- **.validate_combat_state()** (3 connections) — `server/validators/combat_validator.py`
- **.validate_target_alive()** (3 connections) — `server/validators/combat_validator.py`
- **.validate_target_exists()** (3 connections) — `server/validators/combat_validator.py`
- **.get_combat_death_message()** (2 connections) — `server/validators/combat_validator.py`
- **.get_combat_help_message()** (2 connections) — `server/validators/combat_validator.py`
- **.get_combat_result_message()** (2 connections) — `server/validators/combat_validator.py`
- **.get_combat_victory_message()** (2 connections) — `server/validators/combat_validator.py`
- **When party_service is None, validate_can_attack_target allows attack.** (1 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **When both players are in same party, validate_can_attack_target blocks attack.** (1 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **When players are not in same party, validate_can_attack_target allows attack.** (1 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **Enhanced combat command validator with thematic error messages. Provides…** (1 connections) — `server/validators/combat_validator.py`
- **Validate that attacker is allowed to attack target (e.g. not same party). Hook…** (1 connections) — `server/validators/combat_validator.py`
- **Validate that a target exists with thematic error messages. Args: target_name:…** (1 connections) — `server/validators/combat_validator.py`
- **Validate that a target is alive with thematic error messages. Args:…** (1 connections) — `server/validators/combat_validator.py`
- **Validate combat state with thematic error messages. Args: is_in_combat: Whether…** (1 connections) — `server/validators/combat_validator.py`
- **Validate attack strength with thematic error messages. Args: player_level:…** (1 connections) — `server/validators/combat_validator.py`
- **Get a random error message for the given error type.** (1 connections) — `server/validators/combat_validator.py`
- **Get a thematic help message for combat commands.** (1 connections) — `server/validators/combat_validator.py`
- *... and 3 more nodes in this community*

## Relationships

- [.validate_combat_command](validate_combat_command.md) (7 shared connections)
- [test_combat_validator.py](test_combat_validator.py.md) (4 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [combat_validator](combat_validator.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_combat_validator.py`
- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 43 (90%)
- INFERRED: 5 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*