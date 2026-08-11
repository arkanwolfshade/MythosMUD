# NPC Admin API

> 131 nodes

## Key Concepts

- **ZoneConfiguration** (55 connections) — `server/npc/zone_configuration.py`
- **test_zone_config_loader.py** (35 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_zone_configuration.py** (23 connections) — `server/tests/unit/npc/test_zone_configuration.py`
- **zone_config_loader.py** (22 connections) — `server/npc/zone_config_loader.py`
- **process_zone_rows()** (13 connections) — `server/npc/zone_config_loader.py`
- **async_load_zone_configurations()** (13 connections) — `server/npc/zone_config_loader.py`
- **_empty_zone_load_result()** (13 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **ZoneLoadResult** (12 connections) — `server/npc/zone_config_loader.py`
- **parse_json_field()** (11 connections) — `server/npc/zone_config_loader.py`
- **zone_configuration.py** (11 connections) — `server/npc/zone_configuration.py`
- **extract_zone_name()** (9 connections) — `server/npc/zone_config_loader.py`
- **_store_subzone_row()** (9 connections) — `server/npc/zone_config_loader.py`
- **process_subzone_rows()** (9 connections) — `server/npc/zone_config_loader.py`
- **load_zone_configurations()** (9 connections) — `server/npc/zone_config_loader.py`
- **ZoneSpecialRules** (7 connections) — `server/npc/zone_configuration.py`
- **ZoneConfigurationData** (7 connections) — `server/npc/zone_configuration.py`
- **parse_zone_special_rules()** (6 connections) — `server/npc/zone_config_loader.py`
- **_ZoneConfigBucket** (5 connections) — `server/npc/zone_config_loader.py`
- **test_process_zone_rows()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_subzone_rows()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_converts_url()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_async_load_zone_configurations_passes_search_path_for_mythos_e2e()** (5 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_zone_rows_empty()** (4 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_zone_rows_json_strings()** (4 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_process_subzone_rows_empty()** (4 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- *... and 106 more nodes in this community*

## Relationships

- [Command Parser Tests](Command_Parser_Tests.md) (9 shared connections)
- [Commands Look Item](Commands_Look_Item.md) (6 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (5 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Whisper Remediation Plan](Whisper_Remediation_Plan.md) (3 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (1 shared connections)
- [Nats Anti Patterns](Nats_Anti_Patterns.md) (1 shared connections)
- [Lucidity Recovery Commands](Lucidity_Recovery_Commands.md) (1 shared connections)

## Source Files

- `server/npc/zone_config_loader.py`
- `server/npc/zone_configuration.py`
- `server/tests/unit/npc/test_zone_config_loader.py`
- `server/tests/unit/npc/test_zone_configuration.py`

## Audit Trail

- EXTRACTED: 472 (96%)
- INFERRED: 19 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*