# Server Npc (10)

> 38 nodes

## Key Concepts

- **test_zone_config_loader.py** (35 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **process_zone_rows()** (13 connections) — `server/npc/zone_config_loader.py`
- **async_load_zone_configurations()** (13 connections) — `server/npc/zone_config_loader.py`
- **_empty_zone_load_result()** (13 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **process_subzone_rows()** (9 connections) — `server/npc/zone_config_loader.py`
- **test_process_zone_rows()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_subzone_rows()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_converts_url()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_passes_search_path_for_mythos_e2e()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_zone_rows_empty()** (4 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_zone_rows_json_strings()** (4 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_subzone_rows_empty()** (4 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_success()** (4 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_no_database_url()** (4 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_error()** (4 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_closes_connection()** (4 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_load_zone_configurations_success()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_load_zone_configurations_merges_zone_and_subzone()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_load_zone_configurations_error()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Connection** (2 connections)
- **MonkeyPatch** (2 connections)
- **Test process_zone_rows() handles empty result.** (2 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **Process zone rows from database and populate zone configurations.      Args:** (1 connections) — `server/npc/zone_config_loader.py`
- **Process subzone rows from database and populate subzone configurations.      Arg** (1 connections) — `server/npc/zone_config_loader.py`
- **Async helper to load zone configurations from PostgreSQL database.** (1 connections) — `server/npc/zone_config_loader.py`
- *... and 13 more nodes in this community*

## Relationships

- [Server Npc (15)](Server_Npc_%2815%29.md) (12 shared connections)
- [Server Npc (17)](Server_Npc_%2817%29.md) (7 shared connections)
- [Server Npc (18)](Server_Npc_%2818%29.md) (6 shared connections)
- [Server Npc (9)](Server_Npc_%289%29.md) (4 shared connections)
- [Server Events](Server_Events.md) (4 shared connections)
- [Server Services (42)](Server_Services_%2842%29.md) (1 shared connections)

## Source Files

- `server/npc/zone_config_loader.py`
- `server/tests/unit/npc/test_zone_config_loader.py`

## Audit Trail

- EXTRACTED: 160 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*