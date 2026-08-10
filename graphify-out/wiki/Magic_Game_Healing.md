# Magic Game Healing

> 6 nodes

## Key Concepts

- **_get_death_location_name()** (4 connections) — `server/realtime/websocket_initial_state.py`
- **.item_instance_exists()** (3 connections) — `server/async_persistence.py`
- **Get the global async persistence instance.      DEPRECATED: Use ApplicationConta** (2 connections) — `server/async_persistence.py`
- **Check if an item instance exists. Delegates to ItemRepository.** (1 connections) — `server/async_persistence.py`
- **Room** (1 connections)
- **Extract death location name from room object or dict.** (1 connections) — `server/realtime/websocket_initial_state.py`

## Relationships

- [WebSocket Initial State](WebSocket_Initial_State.md) (3 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/realtime/websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 12 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*