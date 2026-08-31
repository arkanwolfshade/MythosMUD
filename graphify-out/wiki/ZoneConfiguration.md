# ZoneConfiguration

> 131 nodes

## Key Concepts

- **ZoneConfiguration** (54 connections) — `server/npc/zone_configuration.py`
- **NPCSpawnRule** (47 connections) — `server/models/npc.py`
- **models/npc.py** (39 connections) — `server/models/npc.py`
- **test_spawn_validator.py** (25 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **should_spawn_npc()** (24 connections) — `server/npc/spawn_validator.py`
- **test_zone_configuration.py** (23 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **spawn_validator.py** (14 connections) — `server/npc/spawn_validator.py`
- **zone_configuration.py** (11 connections) — `server/npc/zone_configuration.py`
- **NPCRelationship** (9 connections) — `server/models/npc.py`
- **._should_spawn_npc()** (8 connections) — `server/npc/population_control.py`
- **_try_spawn_rules()** (8 connections) — `server/npc/spawn_validator.py`
- **._evaluate_spawn_rules()** (7 connections) — `server/npc/spawning_service.py`
- **Base** (6 connections) — `server/models/npc.py`
- **_spawn_rule_passes()** (6 connections) — `server/npc/spawn_validator.py`
- **._calculate_spawn_priority()** (6 connections) — `server/npc/spawning_service.py`
- **_population_allows_spawn()** (5 connections) — `server/npc/spawn_validator.py`
- **.__init__()** (4 connections) — `server/npc/spawning_models.py`
- **mock_zone_config()** (4 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **npc_metadata.py** (4 connections) — `server/npc_metadata.py`
- **.load_spawn_rules()** (3 connections) — `server/npc/population_control.py`
- **test_check_spawn_requirements_for_room_with_definitions()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_configuration_exact_match()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_configuration_no_slash()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_configuration_zone_fallback()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **mock_npc_definition()** (3 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- *... and 106 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (26 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (26 shared connections)
- [test_zone_config_loader.py](test_zone_config_loader.py.md) (14 shared connections)
- [_JSONDict](_JSONDict.md) (12 shared connections)
- [event_types.py](event_types.py.md) (11 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [NPCSpawnRuleCRUDMixin](NPCSpawnRuleCRUDMixin.md) (5 shared connections)
- [Player](Player.md) (4 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (4 shared connections)
- [NPCBase](NPCBase.md) (3 shared connections)
- [test_npc_service.py](test_npc_service.py.md) (2 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (2 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/population_control.py`
- `server/npc/spawn_validator.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_service.py`
- `server/npc/zone_configuration.py`
- `server/npc_metadata.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/npc/test_spawn_validator.py`
- `server/tests/unit/npc/test_zone_configuration.py`

## Audit Trail

- EXTRACTED: 305 (97%)
- INFERRED: 10 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*