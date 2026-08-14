# event_handlers.py

> 13 nodes

## Key Concepts

- **event_handlers.py** (24 connections) — `server/realtime/event_handlers.py`
- **_npc_died_broadcast_and_bridge()** (7 connections) — `server/realtime/event_handlers.py`
- **_npc_died_ids_or_warn()** (5 connections) — `server/realtime/event_handlers.py`
- **_publish_npc_died_to_event_bus()** (5 connections) — `server/realtime/event_handlers.py`
- **_refresh_room_after_npc_death()** (5 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_died_event()** (3 connections) — `server/realtime/event_handlers.py`
- **test_npc_died_ids_or_warn_missing_fields()** (2 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **Event handlers for NATS message handler. This module handles all event-type…** (1 connections) — `server/realtime/event_handlers.py`
- **Publish NPCDied to the in-process EventBus when configured on ConnectionManager.** (1 connections) — `server/realtime/event_handlers.py`
- **Best-effort room occupants refresh after NPC death.** (1 connections) — `server/realtime/event_handlers.py`
- **Broadcast npc_died to WebSocket, publish NPCDied to EventBus, refresh room…** (1 connections) — `server/realtime/event_handlers.py`
- **Handle npc_died event - NATS to EventBus bridge pattern. ARCHITECTURE NOTE -…** (1 connections) — `server/realtime/event_handlers.py`
- **Return (room_id, npc_id, npc_name) or None after logging warnings.** (1 connections) — `server/realtime/event_handlers.py`

## Relationships

- [EventHandler](EventHandler.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [ConnectionManager](ConnectionManager.md) (4 shared connections)
- [lifecycle_manager.py](lifecycle_manager.py.md) (2 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [_send_combat_participant_updates](_send_combat_participant_updates.md) (2 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)
- [nats_exceptions.py](nats_exceptions.py.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)
- [_EventBusPublishPort](_EventBusPublishPort.md) (1 shared connections)

## Source Files

- `server/realtime/event_handlers.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`

## Audit Trail

- EXTRACTED: 42 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*