# Coverage Improvement Summary - Plan 2 Execution

> 35 nodes

## Key Concepts

- **test_nats_service_pool.py** (19 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **NATSService** (13 connections)
- **.initialize()** (12 connections) — `server/container/bundles/monitoring.py`
- **asyncio** (11 connections)
- **nats_service()** (8 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **nats_config()** (4 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_cleanup_connection_pool_swallows_cancelled_error()** (4 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_cleanup_connection_pool_swallows_close_error()** (4 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_cleanup_connection_pool_swallows_outer_exception()** (4 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_flush_batch_records_partial_success_and_cancels_batch_task()** (4 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_publish_batch_returns_false_on_subject_validation_failure()** (4 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_publish_batch_returns_false_on_unexpected_exception()** (4 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_publish_with_pool_wraps_unexpected_exception()** (4 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_recover_failed_batches_recovers_successfully()** (4 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_recover_failed_batches_requeues_on_repeated_failure()** (4 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_retry_failed_batch_groups_recovers_on_retry()** (4 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_validate_pool_publish_subject_rejects_invalid_subject()** (3 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **test_validate_pool_publish_subject_wraps_validation_error()** (3 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **NATSConfig** (2 connections)
- **fixture** (2 connections)
- **_cleanup_connection_pool logs and continues when a connection.close() is…** (2 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **Initialize monitoring services. Depends on Core/Realtime/Game for injected deps.** (1 connections) — `server/container/bundles/monitoring.py`
- **Unit tests for NATSServicePoolMixin's exception-handling and retry branches.…** (1 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **_cleanup_connection_pool's outer try/except tolerates a failure enumerating the…** (1 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **publish_batch returns False (not raise) when subject validation rejects the…** (1 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- *... and 10 more nodes in this community*

## Relationships

- [api/character_creation.py](api-character_creation.py.md) (2 shared connections)
- [TestMonitoringEndpoints](TestMonitoringEndpoints.md) (1 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (1 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (1 shared connections)
- [NPCStartupService](NPCStartupService.md) (1 shared connections)
- [test_combat_cleanup_handler.py](test_combat_cleanup_handler.py.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [PopulationStats](PopulationStats.md) (1 shared connections)
- [ChatMessage](ChatMessage.md) (1 shared connections)
- [**~25-30% provide CRITICAL coverage**](__~25-30__provide_CRITICAL_coverage__.md) (1 shared connections)
- [test_who_commands.py](test_who_commands.py.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/container/bundles/monitoring.py`
- `server/tests/unit/services/test_nats_service_pool.py`

## Audit Trail

- EXTRACTED: 68 (92%)
- INFERRED: 6 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*