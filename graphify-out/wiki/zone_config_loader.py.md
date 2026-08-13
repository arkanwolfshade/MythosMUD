# zone_config_loader.py

> 18 nodes

## Key Concepts

- **zone_config_loader.py** (22 connections) — `server/npc/zone_config_loader.py`
- **ZoneLoadResult** (12 connections) — `server/npc/zone_config_loader.py`
- **_store_subzone_row()** (9 connections) — `server/npc/zone_config_loader.py`
- **ZoneConfigurationData** (7 connections) — `server/npc/zone_configuration.py`
- **ZoneSpecialRules** (7 connections) — `server/npc/zone_configuration.py`
- **parse_zone_special_rules()** (6 connections) — `server/npc/zone_config_loader.py`
- **_ZoneConfigBucket** (5 connections) — `server/npc/zone_config_loader.py`
- **.__init__()** (3 connections) — `server/npc/zone_configuration.py`
- **TypedDict** (2 connections)
- **TypedDict** (2 connections)
- **Record** (1 connections)
- **Zone Configuration Loader Module. This module handles loading zone and sub-zone…** (1 connections) — `server/npc/zone_config_loader.py`
- **Build and store one subzone configuration from a database row.** (1 connections) — `server/npc/zone_config_loader.py`
- **Result of loading zone and sub-zone configs from PostgreSQL.** (1 connections) — `server/npc/zone_config_loader.py`
- **Parse a zone special_rules field from the database.** (1 connections) — `server/npc/zone_config_loader.py`
- **NPC-related modifiers and access rules stored in zone special_rules JSON.** (1 connections) — `server/npc/zone_configuration.py`
- **Raw zone or sub-zone configuration payload from the database or tests.** (1 connections) — `server/npc/zone_configuration.py`
- **Initialize zone configuration. Args: config_data: Dictionary containing zone…** (1 connections) — `server/npc/zone_configuration.py`

## Relationships

- [EventBus](EventBus.md) (10 shared connections)
- [test_zone_config_loader.py](test_zone_config_loader.py.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [async_load_zone_configurations](async_load_zone_configurations.md) (3 shared connections)
- [process_subzone_rows](process_subzone_rows.md) (3 shared connections)
- [process_zone_rows](process_zone_rows.md) (3 shared connections)
- [extract_zone_name](extract_zone_name.md) (2 shared connections)

## Source Files

- `server/npc/zone_config_loader.py`
- `server/npc/zone_configuration.py`

## Audit Trail

- EXTRACTED: 51 (89%)
- INFERRED: 6 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*