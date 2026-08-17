# zone_config_loader.py

> 23 nodes

## Key Concepts

- **zone_config_loader.py** (23 connections) — `server/npc/zone_config_loader.py`
- **process_zone_rows()** (14 connections) — `server/npc/zone_config_loader.py`
- **_store_subzone_row()** (10 connections) — `server/npc/zone_config_loader.py`
- **ZoneLoadResult** (9 connections) — `server/npc/zone_config_loader.py`
- **process_subzone_rows()** (9 connections) — `server/npc/zone_config_loader.py`
- **ZoneConfigurationData** (7 connections) — `server/npc/zone_configuration.py`
- **parse_zone_special_rules()** (6 connections) — `server/npc/zone_config_loader.py`
- **ZoneSpecialRules** (5 connections) — `server/npc/zone_configuration.py`
- **_ZoneConfigBucket** (3 connections) — `server/npc/zone_config_loader.py`
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
- **NPC-related modifiers and access rules stored in zone special_rules JSON.** (1 connections) — `server/npc/zone_configuration.py`
- **Raw zone or sub-zone configuration payload from the database or tests.** (1 connections) — `server/npc/zone_configuration.py`
- **Initialize zone configuration. Args: config_data: Dictionary containing zone…** (1 connections) — `server/npc/zone_configuration.py`

## Relationships

- [async_load_zone_configurations](async_load_zone_configurations.md) (10 shared connections)
- [NPCDefinition](NPCDefinition.md) (9 shared connections)
- [test_zone_config_loader.py](test_zone_config_loader.py.md) (8 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [extract_zone_name](extract_zone_name.md) (3 shared connections)
- [npc_database.py](npc_database.py.md) (2 shared connections)
- [load_zone_configurations](load_zone_configurations.md) (1 shared connections)

## Source Files

- `server/npc/zone_config_loader.py`
- `server/npc/zone_configuration.py`

## Audit Trail

- EXTRACTED: 64 (90%)
- INFERRED: 7 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*