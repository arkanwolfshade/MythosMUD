# Spawning Service

> 15 nodes

## Key Concepts

- **._evaluate_spawn_requirements()** (8 connections) — `server/npc/spawning_service.py`
- **._evaluate_spawn_rules()** (7 connections) — `server/npc/spawning_service.py`
- **._calculate_spawn_priority()** (6 connections) — `server/npc/spawning_service.py`
- **._maybe_add_required_npc_request()** (6 connections) — `server/npc/spawning_service.py`
- **._check_spawn_requirements_for_room()** (5 connections) — `server/npc/spawning_service.py`
- **NPCSpawnRequest** (5 connections)
- **._handle_player_entered_room()** (4 connections) — `server/npc/spawning_service.py`
- **._queue_spawn_request()** (4 connections) — `server/npc/spawning_service.py`
- **Handle player entering a room - trigger spawn checks.** (1 connections) — `server/npc/spawning_service.py`
- **Check if NPCs need to be spawned for a specific room. Args: room_id: The room…** (1 connections) — `server/npc/spawning_service.py`
- **Evaluate spawn rules for a definition and return requests that pass conditions…** (1 connections) — `server/npc/spawning_service.py`
- **If definition is required and not yet represented, append a required spawn…** (1 connections) — `server/npc/spawning_service.py`
- **Evaluate spawn requirements for an NPC definition. Args: definition: NPC…** (1 connections) — `server/npc/spawning_service.py`
- **Calculate spawn priority for an NPC. Args: definition: NPC definition rule:…** (1 connections) — `server/npc/spawning_service.py`
- **Queue a spawn request for processing. Args: request: Spawn request to queue** (1 connections) — `server/npc/spawning_service.py`

## Relationships

- [NPC Behavior & Spawning](NPC_Behavior_&_Spawning.md) (8 shared connections)
- [NPC Models](NPC_Models.md) (5 shared connections)
- [Test Zone Config Loader](Test_Zone_Config_Loader.md) (3 shared connections)
- [Test Player Event Handlers Room](Test_Player_Event_Handlers_Room.md) (1 shared connections)
- [Test Population Stats](Test_Population_Stats.md) (1 shared connections)

## Source Files

- `server/npc/spawning_service.py`

## Audit Trail

- EXTRACTED: 35 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*