# Server Npc (15)

> 20 nodes

## Key Concepts

- **zone_config_loader.py** (22 connections) — `server/npc/zone_config_loader.py`
- **ZoneLoadResult** (12 connections) — `server/npc/zone_config_loader.py`
- **zone_configuration.py** (11 connections) — `server/npc/zone_configuration.py`
- **_store_subzone_row()** (9 connections) — `server/npc/zone_config_loader.py`
- **ZoneSpecialRules** (7 connections) — `server/npc/zone_configuration.py`
- **ZoneConfigurationData** (7 connections) — `server/npc/zone_configuration.py`
- **parse_zone_special_rules()** (6 connections) — `server/npc/zone_config_loader.py`
- **_ZoneConfigBucket** (5 connections) — `server/npc/zone_config_loader.py`
- **.__init__()** (3 connections) — `server/npc/zone_configuration.py`
- **TypedDict** (2 connections)
- **TypedDict** (2 connections)
- **Record** (1 connections)
- **Zone Configuration Loader Module.  This module handles loading zone and sub-zone** (1 connections) — `server/npc/zone_config_loader.py`
- **Result of loading zone and sub-zone configs from PostgreSQL.** (1 connections) — `server/npc/zone_config_loader.py`
- **Parse a zone special_rules field from the database.** (1 connections) — `server/npc/zone_config_loader.py`
- **Build and store one subzone configuration from a database row.** (1 connections) — `server/npc/zone_config_loader.py`
- **Zone Configuration Module.  This module provides the ZoneConfiguration class for** (1 connections) — `server/npc/zone_configuration.py`
- **NPC-related modifiers and access rules stored in zone special_rules JSON.** (1 connections) — `server/npc/zone_configuration.py`
- **Raw zone or sub-zone configuration payload from the database or tests.** (1 connections) — `server/npc/zone_configuration.py`
- **Initialize zone configuration.          Args:             config_data: Dictionar** (1 connections) — `server/npc/zone_configuration.py`

## Relationships

- [Server Npc (10)](Server_Npc_%2810%29.md) (12 shared connections)
- [Server Npc (9)](Server_Npc_%289%29.md) (7 shared connections)
- [Server Events](Server_Events.md) (3 shared connections)
- [Server Npc (17)](Server_Npc_%2817%29.md) (3 shared connections)
- [Server Services (42)](Server_Services_%2842%29.md) (2 shared connections)
- [Server Npc (18)](Server_Npc_%2818%29.md) (2 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Models (3)](Server_Models_%283%29.md) (2 shared connections)
- [Server Npc (6)](Server_Npc_%286%29.md) (1 shared connections)
- [Server Npc (4)](Server_Npc_%284%29.md) (1 shared connections)

## Source Files

- `server/npc/zone_config_loader.py`
- `server/npc/zone_configuration.py`

## Audit Trail

- EXTRACTED: 85 (89%)
- INFERRED: 10 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*