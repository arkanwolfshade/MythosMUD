# Community 381

> 46 nodes

## Key Concepts

- **CombatValidator** (26 connections) — `server/validators/combat_validator.py`
- **.__init__()** (11 connections) — `server/commands/combat_handler.py`
- **._get_random_error_message()** (8 connections) — `server/validators/combat_validator.py`
- **.validate_combat_command()** (7 connections) — `server/validators/combat_validator.py`
- **combat_validator()** (4 connections) — `server/tests/unit/validators/test_combat_validator.py`
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
- **EventBus** (1 connections)
- **fixture** (1 connections)
- *... and 21 more nodes in this community*

## Relationships

- [Community 153](Community_153.md) (5 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (2 shared connections)
- [Community 263](Community_263.md) (2 shared connections)
- [Community 126](Community_126.md) (1 shared connections)
- [NPC Combat Integration](NPC_Combat_Integration.md) (1 shared connections)
- [API Response Models](API_Response_Models.md) (1 shared connections)
- [Community 415](Community_415.md) (1 shared connections)
- [Community 106](Community_106.md) (1 shared connections)
- [Spell Effects & Combat Wiring](Spell_Effects_&_Combat_Wiring.md) (1 shared connections)
- [Community 82](Community_82.md) (1 shared connections)
- [Community 226](Community_226.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/tests/unit/validators/test_combat_validator.py`
- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 71 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*