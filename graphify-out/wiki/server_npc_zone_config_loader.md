# server npc zone config loader

> 126 nodes

## Key Concepts

- **ZoneConfiguration** (54 connections) — `server/npc/zone_configuration.py`
- **test_zone_config_loader.py** (36 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **zone_config_loader.py** (23 connections) — `server/npc/zone_config_loader.py`
- **test_zone_configuration.py** (23 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **process_zone_rows()** (14 connections) — `server/npc/zone_config_loader.py`
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
- **ZoneConfigurationData** (7 connections) — `server/npc/zone_configuration.py`
- **parse_zone_special_rules()** (6 connections) — `server/npc/zone_config_loader.py`
- **test_async_load_zone_configurations_converts_url()** (6 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_passes_search_path_for_mythos_e2e()** (6 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_subzone_rows()** (6 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_zone_rows()** (6 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_zone_rows_json_strings()** (6 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **ZoneSpecialRules** (5 connections) — `server/npc/zone_configuration.py`
- **test_async_load_zone_configurations_closes_connection()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_error()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- *... and 101 more nodes in this community*

## Relationships

- [draft7validator](draft7validator.md) (10 shared connections)
- [server npc population control npcpopulationcontroller](server_npc_population_control_npcpopulationcontroller.md) (7 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [server models npc npcdefinition is](server_models_npc_npcdefinition_is.md) (4 shared connections)
- [server app lifespan startup create](server_app_lifespan_startup_create.md) (3 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (2 shared connections)
- [server database config helpers get](server_database_config_helpers_get.md) (2 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/npc/zone_config_loader.py`
- `server/npc/zone_configuration.py`
- `server/tests/unit/npc/test_zone_config_loader.py`
- `server/tests/unit/npc/test_zone_configuration.py`

## Audit Trail

- EXTRACTED: 231 (85%)
- INFERRED: 41 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*