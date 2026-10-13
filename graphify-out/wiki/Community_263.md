# Community 263

> 61 nodes

## Key Concepts

- **CombatCommandHandler** (52 connections) — `server/commands/combat_handler.py`
- **._get_persistence_from_app()** (6 connections) — `server/commands/combat_handler.py`
- **.get_player_and_room()** (6 connections) — `server/commands/combat_handler.py`
- **.resolve_combat_target()** (6 connections) — `server/commands/combat_handler.py`
- **Any** (6 connections)
- **.handle_assist_command()** (5 connections) — `server/commands/combat_handler.py`
- **.handle_attack_command()** (5 connections) — `server/commands/combat_handler.py`
- **.handle_protect_command()** (5 connections) — `server/commands/combat_handler.py`
- **._validate_combat_target_match()** (5 connections) — `server/commands/combat_handler.py`
- **.combat_service()** (4 connections) — `server/commands/combat_handler.py`
- **.extract_combat_command_data()** (4 connections) — `server/commands/combat_handler.py`
- **.get_npc_instance()** (4 connections) — `server/commands/combat_handler.py`
- **.handle_flee_command()** (4 connections) — `server/commands/combat_handler.py`
- **test_the_combat_handler_exposes_the_party_service_it_was_given()** (4 connections) — `server/tests/unit/commands/test_assist_wiring.py`
- **test_combat_command_handler_extras_optional()** (4 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **.get_room_data()** (3 connections) — `server/commands/combat_handler.py`
- **.movement_service()** (3 connections) — `server/commands/combat_handler.py`
- **.party_service()** (3 connections) — `server/commands/combat_handler.py`
- **.player_position_service()** (3 connections) — `server/commands/combat_handler.py`
- **.room_forbids_combat()** (3 connections) — `server/commands/combat_handler.py`
- **.validate_combat_action()** (3 connections) — `server/commands/combat_handler.py`
- **.validate_target_name()** (3 connections) — `server/commands/combat_handler.py`
- **test_the_combat_handler_routes_assist_to_its_command_module()** (3 connections) — `server/tests/unit/commands/test_assist_wiring.py`
- **test_the_loader_delegates_assist_to_the_combat_handler()** (3 connections) — `server/tests/unit/commands/test_assist_wiring.py`
- **test_combat_command_handler_requires_async_persistence()** (3 connections) — `server/tests/unit/commands/test_combat_handler.py`
- *... and 36 more nodes in this community*

## Relationships

- [Community 415](Community_415.md) (11 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (9 shared connections)
- [Community 456](Community_456.md) (6 shared connections)
- [Assist Wiring Tests](Assist_Wiring_Tests.md) (5 shared connections)
- [Community 283](Community_283.md) (4 shared connections)
- [Community 46](Community_46.md) (4 shared connections)
- [Community 126](Community_126.md) (3 shared connections)
- [Community 76](Community_76.md) (2 shared connections)
- [Community 381](Community_381.md) (2 shared connections)
- [Spell Effects & Combat Wiring](Spell_Effects_&_Combat_Wiring.md) (2 shared connections)
- [Community 480](Community_480.md) (1 shared connections)
- [API Response Models](API_Response_Models.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/tests/unit/commands/test_assist_wiring.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/commands/test_protect_wiring.py`

## Audit Trail

- EXTRACTED: 103 (81%)
- INFERRED: 24 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*