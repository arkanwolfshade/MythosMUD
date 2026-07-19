# Time Event Consumer

> 22 nodes · cohesion 0.14

## Key Concepts

- **ChronicleLike** (26 connections) — `server/time/time_service.py`
- **MythosTimeEventConsumer** (21 connections) — `server/time/time_event_consumer.py`
- **MythosHourTickEvent** (10 connections) — `server/time/time_event_consumer.py`
- **Any** (10 connections) — `server/time/time_event_consumer.py`
- **HolidayService** (9 connections) — `server/time/time_event_consumer.py`
- **ScheduleService** (9 connections) — `server/time/time_event_consumer.py`
- **ChronicleLike** (9 connections) — `server/time/time_event_consumer.py`
- **EventBus** (9 connections) — `server/time/time_event_consumer.py`
- **NPCLifecycleManager** (9 connections) — `server/time/time_event_consumer.py`
- **RoomService** (9 connections) — `server/time/time_event_consumer.py`
- **.__init__()** (7 connections) — `server/time/time_event_consumer.py`
- **.initialize()** (5 connections) — `server/container/bundles/time.py`
- **._build_broadcast_payload()** (5 connections) — `server/time/time_event_consumer.py`
- **._handle_tick()** (5 connections) — `server/time/time_event_consumer.py`
- **ApplicationContainer** (3 connections) — `server/container/bundles/time.py`
- **.describe_state()** (3 connections) — `server/time/time_event_consumer.py`
- **Initialize Mythos time event consumer.** (1 connections) — `server/container/bundles/time.py`
- **Helper for admin diagnostics.** (1 connections) — `server/time/time_event_consumer.py`
- **Create the SSE payload consumed by the client HUD.** (1 connections) — `server/time/time_event_consumer.py`
- **Bridges hour tick events into downstream systems such as NPC schedules and room** (1 connections) — `server/time/time_event_consumer.py`
- **Dispatch hour tick events to each dependent subsystem.** (1 connections) — `server/time/time_event_consumer.py`
- **Minimal chronicle contract required by downstream systems.      The canonical My** (1 connections) — `server/time/time_service.py`

## Relationships

- [[Holiday Persistence Models]] (18 shared connections)
- [[NPC Admin API]] (14 shared connections)
- [[Async Task Registry]] (10 shared connections)
- [[Distributed Event Bus]] (9 shared connections)
- [[Maps API Endpoints]] (9 shared connections)
- [[NPC Death Lifecycle]] (9 shared connections)
- [[Game Service Bundle]] (9 shared connections)
- [[Application DI Bundles]] (4 shared connections)
- [[Lifespan Startup Hooks]] (2 shared connections)
- [[Mythos Calendar Time Service]] (2 shared connections)
- [[Game Tick Processing]] (1 shared connections)
- [[Combat Player Broadcasts]] (1 shared connections)

## Source Files

- `server/container/bundles/time.py`
- `server/time/time_event_consumer.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 61 (39%)
- INFERRED: 94 (61%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
