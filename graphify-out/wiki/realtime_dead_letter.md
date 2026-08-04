# realtime dead letter

> 13 nodes

## Key Concepts

- **_EventBusPublishPort** (7 connections) — `server/realtime/event_handlers.py`
- **_publish_npc_died_to_event_bus()** (7 connections) — `server/realtime/event_handlers.py`
- **_npc_died_broadcast_and_bridge()** (7 connections) — `server/realtime/event_handlers.py`
- **_refresh_room_after_npc_death()** (5 connections) — `server/realtime/event_handlers.py`
- **.publish()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_died_event()** (3 connections) — `server/realtime/event_handlers.py`
- **Protocol** (1 connections)
- **Minimal surface for publishing domain events from ConnectionManager.event_bus.** (1 connections) — `server/realtime/event_handlers.py`
- **Publish a single event to the in-process bus.** (1 connections) — `server/realtime/event_handlers.py`
- **Publish NPCDied to the in-process EventBus when configured on ConnectionManager.** (1 connections) — `server/realtime/event_handlers.py`
- **Best-effort room occupants refresh after NPC death.** (1 connections) — `server/realtime/event_handlers.py`
- **Broadcast npc_died to WebSocket, publish NPCDied to EventBus, refresh room occup** (1 connections) — `server/realtime/event_handlers.py`
- **Handle npc_died event - NATS to EventBus bridge pattern.          ARCHITECTURE** (1 connections) — `server/realtime/event_handlers.py`

## Relationships

- [Room Broadcast](Room_Broadcast.md) (4 shared connections)
- [NPC Combat](NPC_Combat.md) (4 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (2 shared connections)
- [follow game service](follow_game_service.md) (2 shared connections)
- [command models moderation](command_models_moderation.md) (1 shared connections)

## Source Files

- `server/realtime/event_handlers.py`

## Audit Trail

- EXTRACTED: 35 (90%)
- INFERRED: 4 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*