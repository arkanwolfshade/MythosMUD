# E2E Whisper Fix Report

> 21 nodes · cohesion 0.12

## Key Concepts

- **CorpseLifecycleService** (23 connections) — `server/services/corpse_lifecycle_service.py`
- **.get_decayed_corpses_in_room()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **.get_all_decayed_corpses()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **ContainerComponent** (5 connections)
- **.can_access_corpse()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_all_decayed_corpses()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_decayed_corpses_in_room()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.is_corpse_decayed()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.__init__()** (3 connections) — `server/services/corpse_lifecycle_service.py`
- **corpse_service()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_corpse_lifecycle_service_init_no_persistence()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **Check if a player can access a corpse container.          During grace period, o** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Check if a corpse container has decayed.          Args:             corpse: Corp** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Get all decayed corpse containers in a room.          Args:             room_id:** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Clean up all decayed corpse containers in a room.          Args:             roo** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Get all decayed corpse containers across all rooms.          Returns:** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Clean up all decayed corpse containers across all rooms.          Returns:** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Service for managing corpse container lifecycle.      Handles creation on death,** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Initialize the corpse lifecycle service.          Args:             persistence:** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Create a CorpseLifecycleService instance.** (1 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **Test CorpseLifecycleService initialization fails without persistence.** (1 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Relationships

- [Combat Death Handling](Combat_Death_Handling.md) (12 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (5 shared connections)
- [Game Tick Processing](Game_Tick_Processing.md) (2 shared connections)
- [Archive Circuit Breaker](Archive_Circuit_Breaker.md) (1 shared connections)
- [App Lifespan Management](App_Lifespan_Management.md) (1 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (1 shared connections)

## Source Files

- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 70 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*