# server commands combat handler combatcommandhandler

> 37 nodes

## Key Concepts

- **CombatValidator** (26 connections) — `server/validators/combat_validator.py`
- **.__init__()** (11 connections) — `server/commands/combat_handler.py`
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

- [server tests unit validators test](server_tests_unit_validators_test.md) (5 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server commands combat app protocols](server_commands_combat_app_protocols.md) (2 shared connections)
- [server game mechanics](server_game_mechanics.md) (1 shared connections)
- [server schemas shared target metadata](server_schemas_shared_target_metadata.md) (1 shared connections)
- [server api players](server_api_players.md) (1 shared connections)
- [server commands combat](server_commands_combat.md) (1 shared connections)
- [server async persistence asyncpersistencelayer](server_async_persistence_asyncpersistencelayer.md) (1 shared connections)
- [moduletype](moduletype.md) (1 shared connections)
- [server events combat events](server_events_combat_events.md) (1 shared connections)
- [server game magic spell targeting](server_game_magic_spell_targeting.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 63 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*