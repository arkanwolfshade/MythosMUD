# LRU Cache Manager

> 249 nodes

## Key Concepts

- **NPCPopulationController** (64 connections) — `server/npc/population_control.py`
- **NPCCombatIntegration** (63 connections) — `server/npc/combat_integration.py`
- **test_npc_instance_service.py** (53 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **NPCSpawningService** (50 connections) — `server/npc/spawning_service.py`
- **NPCInstanceService** (24 connections) — `server/services/npc_instance_service.py`
- **test_npc_combat_integration_class.py** (23 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **npc.py** (14 connections) — `server/container/bundles/npc.py`
- **NPCBundle** (14 connections) — `server/container/bundles/npc.py`
- **initialize_npc_instance_service()** (14 connections) — `server/services/npc_instance_service.py`
- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **_create_npc_services_on_app()** (10 connections) — `server/app/lifespan_startup.py`
- **._create_npc_services()** (8 connections) — `server/container/bundles/npc.py`
- **._build_player_attacked_event()** (8 connections) — `server/npc/combat_integration.py`
- **Any** (8 connections)
- **UUID** (7 connections)
- **.get_combat_stats()** (7 connections) — `server/npc/combat_integration.py`
- **CombatEventPublisherProtocol** (7 connections) — `server/npc/combat_integration_protocols.py`
- **.__init__()** (7 connections) — `server/npc/population_control.py`
- **._check_spawn_requirements_for_room()** (7 connections) — `server/npc/population_control.py`
- **.__init__()** (7 connections) — `server/npc/spawning_service.py`
- **.initialize()** (6 connections) — `server/container/bundles/npc.py`
- **._compute_dp_update_fields()** (6 connections) — `server/npc/combat_integration.py`
- **._get_combat_event_publisher()** (6 connections) — `server/npc/combat_integration.py`
- **._calculate_max_dp()** (6 connections) — `server/npc/combat_integration.py`
- **.__init__()** (6 connections) — `server/services/npc_instance_service.py`
- *... and 224 more nodes in this community*

## Relationships

- [Level and XP Curve](Level_and_XP_Curve.md) (71 shared connections)
- [Spell Effect Protocols](Spell_Effect_Protocols.md) (24 shared connections)
- [Command Parser Tests](Command_Parser_Tests.md) (19 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (11 shared connections)
- [MP Regeneration Service](MP_Regeneration_Service.md) (9 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (9 shared connections)
- [Lucidity Recovery Commands](Lucidity_Recovery_Commands.md) (7 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (5 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (4 shared connections)
- [Plan Cursor Plans](Plan_Cursor_Plans.md) (4 shared connections)
- [Realtime Errors Error](Realtime_Errors_Error.md) (3 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (3 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/container/bundles/npc.py`
- `server/npc/combat_integration.py`
- `server/npc/combat_integration_protocols.py`
- `server/npc/npc_base.py`
- `server/npc/population_control.py`
- `server/npc/spawning_service.py`
- `server/services/npc_instance_service.py`
- `server/services/npc_service/__init__.py`
- `server/tests/unit/npc/test_npc_combat_integration_class.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 798 (92%)
- INFERRED: 73 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*