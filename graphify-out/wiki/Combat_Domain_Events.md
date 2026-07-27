# Combat Domain Events

> 351 nodes · cohesion 0.01

## Key Concepts

- **NATSService** (93 connections) — `server/services/nats_service.py`
- **NATSError** (90 connections) — `server/services/nats_exceptions.py`
- **test_nats_service.py** (71 connections) — `server/tests/unit/services/test_nats_service.py`
- **NATSPublishError** (45 connections) — `server/services/nats_exceptions.py`
- **NATSMetrics** (36 connections) — `server/services/nats_metrics.py`
- **NATSSubscribeError** (31 connections) — `server/services/nats_exceptions.py`
- **Exception** (22 connections)
- **Any** (22 connections) — `server/services/nats_service.py`
- **nats_service.py** (20 connections) — `server/services/nats_service.py`
- **NATSConnectionError** (18 connections) — `server/services/nats_exceptions.py`
- **NATSHealthCheckError** (17 connections) — `server/services/nats_exceptions.py`
- **NATSUnsubscribeError** (16 connections) — `server/services/nats_exceptions.py`
- **nats_exceptions.py** (15 connections) — `server/services/nats_exceptions.py`
- **NATSRequestError** (14 connections) — `server/services/nats_exceptions.py`
- **test_nats_exceptions.py** (12 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **._create_event_message()** (11 connections) — `server/services/combat_event_publisher.py`
- **.disconnect()** (11 connections) — `server/services/nats_service.py`
- **TestExceptionHierarchy** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSConnectionError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSHealthCheckError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSPublishError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSSubscribeError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.publish_with_pool()** (10 connections) — `server/services/nats_service.py`
- **NATS** (9 connections) — `server/services/nats_service.py`
- **._create_tracked_task()** (9 connections) — `server/services/nats_service.py`
- *... and 326 more nodes in this community*

## Relationships

- [[Combat Service Bundle]] (52 shared connections)
- [[NATS Message Handler Tests]] (15 shared connections)
- [[NPC Admin API]] (13 shared connections)
- [[Realtime Nats Message]] (10 shared connections)
- [[Combat Aggro Threat]] (9 shared connections)
- [[Combat Death Handling]] (6 shared connections)
- [[Combat Attack Service]] (6 shared connections)
- [[Realtime Service Bundle]] (5 shared connections)
- [[NATS Message Broker]] (4 shared connections)
- [[Services Combat Persistence]] (3 shared connections)
- [[NATS Connection State Machine]] (3 shared connections)
- [[NATS Subject Manager]] (3 shared connections)

## Source Files

- `server/domain/exceptions/__init__.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/nats_exceptions.py`
- `server/services/nats_metrics.py`
- `server/services/nats_service.py`
- `server/tests/unit/realtime/test_nats_message_handler.py`
- `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- `server/tests/unit/services/test_nats_exceptions.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 1103 (83%)
- INFERRED: 228 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
