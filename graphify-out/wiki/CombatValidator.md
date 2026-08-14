# CombatValidator

> 35 nodes

## Key Concepts

- **CombatValidator** (28 connections) — `server/validators/combat_validator.py`
- **._get_random_error_message()** (8 connections) — `server/validators/combat_validator.py`
- **.validate_combat_command()** (7 connections) — `server/validators/combat_validator.py`
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
- **Enhanced combat command validator with thematic error messages. Provides…** (1 connections) — `server/validators/combat_validator.py`
- **Initialize the combat validator. Args: party_service: Optional PartyService for…** (1 connections) — `server/validators/combat_validator.py`
- **Validate that attacker is allowed to attack target (e.g. not same party). Hook…** (1 connections) — `server/validators/combat_validator.py`
- **Validate a combat command with thematic error messages. Args: command_data: The…** (1 connections) — `server/validators/combat_validator.py`
- **Validate that a target exists with thematic error messages. Args: target_name:…** (1 connections) — `server/validators/combat_validator.py`
- **Validate that a target is alive with thematic error messages. Args:…** (1 connections) — `server/validators/combat_validator.py`
- **Validate combat state with thematic error messages. Args: is_in_combat: Whether…** (1 connections) — `server/validators/combat_validator.py`
- *... and 10 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (3 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (2 shared connections)
- [combat_validator](combat_validator.md) (1 shared connections)
- [test_validate_can_attack_target_different_party_allows](test_validate_can_attack_target_different_party_allows.md) (1 shared connections)
- [test_validate_can_attack_target_no_party_service_allows](test_validate_can_attack_target_no_party_service_allows.md) (1 shared connections)
- [test_validate_can_attack_target_same_party_blocks](test_validate_can_attack_target_same_party_blocks.md) (1 shared connections)
- [test_combat_validator.py](test_combat_validator.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 54 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*