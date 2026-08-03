# emote models rationale

> 12 nodes

## Key Concepts

- **test_combat_validator.py** (50 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_combat_command_valid()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_validate_attack_strength_success()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_get_random_error_message()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_get_random_error_message_unknown_type()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **test_get_combat_result_message_failure()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **Unit tests for combat validator.  Tests the CombatValidator class for combat com** (1 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **Test validate_combat_command with valid command.** (1 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **Test validate_attack_strength with successful validation.** (1 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **Test _get_random_error_message returns error message.** (1 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **Test _get_random_error_message with unknown error type.** (1 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **Test get_combat_result_message with failed attack.** (1 connections) — `server/tests/unit/validators/test_combat_validator.py`

## Relationships

- [services player death](services_player_death.md) (14 shared connections)
- [death services player](death_services_player.md) (7 shared connections)
- [player services death](player_services_death.md) (6 shared connections)
- [player death services](player_death_services.md) (5 shared connections)
- [combat services npc](combat_services_npc.md) (2 shared connections)
- [player death service](player_death_service.md) (2 shared connections)
- [npc services combat](npc_services_combat.md) (2 shared connections)
- [player service services](player_service_services.md) (1 shared connections)
- [position services player](position_services_player.md) (1 shared connections)
- [player position services](player_position_services.md) (1 shared connections)
- [services player position](services_player_position.md) (1 shared connections)
- [NATS Messaging](NATS_Messaging.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_combat_validator.py`

## Audit Trail

- EXTRACTED: 66 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*