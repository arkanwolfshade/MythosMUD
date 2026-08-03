# spell models rationale

> 25 nodes

## Key Concepts

- **._get_random_error_message()** (8 connections) — `server/validators/combat_validator.py`
- **.validate_combat_command()** (7 connections) — `server/validators/combat_validator.py`
- **Any** (4 connections)
- **._is_rate_limited()** (4 connections) — `server/validators/combat_validator.py`
- **.__init__()** (3 connections) — `server/validators/combat_validator.py`
- **.validate_can_attack_target()** (3 connections) — `server/validators/combat_validator.py`
- **.validate_target_exists()** (3 connections) — `server/validators/combat_validator.py`
- **.validate_target_alive()** (3 connections) — `server/validators/combat_validator.py`
- **.validate_combat_state()** (3 connections) — `server/validators/combat_validator.py`
- **.validate_attack_strength()** (3 connections) — `server/validators/combat_validator.py`
- **._is_valid_target_name()** (3 connections) — `server/validators/combat_validator.py`
- **._contains_suspicious_patterns()** (3 connections) — `server/validators/combat_validator.py`
- **.get_combat_status_message()** (3 connections) — `server/validators/combat_validator.py`
- **Initialize the combat validator.          Args:             party_service: Optio** (1 connections) — `server/validators/combat_validator.py`
- **Validate that attacker is allowed to attack target (e.g. not same party).** (1 connections) — `server/validators/combat_validator.py`
- **Validate a combat command with thematic error messages.          Args:** (1 connections) — `server/validators/combat_validator.py`
- **Validate that a target exists with thematic error messages.          Args:** (1 connections) — `server/validators/combat_validator.py`
- **Validate that a target is alive with thematic error messages.          Args:** (1 connections) — `server/validators/combat_validator.py`
- **Validate combat state with thematic error messages.          Args:             i** (1 connections) — `server/validators/combat_validator.py`
- **Validate attack strength with thematic error messages.          Args:** (1 connections) — `server/validators/combat_validator.py`
- **Check if target name is valid.** (1 connections) — `server/validators/combat_validator.py`
- **Check for suspicious patterns in target name.** (1 connections) — `server/validators/combat_validator.py`
- **Check if player is rate limited.** (1 connections) — `server/validators/combat_validator.py`
- **Get a random error message for the given error type.** (1 connections) — `server/validators/combat_validator.py`
- **Get a thematic combat status message.** (1 connections) — `server/validators/combat_validator.py`

## Relationships

- [NPC Combat](NPC_Combat.md) (12 shared connections)

## Source Files

- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 62 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*