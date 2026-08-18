# server services nats service natsservice

> 28 nodes

## Key Concepts

- **._create_tracked_task()** (7 connections) — `server/services/nats_service.py`
- **.connect()** (6 connections) — `server/services/nats_service.py`
- **._on_error()** (5 connections) — `server/services/nats_service.py`
- **._start_health_monitoring()** (5 connections) — `server/services/nats_service.py`
- **._handle_error_async()** (4 connections) — `server/services/nats_service.py`
- **._health_check_loop()** (4 connections) — `server/services/nats_service.py`
- **._on_disconnect()** (4 connections) — `server/services/nats_service.py`
- **._on_reconnect()** (4 connections) — `server/services/nats_service.py`
- **._check_connection_allowed()** (3 connections) — `server/services/nats_service.py`
- **._handle_disconnect_async()** (3 connections) — `server/services/nats_service.py`
- **._handle_reconnect_async()** (3 connections) — `server/services/nats_service.py`
- **._perform_health_check()** (3 connections) — `server/services/nats_service.py`
- **._setup_connection_handlers()** (3 connections) — `server/services/nats_service.py`
- **BaseException** (2 connections)
- **Task** (1 connections)
- **Async handler for NATS reconnection events.** (1 connections) — `server/services/nats_service.py`
- **Check if connection attempt is allowed by state machine.** (1 connections) — `server/services/nats_service.py`
- **Set up connection event handlers.** (1 connections) — `server/services/nats_service.py`
- **Connect to NATS server with state machine tracking. Returns: True if connection…** (1 connections) — `server/services/nats_service.py`
- **Start periodic health check monitoring task.** (1 connections) — `server/services/nats_service.py`
- **Periodic health check loop using ping/pong.** (1 connections) — `server/services/nats_service.py`
- **Perform a single health check via ping/pong. Returns: True if health check…** (1 connections) — `server/services/nats_service.py`
- **Create a tracked background task with proper lifecycle management. AnyIO…** (1 connections) — `server/services/nats_service.py`
- **Handle NATS connection errors with state machine tracking. AI: Errors may…** (1 connections) — `server/services/nats_service.py`
- **Async handler for NATS connection errors.** (1 connections) — `server/services/nats_service.py`
- *... and 3 more nodes in this community*

## Relationships

- [server services nats service natsservice](server_services_nats_service_natsservice.md) (13 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)

## Source Files

- `server/services/nats_service.py`

## Audit Trail

- EXTRACTED: 41 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*