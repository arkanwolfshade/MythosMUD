# NATS Configuration

> 216 nodes

## Key Concepts

- **NATSService** (165 connections) — `server/services/nats_service.py`
- **test_nats_service_helpers.py** (59 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **NATSConfig** (33 connections) — `server/config/models/nats.py`
- **asyncio** (26 connections)
- **test_nats_service_pool.py** (23 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_nats_service_health.py** (22 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **asyncio** (15 connections)
- **NATSUnsubscribeError** (14 connections) — `server/services/nats_exceptions.py`
- **asyncio** (11 connections)
- **.disconnect()** (8 connections) — `server/services/nats_service.py`
- **._create_tracked_task()** (7 connections) — `server/services/nats_service.py`
- **_mock_create_tracked_task()** (7 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **.connect()** (6 connections) — `server/services/nats_service.py`
- **.__init__()** (6 connections) — `server/services/nats_service.py`
- **._verify_subscription_cleanup()** (6 connections) — `server/services/nats_service.py`
- **_assert_tracked_coro_closed()** (6 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_start_health_monitoring_creates_task()** (6 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_nats_service_init_with_config()** (6 connections) — `server/tests/unit/services/test_nats_service.py`
- **._on_error()** (5 connections) — `server/services/nats_service.py`
- **._start_health_monitoring()** (5 connections) — `server/services/nats_service.py`
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_flush_batch_records_partial_success_and_cancels_batch_task()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_publish_batch_returns_false_on_subject_validation_failure()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- *... and 191 more nodes in this community*

## Relationships

- [Realtime Message Filtering & Formatting](Realtime_Message_Filtering_&_Formatting.md) (67 shared connections)
- [Community 524](Community_524.md) (9 shared connections)
- [Community 28](Community_28.md) (7 shared connections)
- [AppConfig Composite Settings](AppConfig_Composite_Settings.md) (5 shared connections)
- [Community 87](Community_87.md) (3 shared connections)
- [Combat Cleanup & Results](Combat_Cleanup_&_Results.md) (3 shared connections)
- [Community 55](Community_55.md) (2 shared connections)
- [Event Bus](Event_Bus.md) (2 shared connections)
- [Community 645](Community_645.md) (2 shared connections)
- [Combat Events](Combat_Events.md) (1 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (1 shared connections)

## Source Files

- `server/config/models/nats.py`
- `server/services/nats_exceptions.py`
- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_service.py`
- `server/tests/unit/services/test_nats_service_health.py`
- `server/tests/unit/services/test_nats_service_helpers.py`
- `server/tests/unit/services/test_nats_service_pool.py`

## Audit Trail

- EXTRACTED: 387 (77%)
- INFERRED: 117 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*