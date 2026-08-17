# npc_combat_integration_service.py

> 88 nodes

## Key Concepts

- **npc_combat_integration_service.py** (53 connections) — `server/services/npc_combat_integration_service.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **combat_taunt.py** (32 connections) — `server/commands/combat_taunt.py`
- **TauntCommandHandler** (27 connections) — `server/commands/combat_taunt.py`
- **test_combat_taunt.py** (21 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **AppWithState** (15 connections) — `server/commands/combat_app_protocols.py`
- **run_handle_taunt_command()** (14 connections) — `server/commands/combat_taunt.py`
- **_validate_taunt_context()** (12 connections) — `server/commands/combat_taunt.py`
- **is_npc_attack_on_player_blocked_by_login_grace_period()** (10 connections) — `server/services/npc_combat_grace.py`
- **is_player_attack_blocked_by_login_grace_period()** (10 connections) — `server/services/npc_combat_grace.py`
- **_apply_taunt_and_maybe_broadcast()** (9 connections) — `server/commands/combat_taunt.py`
- **_resolve_taunt_combat_and_participant()** (9 connections) — `server/commands/combat_taunt.py`
- **test_npc_combat_grace.py** (9 connections) — `server/tests/unit/services/test_npc_combat_grace.py`
- **_validate_taunt_target()** (8 connections) — `server/commands/combat_taunt.py`
- **_connection_manager_from_config_app()** (8 connections) — `server/services/npc_combat_grace.py`
- **test_run_handle_taunt_success()** (8 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **_resolve_taunt_room_and_player()** (6 connections) — `server/commands/combat_taunt.py`
- **test_run_handle_taunt_no_combat_service()** (6 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_run_handle_taunt_not_in_combat()** (6 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **combat_app_protocols.py** (6 connections) — `server/commands/combat_app_protocols.py`
- **_validate_taunt_target_name()** (5 connections) — `server/commands/combat_taunt.py`
- **test_validate_taunt_target_dead()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_validate_taunt_target_not_npc()** (5 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **UUID** (5 connections)
- **_RoomWithIdOnly** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- *... and 63 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (22 shared connections)
- [CombatService](CombatService.md) (17 shared connections)
- [TargetMatch](TargetMatch.md) (12 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (11 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (9 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (6 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (6 shared connections)
- [CombatInstance](CombatInstance.md) (6 shared connections)
- [CombatParticipant](CombatParticipant.md) (6 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (5 shared connections)
- [test_combat_handler.py](test_combat_handler.py.md) (4 shared connections)
- [NPCCombatUUIDMapping](NPCCombatUUIDMapping.md) (4 shared connections)

## Source Files

- `server/commands/combat_app_protocols.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_taunt.py`
- `server/services/npc_combat_grace.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/commands/test_combat_taunt.py`
- `server/tests/unit/services/test_npc_combat_grace.py`

## Audit Trail

- EXTRACTED: 270 (90%)
- INFERRED: 30 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*