# Whisper Remediation Plan

> 81 nodes

## Key Concepts

- **NPCDefinition** (126 connections) — `server/models/npc.py`
- **NPCDefinitionCRUDMixin** (18 connections) — `server/services/npc_service/definition_crud.py`
- **_row_to_npc_definition()** (12 connections) — `server/services/npc_service_models.py`
- **NPCDefinitionUpdateParams** (11 connections) — `server/services/npc_service_models.py`
- **._evaluate_spawn_requirements()** (9 connections) — `server/npc/spawning_service.py`
- **.update_npc_definition()** (9 connections) — `server/services/npc_service/definition_crud.py`
- **AsyncSession** (8 connections)
- **.create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_npc_update()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._evaluate_spawn_rules()** (7 connections) — `server/npc/spawning_service.py`
- **.get_npc_definitions()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **.get_npc_definition()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **._build_npc_update_data()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **._maybe_add_required_npc_request()** (6 connections) — `server/npc/spawning_service.py`
- **._calculate_spawn_priority()** (6 connections) — `server/npc/spawning_service.py`
- **CreateNPCDefinitionInput** (6 connections) — `server/services/npc_service_models.py`
- **NPCSpawnRequest** (5 connections)
- **.get_npc_definition_by_name()** (5 connections) — `server/services/npc_service/definition_crud.py`
- **.get_npc_definitions_by_type()** (5 connections) — `server/services/npc_service/queries.py`
- **.get_npc_definitions_by_sub_zone()** (5 connections) — `server/services/npc_service/queries.py`
- **.get_system_statistics()** (5 connections) — `server/services/npc_service/queries.py`
- **.can_spawn_npc()** (4 connections) — `server/npc/lifecycle_manager.py`
- **.get_population_stats()** (4 connections) — `server/npc/spawning_service.py`
- **._log_npc_definition_created()** (4 connections) — `server/services/npc_service/definition_crud.py`
- *... and 56 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (23 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (19 shared connections)
- [Command Parser Tests](Command_Parser_Tests.md) (17 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (13 shared connections)
- [FastAPI App Factory](FastAPI_App_Factory.md) (13 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (12 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (9 shared connections)
- [Commands Look Item](Commands_Look_Item.md) (9 shared connections)
- [Mythos Calendar Time Service](Mythos_Calendar_Time_Service.md) (5 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (4 shared connections)
- [NPC Definition Schemas](NPC_Definition_Schemas.md) (3 shared connections)
- [Nats Anti Patterns](Nats_Anti_Patterns.md) (3 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/npc_base.py`
- `server/npc/population_control.py`
- `server/npc/spawning_service.py`
- `server/npc/threading.py`
- `server/services/npc_service/definition_crud.py`
- `server/services/npc_service/queries.py`
- `server/services/npc_service_models.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 372 (95%)
- INFERRED: 20 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*