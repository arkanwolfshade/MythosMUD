# CombatService

> 186 nodes

## Key Concepts

- **CombatService** (165 connections) — `server/services/combat_service.py`
- **combat_service.py** (99 connections) — `server/services/combat_service.py`
- **combat_service_npc.py** (31 connections) — `server/services/combat_service_npc.py`
- **test_combat_service_npc_helpers.py** (31 connections) — `server/tests/unit/services/test_combat_service_npc_helpers.py`
- **combat_service_attack.py** (28 connections) — `server/services/combat_service_attack.py`
- **CombatResult** (20 connections) — `server/models/combat.py`
- **UUID** (20 connections)
- **npc_combat_integration_combat_mixin.py** (18 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **get_combat_id_for_npc()** (17 connections) — `server/services/combat_service_npc.py`
- **.__init__()** (14 connections) — `server/services/combat_service.py`
- **CombatCleanupHandler** (12 connections) — `server/services/combat_cleanup_handler.py`
- **find_participant_uuid_by_string_id()** (11 connections) — `server/services/combat_service_npc.py`
- **resolve_npc_participant_id_in_combat()** (11 connections) — `server/services/combat_service_npc.py`
- **spell_effects_internal.py** (11 connections) — `server/game/magic/spell_effects_internal.py`
- **combat_cleanup_handler.py** (11 connections) — `server/services/combat_cleanup_handler.py`
- **finalize_attack_result()** (10 connections) — `server/services/combat_service_attack.py`
- **_get_uuid_mapping()** (10 connections) — `server/services/combat_service_npc.py`
- **UUID** (10 connections)
- **validate_melee_location()** (9 connections) — `server/services/combat_service_attack.py`
- **validate_melee_or_end_combat()** (9 connections) — `server/services/combat_service_attack.py`
- **get_combat_id_for_npc_via_mapping()** (9 connections) — `server/services/combat_service_npc.py`
- **get_participant_current_room()** (9 connections) — `server/services/combat_service_npc.py`
- **sync_npc_participant_dp_after_spell_damage()** (9 connections) — `server/services/combat_service_npc.py`
- **test_combat_service_npc_in_combat.py** (9 connections) — `server/tests/unit/services/test_combat_service_npc_in_combat.py`
- **combat_room_id_for_npc_spell()** (8 connections) — `server/game/magic/spell_effects_internal.py`
- *... and 161 more nodes in this community*

## Relationships

- [CombatInstance](CombatInstance.md) (36 shared connections)
- [get_logger](get_logger.md) (35 shared connections)
- [TargetMatch](TargetMatch.md) (34 shared connections)
- [CombatParticipant](CombatParticipant.md) (31 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (29 shared connections)
- [models/combat.py](models-combat.py.md) (20 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (10 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (10 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (9 shared connections)
- [.connection_manager](connection_manager.md) (8 shared connections)
- [test_combat_service.py](test_combat_service.py.md) (6 shared connections)
- [PlayerService](PlayerService.md) (6 shared connections)

## Source Files

- `server/game/magic/spell_effects_internal.py`
- `server/models/combat.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_npc.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/tests/unit/services/test_combat_service_npc_helpers.py`
- `server/tests/unit/services/test_combat_service_npc_in_combat.py`

## Audit Trail

- EXTRACTED: 561 (87%)
- INFERRED: 84 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*