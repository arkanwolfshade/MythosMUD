# combat_taunt.py

> 58 nodes

## Key Concepts

- **combat_taunt.py** (32 connections) — `server/commands/combat_taunt.py`
- **TauntCommandHandler** (27 connections) — `server/commands/combat_taunt.py`
- **test_combat_taunt.py** (20 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **run_handle_taunt_command()** (13 connections) — `server/commands/combat_taunt.py`
- **_validate_taunt_context()** (12 connections) — `server/commands/combat_taunt.py`
- **_apply_taunt_and_maybe_broadcast()** (9 connections) — `server/commands/combat_taunt.py`
- **_resolve_taunt_combat_and_participant()** (9 connections) — `server/commands/combat_taunt.py`
- **_validate_taunt_target()** (8 connections) — `server/commands/combat_taunt.py`
- **test_run_handle_taunt_success()** (8 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **_resolve_taunt_room_and_player()** (6 connections) — `server/commands/combat_taunt.py`
- **test_run_handle_taunt_no_combat_service()** (6 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_run_handle_taunt_not_in_combat()** (6 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **_validate_taunt_target_name()** (5 connections) — `server/commands/combat_taunt.py`
- **test_validate_taunt_target_dead()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_validate_taunt_target_not_npc()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **UUID** (5 connections)
- **_RoomWithIdOnly** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **.is_alive()** (4 connections) — `server/models/combat.py`
- **mock_handler()** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_resolve_taunt_room_and_player_falls_back_to_id()** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_validate_taunt_target_name_from_target_key()** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **.check_and_interrupt_rest()** (3 connections) — `server/commands/combat_taunt.py`
- **.combat_service()** (3 connections) — `server/commands/combat_taunt.py`
- **.get_player_and_room()** (3 connections) — `server/commands/combat_taunt.py`
- **test_resolve_taunt_room_and_player_uses_room_id_attr()** (3 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- *... and 33 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (11 shared connections)
- [models/combat.py](models-combat.py.md) (9 shared connections)
- [CombatParticipant](CombatParticipant.md) (7 shared connections)
- [CombatInstance](CombatInstance.md) (6 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (5 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (4 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)
- [combat_service_npc.py](combat_service_npc.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (1 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/models/combat.py`
- `server/tests/unit/commands/test_combat_taunt.py`

## Audit Trail

- EXTRACTED: 130 (85%)
- INFERRED: 23 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*