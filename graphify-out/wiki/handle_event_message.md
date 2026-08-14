# .handle_event_message

> 6 nodes

## Key Concepts

- **.handle_event_message()** (5 connections) — `server/realtime/event_handlers.py`
- **.get_event_handler_map()** (3 connections) — `server/realtime/event_handlers.py`
- **.validate_event_message()** (3 connections) — `server/realtime/event_handlers.py`
- **Get mapping of event types to their handler methods. Returns: Dictionary…** (1 connections) — `server/realtime/event_handlers.py`
- **Validate that event message has required fields. Args: event_type: Event type…** (1 connections) — `server/realtime/event_handlers.py`
- **Handle incoming event messages from NATS. Args: message_data: Event message…** (1 connections) — `server/realtime/event_handlers.py`

## Relationships

- [EventHandler](EventHandler.md) (3 shared connections)
- [_as_event_data_dict](_as_event_data_dict.md) (1 shared connections)

## Source Files

- `server/realtime/event_handlers.py`

## Audit Trail

- EXTRACTED: 9 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*