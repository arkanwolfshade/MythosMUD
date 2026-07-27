# Zone Config Loader

> 128 nodes · cohesion 0.03

## Key Concepts

- **ZoneConfiguration** (63 connections) — `server/npc/zone_configuration.py`
- **test_zone_config_loader.py** (33 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_zone_configuration.py** (22 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **zone_config_loader.py** (20 connections) — `server/npc/zone_config_loader.py`
- **process_zone_rows()** (14 connections) — `server/npc/zone_config_loader.py`
- **_empty_zone_load_result()** (13 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **async_load_zone_configurations()** (13 connections) — `server/npc/zone_config_loader.py`
- **ZoneLoadResult** (13 connections) — `server/npc/zone_config_loader.py`
- **parse_json_field()** (11 connections) — `server/npc/zone_config_loader.py`
- **ZoneConfigurationData** (11 connections) — `server/npc/zone_configuration.py`
- **load_zone_configurations()** (10 connections) — `server/npc/zone_config_loader.py`
- **_store_subzone_row()** (10 connections) — `server/npc/zone_config_loader.py`
- **ZoneSpecialRules** (10 connections) — `server/npc/zone_configuration.py`
- **spawn_validator.py** (9 connections) — `server/npc/spawn_validator.py`
- **extract_zone_name()** (9 connections) — `server/npc/zone_config_loader.py`
- **process_subzone_rows()** (9 connections) — `server/npc/zone_config_loader.py`
- **zone_configuration.py** (7 connections) — `server/npc/zone_configuration.py`
- **parse_zone_special_rules()** (6 connections) — `server/npc/zone_config_loader.py`
- **ZoneConfiguration** (6 connections) — `server/npc/zone_config_loader.py`
- **test_async_load_zone_configurations_converts_url()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_passes_search_path_for_mythos_e2e()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Test get_effective_spawn_probability() with no modifier.** (5 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **_ZoneConfigBucket** (5 connections) — `server/npc/zone_config_loader.py`
- **Connection** (5 connections) — `server/npc/zone_config_loader.py`
- **._load_zone_configurations()** (4 connections) — `server/npc/population_control.py`
- *... and 103 more nodes in this community*

## Relationships

- [[Distributed Event Bus]] (14 shared connections)
- [[NPC Spawn Validator]] (6 shared connections)
- [[NPC Population Control]] (6 shared connections)
- [[NPC Services Bundle]] (5 shared connections)
- [[NPC Admin API]] (5 shared connections)
- [[Dependency Risk Analyzer]] (4 shared connections)
- [[NPC Definition Schemas]] (2 shared connections)
- [[Lucidity Rate Overrides]] (2 shared connections)
- [[Database Manager Tests]] (1 shared connections)

## Source Files

- `server/npc/population_control.py`
- `server/npc/spawn_validator.py`
- `server/npc/zone_config_loader.py`
- `server/npc/zone_configuration.py`
- `server/tests/unit/npc/test_zone_config_loader.py`
- `server/tests/unit/npc/test_zone_configuration.py`

## Audit Trail

- EXTRACTED: 470 (89%)
- INFERRED: 61 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
