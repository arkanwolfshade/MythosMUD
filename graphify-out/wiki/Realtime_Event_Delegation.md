# Realtime Event Delegation

> 29 nodes

## Key Concepts

- **NATSMessageBroker** (32 connections) — `server/infrastructure/nats_broker.py`
- **.connect()** (5 connections) — `server/infrastructure/nats_broker.py`
- **._start_health_monitoring()** (5 connections) — `server/infrastructure/nats_broker.py`
- **._configure_tls()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._error_callback()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._handle_error_async()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._handle_reconnect_async()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._health_check_loop()** (4 connections) — `server/infrastructure/nats_broker.py`
- **test_connect_with_tls_enabled_passes_tls_options()** (4 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **._disconnected_callback()** (3 connections) — `server/infrastructure/nats_broker.py`
- **._handle_disconnect_async()** (3 connections) — `server/infrastructure/nats_broker.py`
- **._reconnected_callback()** (3 connections) — `server/infrastructure/nats_broker.py`
- **._perform_health_check()** (3 connections) — `server/infrastructure/nats_broker.py`
- **nats_broker()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Exception** (2 connections)
- **NATS implementation of MessageBroker protocol.      This class wraps NATS clie** (1 connections) — `server/infrastructure/nats_broker.py`
- **Configure TLS settings for NATS connection (mirrors NATSService._configure_tls).** (1 connections) — `server/infrastructure/nats_broker.py`
- **Connect to NATS server.          Returns:             bool: True if connectio** (1 connections) — `server/infrastructure/nats_broker.py`
- **Handle NATS errors.          AI: Runs as fire-and-forget async task to prevent** (1 connections) — `server/infrastructure/nats_broker.py`
- **Async handler for NATS connection errors.** (1 connections) — `server/infrastructure/nats_broker.py`
- **Handle NATS disconnection.          AI: Runs as fire-and-forget async task to** (1 connections) — `server/infrastructure/nats_broker.py`
- **Async handler for NATS disconnection events.** (1 connections) — `server/infrastructure/nats_broker.py`
- **Handle NATS reconnection.          AI: Runs as fire-and-forget async task to p** (1 connections) — `server/infrastructure/nats_broker.py`
- **Async handler for NATS reconnection events.** (1 connections) — `server/infrastructure/nats_broker.py`
- **Start periodic health check monitoring task.** (1 connections) — `server/infrastructure/nats_broker.py`
- *... and 4 more nodes in this community*

## Relationships

- [Services Combat Persistence](Services_Combat_Persistence.md) (8 shared connections)
- [Multiplayer Browser Helpers](Multiplayer_Browser_Helpers.md) (6 shared connections)
- [Cursor Skills Mythosmud](Cursor_Skills_Mythosmud.md) (3 shared connections)
- [Combat Monitoring Service](Combat_Monitoring_Service.md) (3 shared connections)
- [Combat Service Bundle](Combat_Service_Bundle.md) (2 shared connections)
- [Realtime Maintenance Connection](Realtime_Maintenance_Connection.md) (1 shared connections)

## Source Files

- `server/infrastructure/nats_broker.py`
- `server/tests/unit/infrastructure/test_nats_broker.py`

## Audit Trail

- EXTRACTED: 91 (94%)
- INFERRED: 6 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*