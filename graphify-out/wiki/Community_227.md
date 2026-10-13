# Community 227

> 68 nodes

## Key Concepts

- **TauntCommandHandler** (26 connections) — `server/commands/combat_taunt.py`
- **combat_taunt.py** (26 connections) — `server/commands/combat_taunt.py`
- **test_combat_taunt.py** (25 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **target_resolution.py** (14 connections) — `server/schemas/shared/target_resolution.py`
- **run_handle_taunt_command()** (12 connections) — `server/commands/combat_taunt.py`
- **_validate_taunt_context()** (11 connections) — `server/commands/combat_taunt.py`
- **_queue_taunt()** (10 connections) — `server/commands/combat_taunt.py`
- **_resolve_taunt_combat_and_participant()** (9 connections) — `server/commands/combat_taunt.py`
- **_validate_taunt_target()** (8 connections) — `server/commands/combat_taunt.py`
- **_resolve_taunt_room_and_player()** (7 connections) — `server/commands/combat_taunt.py`
- **_ghoul_fight()** (7 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_queue_taunt_replaces_whatever_was_already_queued_for_the_round()** (7 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_run_handle_taunt_success_queues_the_taunt_as_the_rounds_action()** (7 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **asyncio** (6 connections)
- **_validate_taunt_target_name()** (5 connections) — `server/commands/combat_taunt.py`
- **_handler_with()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_queue_taunt_reports_a_failed_queue()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_queue_taunt_without_a_combat_service()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_run_handle_taunt_no_combat_service()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_run_handle_taunt_not_in_combat()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **UUID** (5 connections)
- **_RoomWithIdOnly** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **mock_handler()** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_resolve_taunt_room_and_player_falls_back_to_id()** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_validate_taunt_target_dead()** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- *... and 43 more nodes in this community*

## Relationships

- [Combat Participants](Combat_Participants.md) (9 shared connections)
- [Combat Instance Turns](Combat_Instance_Turns.md) (7 shared connections)
- [Combat Attack Execution](Combat_Attack_Execution.md) (7 shared connections)
- [Spell Effects & Combat Wiring](Spell_Effects_&_Combat_Wiring.md) (6 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (5 shared connections)
- [Community 126](Community_126.md) (5 shared connections)
- [NPC Combat Integration](NPC_Combat_Integration.md) (3 shared connections)
- [Community 187](Community_187.md) (2 shared connections)
- [Community 207](Community_207.md) (1 shared connections)
- [Community 277](Community_277.md) (1 shared connections)
- [Community 45](Community_45.md) (1 shared connections)
- [Community 283](Community_283.md) (1 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/commands/test_combat_taunt.py`

## Audit Trail

- EXTRACTED: 158 (92%)
- INFERRED: 13 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*