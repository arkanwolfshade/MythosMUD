# NATS Service Client

> 214 nodes

## Key Concepts

- **NATSService** (165 connections) — `server/services/nats_service.py`
- **test_nats_service_helpers.py** (60 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **asyncio** (26 connections)
- **test_nats_service_pool.py** (24 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_nats_service_health.py** (23 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **asyncio** (15 connections)
- **asyncio** (11 connections)
- **JsonMap** (9 connections)
- **.disconnect()** (8 connections) — `server/services/nats_service.py`
- **._create_tracked_task()** (7 connections) — `server/services/nats_service.py`
- **_mock_create_tracked_task()** (7 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **.connect()** (6 connections) — `server/services/nats_service.py`
- **._verify_subscription_cleanup()** (6 connections) — `server/services/nats_service.py`
- **_assert_tracked_coro_closed()** (6 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_start_health_monitoring_creates_task()** (6 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **_NatsListenerClient** (5 connections) — `server/services/nats_service.py`
- **NatsMessageCallback** (5 connections) — `server/services/nats_service.py`
- **._on_error()** (5 connections) — `server/services/nats_service.py`
- **._start_health_monitoring()** (5 connections) — `server/services/nats_service.py`
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_flush_batch_records_partial_success_and_cancels_batch_task()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_publish_batch_returns_false_on_subject_validation_failure()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_publish_with_pool_wraps_unexpected_exception()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_recover_failed_batches_requeues_on_repeated_failure()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- *... and 189 more nodes in this community*

## Relationships

- [NATS Messaging Config](NATS_Messaging_Config.md) (75 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (3 shared connections)
- [Combat Events](Combat_Events.md) (3 shared connections)
- [Test Manager](Test_Manager.md) (3 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (3 shared connections)
- [Test Container Bundles](Test_Container_Bundles.md) (2 shared connections)
- [Test Subscription Patterns](Test_Subscription_Patterns.md) (2 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (1 shared connections)
- [Nats Event Bridge](Nats_Event_Bridge.md) (1 shared connections)
- [Combat Service Attack](Combat_Service_Attack.md) (1 shared connections)

## Source Files

- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_service_health.py`
- `server/tests/unit/services/test_nats_service_helpers.py`
- `server/tests/unit/services/test_nats_service_pool.py`

## Audit Trail

- EXTRACTED: 369 (77%)
- INFERRED: 111 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*