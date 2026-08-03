# combat validator validators

> 35 nodes

## Key Concepts

- **CombatValidator** (28 connections) — `server/validators/combat_validator.py`
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
- **.get_combat_help_message()** (2 connections) — `server/validators/combat_validator.py`
- **.get_combat_result_message()** (2 connections) — `server/validators/combat_validator.py`
- **.get_combat_death_message()** (2 connections) — `server/validators/combat_validator.py`
- **.get_combat_victory_message()** (2 connections) — `server/validators/combat_validator.py`
- **Enhanced combat command validator with thematic error messages.      Provides co** (1 connections) — `server/validators/combat_validator.py`
- **Initialize the combat validator.          Args:             party_service: Optio** (1 connections) — `server/validators/combat_validator.py`
- **Validate that attacker is allowed to attack target (e.g. not same party).** (1 connections) — `server/validators/combat_validator.py`
- **Validate a combat command with thematic error messages.          Args:** (1 connections) — `server/validators/combat_validator.py`
- **Validate that a target exists with thematic error messages.          Args:** (1 connections) — `server/validators/combat_validator.py`
- **Validate that a target is alive with thematic error messages.          Args:** (1 connections) — `server/validators/combat_validator.py`
- **Validate combat state with thematic error messages.          Args:             i** (1 connections) — `server/validators/combat_validator.py`
- *... and 10 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (3 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [combat commands handler](combat_commands_handler.md) (1 shared connections)
- [emote models rationale](emote_models_rationale.md) (1 shared connections)
- [combat services npc](combat_services_npc.md) (1 shared connections)
- [player death services](player_death_services.md) (1 shared connections)
- [player services death](player_services_death.md) (1 shared connections)
- [player death service](player_death_service.md) (1 shared connections)

## Source Files

- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 100 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*