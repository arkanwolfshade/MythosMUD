# jsondict

> 262 nodes

## Key Concepts

- **NPCDefinition** (110 connections) — `server/models/npc.py`
- **NPCSpawnRule** (47 connections) — `server/models/npc.py`
- **models/npc.py** (39 connections) — `server/models/npc.py`
- **test_npc_models.py** (33 connections) — `server/tests/unit/models/test_npc_models.py`
- **test_spawn_validator.py** (25 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **should_spawn_npc()** (24 connections) — `server/npc/spawn_validator.py`
- **npc_service/__init__.py** (22 connections) — `server/services/npc_service/__init__.py`
- **NPCDefinitionCRUDMixin** (18 connections) — `server/services/npc_service/definition_crud.py`
- **definition.py** (17 connections) — `server/commands/npc_admin/definition.py`
- **definition_crud.py** (16 connections) — `server/services/npc_service/definition_crud.py`
- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **spawn_validator.py** (14 connections) — `server/npc/spawn_validator.py`
- **combat_schema.py** (13 connections) — `server/schemas/combat/combat_schema.py`
- **npc_service_models.py** (13 connections) — `server/services/npc_service_models.py`
- **_row_to_npc_definition()** (12 connections) — `server/services/npc_service_models.py`
- **queries.py** (12 connections) — `server/services/npc_service/queries.py`
- **spawn_rule_crud.py** (12 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **NPCDefinitionType** (11 connections) — `server/models/npc.py`
- **NPCDefinitionUpdateParams** (11 connections) — `server/services/npc_service_models.py`
- **NPCSpawnRuleCRUDMixin** (10 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **_JSONDict** (10 connections)
- **NPCRelationship** (9 connections) — `server/models/npc.py`
- **.update_npc_definition()** (9 connections) — `server/services/npc_service/definition_crud.py`
- **._should_spawn_npc()** (8 connections) — `server/npc/population_control.py`
- **_try_spawn_rules()** (8 connections) — `server/npc/spawn_validator.py`
- *... and 237 more nodes in this community*

## Relationships

- [server app lifespan startup](server_app_lifespan_startup.md) (29 shared connections)
- [server npc npc base npcbase](server_npc_npc_base_npcbase.md) (24 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (23 shared connections)
- [draft7validator](draft7validator.md) (17 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (16 shared connections)
- [server npc population control npcpopulationcontroller](server_npc_population_control_npcpopulationcontroller.md) (15 shared connections)
- [server api admin npc definitions](server_api_admin_npc_definitions.md) (12 shared connections)
- [server commands npc admin behavior](server_commands_npc_admin_behavior.md) (12 shared connections)
- [fixturerequest](fixturerequest.md) (6 shared connections)
- [server tests unit services test](server_tests_unit_services_test.md) (6 shared connections)
- [server events event types npcdied](server_events_event_types_npcdied.md) (5 shared connections)
- [holidayresolver](holidayresolver.md) (5 shared connections)

## Source Files

- `server/commands/npc_admin/definition.py`
- `server/models/npc.py`
- `server/npc/population_control.py`
- `server/npc/spawn_validator.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_service.py`
- `server/schemas/combat/combat_schema.py`
- `server/services/npc_service/__init__.py`
- `server/services/npc_service/definition_crud.py`
- `server/services/npc_service/queries.py`
- `server/services/npc_service/spawn_rule_crud.py`
- `server/services/npc_service_models.py`
- `server/tests/unit/models/test_npc_models.py`
- `server/tests/unit/npc/test_spawn_validator.py`

## Audit Trail

- EXTRACTED: 627 (99%)
- INFERRED: 7 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*