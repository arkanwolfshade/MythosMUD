# ErrorType

> 237 nodes · cohesion 0.01

## Key Concepts

- **NPCDefinition** (110 connections) — `server/models/npc.py`
- **NPCSpawnRule** (47 connections) — `server/models/npc.py`
- **test_npc_models.py** (33 connections) — `server/tests/unit/models/test_npc_models.py`
- **should_spawn_npc()** (24 connections) — `server/npc/spawn_validator.py`
- **test_spawn_validator.py** (24 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **NPCDefinitionCRUDMixin** (18 connections) — `server/services/npc_service/definition_crud.py`
- **spawn_validator.py** (14 connections) — `server/npc/spawn_validator.py`
- **_row_to_npc_definition()** (12 connections) — `server/services/npc_service_models.py`
- **_JSONDict** (10 connections)
- **NPCSpawnRuleCRUDMixin** (10 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **NPCRelationship** (9 connections) — `server/models/npc.py`
- **.update_npc_definition()** (9 connections) — `server/services/npc_service/definition_crud.py`
- **_try_spawn_rules()** (8 connections) — `server/npc/spawn_validator.py`
- **.create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_create_npc_definition()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **._execute_npc_update()** (8 connections) — `server/services/npc_service/definition_crud.py`
- **AsyncSession** (8 connections)
- **_row_to_npc_spawn_rule()** (8 connections) — `server/services/npc_service_models.py`
- **._execute_create_spawn_rule()** (8 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **_loads_json_dict()** (7 connections) — `server/models/npc.py`
- **._build_npc_update_data()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **.get_npc_definition()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **.get_npc_definitions()** (7 connections) — `server/services/npc_service/definition_crud.py`
- **.create_spawn_rule()** (7 connections) — `server/services/npc_service/spawn_rule_crud.py`
- **Base** (6 connections) — `server/models/npc.py`
- *... and 212 more nodes in this community*

## Relationships

- [CombatInstance](CombatInstance.md) (34 shared connections)
- [Room](Room.md) (24 shared connections)
- [RoomLoader](RoomLoader.md) (17 shared connections)
- [test_message_category_invariants.py](test_message_category_invariants.py.md) (8 shared connections)
- [Test Suite Quality Audit - Executive Summary](Test_Suite_Quality_Audit_-_Executive_Summary.md) (6 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (6 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (5 shared connections)
- [BaseEvent](BaseEvent.md) (4 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (3 shared connections)
- [SpellEffectType](SpellEffectType.md) (3 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/npc_base.py`
- `server/npc/population_control.py`
- `server/npc/spawn_validator.py`
- `server/npc/spawning_models.py`
- `server/services/npc_service/definition_crud.py`
- `server/services/npc_service/queries.py`
- `server/services/npc_service/spawn_rule_crud.py`
- `server/services/npc_service_models.py`
- `server/tests/unit/models/test_npc_models.py`
- `server/tests/unit/npc/test_spawn_validator.py`

## Audit Trail

- EXTRACTED: 489 (98%)
- INFERRED: 10 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*