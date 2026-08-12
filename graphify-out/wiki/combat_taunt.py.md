# combat_taunt.py

> 94 nodes

## Key Concepts

- **combat_taunt.py** (32 connections) — `server/commands/combat_taunt.py`
- **combat_service_npc.py** (30 connections) — `server/services/combat_service_npc.py`
- **TauntCommandHandler** (29 connections) — `server/commands/combat_taunt.py`
- **test_combat_taunt.py** (20 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **run_handle_taunt_command()** (12 connections) — `server/commands/combat_taunt.py`
- **_validate_taunt_context()** (11 connections) — `server/commands/combat_taunt.py`
- **_get_uuid_mapping()** (10 connections) — `server/services/combat_service_npc.py`
- **UUID** (10 connections)
- **_apply_taunt_and_maybe_broadcast()** (9 connections) — `server/commands/combat_taunt.py`
- **_resolve_taunt_combat_and_participant()** (9 connections) — `server/commands/combat_taunt.py`
- **find_participant_uuid_by_string_id()** (9 connections) — `server/services/combat_service_npc.py`
- **resolve_npc_participant_id_in_combat()** (9 connections) — `server/services/combat_service_npc.py`
- **DataProviderProtocol** (8 connections) — `server/services/combat_service_npc.py`
- **UUIDMappingProtocol** (8 connections) — `server/services/combat_service_npc.py`
- **_validate_taunt_target()** (8 connections) — `server/commands/combat_taunt.py`
- **_fallback_find_combat_id_for_npc()** (8 connections) — `server/services/combat_service_npc.py`
- **get_npc_participant_current_room()** (8 connections) — `server/services/combat_service_npc.py`
- **test_run_handle_taunt_success()** (8 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **get_combat_id_for_npc_via_mapping()** (7 connections) — `server/services/combat_service_npc.py`
- **get_participant_current_room()** (7 connections) — `server/services/combat_service_npc.py`
- **_RoomWithIdOnly** (6 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **_resolve_taunt_room_and_player()** (6 connections) — `server/commands/combat_taunt.py`
- **_get_data_provider()** (6 connections) — `server/services/combat_service_npc.py`
- **_iter_active_combats()** (6 connections) — `server/services/combat_service_npc.py`
- **test_run_handle_taunt_no_combat_service()** (6 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- *... and 69 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (36 shared connections)
- [TargetMatch](TargetMatch.md) (17 shared connections)
- [CombatInstance](CombatInstance.md) (10 shared connections)
- [CombatParticipant](CombatParticipant.md) (10 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (8 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (5 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [npc_combat_grace.py](npc_combat_grace.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/services/combat_service_npc.py`
- `server/tests/unit/commands/test_combat_taunt.py`

## Audit Trail

- EXTRACTED: 394 (95%)
- INFERRED: 20 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*