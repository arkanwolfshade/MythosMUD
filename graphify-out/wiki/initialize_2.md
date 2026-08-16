# .initialize

> 18 nodes

## Key Concepts

- **.initialize()** (8 connections) — `server/container/bundles/realtime.py`
- **.initialize()** (7 connections) — `server/container/bundles/chat.py`
- **._connect_nats()** (7 connections) — `server/container/bundles/realtime.py`
- **subject_manager()** (7 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **._setup_nats_dependent_services()** (6 connections) — `server/container/bundles/realtime.py`
- **._handle_nats_connect_error()** (5 connections) — `server/container/bundles/realtime.py`
- **._handle_nats_connect_false()** (4 connections) — `server/container/bundles/realtime.py`
- **._raise_if_e2e_nats_required()** (4 connections) — `server/container/bundles/realtime.py`
- **Any** (1 connections)
- **BaseException** (1 connections)
- **Initialize chat service.** (1 connections) — `server/container/bundles/chat.py`
- **Attach event publisher and message handler when NATS is available.** (1 connections) — `server/container/bundles/realtime.py`
- **Initialize real-time services. Requires CoreBundle attributes on container.** (1 connections) — `server/container/bundles/realtime.py`
- **Raise RuntimeError when e2e requires live NATS; no-op for other environments.** (1 connections) — `server/container/bundles/realtime.py`
- **Convert connect failures into hard error (e2e) or soft log (other envs).** (1 connections) — `server/container/bundles/realtime.py`
- **Handle connect() returning False; raise for e2e, soft-warn otherwise.** (1 connections) — `server/container/bundles/realtime.py`
- **Connect to NATS if enabled and not unit_test. Returns NATSService or None.…** (1 connections) — `server/container/bundles/realtime.py`
- **Create NATSSubjectManager instance.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`

## Relationships

- [test_container_bundles.py](test_container_bundles.py.md) (8 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [test_manager.py](test_manager.py.md) (2 shared connections)
- [ChatService](ChatService.md) (1 shared connections)
- [NATSService](NATSService.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (1 shared connections)
- [EventPublisher](EventPublisher.md) (1 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (1 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (1 shared connections)
- [test_lifespan_startup.py](test_lifespan_startup.py.md) (1 shared connections)

## Source Files

- `server/container/bundles/chat.py`
- `server/container/bundles/realtime.py`
- `server/tests/unit/services/nats_subject_manager/test_manager.py`

## Audit Trail

- EXTRACTED: 36 (90%)
- INFERRED: 4 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*