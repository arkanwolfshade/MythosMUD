# combat_taunt.py

> 58 nodes

## Key Concepts

- **combat_taunt.py** (32 connections) — `server/commands/combat_taunt.py`
- **TauntCommandHandler** (29 connections) — `server/commands/combat_taunt.py`
- **test_combat_taunt.py** (20 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **run_handle_taunt_command()** (12 connections) — `server/commands/combat_taunt.py`
- **_validate_taunt_context()** (11 connections) — `server/commands/combat_taunt.py`
- **_apply_taunt_and_maybe_broadcast()** (9 connections) — `server/commands/combat_taunt.py`
- **_resolve_taunt_combat_and_participant()** (9 connections) — `server/commands/combat_taunt.py`
- **_validate_taunt_target()** (8 connections) — `server/commands/combat_taunt.py`
- **test_run_handle_taunt_success()** (8 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **_RoomWithIdOnly** (6 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **_resolve_taunt_room_and_player()** (6 connections) — `server/commands/combat_taunt.py`
- **test_run_handle_taunt_no_combat_service()** (6 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_run_handle_taunt_not_in_combat()** (6 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **_validate_taunt_target_name()** (5 connections) — `server/commands/combat_taunt.py`
- **test_validate_taunt_target_dead()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_validate_taunt_target_not_npc()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **UUID** (5 connections)
- **mock_handler()** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_resolve_taunt_room_and_player_falls_back_to_id()** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_validate_taunt_target_name_from_target_key()** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **.check_and_interrupt_rest()** (3 connections) — `server/commands/combat_taunt.py`
- **.combat_service()** (3 connections) — `server/commands/combat_taunt.py`
- **.get_player_and_room()** (3 connections) — `server/commands/combat_taunt.py`
- **.resolve_combat_target()** (3 connections) — `server/commands/combat_taunt.py`
- **test_resolve_taunt_room_and_player_uses_room_id_attr()** (3 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- *... and 33 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (23 shared connections)
- [TargetMatch](TargetMatch.md) (14 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (8 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (4 shared connections)
- [AliasStorage](AliasStorage.md) (4 shared connections)
- [update_aggro](update_aggro.md) (4 shared connections)
- [aggro_threat.py](aggro_threat.py.md) (1 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/tests/unit/commands/test_combat_taunt.py`

## Audit Trail

- EXTRACTED: 145 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*