# Any

> 11 nodes

## Key Concepts

- **Any** (7 connections)
- **.get_event_bus()** (4 connections) — `server/realtime/request_context.py`
- **.get_persistence()** (3 connections) — `server/realtime/request_context.py`
- **.__init__()** (3 connections) — `server/realtime/request_context.py`
- **.set_alias_storage()** (3 connections) — `server/realtime/request_context.py`
- **.set_app_state_services()** (3 connections) — `server/realtime/request_context.py`
- **Get the event bus from the request context.** (1 connections) — `server/realtime/request_context.py`
- **Initialize the WebSocket request context. Args: app_state: Real application…** (1 connections) — `server/realtime/request_context.py`
- **Set the alias storage in the app state. Args: alias_storage: Alias storage…** (1 connections) — `server/realtime/request_context.py`
- **Set the app state services in the request context. Note: This method is kept…** (1 connections) — `server/realtime/request_context.py`
- **Get the persistence layer from the request context.** (1 connections) — `server/realtime/request_context.py`

## Relationships

- [get_logger](get_logger.md) (5 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [.state](state.md) (1 shared connections)
- [Alias](Alias.md) (1 shared connections)

## Source Files

- `server/realtime/request_context.py`

## Audit Trail

- EXTRACTED: 17 (94%)
- INFERRED: 1 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*