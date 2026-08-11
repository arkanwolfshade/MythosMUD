# E 2 E Testing Guide

> 7 nodes

## Key Concepts

- **_filter_container_data()** (8 connections) — `server/services/wearable_container_service.py`
- **.get_wearable_containers_for_player()** (5 connections) — `server/services/wearable_container_service.py`
- **test_filter_container_data()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **ContainerComponent** (2 connections)
- **Filter out database-only fields from container data before validation.      The** (1 connections) — `server/services/wearable_container_service.py`
- **Get all wearable containers for a player.          Args:             player_id:** (1 connections) — `server/services/wearable_container_service.py`
- **Test _filter_container_data filters database-only fields.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`

## Relationships

- [Schedule Service Loader](Schedule_Service_Loader.md) (6 shared connections)
- [Exploration Command Factories](Exploration_Command_Factories.md) (2 shared connections)
- [Structured Concurrency Patterns](Structured_Concurrency_Patterns.md) (1 shared connections)

## Source Files

- `server/services/wearable_container_service.py`
- `server/tests/unit/services/test_wearable_container_service.py`

## Audit Trail

- EXTRACTED: 21 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*