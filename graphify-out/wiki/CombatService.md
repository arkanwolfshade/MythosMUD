# CombatService

> 255 nodes

## Key Concepts

- **CombatService** (173 connections) — `server/services/combat_service.py`
- **combat_service.py** (104 connections) — `server/services/combat_service.py`
- **models/combat.py** (61 connections) — `server/models/combat.py`
- **CombatParticipantType** (46 connections) — `server/models/combat.py`
- **CombatParticipantData** (39 connections) — `server/services/combat_types.py`
- **combat_taunt.py** (34 connections) — `server/commands/combat_taunt.py`
- **combat_service_npc.py** (31 connections) — `server/services/combat_service_npc.py`
- **test_combat_service_npc_helpers.py** (30 connections) — `server/tests/unit/services/test_combat_service_npc_helpers.py`
- **combat_service_start.py** (29 connections) — `server/services/combat_service_start.py`
- **test_combat_taunt.py** (21 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **UUID** (20 connections)
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **test_combat_cleanup_handler.py** (18 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **get_combat_id_for_npc()** (17 connections) — `server/services/combat_service_npc.py`
- **combat_initialization.py** (15 connections) — `server/services/combat_initialization.py`
- **CombatStatus** (13 connections) — `server/models/combat.py`
- **CombatCleanupHandler** (12 connections) — `server/services/combat_cleanup_handler.py`
- **TestCombatParticipantData** (12 connections) — `server/tests/unit/services/test_combat_types.py`
- **target_resolution.py** (12 connections) — `server/schemas/shared/target_resolution.py`
- **test_combat_turn_participant_actions.py** (12 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **find_participant_uuid_by_string_id()** (11 connections) — `server/services/combat_service_npc.py`
- **resolve_npc_participant_id_in_combat()** (11 connections) — `server/services/combat_service_npc.py`
- **spell_effects_internal.py** (11 connections) — `server/game/magic/spell_effects_internal.py`
- **combat_cleanup_handler.py** (11 connections) — `server/services/combat_cleanup_handler.py`
- **combat_types.py** (11 connections) — `server/services/combat_types.py`
- *... and 230 more nodes in this community*

## Relationships

- [test_combat_service_modules.py](test_combat_service_modules.py.md) (45 shared connections)
- [CombatInstance](CombatInstance.md) (44 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (42 shared connections)
- [CombatParticipant](CombatParticipant.md) (37 shared connections)
- [TargetMatch](TargetMatch.md) (35 shared connections)
- [TauntCommandHandler](TauntCommandHandler.md) (24 shared connections)
- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (22 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (21 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (16 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (16 shared connections)
- [.create_combat_instance](create_combat_instance.md) (14 shared connections)
- [get_logger](get_logger.md) (13 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/container/bundles/combat.py`
- `server/game/magic/spell_effects_internal.py`
- `server/models/combat.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_initialization.py`
- `server/services/combat_service.py`
- `server/services/combat_service_npc.py`
- `server/services/combat_service_start.py`
- `server/services/combat_service_state.py`
- `server/services/combat_service_types.py`
- `server/services/combat_turn_processor.py`
- `server/services/combat_types.py`
- `server/tests/unit/commands/test_combat_taunt.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`
- `server/tests/unit/services/test_combat_initialization.py`
- `server/tests/unit/services/test_combat_service_npc_helpers.py`
- `server/tests/unit/services/test_combat_service_npc_in_combat.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`

## Audit Trail

- EXTRACTED: 804 (89%)
- INFERRED: 103 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*