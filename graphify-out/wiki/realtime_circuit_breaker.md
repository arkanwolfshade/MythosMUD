# realtime circuit breaker

> 18 nodes

## Key Concepts

- **.connect()** (8 connections) — `server/services/nats_service.py`
- **._start_health_monitoring()** (5 connections) — `server/services/nats_service.py`
- **._build_connect_options()** (4 connections) — `server/services/nats_service.py`
- **._configure_tls()** (4 connections) — `server/services/nats_service.py`
- **._health_check_loop()** (4 connections) — `server/services/nats_service.py`
- **._check_connection_allowed()** (3 connections) — `server/services/nats_service.py`
- **._setup_connection_handlers()** (3 connections) — `server/services/nats_service.py`
- **._perform_health_check()** (3 connections) — `server/services/nats_service.py`
- **._initialize_connection_pool()** (3 connections) — `server/services/nats_service.py`
- **Check if connection attempt is allowed by state machine.** (1 connections) — `server/services/nats_service.py`
- **Build connection options for NATS.** (1 connections) — `server/services/nats_service.py`
- **Configure TLS settings for NATS connection.** (1 connections) — `server/services/nats_service.py`
- **Set up connection event handlers.** (1 connections) — `server/services/nats_service.py`
- **Connect to NATS server with state machine tracking.          Returns:** (1 connections) — `server/services/nats_service.py`
- **Start periodic health check monitoring task.** (1 connections) — `server/services/nats_service.py`
- **Periodic health check loop using ping/pong.** (1 connections) — `server/services/nats_service.py`
- **Perform a single health check via ping/pong.          Returns:             True** (1 connections) — `server/services/nats_service.py`
- **Initialize connection pool for high-throughput scenarios.          AI: Tracks su** (1 connections) — `server/services/nats_service.py`

## Relationships

- [combat validator validators](combat_validator_validators.md) (9 shared connections)
- [target resolution service](target_resolution_service.md) (3 shared connections)

## Source Files

- `server/services/nats_service.py`

## Audit Trail

- EXTRACTED: 46 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*