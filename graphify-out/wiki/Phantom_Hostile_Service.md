# Phantom Hostile Service

> 34 nodes

## Key Concepts

- **PhantomHostileService** (18 connections) — `server/services/phantom_hostile_service.py`
- **UUID** (6 connections)
- **.create_phantom_hostile_data()** (5 connections) — `server/services/phantom_hostile_service.py`
- **.find_phantom_by_name_in_room()** (5 connections) — `server/services/phantom_hostile_service.py`
- **.get_active_phantoms()** (4 connections) — `server/services/phantom_hostile_service.py`
- **.clear_all_phantoms()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.generate_phantom_name()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.get_phantom_data()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.remove_phantom()** (3 connections) — `server/services/phantom_hostile_service.py`
- **test_phantom_create_track_remove_clear()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_phantom_generate_name()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_phantom_get_data_and_find_by_name_in_room()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_phantom_remove_clears_phantom_data()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_phantom_should_spawn_deranged()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_phantom_should_spawn_fractured()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **Any** (3 connections)
- **.__init__()** (2 connections) — `server/services/phantom_hostile_service.py`
- **.should_spawn_phantom_hostile()** (2 connections) — `server/services/phantom_hostile_service.py`
- **Return the full data dict for one phantom, or None if it's gone (#625).** (1 connections) — `server/services/phantom_hostile_service.py`
- **Find one of the player's active phantoms by (case-insensitive) name, scoped to…** (1 connections) — `server/services/phantom_hostile_service.py`
- **Remove a phantom hostile from tracking. Args: player_id: Player UUID…** (1 connections) — `server/services/phantom_hostile_service.py`
- **Get list of active phantom IDs for a player. Args: player_id: Player UUID…** (1 connections) — `server/services/phantom_hostile_service.py`
- **Clear all phantom hostiles for a player. Args: player_id: Player UUID** (1 connections) — `server/services/phantom_hostile_service.py`
- **Service for managing phantom hostile spawns for hallucinations. NOTE: This is a…** (1 connections) — `server/services/phantom_hostile_service.py`
- **Initialize the phantom hostile service.** (1 connections) — `server/services/phantom_hostile_service.py`
- *... and 9 more nodes in this community*

## Relationships

- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (9 shared connections)

## Source Files

- `server/services/phantom_hostile_service.py`
- `server/tests/unit/services/test_hallucination_services.py`

## Audit Trail

- EXTRACTED: 50 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*