# CombatService

> 714 nodes

## Key Concepts

- **CombatService** (181 connections) — `server/services/combat_service.py`
- **combat_service.py** (100 connections) — `server/services/combat_service.py`
- **PlayerCombatService** (79 connections) — `server/services/player_combat_service.py`
- **models/combat.py** (56 connections) — `server/models/combat.py`
- **npc_combat_integration_service.py** (52 connections) — `server/services/npc_combat_integration_service.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **CombatParticipantType** (44 connections) — `server/models/combat.py`
- **NPCCombatDataProvider** (40 connections) — `server/services/npc_combat_data_provider.py`
- **TargetType** (39 connections) — `server/schemas/shared/target_resolution.py`
- **NPCCombatUUIDMapping** (39 connections) — `server/services/npc_combat_uuid_mapping.py`
- **CombatParticipantData** (37 connections) — `server/services/combat_types.py`
- **test_player_combat_service.py** (37 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **player_combat_service.py** (36 connections) — `server/services/player_combat_service.py`
- **combat_taunt.py** (32 connections) — `server/commands/combat_taunt.py`
- **combat_service_npc.py** (31 connections) — `server/services/combat_service_npc.py`
- **test_combat_service_npc_helpers.py** (30 connections) — `server/tests/unit/services/test_combat_service_npc_helpers.py`
- **TauntCommandHandler** (29 connections) — `server/commands/combat_taunt.py`
- **PlayerDeathService** (28 connections) — `server/services/player_death_service.py`
- **combat_service_start.py** (28 connections) — `server/services/combat_service_start.py`
- **combat_service_attack.py** (27 connections) — `server/services/combat_service_attack.py`
- **TestNPCCombatUUIDMapping** (22 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **combat_death_handler.py** (22 connections) — `server/services/combat_death_handler.py`
- **asyncio** (22 connections)
- **CombatResult** (20 connections) — `server/models/combat.py`
- **UUID** (20 connections)
- *... and 689 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (81 shared connections)
- [TargetMatch](TargetMatch.md) (71 shared connections)
- [CombatInstance](CombatInstance.md) (65 shared connections)
- [CombatParticipant](CombatParticipant.md) (45 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (40 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (29 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (27 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (25 shared connections)
- [event_types.py](event_types.py.md) (25 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (20 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (18 shared connections)
- [PlayerService](PlayerService.md) (17 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/commands/combat_taunt.py`
- `server/container/bundles/combat.py`
- `server/game/magic/spell_effects_internal.py`
- `server/game/magic/spell_targeting.py`
- `server/models/combat.py`
- `server/models/npc.py`
- `server/schemas/shared/__init__.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_initialization.py`
- `server/services/combat_messaging/__init__.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging_integration.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_end.py`
- `server/services/combat_service_events.py`

## Audit Trail

- EXTRACTED: 1914 (93%)
- INFERRED: 136 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*