# Test Zone Config Loader

> 172 nodes

## Key Concepts

- **ZoneConfiguration** (54 connections) — `server/npc/zone_configuration.py`
- **test_zone_config_loader.py** (36 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_spawn_validator.py** (25 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **should_spawn_npc()** (24 connections) — `server/npc/spawn_validator.py`
- **zone_config_loader.py** (23 connections) — `server/npc/zone_config_loader.py`
- **test_zone_configuration.py** (23 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **process_zone_rows()** (14 connections) — `server/npc/zone_config_loader.py`
- **spawn_validator.py** (14 connections) — `server/npc/spawn_validator.py`
- **async_load_zone_configurations()** (13 connections) — `server/npc/zone_config_loader.py`
- **_empty_zone_load_result()** (13 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **parse_json_field()** (11 connections) — `server/npc/zone_config_loader.py`
- **zone_configuration.py** (11 connections) — `server/npc/zone_configuration.py`
- **asyncio** (11 connections)
- **_store_subzone_row()** (10 connections) — `server/npc/zone_config_loader.py`
- **ZoneLoadResult** (9 connections) — `server/npc/zone_config_loader.py`
- **extract_zone_name()** (9 connections) — `server/npc/zone_config_loader.py`
- **load_zone_configurations()** (9 connections) — `server/npc/zone_config_loader.py`
- **process_subzone_rows()** (9 connections) — `server/npc/zone_config_loader.py`
- **_try_spawn_rules()** (8 connections) — `server/npc/spawn_validator.py`
- **ZoneConfigurationData** (7 connections) — `server/npc/zone_configuration.py`
- **_spawn_rule_passes()** (6 connections) — `server/npc/spawn_validator.py`
- **parse_zone_special_rules()** (6 connections) — `server/npc/zone_config_loader.py`
- **test_async_load_zone_configurations_converts_url()** (6 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_passes_search_path_for_mythos_e2e()** (6 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_subzone_rows()** (6 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- *... and 147 more nodes in this community*

## Relationships

- [NPC Models](NPC_Models.md) (11 shared connections)
- [Test Population Control](Test_Population_Control.md) (7 shared connections)
- [Test Npc Utils](Test_Npc_Utils.md) (6 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (6 shared connections)
- [NPC Behavior & Spawning](NPC_Behavior_&_Spawning.md) (4 shared connections)
- [Population Control](Population_Control.md) (3 shared connections)
- [Spawning Service](Spawning_Service.md) (3 shared connections)
- [Test Rate Overrides](Test_Rate_Overrides.md) (2 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (2 shared connections)
- [Database](Database.md) (1 shared connections)

## Source Files

- `server/npc/spawn_validator.py`
- `server/npc/zone_config_loader.py`
- `server/npc/zone_configuration.py`
- `server/tests/unit/npc/test_spawn_validator.py`
- `server/tests/unit/npc/test_zone_config_loader.py`
- `server/tests/unit/npc/test_zone_configuration.py`

## Audit Trail

- EXTRACTED: 343 (96%)
- INFERRED: 14 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*