# Community 413

> 43 nodes

## Key Concepts

- **CombatValidator** (26 connections) — `server/validators/combat_validator.py`
- **.__init__()** (11 connections) — `server/commands/combat_handler.py`
- **._get_random_error_message()** (8 connections) — `server/validators/combat_validator.py`
- **.validate_combat_command()** (7 connections) — `server/validators/combat_validator.py`
- **._is_rate_limited()** (4 connections) — `server/validators/combat_validator.py`
- **Any** (4 connections)
- **test_validate_can_attack_target_different_party_allows()** (3 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_can_attack_target_no_party_service_allows()** (3 connections) — `server/tests/unit/validators/test_combat_validator.py`
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
- **ConnectionManager** (1 connections)
- **When party_service is None, validate_can_attack_target allows attack.** (1 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **When both players are in same party, validate_can_attack_target blocks attack.** (1 connections) — `server/tests/unit/validators/test_combat_validator.py`
- *... and 18 more nodes in this community*

## Relationships

- [Community 129](Community_129.md) (5 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (2 shared connections)
- [Community 198](Community_198.md) (2 shared connections)
- [Community 82](Community_82.md) (1 shared connections)
- [Community 44](Community_44.md) (1 shared connections)
- [DI Containers & API Bootstrap](DI_Containers_&_API_Bootstrap.md) (1 shared connections)
- [Community 245](Community_245.md) (1 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (1 shared connections)
- [Event Bus](Event_Bus.md) (1 shared connections)
- [Combat Cleanup & Results](Combat_Cleanup_&_Results.md) (1 shared connections)
- [Community 65](Community_65.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/tests/unit/validators/test_combat_validator.py`
- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 69 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*