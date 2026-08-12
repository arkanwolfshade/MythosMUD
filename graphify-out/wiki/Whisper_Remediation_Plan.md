# Whisper Remediation Plan

> 134 nodes

## Key Concepts

- **NPCDefinition** (126 connections) — `server/models/npc.py`
- **NPCDefinitionCRUDMixin** (18 connections) — `server/services/npc_service/definition_crud.py`
- **._spawn_npc_impl()** (14 connections) — `server/npc/lifecycle_manager.py`
- **_JSONDict** (10 connections)
- **._evaluate_spawn_requirements()** (9 connections) — `server/npc/spawning_service.py`
- **.update_npc_definition()** (9 connections) — `server/services/npc_service/definition_crud.py`
- **AsyncSession** (8 connections)
- **.create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_npc_update()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **_loads_json_dict()** (7 connections) — `server/models/npc.py`
- **._spawn_npc()** (7 connections) — `server/npc/population_control.py`
- **._evaluate_spawn_rules()** (7 connections) — `server/npc/spawning_service.py`
- **.get_npc_definitions()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **.get_npc_definition()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **._build_npc_update_data()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **.get_base_stats()** (6 connections) — `server/models/npc.py`
- **._notify_room_and_threads()** (6 connections) — `server/npc/lifecycle_manager.py`
- **._register_spawned_npc_in_population_stats()** (6 connections) — `server/npc/population_control.py`
- **._maybe_add_required_npc_request()** (6 connections) — `server/npc/spawning_service.py`
- **._calculate_spawn_priority()** (6 connections) — `server/npc/spawning_service.py`
- **.get_spawn_conditions()** (5 connections) — `server/models/npc.py`
- **._queue_npc_thread_start()** (5 connections) — `server/npc/lifecycle_manager.py`
- **._handle_spawn_service_failure()** (5 connections) — `server/npc/lifecycle_manager.py`
- **._check_spawn_requirements_for_room()** (5 connections) — `server/npc/spawning_service.py`
- *... and 109 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (46 shared connections)
- [Command Parser Tests](Command_Parser_Tests.md) (26 shared connections)
- [FastAPI App Factory](FastAPI_App_Factory.md) (14 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (13 shared connections)
- [Commands Look Item](Commands_Look_Item.md) (11 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (9 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [Container Data Models](Container_Data_Models.md) (4 shared connections)
- [Lucidity Recovery Commands](Lucidity_Recovery_Commands.md) (4 shared connections)
- [NPC Admin API](NPC_Admin_API.md) (4 shared connections)
- [NPC Definition Schemas](NPC_Definition_Schemas.md) (3 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (3 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/population_control.py`
- `server/npc/spawning_service.py`
- `server/npc/threading.py`
- `server/services/npc_service/definition_crud.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 494 (94%)
- INFERRED: 32 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*