# Nats Anti Patterns

> 11 nodes

## Key Concepts

- **._check_spawn_requirements_for_room()** (7 connections) — `server/npc/population_control.py`
- **._spawn_npc()** (7 connections) — `server/npc/population_control.py`
- **._register_spawned_npc_in_population_stats()** (6 connections) — `server/npc/population_control.py`
- **.spawn_npc()** (4 connections) — `server/npc/population_control.py`
- **.get_zone_configuration()** (4 connections) — `server/npc/population_control.py`
- **Spawn an NPC instance; returns (npc_id, None) or (None, failure_reason).** (1 connections) — `server/npc/population_control.py`
- **Get zone configuration for a given zone key.          Args:             zone_** (1 connections) — `server/npc/population_control.py`
- **Check if NPCs need to be spawned for a specific room.          Args:** (1 connections) — `server/npc/population_control.py`
- **After lifecycle_manager.spawn_npc succeeds, update zone aggregates and log.** (1 connections) — `server/npc/population_control.py`
- **Spawn an NPC instance using the lifecycle manager.          Args:** (1 connections) — `server/npc/population_control.py`
- **Spawn an NPC instance using the population controller.          This is the pu** (1 connections) — `server/npc/population_control.py`

## Relationships

- [Client Event Store](Client_Event_Store.md) (6 shared connections)
- [Whisper Remediation Plan](Whisper_Remediation_Plan.md) (3 shared connections)
- [Container Data Models](Container_Data_Models.md) (2 shared connections)
- [NPC Admin API](NPC_Admin_API.md) (1 shared connections)
- [Command Parser Tests](Command_Parser_Tests.md) (1 shared connections)
- [Lucidity Recovery Commands](Lucidity_Recovery_Commands.md) (1 shared connections)

## Source Files

- `server/npc/population_control.py`

## Audit Trail

- EXTRACTED: 34 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*