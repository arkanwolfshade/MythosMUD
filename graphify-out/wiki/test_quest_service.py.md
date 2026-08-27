# test_quest_service.py

> 77 nodes

## Key Concepts

- **test_zone_config_loader.py** (36 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **zone_config_loader.py** (19 connections) — `server/npc/zone_config_loader.py`
- **process_zone_rows()** (13 connections) — `server/npc/zone_config_loader.py`
- **_empty_zone_load_result()** (13 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **async_load_zone_configurations()** (12 connections) — `server/npc/zone_config_loader.py`
- **parse_json_field()** (11 connections) — `server/npc/zone_config_loader.py`
- **asyncio** (11 connections)
- **ZoneLoadResult** (9 connections) — `server/npc/zone_config_loader.py`
- **extract_zone_name()** (9 connections) — `server/npc/zone_config_loader.py`
- **load_zone_configurations()** (9 connections) — `server/npc/zone_config_loader.py`
- **process_subzone_rows()** (9 connections) — `server/npc/zone_config_loader.py`
- **_store_subzone_row()** (9 connections) — `server/npc/zone_config_loader.py`
- **parse_zone_special_rules()** (6 connections) — `server/npc/zone_config_loader.py`
- **test_async_load_zone_configurations_converts_url()** (6 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_passes_search_path_for_mythos_e2e()** (6 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_subzone_rows()** (6 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_zone_rows()** (6 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_zone_rows_json_strings()** (6 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_closes_connection()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_error()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_no_database_url()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_success()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_subzone_rows_empty()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_zone_rows_empty()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_extract_zone_name_empty()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- *... and 52 more nodes in this community*

## Relationships

- [test_async_persistence_delegates.py](test_async_persistence_delegates.py.md) (6 shared connections)
- [NPCDefinition](NPCDefinition.md) (3 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (3 shared connections)
- [test_combat_attack_handler.py](test_combat_attack_handler.py.md) (1 shared connections)
- [mock_connection_manager](mock_connection_manager.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/npc/zone_config_loader.py`
- `server/tests/unit/npc/test_zone_config_loader.py`

## Audit Trail

- EXTRACTED: 158 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*