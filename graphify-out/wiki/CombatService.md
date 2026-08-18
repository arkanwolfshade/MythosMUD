# CombatService

> 238 nodes

## Key Concepts

- **CombatService** (165 connections) — `server/services/combat_service.py`
- **combat_service.py** (99 connections) — `server/services/combat_service.py`
- **NATSError** (70 connections) — `server/services/nats_exceptions.py`
- **combat_service_attack.py** (28 connections) — `server/services/combat_service_attack.py`
- **combat_death_handler.py** (22 connections) — `server/services/combat_death_handler.py`
- **CombatResult** (20 connections) — `server/models/combat.py`
- **CombatDeathHandler** (20 connections) — `server/services/combat_death_handler.py`
- **UUID** (20 connections)
- **test_combat_cleanup_handler.py** (19 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **npc_combat_integration_combat_mixin.py** (18 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **NPCDiedEvent** (16 connections) — `server/events/combat_events.py`
- **combat_service_events.py** (15 connections) — `server/services/combat_service_events.py`
- **_NPCCombatIntegrationDeps** (14 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.__init__()** (14 connections) — `server/services/combat_service.py`
- **CombatCleanupHandler** (12 connections) — `server/services/combat_cleanup_handler.py`
- **spell_effects_internal.py** (11 connections) — `server/game/magic/spell_effects_internal.py`
- **combat_cleanup_handler.py** (11 connections) — `server/services/combat_cleanup_handler.py`
- **finalize_attack_result()** (10 connections) — `server/services/combat_service_attack.py`
- **NPCCombatIntegrationCombatMixin** (9 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._create_corpse_on_death()** (9 connections) — `server/services/combat_death_handler.py`
- **validate_melee_location()** (9 connections) — `server/services/combat_service_attack.py`
- **validate_melee_or_end_combat()** (9 connections) — `server/services/combat_service_attack.py`
- **publish_npc_damage_event()** (9 connections) — `server/services/combat_service_events.py`
- **test_combat_service_npc_in_combat.py** (9 connections) — `server/tests/unit/services/test_combat_service_npc_in_combat.py`
- **combat_room_id_for_npc_spell()** (8 connections) — `server/game/magic/spell_effects_internal.py`
- *... and 213 more nodes in this community*

## Relationships

- [CombatParticipant](CombatParticipant.md) (55 shared connections)
- [get_logger](get_logger.md) (43 shared connections)
- [CombatInstance](CombatInstance.md) (35 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (29 shared connections)
- [TargetMatch](TargetMatch.md) (28 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (27 shared connections)
- [combat_service_npc.py](combat_service_npc.py.md) (26 shared connections)
- [CombatParticipantData](CombatParticipantData.md) (21 shared connections)
- [NATSSubscribeError](NATSSubscribeError.md) (10 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (9 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (7 shared connections)
- [test_combat_service.py](test_combat_service.py.md) (6 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/game/magic/spell_effects_internal.py`
- `server/models/combat.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_events.py`
- `server/services/nats_exceptions.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/tests/unit/game/magic/test_spell_effects_internal.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`
- `server/tests/unit/services/test_combat_service_modules.py`
- `server/tests/unit/services/test_combat_service_npc_in_combat.py`
- `server/tests/unit/services/test_nats_exceptions.py`

## Audit Trail

- EXTRACTED: 656 (84%)
- INFERRED: 124 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*