# _EventBusPublishPort

> 5 nodes

## Key Concepts

- **_EventBusPublishPort** (6 connections) — `server/realtime/event_handlers.py`
- **.publish()** (2 connections) — `server/realtime/event_handlers.py`
- **Protocol** (1 connections)
- **Minimal surface for publishing domain events from ConnectionManager.event_bus.** (1 connections) — `server/realtime/event_handlers.py`
- **Publish a single event to the in-process bus.** (1 connections) — `server/realtime/event_handlers.py`

## Relationships

- [get_logger](get_logger.md) (1 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)

## Source Files

- `server/realtime/event_handlers.py`

## Audit Trail

- EXTRACTED: 5 (71%)
- INFERRED: 2 (29%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*