# .disconnect

> 17 nodes

## Key Concepts

- **.disconnect()** (8 connections) — `server/services/nats_service.py`
- **._verify_subscription_cleanup()** (6 connections) — `server/services/nats_service.py`
- **._cancel_background_tasks()** (3 connections) — `server/services/nats_service.py`
- **._close_all_subscriptions()** (3 connections) — `server/services/nats_service.py`
- **._close_nats_connection()** (3 connections) — `server/services/nats_service.py`
- **._drain_subscriptions()** (3 connections) — `server/services/nats_service.py`
- **.get_active_subscriptions()** (3 connections) — `server/services/nats_service.py`
- **._stop_health_monitoring()** (3 connections) — `server/services/nats_service.py`
- **Drain in-flight messages from all subscriptions.** (1 connections) — `server/services/nats_service.py`
- **Close and unsubscribe from all subscriptions.** (1 connections) — `server/services/nats_service.py`
- **Verify all subscriptions were cleaned up and log warnings if any remain.** (1 connections) — `server/services/nats_service.py`
- **Close NATS connection and transition to disconnected state.** (1 connections) — `server/services/nats_service.py`
- **Disconnect from NATS with graceful shutdown and message draining. AI: State…** (1 connections) — `server/services/nats_service.py`
- **Cancel all tracked background tasks for proper cleanup. AnyIO Pattern:…** (1 connections) — `server/services/nats_service.py`
- **Stop health check monitoring task.** (1 connections) — `server/services/nats_service.py`
- **Get list of all active NATS subscription subjects. Returns: List of subject…** (1 connections) — `server/services/nats_service.py`
- **Verify that all subscriptions are properly cleaned up. Returns: Dictionary with…** (1 connections) — `server/services/nats_service.py`

## Relationships

- [NATSService](NATSService.md) (8 shared connections)
- [JsonMap](JsonMap.md) (1 shared connections)

## Source Files

- `server/services/nats_service.py`

## Audit Trail

- EXTRACTED: 25 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*