# PlayerNameExtractor

> 58 nodes · cohesion 0.08

## Key Concepts

- **test_npc_definitions_api.py** (35 connections) — `server/tests/unit/api/test_npc_definitions_api.py`
- **npc_definitions_api.py** (31 connections) — `server/api/admin/npc_definitions_api.py`
- **_update_npc_definition_internal()** (16 connections) — `server/api/admin/npc_definitions_api.py`
- **get_npc_definitions()** (15 connections) — `server/api/admin/npc_definitions_api.py`
- **create_npc_definition()** (14 connections) — `server/api/admin/npc_definitions_api.py`
- **get_npc_definition()** (14 connections) — `server/api/admin/npc_definitions_api.py`
- **delete_npc_definition()** (12 connections) — `server/api/admin/npc_definitions_api.py`
- **_admin_user()** (12 connections) — `server/tests/unit/api/test_npc_definitions_api.py`
- **NPCBehaviorConfigModel** (10 connections) — `server/api/admin/npc_schemas.py`
- **NPCDefinitionResponse** (10 connections) — `server/api/admin/npc_schemas.py`
- **.from_orm()** (10 connections) — `server/api/admin/npc_schemas.py`
- **NPCDefinitionUpdate** (10 connections) — `server/api/admin/npc_schemas.py`
- **asyncio** (10 connections)
- **patch** (10 connections)
- **test_create_npc_definition()** (10 connections) — `server/tests/unit/api/test_npc_definitions_api.py`
- **update_npc_definition()** (9 connections) — `server/api/admin/npc_definitions_api.py`
- **NPCBaseStatsModel** (7 connections) — `server/api/admin/npc_schemas.py`
- **NPCDefinitionCreate** (7 connections) — `server/api/admin/npc_schemas.py`
- **test_update_npc_definition_internal()** (7 connections) — `server/tests/unit/api/test_npc_definitions_api.py`
- **test_update_npc_definition_not_found()** (7 connections) — `server/tests/unit/api/test_npc_definitions_api.py`
- **build_update_params_from_model()** (6 connections) — `server/api/admin/npc_schemas.py`
- **NPCAIIntegrationModel** (6 connections) — `server/api/admin/npc_schemas.py`
- **test_delete_npc_definition_not_found()** (6 connections) — `server/tests/unit/api/test_npc_definitions_api.py`
- **test_get_npc_definition_found()** (6 connections) — `server/tests/unit/api/test_npc_definitions_api.py`
- **test_get_npc_definition_not_found()** (6 connections) — `server/tests/unit/api/test_npc_definitions_api.py`
- *... and 33 more nodes in this community*

## Relationships

- [useMythosAppActions.ts](useMythosAppActions.ts.md) (19 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (11 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [useGameConnectionRefactored.ts](useGameConnectionRefactored.ts.md) (9 shared connections)
- [test_npc_startup_service.py](test_npc_startup_service.py.md) (7 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (6 shared connections)
- [Room](Room.md) (4 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (3 shared connections)
- [saveMapChanges.ts](saveMapChanges.ts.md) (3 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [test_item_catalog.py](test_item_catalog.py.md) (2 shared connections)
- [ItemFactory](ItemFactory.md) (1 shared connections)

## Source Files

- `server/api/admin/npc_definitions_api.py`
- `server/api/admin/npc_schemas.py`
- `server/tests/unit/api/test_npc_definitions_api.py`

## Audit Trail

- EXTRACTED: 196 (90%)
- INFERRED: 21 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*