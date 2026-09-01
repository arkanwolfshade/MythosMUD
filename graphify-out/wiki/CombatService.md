# CombatService

> 233 nodes

## Key Concepts

- **CombatService** (173 connections) — `server/services/combat_service.py`
- **combat_service.py** (104 connections) — `server/services/combat_service.py`
- **combat_service_npc.py** (31 connections) — `server/services/combat_service_npc.py`
- **test_combat_service_npc_helpers.py** (31 connections) — `server/tests/unit/services/test_combat_service_npc_helpers.py`
- **combat_service_start.py** (29 connections) — `server/services/combat_service_start.py`
- **combat_service_attack.py** (28 connections) — `server/services/combat_service_attack.py`
- **CombatResult** (22 connections) — `server/models/combat.py`
- **UUID** (20 connections)
- **get_combat_id_for_npc()** (17 connections) — `server/services/combat_service_npc.py`
- **CombatStartedEvent** (16 connections) — `server/events/combat_events.py`
- **.__init__()** (14 connections) — `server/services/combat_service.py`
- **CombatCleanupHandler** (12 connections) — `server/services/combat_cleanup_handler.py`
- **finalize_attack_result()** (11 connections) — `server/services/combat_service_attack.py`
- **find_participant_uuid_by_string_id()** (11 connections) — `server/services/combat_service_npc.py`
- **resolve_npc_participant_id_in_combat()** (11 connections) — `server/services/combat_service_npc.py`
- **spell_effects_internal.py** (11 connections) — `server/game/magic/spell_effects_internal.py`
- **_get_uuid_mapping()** (10 connections) — `server/services/combat_service_npc.py`
- **apply_target_rest_and_grace_checks()** (10 connections) — `server/services/combat_service_start.py`
- **UUID** (10 connections)
- **apply_damage_and_check_involuntary_flee()** (9 connections) — `server/services/combat_service_attack.py`
- **validate_melee_location()** (9 connections) — `server/services/combat_service_attack.py`
- **validate_melee_or_end_combat()** (9 connections) — `server/services/combat_service_attack.py`
- **get_combat_id_for_npc_via_mapping()** (9 connections) — `server/services/combat_service_npc.py`
- **get_participant_current_room()** (9 connections) — `server/services/combat_service_npc.py`
- **sync_npc_participant_dp_after_spell_damage()** (9 connections) — `server/services/combat_service_npc.py`
- *... and 208 more nodes in this community*

## Relationships

- [CombatParticipant](CombatParticipant.md) (55 shared connections)
- [CombatInstance](CombatInstance.md) (41 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (40 shared connections)
- [TargetMatch](TargetMatch.md) (31 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (27 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (14 shared connections)
- [CombatParticipantData](CombatParticipantData.md) (14 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (13 shared connections)
- [event_types.py](event_types.py.md) (9 shared connections)
- [magic_service.py](magic_service.py.md) (8 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [test_combat_service.py](test_combat_service.py.md) (6 shared connections)

## Source Files

- `server/container/bundles/combat.py`
- `server/events/combat_events.py`
- `server/game/magic/spell_effects_internal.py`
- `server/models/combat.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_npc.py`
- `server/services/combat_service_start.py`
- `server/services/combat_service_state.py`
- `server/services/combat_service_types.py`
- `server/tests/unit/game/magic/test_spell_effects_internal.py`
- `server/tests/unit/services/test_combat_service_npc_helpers.py`
- `server/tests/unit/services/test_combat_service_npc_in_combat.py`

## Audit Trail

- EXTRACTED: 652 (86%)
- INFERRED: 102 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*