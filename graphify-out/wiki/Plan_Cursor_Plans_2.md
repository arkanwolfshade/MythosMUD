# Plan Cursor Plans

> 18 nodes

## Key Concepts

- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **NPCQueryMixin** (7 connections) — `server/services/npc_service/queries.py`
- **.get_npc_definitions_by_type()** (5 connections) — `server/services/npc_service/queries.py`
- **.get_npc_definitions_by_sub_zone()** (5 connections) — `server/services/npc_service/queries.py`
- **.get_system_statistics()** (5 connections) — `server/services/npc_service/queries.py`
- **AsyncSession** (3 connections)
- **npc_service()** (3 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_npc_service_init()** (3 connections) — `server/tests/unit/services/test_npc_service.py`
- **.__init__()** (2 connections) — `server/services/npc_service/__init__.py`
- **Comprehensive NPC management service.      Handles CRUD operations for NPC defin** (1 connections) — `server/services/npc_service/__init__.py`
- **Initialize the NPC service.** (1 connections) — `server/services/npc_service/__init__.py`
- **Any** (1 connections)
- **Mixin providing NPC query operations.** (1 connections) — `server/services/npc_service/queries.py`
- **Get NPC definitions by type.** (1 connections) — `server/services/npc_service/queries.py`
- **Get NPC definitions by sub-zone.** (1 connections) — `server/services/npc_service/queries.py`
- **Get system-wide NPC statistics.** (1 connections) — `server/services/npc_service/queries.py`
- **Create NPCService instance.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test NPCService initialization.** (1 connections) — `server/tests/unit/services/test_npc_service.py`

## Relationships

- [Whisper Remediation Plan](Whisper_Remediation_Plan.md) (5 shared connections)
- [App Lifespan Management](App_Lifespan_Management.md) (3 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (3 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (2 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (2 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (1 shared connections)
- [Cursor Plans Best](Cursor_Plans_Best.md) (1 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (1 shared connections)

## Source Files

- `server/services/npc_service/__init__.py`
- `server/services/npc_service/queries.py`
- `server/tests/unit/services/test_npc_service.py`

## Audit Trail

- EXTRACTED: 52 (93%)
- INFERRED: 4 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*