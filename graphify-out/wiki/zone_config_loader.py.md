# zone_config_loader.py

> 25 nodes

## Key Concepts

- **zone_config_loader.py** (22 connections) — `server/npc/zone_config_loader.py`
- **process_zone_rows()** (13 connections) — `server/npc/zone_config_loader.py`
- **ZoneLoadResult** (12 connections) — `server/npc/zone_config_loader.py`
- **zone_configuration.py** (11 connections) — `server/npc/zone_configuration.py`
- **process_subzone_rows()** (9 connections) — `server/npc/zone_config_loader.py`
- **_store_subzone_row()** (9 connections) — `server/npc/zone_config_loader.py`
- **ZoneConfigurationData** (7 connections) — `server/npc/zone_configuration.py`
- **ZoneSpecialRules** (7 connections) — `server/npc/zone_configuration.py`
- **parse_zone_special_rules()** (6 connections) — `server/npc/zone_config_loader.py`
- **_ZoneConfigBucket** (5 connections) — `server/npc/zone_config_loader.py`
- **.__init__()** (3 connections) — `server/npc/zone_configuration.py`
- **Connection** (2 connections)
- **TypedDict** (2 connections)
- **TypedDict** (2 connections)
- **Record** (1 connections)
- **Zone Configuration Loader Module. This module handles loading zone and sub-zone…** (1 connections) — `server/npc/zone_config_loader.py`
- **Build and store one subzone configuration from a database row.** (1 connections) — `server/npc/zone_config_loader.py`
- **Process subzone rows from database and populate subzone configurations. Args:…** (1 connections) — `server/npc/zone_config_loader.py`
- **Result of loading zone and sub-zone configs from PostgreSQL.** (1 connections) — `server/npc/zone_config_loader.py`
- **Parse a zone special_rules field from the database.** (1 connections) — `server/npc/zone_config_loader.py`
- **Process zone rows from database and populate zone configurations. Args: conn:…** (1 connections) — `server/npc/zone_config_loader.py`
- **Zone Configuration Module. This module provides the ZoneConfiguration class for…** (1 connections) — `server/npc/zone_configuration.py`
- **NPC-related modifiers and access rules stored in zone special_rules JSON.** (1 connections) — `server/npc/zone_configuration.py`
- **Raw zone or sub-zone configuration payload from the database or tests.** (1 connections) — `server/npc/zone_configuration.py`
- **Initialize zone configuration. Args: config_data: Dictionary containing zone…** (1 connections) — `server/npc/zone_configuration.py`

## Relationships

- [test_zone_config_loader.py](test_zone_config_loader.py.md) (15 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (8 shared connections)
- [parse_json_field](parse_json_field.md) (4 shared connections)
- [EventBus](EventBus.md) (4 shared connections)
- [extract_zone_name](extract_zone_name.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [threading.py](threading.py.md) (1 shared connections)
- [HolidayService](HolidayService.md) (1 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)
- [load_zone_configurations](load_zone_configurations.md) (1 shared connections)
- [test_population_control.py](test_population_control.py.md) (1 shared connections)

## Source Files

- `server/npc/zone_config_loader.py`
- `server/npc/zone_configuration.py`

## Audit Trail

- EXTRACTED: 111 (92%)
- INFERRED: 10 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*