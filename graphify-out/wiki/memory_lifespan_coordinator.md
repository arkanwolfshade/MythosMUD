# memory lifespan coordinator

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

- [HealthMonitor](HealthMonitor.md) (12 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (7 shared connections)
- [Represents the configuration for a](Represents_the_configuration_for_a.md) (7 shared connections)
- [.apply dp change()](apply_dp_change%28%29.md) (3 shared connections)
- [src/**/*.spec](src-__-_.spec.md) (2 shared connections)
- [real time](real_time.md) (1 shared connections)
- [rate overrides](rate_overrides.md) (1 shared connections)
- [MutableHeaders](MutableHeaders.md) (1 shared connections)
- [. repr ()](_repr_%28%29.md) (1 shared connections)

## Source Files

- `server/npc/zone_config_loader.py`
- `server/npc/zone_configuration.py`

## Audit Trail

- EXTRACTED: 85 (89%)
- INFERRED: 10 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*