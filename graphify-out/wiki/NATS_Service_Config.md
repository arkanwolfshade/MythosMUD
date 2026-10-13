# NATS Service Config

> 146 nodes

## Key Concepts

- **NATSService** (154 connections) — `server/services/nats_service.py`
- **test_nats_service_helpers.py** (59 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **NATSConfig** (26 connections) — `server/config/models/nats.py`
- **asyncio** (26 connections)
- **._create_tracked_task()** (7 connections) — `server/services/nats_service.py`
- **_mock_create_tracked_task()** (7 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **.connect()** (6 connections) — `server/services/nats_service.py`
- **_assert_tracked_coro_closed()** (6 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_start_health_monitoring_creates_task()** (6 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_nats_service_init_with_config()** (6 connections) — `server/tests/unit/services/test_nats_service.py`
- **.disconnect()** (5 connections) — `server/services/nats_service.py`
- **._on_error()** (5 connections) — `server/services/nats_service.py`
- **._start_health_monitoring()** (5 connections) — `server/services/nats_service.py`
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_nats_service_init_with_subject_manager()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **.validate_tls_files()** (4 connections) — `server/config/models/nats.py`
- **._cancel_background_tasks()** (4 connections) — `server/services/nats_service.py`
- **._force_cancel_pending_tasks()** (4 connections) — `server/services/nats_service.py`
- **.get_connection_stats()** (4 connections) — `server/services/nats_service.py`
- **._handle_error_async()** (4 connections) — `server/services/nats_service.py`
- **._health_check_loop()** (4 connections) — `server/services/nats_service.py`
- **.__init__()** (4 connections) — `server/services/nats_service.py`
- **._on_disconnect()** (4 connections) — `server/services/nats_service.py`
- **._on_reconnect()** (4 connections) — `server/services/nats_service.py`
- *... and 121 more nodes in this community*

## Relationships

- [Community 63](Community_63.md) (43 shared connections)
- [Community 475](Community_475.md) (17 shared connections)
- [Community 96](Community_96.md) (16 shared connections)
- [Community 69](Community_69.md) (4 shared connections)
- [Community 304](Community_304.md) (2 shared connections)
- [Community 500](Community_500.md) (2 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (2 shared connections)
- [Distributed Event Bus (NATS)](Distributed_Event_Bus_NATS.md) (2 shared connections)
- [NPC Movement Events](NPC_Movement_Events.md) (2 shared connections)
- [Community 47](Community_47.md) (1 shared connections)
- [Community 98](Community_98.md) (1 shared connections)
- [Combat Attack Execution](Combat_Attack_Execution.md) (1 shared connections)

## Source Files

- `server/config/models/nats.py`
- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_service.py`
- `server/tests/unit/services/test_nats_service_helpers.py`
- `server/tests/unit/services/test_nats_service_pool.py`

## Audit Trail

- EXTRACTED: 259 (71%)
- INFERRED: 104 (29%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*