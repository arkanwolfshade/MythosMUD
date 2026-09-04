# Event Handlers

> 11 nodes

## Key Concepts

- **_npc_died_broadcast_and_bridge()** (8 connections) — `server/realtime/event_handlers.py`
- **_publish_npc_died_to_event_bus()** (6 connections) — `server/realtime/event_handlers.py`
- **_refresh_room_after_npc_death()** (6 connections) — `server/realtime/event_handlers.py`
- **ConnectionManager** (5 connections)
- **.handle_npc_died_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.__init__()** (3 connections) — `server/realtime/event_handlers.py`
- **Publish NPCDied to the in-process EventBus when configured on ConnectionManager.** (1 connections) — `server/realtime/event_handlers.py`
- **Best-effort room occupants refresh after NPC death.** (1 connections) — `server/realtime/event_handlers.py`
- **Broadcast npc_died to WebSocket, publish NPCDied to EventBus, refresh room…** (1 connections) — `server/realtime/event_handlers.py`
- **Initialize event handler. Args: connection_manager: ConnectionManager instance…** (1 connections) — `server/realtime/event_handlers.py`
- **Handle npc_died event - NATS to EventBus bridge pattern. ARCHITECTURE NOTE -…** (1 connections) — `server/realtime/event_handlers.py`

## Relationships

- [Event Handlers](Event_Handlers.md) (4 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (3 shared connections)
- [Connection Manager](Connection_Manager.md) (3 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (1 shared connections)
- [Test Websocket Room Updates](Test_Websocket_Room_Updates.md) (1 shared connections)

## Source Files

- `server/realtime/event_handlers.py`

## Audit Trail

- EXTRACTED: 21 (88%)
- INFERRED: 3 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*