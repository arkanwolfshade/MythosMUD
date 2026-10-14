# combat_taunt.py

> 65 nodes

## Key Concepts

- **combat_taunt.py** (29 connections) — `server/commands/combat_taunt.py`
- **TauntCommandHandler** (28 connections) — `server/commands/combat_taunt.py`
- **test_combat_taunt.py** (27 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **run_handle_taunt_command()** (13 connections) — `server/commands/combat_taunt.py`
- **_validate_taunt_context()** (12 connections) — `server/commands/combat_taunt.py`
- **_queue_taunt()** (10 connections) — `server/commands/combat_taunt.py`
- **_resolve_taunt_combat_and_participant()** (9 connections) — `server/commands/combat_taunt.py`
- **_validate_taunt_target()** (8 connections) — `server/commands/combat_taunt.py`
- **test_run_handle_taunt_success_queues_the_taunt_as_the_rounds_action()** (8 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **_ghoul_fight()** (7 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_queue_taunt_replaces_whatever_was_already_queued_for_the_round()** (7 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **_resolve_taunt_room_and_player()** (6 connections) — `server/commands/combat_taunt.py`
- **test_run_handle_taunt_no_combat_service()** (6 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_run_handle_taunt_not_in_combat()** (6 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **asyncio** (6 connections)
- **_validate_taunt_target_name()** (5 connections) — `server/commands/combat_taunt.py`
- **_handler_with()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_queue_taunt_reports_a_failed_queue()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_queue_taunt_without_a_combat_service()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_validate_taunt_target_dead()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_validate_taunt_target_not_npc()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **UUID** (5 connections)
- **_RoomWithIdOnly** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **mock_handler()** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_resolve_taunt_room_and_player_falls_back_to_id()** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- *... and 40 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (12 shared connections)
- [TargetMatch](TargetMatch.md) (11 shared connections)
- [CombatParticipant](CombatParticipant.md) (9 shared connections)
- [CombatInstance](CombatInstance.md) (7 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (5 shared connections)
- [TargetType](TargetType.md) (4 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (2 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/tests/unit/commands/test_combat_taunt.py`

## Audit Trail

- EXTRACTED: 151 (88%)
- INFERRED: 21 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*