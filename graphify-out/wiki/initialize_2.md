# .initialize

> 14 nodes

## Key Concepts

- **.initialize()** (8 connections) — `server/container/bundles/realtime.py`
- **._connect_nats()** (7 connections) — `server/container/bundles/realtime.py`
- **._setup_nats_dependent_services()** (7 connections) — `server/container/bundles/realtime.py`
- **._handle_nats_connect_error()** (5 connections) — `server/container/bundles/realtime.py`
- **._handle_nats_connect_false()** (4 connections) — `server/container/bundles/realtime.py`
- **._raise_if_e2e_nats_required()** (4 connections) — `server/container/bundles/realtime.py`
- **Any** (2 connections)
- **BaseException** (1 connections)
- **Attach event publisher and message handler when NATS is available.** (1 connections) — `server/container/bundles/realtime.py`
- **Initialize real-time services. Requires CoreBundle attributes on container.** (1 connections) — `server/container/bundles/realtime.py`
- **Raise RuntimeError when e2e requires live NATS; no-op for other environments.** (1 connections) — `server/container/bundles/realtime.py`
- **Convert connect failures into hard error (e2e) or soft log (other envs).** (1 connections) — `server/container/bundles/realtime.py`
- **Handle connect() returning False; raise for e2e, soft-warn otherwise.** (1 connections) — `server/container/bundles/realtime.py`
- **Connect to NATS if enabled and not unit_test. Returns NATSService or None.…** (1 connections) — `server/container/bundles/realtime.py`

## Relationships

- [test_container_bundles.py](test_container_bundles.py.md) (7 shared connections)
- [NATSService](NATSService.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [EventPublisher](EventPublisher.md) (1 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (1 shared connections)
- [test_manager.py](test_manager.py.md) (1 shared connections)

## Source Files

- `server/container/bundles/realtime.py`

## Audit Trail

- EXTRACTED: 28 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*