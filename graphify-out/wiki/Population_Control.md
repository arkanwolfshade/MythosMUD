# Population Control

> 22 nodes

## Key Concepts

- **._should_spawn_npc()** (8 connections) — `server/npc/population_control.py`
- **._check_spawn_requirements_for_room()** (7 connections) — `server/npc/population_control.py`
- **._register_spawned_npc_in_population_stats()** (6 connections) — `server/npc/population_control.py`
- **._spawn_npc()** (6 connections) — `server/npc/population_control.py`
- **._get_zone_key_from_room_id()** (5 connections) — `server/npc/population_control.py`
- **._handle_player_entered_room()** (5 connections) — `server/npc/population_control.py`
- **.get_population_stats()** (4 connections) — `server/npc/population_control.py`
- **.get_zone_configuration()** (4 connections) — `server/npc/population_control.py`
- **._handle_player_left_room()** (4 connections) — `server/npc/population_control.py`
- **._update_player_count()** (4 connections) — `server/npc/population_control.py`
- **Handle player entering a room.** (1 connections) — `server/npc/population_control.py`
- **Handle player leaving a room.** (1 connections) — `server/npc/population_control.py`
- **Update the current player count in game state.** (1 connections) — `server/npc/population_control.py`
- **Get zone configuration for a given zone key. Args: zone_key: Zone key in format…** (1 connections) — `server/npc/population_control.py`
- **Get population statistics for a given zone. Args: zone_key: Zone key in format…** (1 connections) — `server/npc/population_control.py`
- **Extract zone key from room ID. Args: room_id: The room identifier Returns: Zone…** (1 connections) — `server/npc/population_control.py`
- **Public wrapper to extract a zone key from a room ID. This delegates to the…** (1 connections) — `server/npc/population_control.py`
- **Check if NPCs need to be spawned for a specific room. Args: room_id: The room…** (1 connections) — `server/npc/population_control.py`
- **Determine if an NPC should spawn based on conditions. Args: definition: NPC…** (1 connections) — `server/npc/population_control.py`
- **After lifecycle_manager.spawn_npc succeeds, update zone aggregates and log.…** (1 connections) — `server/npc/population_control.py`
- **Spawn an NPC instance using the lifecycle manager. Args: definition: NPC…** (1 connections) — `server/npc/population_control.py`
- **Spawn an NPC instance using the population controller. This is the public API…** (1 connections) — `server/npc/population_control.py`

## Relationships

- [NPC Behavior & Spawning](NPC_Behavior_&_Spawning.md) (10 shared connections)
- [Test Npc Utils](Test_Npc_Utils.md) (3 shared connections)
- [Test Zone Config Loader](Test_Zone_Config_Loader.md) (3 shared connections)
- [NPC Models](NPC_Models.md) (3 shared connections)
- [Test Population Stats](Test_Population_Stats.md) (2 shared connections)
- [Test Player Event Handlers Room](Test_Player_Event_Handlers_Room.md) (1 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (1 shared connections)

## Source Files

- `server/npc/population_control.py`

## Audit Trail

- EXTRACTED: 44 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*