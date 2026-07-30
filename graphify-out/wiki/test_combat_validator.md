# test combat validator

> 133 nodes

## Key Concepts

- **test_combat_validator.py** (50 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **CombatValidator** (28 connections) — `server/validators/combat_validator.py`
- **._get_random_error_message()** (8 connections) — `server/validators/combat_validator.py`
- **.validate_combat_command()** (7 connections) — `server/validators/combat_validator.py`
- **combat_validator.py** (6 connections) — `server/validators/combat_validator.py`
- **Any** (4 connections)
- **._is_rate_limited()** (4 connections) — `server/validators/combat_validator.py`
- **combat_validator()** (3 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_can_attack_target_no_party_service_allows()** (3 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_can_attack_target_same_party_blocks()** (3 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_can_attack_target_different_party_allows()** (3 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **.__init__()** (3 connections) — `server/validators/combat_validator.py`
- **.validate_can_attack_target()** (3 connections) — `server/validators/combat_validator.py`
- **.validate_target_exists()** (3 connections) — `server/validators/combat_validator.py`
- **.validate_target_alive()** (3 connections) — `server/validators/combat_validator.py`
- **.validate_combat_state()** (3 connections) — `server/validators/combat_validator.py`
- **.validate_attack_strength()** (3 connections) — `server/validators/combat_validator.py`
- **._is_valid_target_name()** (3 connections) — `server/validators/combat_validator.py`
- **._contains_suspicious_patterns()** (3 connections) — `server/validators/combat_validator.py`
- **.get_combat_status_message()** (3 connections) — `server/validators/combat_validator.py`
- **test_combat_validator_init()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_combat_command_valid()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_combat_command_invalid_command_type()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_combat_command_no_target()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_combat_command_invalid_target_name()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- *... and 108 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (5 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (2 shared connections)
- [combat](combat.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_combat_validator.py`
- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 303 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*