# ApplicationContainer

> 191 nodes

## Key Concepts

- **ApplicationContainer** (145 connections) — `server/container/main.py`
- **.get_instance()** (34 connections) — `server/container/main.py`
- **container/main.py** (33 connections) — `server/container/main.py`
- **test_application_container.py** (28 connections) — `server/tests/unit/test_application_container.py`
- **RealtimeBundle** (24 connections) — `server/container/bundles/realtime.py`
- **EventPublisher** (20 connections) — `server/realtime/event_publisher.py`
- **bundles/__init__.py** (19 connections) — `server/container/bundles/__init__.py`
- **core.py** (18 connections) — `server/container/bundles/core.py`
- **get_container()** (17 connections) — `server/container/main.py`
- **TrackedTaskManager** (14 connections) — `server/app/tracked_task_manager.py`
- **CoreBundle** (14 connections) — `server/container/bundles/core.py`
- **MonitoringBundle** (13 connections) — `server/container/bundles/monitoring.py`
- **bundles/realtime.py** (13 connections) — `server/container/bundles/realtime.py`
- **DistributedEventBus** (12 connections) — `server/events/distributed_event_bus.py`
- **.initialize()** (12 connections) — `server/container/bundles/core.py`
- **bundles/monitoring.py** (11 connections) — `server/container/bundles/monitoring.py`
- **._initialize_primary_bundles()** (10 connections) — `server/container/main.py`
- **test_realtime_bundle_nats.py** (10 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **TimeBundle** (8 connections) — `server/container/bundles/time.py`
- **.initialize()** (8 connections) — `server/container/bundles/realtime.py`
- **reset_container()** (8 connections) — `server/container/main.py`
- **chat.py** (8 connections) — `server/container/bundles/chat.py`
- **utils.py** (8 connections) — `server/container/utils.py`
- **ChatBundle** (7 connections) — `server/container/bundles/chat.py`
- **.initialize()** (7 connections) — `server/container/bundles/monitoring.py`
- *... and 166 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (26 shared connections)
- [magic_service.py](magic_service.py.md) (19 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (19 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (15 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (12 shared connections)
- [GameBundle](GameBundle.md) (12 shared connections)
- [bundles/game.py](bundles-game.py.md) (11 shared connections)
- [time.py](time.py.md) (7 shared connections)
- [TaskRegistry](TaskRegistry.md) (6 shared connections)
- [EventBus](EventBus.md) (6 shared connections)
- [.get_instance](get_instance.md) (5 shared connections)
- [._connect_nats](_connect_nats.md) (5 shared connections)

## Source Files

- `server/app/tracked_task_manager.py`
- `server/container/__init__.py`
- `server/container/bundles/__init__.py`
- `server/container/bundles/chat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/realtime.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/events/distributed_event_bus.py`
- `server/realtime/event_publisher.py`
- `server/tests/unit/container/test_realtime_bundle_nats.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 533 (94%)
- INFERRED: 33 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*