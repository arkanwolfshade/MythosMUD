# CombatService

> 207 nodes

## Key Concepts

- **CombatService** (164 connections) — `server/services/combat_service.py`
- **combat_service.py** (100 connections) — `server/services/combat_service.py`
- **combat_service_start.py** (28 connections) — `server/services/combat_service_start.py`
- **combat_service_attack.py** (27 connections) — `server/services/combat_service_attack.py`
- **combat_death_handler.py** (22 connections) — `server/services/combat_death_handler.py`
- **CombatResult** (20 connections) — `server/models/combat.py`
- **CombatDeathHandler** (20 connections) — `server/services/combat_death_handler.py`
- **UUID** (20 connections)
- **npc_combat_integration_combat_mixin.py** (17 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **NPCDiedEvent** (16 connections) — `server/events/combat_events.py`
- **.connection_manager()** (16 connections) — `server/services/combat_messaging/base.py`
- **combat_service_events.py** (15 connections) — `server/services/combat_service_events.py`
- **.__init__()** (14 connections) — `server/services/combat_service.py`
- **CombatCleanupHandler** (12 connections) — `server/services/combat_cleanup_handler.py`
- **apply_target_rest_and_grace_checks()** (11 connections) — `server/services/combat_service_start.py`
- **spell_effects_internal.py** (11 connections) — `server/game/magic/spell_effects_internal.py`
- **combat_cleanup_handler.py** (11 connections) — `server/services/combat_cleanup_handler.py`
- **finalize_attack_result()** (10 connections) — `server/services/combat_service_attack.py`
- **._create_corpse_on_death()** (9 connections) — `server/services/combat_death_handler.py`
- **validate_melee_location()** (9 connections) — `server/services/combat_service_attack.py`
- **validate_melee_or_end_combat()** (9 connections) — `server/services/combat_service_attack.py`
- **publish_npc_damage_event()** (9 connections) — `server/services/combat_service_events.py`
- **check_attacker_grace_period()** (9 connections) — `server/services/combat_service_start.py`
- **publish_combat_started_event()** (9 connections) — `server/services/combat_service_start.py`
- **combat_room_id_for_npc_spell()** (8 connections) — `server/game/magic/spell_effects_internal.py`
- *... and 182 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (37 shared connections)
- [CombatInstance](CombatInstance.md) (37 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (31 shared connections)
- [CombatParticipant](CombatParticipant.md) (30 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (28 shared connections)
- [TargetMatch](TargetMatch.md) (26 shared connections)
- [combat_service_npc.py](combat_service_npc.py.md) (26 shared connections)
- [models/combat.py](models-combat.py.md) (23 shared connections)
- [CombatParticipantData](CombatParticipantData.md) (14 shared connections)
- [NATSError](NATSError.md) (10 shared connections)
- [_NPCCombatIntegrationDeps](_NPCCombatIntegrationDeps.md) (9 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (7 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/game/magic/spell_effects_internal.py`
- `server/models/combat.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_events.py`
- `server/services/combat_service_start.py`
- `server/services/combat_service_state.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/tests/unit/services/test_combat_service_modules.py`
- `server/tests/unit/services/test_combat_service_npc_in_combat.py`

## Audit Trail

- EXTRACTED: 600 (84%)
- INFERRED: 112 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*