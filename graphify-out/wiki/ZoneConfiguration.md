# ZoneConfiguration

> 188 nodes

## Key Concepts

- **ZoneConfiguration** (54 connections) — `server/npc/zone_configuration.py`
- **test_zone_config_loader.py** (35 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **should_spawn_npc()** (24 connections) — `server/npc/spawn_validator.py`
- **test_spawn_validator.py** (24 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **test_zone_configuration.py** (23 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **zone_config_loader.py** (22 connections) — `server/npc/zone_config_loader.py`
- **async_load_zone_configurations()** (14 connections) — `server/npc/zone_config_loader.py`
- **process_zone_rows()** (14 connections) — `server/npc/zone_config_loader.py`
- **spawn_validator.py** (14 connections) — `server/npc/spawn_validator.py`
- **_empty_zone_load_result()** (13 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **parse_json_field()** (11 connections) — `server/npc/zone_config_loader.py`
- **zone_configuration.py** (11 connections) — `server/npc/zone_configuration.py`
- **asyncio** (11 connections)
- **_store_subzone_row()** (10 connections) — `server/npc/zone_config_loader.py`
- **ZoneLoadResult** (9 connections) — `server/npc/zone_config_loader.py`
- **extract_zone_name()** (9 connections) — `server/npc/zone_config_loader.py`
- **load_zone_configurations()** (9 connections) — `server/npc/zone_config_loader.py`
- **process_subzone_rows()** (9 connections) — `server/npc/zone_config_loader.py`
- **._should_spawn_npc()** (8 connections) — `server/npc/population_control.py`
- **_try_spawn_rules()** (8 connections) — `server/npc/spawn_validator.py`
- **ZoneConfigurationData** (7 connections) — `server/npc/zone_configuration.py`
- **_spawn_rule_passes()** (6 connections) — `server/npc/spawn_validator.py`
- **parse_zone_special_rules()** (6 connections) — `server/npc/zone_config_loader.py`
- **test_async_load_zone_configurations_converts_url()** (6 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_passes_search_path_for_mythos_e2e()** (6 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- *... and 163 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (18 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (6 shared connections)
- [NPCPopulationController](NPCPopulationController.md) (5 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (5 shared connections)
- [PopulationStats](PopulationStats.md) (2 shared connections)
- [test_npc_utils.py](test_npc_utils.py.md) (1 shared connections)
- [ValueError](ValueError.md) (1 shared connections)

## Source Files

- `server/npc/population_control.py`
- `server/npc/spawn_validator.py`
- `server/npc/zone_config_loader.py`
- `server/npc/zone_configuration.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/npc/test_spawn_validator.py`
- `server/tests/unit/npc/test_zone_config_loader.py`
- `server/tests/unit/npc/test_zone_configuration.py`

## Audit Trail

- EXTRACTED: 354 (96%)
- INFERRED: 15 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*