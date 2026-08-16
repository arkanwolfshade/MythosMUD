# combat_taunt.py

> 60 nodes

## Key Concepts

- **combat_taunt.py** (32 connections) — `server/commands/combat_taunt.py`
- **TauntCommandHandler** (27 connections) — `server/commands/combat_taunt.py`
- **test_combat_taunt.py** (21 connections) — `server/tests/unit/commands/test_combat_taunt.py`
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
- **.resolve_combat_target()** (3 connections) — `server/commands/combat_taunt.py`
- *... and 35 more nodes in this community*

## Relationships

- [CombatInstance](CombatInstance.md) (17 shared connections)
- [TargetMatch](TargetMatch.md) (11 shared connections)
- [CombatParticipant](CombatParticipant.md) (7 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (6 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (5 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (5 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (1 shared connections)
- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (1 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/models/combat.py`
- `server/tests/unit/commands/test_combat_taunt.py`

## Audit Trail

- EXTRACTED: 133 (85%)
- INFERRED: 23 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*