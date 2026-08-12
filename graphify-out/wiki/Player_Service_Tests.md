# Player Service Tests

> 98 nodes

## Key Concepts

- **test_combat_validator.py** (50 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **combat_validator.py** (6 connections) — `server/validators/combat_validator.py`
- **combat_validator()** (3 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_can_attack_target_no_party_service_allows()** (3 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_can_attack_target_same_party_blocks()** (3 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_can_attack_target_different_party_allows()** (3 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_combat_validator_init()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_combat_command_valid()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_combat_command_invalid_command_type()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_combat_command_no_target()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_combat_command_invalid_target_name()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_combat_command_suspicious_patterns()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_combat_command_target_too_long()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_combat_command_rate_limited()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_combat_command_exception_handling()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_target_exists_exact_match()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_target_exists_case_insensitive()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_target_exists_partial_match()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_target_exists_no_match()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_target_exists_no_target_name()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_target_alive_alive()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_target_alive_dead()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_combat_state_in_combat_required()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_combat_state_not_in_combat_required()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_combat_state_in_combat_not_required()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- *... and 73 more nodes in this community*

## Relationships

- [Magic Service Bundle](Magic_Service_Bundle.md) (6 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)

## Source Files

- `server/tests/unit/validators/test_combat_validator.py`
- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 203 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*