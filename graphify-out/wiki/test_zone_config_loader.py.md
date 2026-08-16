# test_zone_config_loader.py

> 107 nodes

## Key Concepts

- **test_zone_config_loader.py** (36 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **zone_config_loader.py** (23 connections) — `server/npc/zone_config_loader.py`
- **emote_service.py** (21 connections) — `server/game/emote_service.py`
- **get_asyncpg_server_settings_for_database_url()** (19 connections) — `server/database_config_helpers.py`
- **process_zone_rows()** (14 connections) — `server/npc/zone_config_loader.py`
- **async_load_zone_configurations()** (13 connections) — `server/npc/zone_config_loader.py`
- **_empty_zone_load_result()** (13 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **parse_json_field()** (11 connections) — `server/npc/zone_config_loader.py`
- **asyncio** (11 connections)
- **_store_subzone_row()** (10 connections) — `server/npc/zone_config_loader.py`
- **test_database_config_helpers_asyncpg_settings.py** (10 connections) — `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`
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
- *... and 82 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (14 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (6 shared connections)
- [EmoteService](EmoteService.md) (6 shared connections)
- [database.py](database.py.md) (4 shared connections)
- [rate_overrides.py](rate_overrides.py.md) (2 shared connections)
- [log_and_raise](log_and_raise.md) (2 shared connections)
- [SchemaValidator](SchemaValidator.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [npc_database.py](npc_database.py.md) (1 shared connections)
- [HolidayService](HolidayService.md) (1 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)

## Source Files

- `server/database_config_helpers.py`
- `server/game/emote_service.py`
- `server/npc/zone_config_loader.py`
- `server/npc/zone_configuration.py`
- `server/tests/unit/npc/test_zone_config_loader.py`
- `server/tests/unit/test_database_config_helpers_asyncpg_settings.py`

## Audit Trail

- EXTRACTED: 232 (95%)
- INFERRED: 11 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*