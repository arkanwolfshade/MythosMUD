# middleware metrics collector

> 35 nodes

## Key Concepts

- **nats_message_handler_base.py** (20 connections) — `server/realtime/nats_message_handler_base.py`
- **user_manager.py** (20 connections) — `server/services/user_manager.py`
- **MetricsCollector** (18 connections) — `server/middleware/metrics_collector.py`
- **metrics_collector.py** (10 connections) — `server/middleware/metrics_collector.py`
- **test_metrics_collector.py** (7 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **.__init__()** (3 connections) — `server/middleware/metrics_collector.py`
- **.get_metrics()** (3 connections) — `server/middleware/metrics_collector.py`
- **.get_summary()** (3 connections) — `server/middleware/metrics_collector.py`
- **.record_message_processed()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_message_failed()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_message_retried()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_message_dlq()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_circuit_state_change()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_processing_time()** (2 connections) — `server/middleware/metrics_collector.py`
- **Any** (2 connections)
- **.reset_metrics()** (2 connections) — `server/middleware/metrics_collector.py`
- **test_record_and_get_metrics()** (2 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **test_get_summary()** (2 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **test_reset_metrics()** (2 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **test_circuit_state_change_trims_history()** (2 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **Metrics collection for NATS message delivery.  Collects and exposes metrics for** (1 connections) — `server/middleware/metrics_collector.py`
- **Simple metrics collector for NATS message delivery.      Thread-safe metrics col** (1 connections) — `server/middleware/metrics_collector.py`
- **Initialize metrics collector.          AI: Uses Lock for thread-safety in async** (1 connections) — `server/middleware/metrics_collector.py`
- **Record a successfully processed message.          Args:             channel: Mes** (1 connections) — `server/middleware/metrics_collector.py`
- **Record a failed message.          Args:             channel: Message channel** (1 connections) — `server/middleware/metrics_collector.py`
- *... and 10 more nodes in this community*

## Relationships

- [websocket handler realtime](websocket_handler_realtime.md) (8 shared connections)
- [Loot Generation](Loot_Generation.md) (5 shared connections)
- [services user manager](services_user_manager.md) (4 shared connections)
- [message filtering realtime](message_filtering_realtime.md) (3 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (2 shared connections)
- [follow game service](follow_game_service.md) (2 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (2 shared connections)
- [startup npc services](startup_npc_services.md) (2 shared connections)
- [chat game message](chat_game_message.md) (2 shared connections)
- [metrics schemas rationale](metrics_schemas_rationale.md) (1 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (1 shared connections)
- [container persistence rationale](container_persistence_rationale.md) (1 shared connections)

## Source Files

- `server/middleware/metrics_collector.py`
- `server/realtime/nats_message_handler_base.py`
- `server/services/user_manager.py`
- `server/tests/unit/middleware/test_metrics_collector.py`

## Audit Trail

- EXTRACTED: 122 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*