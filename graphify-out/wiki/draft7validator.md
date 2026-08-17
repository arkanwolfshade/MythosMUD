# draft7validator

> 329 nodes

## Key Concepts

- **NPCDefinition** (110 connections) — `server/models/npc.py`
- **NPCSpawnRule** (47 connections) — `server/models/npc.py`
- **models/npc.py** (39 connections) — `server/models/npc.py`
- **test_npc_models.py** (33 connections) — `server/tests/unit/models/test_npc_models.py`
- **migrate_combat_data.py** (29 connections) — `server/scripts/migrate_combat_data.py`
- **test_spawn_validator.py** (25 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **should_spawn_npc()** (24 connections) — `server/npc/spawn_validator.py`
- **npc_service/__init__.py** (22 connections) — `server/services/npc_service/__init__.py`
- **test_combat_schema.py** (21 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **NPCDefinitionCRUDMixin** (18 connections) — `server/services/npc_service/definition_crud.py`
- **definition_crud.py** (16 connections) — `server/services/npc_service/definition_crud.py`
- **spawn_validator.py** (14 connections) — `server/npc/spawn_validator.py`
- **validate_npc_combat_data()** (13 connections) — `server/schemas/combat/combat_schema.py`
- **combat_schema.py** (13 connections) — `server/schemas/combat/combat_schema.py`
- **npc_service_models.py** (13 connections) — `server/services/npc_service_models.py`
- **_row_to_npc_definition()** (12 connections) — `server/services/npc_service_models.py`
- **queries.py** (12 connections) — `server/services/npc_service/queries.py`
- **spawn_rule_crud.py** (12 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **CombatSchemaValidationError** (11 connections) — `server/schemas/combat/combat_schema.py`
- **NPCDefinitionUpdateParams** (11 connections) — `server/services/npc_service_models.py`
- **validate_base_stats_combat_data()** (11 connections) — `server/schemas/combat/combat_schema.py`
- **validate_combat_messages()** (11 connections) — `server/schemas/combat/combat_schema.py`
- **NPCSpawnRuleCRUDMixin** (10 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **_JSONDict** (10 connections)
- **combat/__init__.py** (10 connections) — `server/schemas/combat/__init__.py`
- *... and 304 more nodes in this community*

## Relationships

- [server events event bus eventbus](server_events_event_bus_eventbus.md) (23 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (22 shared connections)
- [server app lifespan startup create](server_app_lifespan_startup_create.md) (21 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (11 shared connections)
- [server npc zone config loader](server_npc_zone_config_loader.md) (10 shared connections)
- [server events event bus](server_events_event_bus.md) (9 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (9 shared connections)
- [server models npc npcdefinition is](server_models_npc_npcdefinition_is.md) (8 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (8 shared connections)
- [server game skill service](server_game_skill_service.md) (5 shared connections)
- [server npc init](server_npc_init.md) (5 shared connections)
- [server database config helpers get](server_database_config_helpers_get.md) (4 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/population_control.py`
- `server/npc/spawn_validator.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_service.py`
- `server/schemas/combat/__init__.py`
- `server/schemas/combat/combat_schema.py`
- `server/scripts/migrate_combat_data.py`
- `server/services/npc_service/__init__.py`
- `server/services/npc_service/definition_crud.py`
- `server/services/npc_service/queries.py`
- `server/services/npc_service/spawn_rule_crud.py`
- `server/services/npc_service_models.py`
- `server/tests/unit/models/test_npc_models.py`
- `server/tests/unit/npc/test_spawn_validator.py`
- `server/tests/unit/schemas/test_combat_schema.py`

## Audit Trail

- EXTRACTED: 735 (98%)
- INFERRED: 12 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*