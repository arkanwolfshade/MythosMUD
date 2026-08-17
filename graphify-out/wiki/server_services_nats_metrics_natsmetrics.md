# server services nats metrics natsmetrics

> 22 nodes

## Key Concepts

- **NATSMetrics** (12 connections) — `server/services/nats_metrics.py`
- **.get_metrics()** (3 connections) — `server/services/nats_metrics.py`
- **.__init__()** (2 connections) — `server/services/nats_metrics.py`
- **.record_ack_failure()** (2 connections) — `server/services/nats_metrics.py`
- **.record_ack_success()** (2 connections) — `server/services/nats_metrics.py`
- **.record_batch_flush()** (2 connections) — `server/services/nats_metrics.py`
- **.record_nak()** (2 connections) — `server/services/nats_metrics.py`
- **.record_publish()** (2 connections) — `server/services/nats_metrics.py`
- **.record_subscribe()** (2 connections) — `server/services/nats_metrics.py`
- **.update_connection_health()** (2 connections) — `server/services/nats_metrics.py`
- **.update_pool_utilization()** (2 connections) — `server/services/nats_metrics.py`
- **Any** (1 connections)
- **NATS-specific metrics collection for monitoring and alerting.** (1 connections) — `server/services/nats_metrics.py`
- **Record publish operation metrics.** (1 connections) — `server/services/nats_metrics.py`
- **Record subscribe operation metrics.** (1 connections) — `server/services/nats_metrics.py`
- **Record batch flush operation metrics.** (1 connections) — `server/services/nats_metrics.py`
- **Update connection health score (0-100).** (1 connections) — `server/services/nats_metrics.py`
- **Update connection pool utilization (0-1).** (1 connections) — `server/services/nats_metrics.py`
- **Record successful message acknowledgment.** (1 connections) — `server/services/nats_metrics.py`
- **Record failed message acknowledgment.** (1 connections) — `server/services/nats_metrics.py`
- **Record negative acknowledgment (message requeued).** (1 connections) — `server/services/nats_metrics.py`
- **Get comprehensive NATS metrics.** (1 connections) — `server/services/nats_metrics.py`

## Relationships

- [docs nats subject patterns](docs_nats_subject_patterns.md) (1 shared connections)
- [deque](deque.md) (1 shared connections)

## Source Files

- `server/services/nats_metrics.py`

## Audit Trail

- EXTRACTED: 22 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*