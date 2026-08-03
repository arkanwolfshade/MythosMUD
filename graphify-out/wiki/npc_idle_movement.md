# npc idle movement

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

- [npc realtime occupant](npc_realtime_occupant.md) (12 shared connections)
- [spell game magic](spell_game_magic.md) (7 shared connections)
- [models npc rationale](models_npc_rationale.md) (5 shared connections)
- [security headers middleware](security_headers_middleware.md) (3 shared connections)
- [commands lucidity recovery](commands_lucidity_recovery.md) (2 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (2 shared connections)
- [models lucidity rationale](models_lucidity_rationale.md) (2 shared connections)
- [services npc combat](services_npc_combat.md) (1 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (1 shared connections)

## Source Files

- `server/npc/zone_config_loader.py`
- `server/npc/zone_configuration.py`

## Audit Trail

- EXTRACTED: 85 (89%)
- INFERRED: 10 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*