# Server Services (2)

> 194 nodes

## Key Concepts

- **test_nats_service.py** (76 connections) — `server/tests/unit/services/test_nats_service.py`
- **NATSService** (71 connections) — `server/services/nats_service.py`
- **NATSMetrics** (31 connections) — `server/services/nats_metrics.py`
- **nats_service.py** (23 connections) — `server/services/nats_service.py`
- **NATSConfig** (22 connections) — `server/config/models/nats.py`
- **NATSRequestError** (11 connections) — `server/services/nats_exceptions.py`
- **.disconnect()** (11 connections) — `server/services/nats_service.py`
- **NATSUnsubscribeError** (10 connections) — `server/services/nats_exceptions.py`
- **.__init__()** (7 connections) — `server/services/nats_service.py`
- **._verify_subscription_cleanup()** (6 connections) — `server/services/nats_service.py`
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_with_config()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **nats_metrics.py** (4 connections) — `server/services/nats_metrics.py`
- **._close_all_subscriptions()** (4 connections) — `server/services/nats_service.py`
- **.unsubscribe()** (4 connections) — `server/services/nats_service.py`
- **.request()** (4 connections) — `server/services/nats_service.py`
- **._on_disconnect()** (4 connections) — `server/services/nats_service.py`
- **._handle_disconnect_async()** (4 connections) — `server/services/nats_service.py`
- **test_nats_service_init_with_dict()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_with_none()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_with_subject_manager()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **.validate_tls_files()** (3 connections) — `server/config/models/nats.py`
- **.validate_tls_config()** (3 connections) — `server/config/models/nats.py`
- **.get_metrics()** (3 connections) — `server/services/nats_metrics.py`
- **._drain_subscriptions()** (3 connections) — `server/services/nats_service.py`
- *... and 169 more nodes in this community*

## Relationships

- [Server Services (31)](Server_Services_%2831%29.md) (35 shared connections)
- [Server Services (5)](Server_Services_%285%29.md) (18 shared connections)
- [Server Config](Server_Config.md) (6 shared connections)
- [Server Realtime (10)](Server_Realtime_%2810%29.md) (6 shared connections)
- [Server Infrastructure (3)](Server_Infrastructure_%283%29.md) (5 shared connections)
- [Server Commands](Server_Commands.md) (4 shared connections)
- [Server Services (3)](Server_Services_%283%29.md) (4 shared connections)
- [Server Events (3)](Server_Events_%283%29.md) (3 shared connections)
- [Server Services (17)](Server_Services_%2817%29.md) (3 shared connections)
- [Server Realtime (16)](Server_Realtime_%2816%29.md) (3 shared connections)
- [Server Realtime](Server_Realtime.md) (2 shared connections)
- [Server Services (29)](Server_Services_%2829%29.md) (2 shared connections)

## Source Files

- `server/config/models/nats.py`
- `server/services/nats_exceptions.py`
- `server/services/nats_metrics.py`
- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 570 (94%)
- INFERRED: 35 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*