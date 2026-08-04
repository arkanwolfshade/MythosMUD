# middleware metrics collector

> 35 nodes

## Key Concepts

- **MetricsCollector** (18 connections) — `server/middleware/metrics_collector.py`
- **Lock** (9 connections)
- **test_metrics_collector.py** (7 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **.__init__()** (3 connections) — `server/container/main.py`
- **.__init__()** (3 connections) — `server/middleware/metrics_collector.py`
- **.get_metrics()** (3 connections) — `server/middleware/metrics_collector.py`
- **.get_summary()** (3 connections) — `server/middleware/metrics_collector.py`
- **.__init__()** (3 connections) — `server/npc/threading.py`
- **.record_message_processed()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_message_failed()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_message_retried()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_message_dlq()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_circuit_state_change()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_processing_time()** (2 connections) — `server/middleware/metrics_collector.py`
- **Any** (2 connections)
- **.reset_metrics()** (2 connections) — `server/middleware/metrics_collector.py`
- **.__init__()** (2 connections) — `server/services/inventory_mutation_guard.py`
- **test_record_and_get_metrics()** (2 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **test_get_summary()** (2 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **test_reset_metrics()** (2 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **test_circuit_state_change_trims_history()** (2 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **Initialize the container. Services are NOT initialized here - use initialize().** (1 connections) — `server/container/main.py`
- **Simple metrics collector for NATS message delivery.      Thread-safe metrics col** (1 connections) — `server/middleware/metrics_collector.py`
- **Initialize metrics collector.          AI: Uses Lock for thread-safety in async** (1 connections) — `server/middleware/metrics_collector.py`
- **Record a successfully processed message.          Args:             channel: Mes** (1 connections) — `server/middleware/metrics_collector.py`
- *... and 10 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (3 shared connections)
- [room cache services](room_cache_services.md) (2 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [idle npc movement](idle_npc_movement.md) (1 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (1 shared connections)
- [taunt combat commands](taunt_combat_commands.md) (1 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)
- [Exception Containers](Exception_Containers.md) (1 shared connections)

## Source Files

- `server/container/main.py`
- `server/middleware/metrics_collector.py`
- `server/npc/threading.py`
- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/middleware/test_metrics_collector.py`

## Audit Trail

- EXTRACTED: 80 (90%)
- INFERRED: 9 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*