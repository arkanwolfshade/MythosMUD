# arkham_grid_spec.py

> 38 nodes · cohesion 0.05

## Key Concepts

- **._create_tracked_task()** (7 connections) — `server/services/nats_service.py`
- **.connect()** (6 connections) — `server/services/nats_service.py`
- **.disconnect()** (5 connections) — `server/services/nats_service.py`
- **._on_error()** (5 connections) — `server/services/nats_service.py`
- **._start_health_monitoring()** (5 connections) — `server/services/nats_service.py`
- **._cancel_background_tasks()** (4 connections) — `server/services/nats_service.py`
- **._force_cancel_pending_tasks()** (4 connections) — `server/services/nats_service.py`
- **._handle_error_async()** (4 connections) — `server/services/nats_service.py`
- **._health_check_loop()** (4 connections) — `server/services/nats_service.py`
- **._on_disconnect()** (4 connections) — `server/services/nats_service.py`
- **._on_reconnect()** (4 connections) — `server/services/nats_service.py`
- **._check_connection_allowed()** (3 connections) — `server/services/nats_service.py`
- **._close_nats_connection()** (3 connections) — `server/services/nats_service.py`
- **._handle_disconnect_async()** (3 connections) — `server/services/nats_service.py`
- **._handle_reconnect_async()** (3 connections) — `server/services/nats_service.py`
- **._perform_health_check()** (3 connections) — `server/services/nats_service.py`
- **._setup_connection_handlers()** (3 connections) — `server/services/nats_service.py`
- **._stop_health_monitoring()** (3 connections) — `server/services/nats_service.py`
- **BaseException** (2 connections)
- **Task** (2 connections)
- **Check if connection attempt is allowed by state machine.** (1 connections) — `server/services/nats_service.py`
- **Set up connection event handlers.** (1 connections) — `server/services/nats_service.py`
- **Connect to NATS server with state machine tracking. Returns: True if connection…** (1 connections) — `server/services/nats_service.py`
- **Close NATS connection and transition to disconnected state.** (1 connections) — `server/services/nats_service.py`
- **Disconnect from NATS with graceful shutdown and message draining. AI: State…** (1 connections) — `server/services/nats_service.py`
- *... and 13 more nodes in this community*

## Relationships

- [CombatAttackHandler](CombatAttackHandler.md) (18 shared connections)
- [TestRoomDataFixer](TestRoomDataFixer.md) (1 shared connections)

## Source Files

- `server/services/nats_service.py`

## Audit Trail

- EXTRACTED: 56 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*