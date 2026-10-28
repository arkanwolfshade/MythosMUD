# test_message_category_invariants.py

> 126 nodes · cohesion 0.03

## Key Concepts

- **ZoneConfiguration** (54 connections) — `server/npc/zone_configuration.py`
- **test_zone_config_loader.py** (35 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_zone_configuration.py** (23 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **zone_config_loader.py** (22 connections) — `server/npc/zone_config_loader.py`
- **async_load_zone_configurations()** (14 connections) — `server/npc/zone_config_loader.py`
- **process_zone_rows()** (14 connections) — `server/npc/zone_config_loader.py`
- **_empty_zone_load_result()** (13 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **parse_json_field()** (11 connections) — `server/npc/zone_config_loader.py`
- **zone_configuration.py** (11 connections) — `server/npc/zone_configuration.py`
- **asyncio** (11 connections)
- **_store_subzone_row()** (10 connections) — `server/npc/zone_config_loader.py`
- **extract_zone_name()** (9 connections) — `server/npc/zone_config_loader.py`
- **load_zone_configurations()** (9 connections) — `server/npc/zone_config_loader.py`
- **process_subzone_rows()** (9 connections) — `server/npc/zone_config_loader.py`
- **ZoneLoadResult** (9 connections) — `server/npc/zone_config_loader.py`
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

- [CombatInstance](CombatInstance.md) (8 shared connections)
- [ErrorType](ErrorType.md) (8 shared connections)
- [aggro_threat.py](aggro_threat.py.md) (7 shared connections)
- [Room](Room.md) (3 shared connections)
- [RoomLoader](RoomLoader.md) (3 shared connections)
- [test_character_creation_service.py](test_character_creation_service.py.md) (2 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (1 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)

## Source Files

- `server/npc/zone_config_loader.py`
- `server/npc/zone_configuration.py`
- `server/tests/unit/npc/test_zone_config_loader.py`
- `server/tests/unit/npc/test_zone_configuration.py`

## Audit Trail

- EXTRACTED: 256 (94%)
- INFERRED: 15 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*