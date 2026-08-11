# Communication Command Flows

> 1195 nodes

## Key Concepts

- **EventBus** (129 connections) — `server/events/event_bus.py`
- **NPCDefinition** (126 connections) — `server/models/npc.py`
- **time.py** (89 connections) — `server/container/bundles/time.py`
- **NPCBase** (82 connections) — `server/npc/npc_base.py`
- **get_npc_instance_service()** (79 connections) — `server/services/npc_instance_service.py`
- **NPCLifecycleManager** (76 connections) — `server/npc/lifecycle_manager.py`
- **BaseEvent** (75 connections) — `server/events/event_types.py`
- **event_types.py** (74 connections) — `server/events/event_types.py`
- **PlayerEnteredRoom** (68 connections) — `server/events/event_types.py`
- **test_population_control.py** (65 connections) — `server/tests/unit/npc/test_population_control.py`
- **NPCPopulationController** (64 connections) — `server/npc/population_control.py`
- **NPCCombatIntegration** (63 connections) — `server/npc/combat_integration.py`
- **test_npc_instance_service.py** (53 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **PlayerLeftRoom** (51 connections) — `server/events/event_types.py`
- **NPCEnteredRoom** (51 connections) — `server/events/event_types.py`
- **NPCSpawningService** (50 connections) — `server/npc/spawning_service.py`
- **lifecycle_manager.py** (48 connections) — `server/npc/lifecycle_manager.py`
- **threading.py** (47 connections) — `server/npc/threading.py`
- **NPCLeftRoom** (46 connections) — `server/events/event_types.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **PopulationStats** (42 connections) — `server/npc/population_stats.py`
- **npc_base.py** (41 connections) — `server/npc/npc_base.py`
- **test_event_handler.py** (41 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **PlayerDPUpdated** (39 connections) — `server/events/event_types.py`
- **npc.py** (37 connections) — `server/models/npc.py`
- *... and 1170 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (194 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (68 shared connections)
- [Command Parser Tests](Command_Parser_Tests.md) (37 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (31 shared connections)
- [Character Stats Generator](Character_Stats_Generator.md) (28 shared connections)
- [Look Command Helpers](Look_Command_Helpers.md) (25 shared connections)
- [Dual Connection API Reference](Dual_Connection_API_Reference.md) (21 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (20 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (17 shared connections)
- [FastAPI App Factory](FastAPI_App_Factory.md) (17 shared connections)
- [Whisper Remediation Plan](Whisper_Remediation_Plan.md) (17 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (16 shared connections)

## Source Files

- `scripts/run_test_ci.py`
- `server/app/lifespan_startup.py`
- `server/commands/shutdown_process_termination.py`
- `server/container/bundles/npc.py`
- `server/container/bundles/time.py`
- `server/events/__init__.py`
- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_types.py`
- `server/game/follow_service.py`
- `server/models/npc.py`
- `server/models/room.py`
- `server/npc/__init__.py`
- `server/npc/aggressive_mob_npc.py`
- `server/npc/behavior_engine.py`
- `server/npc/behaviors.py`
- `server/npc/combat_integration.py`
- `server/npc/combat_integration_protocols.py`
- `server/npc/communication_integration.py`
- `server/npc/event_reaction_system.py`

## Audit Trail

- EXTRACTED: 4800 (91%)
- INFERRED: 466 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*