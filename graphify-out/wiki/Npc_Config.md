# Npc Config

> 9 nodes

## Key Concepts

- **NPCMaintenanceConfig** (6 connections) — `server/config/npc_config.py`
- **.get_config_summary()** (3 connections) — `server/config/npc_config.py`
- **.should_run_maintenance()** (3 connections) — `server/config/npc_config.py`
- **.get_respawn_delay()** (2 connections) — `server/config/npc_config.py`
- **Any** (1 connections)
- **Configuration for NPC lifecycle maintenance. This class centralizes all timing…** (1 connections) — `server/config/npc_config.py`
- **Get the respawn delay for a specific NPC type. Args: npc_type: Type of NPC…** (1 connections) — `server/config/npc_config.py`
- **Check if NPC maintenance should run on this tick. Args: tick_count: Current…** (1 connections) — `server/config/npc_config.py`
- **Get a summary of all NPC configuration values. Returns: Dictionary containing…** (1 connections) — `server/config/npc_config.py`

## Relationships

- [Game Tick Processing](Game_Tick_Processing.md) (2 shared connections)
- [Test Lifecycle Periodic](Test_Lifecycle_Periodic.md) (1 shared connections)

## Source Files

- `server/config/npc_config.py`

## Audit Trail

- EXTRACTED: 11 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*