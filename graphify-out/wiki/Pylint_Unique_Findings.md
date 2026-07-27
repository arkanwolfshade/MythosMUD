# Pylint Unique Findings

> 14 nodes · cohesion 0.13

## Key Concepts

- **CreateItemInstanceInput** (14 connections) — `server/async_persistence_constants.py`
- **datetime** (6 connections) — `server/async_persistence.py`
- **Profession** (5 connections) — `server/async_persistence.py`
- **.get_decayed_containers()** (4 connections) — `server/async_persistence.py`
- **.update_player_last_active()** (4 connections) — `server/async_persistence.py`
- **.create_item_instance()** (3 connections) — `server/async_persistence.py`
- **.get_profession_by_id()** (3 connections) — `server/async_persistence.py`
- **async_persistence_constants.py** (3 connections) — `server/async_persistence_constants.py`
- **Constants and shared types for async persistence layer.  Extracted to keep async** (1 connections) — `server/async_persistence_constants.py`
- **Optional fields for create_item_instance. owner_type, owner_id, etc. with defaul** (1 connections) — `server/async_persistence_constants.py`
- **Update the last_active timestamp for a player. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Get a profession by ID. Delegates to ProfessionRepository.** (1 connections) — `server/async_persistence.py`
- **Get decayed containers.** (1 connections) — `server/async_persistence.py`
- **Create a new item instance. Delegates to ItemRepository.** (1 connections) — `server/async_persistence.py`

## Relationships

- [Combat Command Handler](Combat_Command_Handler.md) (5 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (3 shared connections)
- [Death Delirium UI Modals](Death_Delirium_UI_Modals.md) (2 shared connections)
- [End-to-End Validation](End-to-End_Validation.md) (2 shared connections)
- [Async Persistence Types](Async_Persistence_Types.md) (2 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (2 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (1 shared connections)
- [Room Subscription Helpers](Room_Subscription_Helpers.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_constants.py`

## Audit Trail

- EXTRACTED: 32 (67%)
- INFERRED: 16 (33%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*