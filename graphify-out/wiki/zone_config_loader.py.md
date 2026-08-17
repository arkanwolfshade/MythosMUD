# zone_config_loader.py

> 18 nodes

## Key Concepts

- **zone_config_loader.py** (23 connections) — `server/npc/zone_config_loader.py`
- **zone_configuration.py** (11 connections) — `server/npc/zone_configuration.py`
- **_store_subzone_row()** (10 connections) — `server/npc/zone_config_loader.py`
- **ZoneConfigurationData** (7 connections) — `server/npc/zone_configuration.py`
- **parse_zone_special_rules()** (6 connections) — `server/npc/zone_config_loader.py`
- **ZoneSpecialRules** (5 connections) — `server/npc/zone_configuration.py`
- **_ZoneConfigBucket** (3 connections) — `server/npc/zone_config_loader.py`
- **.__init__()** (3 connections) — `server/npc/zone_configuration.py`
- **TypedDict** (2 connections)
- **TypedDict** (2 connections)
- **Record** (1 connections)
- **Zone Configuration Loader Module. This module handles loading zone and sub-zone…** (1 connections) — `server/npc/zone_config_loader.py`
- **Build and store one subzone configuration from a database row.** (1 connections) — `server/npc/zone_config_loader.py`
- **Parse a zone special_rules field from the database.** (1 connections) — `server/npc/zone_config_loader.py`
- **Zone Configuration Module. This module provides the ZoneConfiguration class for…** (1 connections) — `server/npc/zone_configuration.py`
- **NPC-related modifiers and access rules stored in zone special_rules JSON.** (1 connections) — `server/npc/zone_configuration.py`
- **Raw zone or sub-zone configuration payload from the database or tests.** (1 connections) — `server/npc/zone_configuration.py`
- **Initialize zone configuration. Args: config_data: Dictionary containing zone…** (1 connections) — `server/npc/zone_configuration.py`

## Relationships

- [test_zone_config_loader.py](test_zone_config_loader.py.md) (11 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (6 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (4 shared connections)
- [parse_json_field](parse_json_field.md) (3 shared connections)
- [extract_zone_name](extract_zone_name.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [load_zone_configurations](load_zone_configurations.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)
- [test_spawn_validator.py](test_spawn_validator.py.md) (1 shared connections)

## Source Files

- `server/npc/zone_config_loader.py`
- `server/npc/zone_configuration.py`

## Audit Trail

- EXTRACTED: 52 (91%)
- INFERRED: 5 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*