# bundles/game.py

> 146 nodes

## Key Concepts

- **bundles/game.py** (42 connections) — `server/container/bundles/game.py`
- **container/main.py** (33 connections) — `server/container/main.py`
- **test_application_container.py** (28 connections) — `server/tests/unit/test_application_container.py`
- **RealtimeBundle** (24 connections) — `server/container/bundles/realtime.py`
- **bundles/__init__.py** (19 connections) — `server/container/bundles/__init__.py`
- **core.py** (18 connections) — `server/container/bundles/core.py`
- **get_container()** (17 connections) — `server/container/main.py`
- **normalize_environment()** (15 connections) — `server/utils/project_paths.py`
- **CoreBundle** (14 connections) — `server/container/bundles/core.py`
- **get_calendar_paths_for_environment()** (14 connections) — `server/utils/project_paths.py`
- **MonitoringBundle** (13 connections) — `server/container/bundles/monitoring.py`
- **bundles/realtime.py** (13 connections) — `server/container/bundles/realtime.py`
- **DistributedEventBus** (12 connections) — `server/events/distributed_event_bus.py`
- **.initialize()** (12 connections) — `server/container/bundles/core.py`
- **project_paths.py** (12 connections) — `server/utils/project_paths.py`
- **bundles/monitoring.py** (11 connections) — `server/container/bundles/monitoring.py`
- **._initialize_primary_bundles()** (10 connections) — `server/container/main.py`
- **get_environment_data_dir()** (10 connections) — `server/utils/project_paths.py`
- **get_project_root()** (10 connections) — `server/utils/project_paths.py`
- **test_realtime_bundle_nats.py** (10 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **test_project_paths.py** (10 connections) — `server/tests/unit/utils/test_project_paths.py`
- **TimeBundle** (8 connections) — `server/container/bundles/time.py`
- **.initialize()** (8 connections) — `server/container/bundles/realtime.py`
- **reset_container()** (8 connections) — `server/container/main.py`
- **chat.py** (8 connections) — `server/container/bundles/chat.py`
- *... and 121 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (51 shared connections)
- [get_logger](get_logger.md) (37 shared connections)
- [GameBundle](GameBundle.md) (13 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (10 shared connections)
- [validate_calendar.py](validate_calendar.py.md) (7 shared connections)
- [magic_service.py](magic_service.py.md) (5 shared connections)
- [DatabaseError](DatabaseError.md) (4 shared connections)
- [ChatService](ChatService.md) (3 shared connections)
- [TaskRegistry](TaskRegistry.md) (3 shared connections)
- [TrackedTaskManager](TrackedTaskManager.md) (3 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (3 shared connections)
- [EventPublisher](EventPublisher.md) (3 shared connections)

## Source Files

- `server/container/__init__.py`
- `server/container/bundles/__init__.py`
- `server/container/bundles/chat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/game.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/realtime.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/events/distributed_event_bus.py`
- `server/services/schedule_service.py`
- `server/tests/unit/container/test_realtime_bundle_nats.py`
- `server/tests/unit/test_application_container.py`
- `server/tests/unit/utils/test_project_paths.py`
- `server/utils/project_paths.py`

## Audit Trail

- EXTRACTED: 628 (96%)
- INFERRED: 28 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*