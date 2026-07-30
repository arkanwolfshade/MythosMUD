# test command parser

> 300 nodes

## Key Concepts

- **ApplicationContainer** (139 connections) — `server/container/main.py`
- **TaskRegistry** (33 connections) — `server/app/task_registry.py`
- **main.py** (33 connections) — `server/container/main.py`
- **test_application_container.py** (26 connections) — `server/tests/unit/test_application_container.py`
- **EventPublisher** (23 connections) — `server/realtime/event_publisher.py`
- **__init__.py** (19 connections) — `server/container/bundles/__init__.py`
- **CombatBundle** (19 connections) — `server/container/bundles/combat.py`
- **get_global_tracked_manager()** (18 connections) — `server/app/tracked_task_manager.py`
- **core.py** (18 connections) — `server/container/bundles/core.py`
- **RealtimeBundle** (17 connections) — `server/container/bundles/realtime.py`
- **get_container()** (17 connections) — `server/container/main.py`
- **tracked_task_manager.py** (14 connections) — `server/app/tracked_task_manager.py`
- **TrackedTaskManager** (14 connections) — `server/app/tracked_task_manager.py`
- **CoreBundle** (14 connections) — `server/container/bundles/core.py`
- **combat.py** (13 connections) — `server/container/bundles/combat.py`
- **MonitoringBundle** (13 connections) — `server/container/bundles/monitoring.py`
- **.initialize()** (12 connections) — `server/container/bundles/core.py`
- **realtime.py** (12 connections) — `server/container/bundles/realtime.py`
- **.initialize()** (12 connections) — `server/container/main.py`
- **DistributedEventBus** (12 connections) — `server/events/distributed_event_bus.py`
- **monitoring.py** (11 connections) — `server/container/bundles/monitoring.py`
- **NPCBundle** (11 connections) — `server/container/bundles/npc.py`
- **memory_cleanup_service.py** (10 connections) — `server/app/memory_cleanup_service.py`
- **MemoryThresholdMonitor** (10 connections) — `server/app/memory_cleanup_service.py`
- **memory_lifespan_coordinator.py** (10 connections) — `server/app/memory_lifespan_coordinator.py`
- *... and 275 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (73 shared connections)
- [Any](Any.md) (26 shared connections)
- [message handler factory](message_handler_factory.md) (19 shared connections)
- [emit close container event()](emit_close_container_event%28%29.md) (15 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (12 shared connections)
- [Player](Player.md) (9 shared connections)
- [. init ()](_init_%28%29.md) (8 shared connections)
- [.shutdown()](shutdown%28%29.md) (7 shared connections)
- [UUID](UUID.md) (6 shared connections)
- [Formatter](Formatter.md) (6 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (5 shared connections)
- [event publisher()](event_publisher%28%29.md) (5 shared connections)

## Source Files

- `server/app/memory_cleanup_service.py`
- `server/app/memory_lifespan_coordinator.py`
- `server/app/task_registry.py`
- `server/app/tracked_task_manager.py`
- `server/container/__init__.py`
- `server/container/bundles/__init__.py`
- `server/container/bundles/chat.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/npc.py`
- `server/container/bundles/realtime.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/events/distributed_event_bus.py`
- `server/realtime/event_publisher.py`
- `server/services/game_tick_service.py`
- `server/tests/fixtures/unit/__init__.py`
- `server/tests/unit/realtime/test_event_publisher_helpers.py`

## Audit Trail

- EXTRACTED: 1137 (95%)
- INFERRED: 65 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*