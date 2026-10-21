# test_lifespan_event_subscriptions.py

> 37 nodes · cohesion 0.07

## Key Concepts

- **CombatValidator** (26 connections) — `server/validators/combat_validator.py`
- **.__init__()** (12 connections) — `server/commands/combat_handler.py`
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
- **ConnectionManager** (1 connections)
- **Enhanced combat command validator with thematic error messages. Provides…** (1 connections) — `server/validators/combat_validator.py`
- **Initialize the combat validator. Args: party_service: Optional PartyService for…** (1 connections) — `server/validators/combat_validator.py`
- **Validate that attacker is allowed to attack target (e.g. not same party). Hook…** (1 connections) — `server/validators/combat_validator.py`
- **Validate a combat command with thematic error messages. Args: command_data: The…** (1 connections) — `server/validators/combat_validator.py`
- **Validate that a target exists with thematic error messages. Args: target_name:…** (1 connections) — `server/validators/combat_validator.py`
- *... and 12 more nodes in this community*

## Relationships

- [test_help_docs.py](test_help_docs.py.md) (2 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)
- [test_user_manager.py](test_user_manager.py.md) (1 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (1 shared connections)
- [command_parser.py](command_parser.py.md) (1 shared connections)
- [test_party_service.py](test_party_service.py.md) (1 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (1 shared connections)
- [validate_secure_path](validate_secure_path.md) (1 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)
- [unit/realtime/maintenance/__init__.py](unit-realtime-maintenance-__init__.py.md) (1 shared connections)
- [unit/persistence/__init__.py](unit-persistence-__init__.py.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 63 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*