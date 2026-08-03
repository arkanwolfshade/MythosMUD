# message formatters realtime

> 8 nodes

## Key Concepts

- **_npc_died_broadcast_and_bridge()** (7 connections) — `server/realtime/event_handlers.py`
- **_refresh_room_after_npc_death()** (5 connections) — `server/realtime/event_handlers.py`
- **_npc_died_ids_or_warn()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_died_event()** (3 connections) — `server/realtime/event_handlers.py`
- **Return (room_id, npc_id, npc_name) or None after logging warnings.** (1 connections) — `server/realtime/event_handlers.py`
- **Best-effort room occupants refresh after NPC death.** (1 connections) — `server/realtime/event_handlers.py`
- **Broadcast npc_died to WebSocket, publish NPCDied to EventBus, refresh room occup** (1 connections) — `server/realtime/event_handlers.py`
- **Handle npc_died event - NATS to EventBus bridge pattern.          ARCHITECTURE** (1 connections) — `server/realtime/event_handlers.py`

## Relationships

- [NATS Messaging](NATS_Messaging.md) (4 shared connections)
- [Room Broadcast](Room_Broadcast.md) (2 shared connections)
- [room websocket updates](room_websocket_updates.md) (1 shared connections)
- [realtime message filtering](realtime_message_filtering.md) (1 shared connections)

## Source Files

- `server/realtime/event_handlers.py`

## Audit Trail

- EXTRACTED: 22 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*