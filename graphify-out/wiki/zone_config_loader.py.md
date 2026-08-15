# zone_config_loader.py

> 28 nodes

## Key Concepts

- **zone_config_loader.py** (22 connections) — `server/npc/zone_config_loader.py`
- **zone_configuration.py** (11 connections) — `server/npc/zone_configuration.py`
- **_store_subzone_row()** (10 connections) — `server/npc/zone_config_loader.py`
- **extract_zone_name()** (9 connections) — `server/npc/zone_config_loader.py`
- **ZoneConfigurationData** (7 connections) — `server/npc/zone_configuration.py`
- **parse_zone_special_rules()** (6 connections) — `server/npc/zone_config_loader.py`
- **ZoneSpecialRules** (5 connections) — `server/npc/zone_configuration.py`
- **_ZoneConfigBucket** (3 connections) — `server/npc/zone_config_loader.py`
- **.__init__()** (3 connections) — `server/npc/zone_configuration.py`
- **test_extract_zone_name_empty()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_extract_zone_name_multiple_slashes()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_extract_zone_name_no_slash()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **test_extract_zone_name_with_slash()** (3 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- **TypedDict** (2 connections)
- **TypedDict** (2 connections)
- **Record** (1 connections)
- **Zone Configuration Loader Module. This module handles loading zone and sub-zone…** (1 connections) — `server/npc/zone_config_loader.py`
- **Build and store one subzone configuration from a database row.** (1 connections) — `server/npc/zone_config_loader.py`
- **Parse a zone special_rules field from the database.** (1 connections) — `server/npc/zone_config_loader.py`
- **Extract zone name from stable_id (format: 'plane/zone'). Args: stable_id: The…** (1 connections) — `server/npc/zone_config_loader.py`
- **Zone Configuration Module. This module provides the ZoneConfiguration class for…** (1 connections) — `server/npc/zone_configuration.py`
- **NPC-related modifiers and access rules stored in zone special_rules JSON.** (1 connections) — `server/npc/zone_configuration.py`
- **Raw zone or sub-zone configuration payload from the database or tests.** (1 connections) — `server/npc/zone_configuration.py`
- **Initialize zone configuration. Args: config_data: Dictionary containing zone…** (1 connections) — `server/npc/zone_configuration.py`
- **Test extract_zone_name() extracts zone from stable_id.** (1 connections) — `server/tests/unit/npc/test_zone_config_loader.py`
- *... and 3 more nodes in this community*

## Relationships

- [test_zone_config_loader.py](test_zone_config_loader.py.md) (17 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (6 shared connections)
- [parse_json_field](parse_json_field.md) (3 shared connections)
- [database_config_helpers.py](database_config_helpers.py.md) (2 shared connections)
- [should_spawn_npc](should_spawn_npc.md) (2 shared connections)

## Source Files

- `server/npc/zone_config_loader.py`
- `server/npc/zone_configuration.py`
- `server/tests/unit/npc/test_zone_config_loader.py`

## Audit Trail

- EXTRACTED: 66 (93%)
- INFERRED: 5 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*