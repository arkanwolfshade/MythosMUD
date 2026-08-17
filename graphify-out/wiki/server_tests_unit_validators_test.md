# server tests unit validators test

> 40 nodes

## Key Concepts

- **CombatValidator** (26 connections) — `server/validators/combat_validator.py`
- **._get_random_error_message()** (8 connections) — `server/validators/combat_validator.py`
- **.validate_combat_command()** (7 connections) — `server/validators/combat_validator.py`
- **combat_validator()** (4 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **._is_rate_limited()** (4 connections) — `server/validators/combat_validator.py`
- **Any** (4 connections)
- **test_validate_can_attack_target_same_party_blocks()** (3 connections) — `server/tests/unit/validators/test_combat_validator.py`
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
- **When both players are in same party, validate_can_attack_target blocks attack.** (1 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **Enhanced combat command validator with thematic error messages. Provides…** (1 connections) — `server/validators/combat_validator.py`
- **Initialize the combat validator. Args: party_service: Optional PartyService for…** (1 connections) — `server/validators/combat_validator.py`
- *... and 15 more nodes in this community*

## Relationships

- [server tests unit validators test](server_tests_unit_validators_test.md) (5 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)

## Source Files

- `server/tests/unit/validators/test_combat_validator.py`
- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 55 (92%)
- INFERRED: 5 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*