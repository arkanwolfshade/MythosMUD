# Realtime Message Filtering & Formatting

> 276 nodes

## Key Concepts

- **NATSError** (67 connections) — `server/services/nats_exceptions.py`
- **test_nats_service.py** (62 connections) — `server/tests/unit/services/test_nats_service.py`
- **NATSPublishError** (41 connections) — `server/services/nats_exceptions.py`
- **nats_exceptions.py** (38 connections) — `server/services/nats_exceptions.py`
- **nats_message_handler.py** (36 connections) — `server/realtime/nats_message_handler.py`
- **NATSMetrics** (33 connections) — `server/services/nats_metrics.py`
- **nats_service.py** (33 connections) — `server/services/nats_service.py`
- **NATSServicePoolMixin** (28 connections) — `server/services/nats_service_pool.py`
- **nats_message_handler_processing.py** (24 connections) — `server/realtime/nats_message_handler_processing.py`
- **NATSSubscribeError** (23 connections) — `server/services/nats_exceptions.py`
- **asyncio** (23 connections)
- **nats_message_handler_base.py** (20 connections) — `server/realtime/nats_message_handler_base.py`
- **nats_service_pool.py** (19 connections) — `server/services/nats_service_pool.py`
- **format_message_content()** (18 connections) — `server/realtime/message_formatters.py`
- **nats_message_handler_broadcast.py** (16 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **test_message_formatters.py** (16 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **NATSConnectionError** (14 connections) — `server/services/nats_exceptions.py`
- **NATSHealthCheckError** (13 connections) — `server/services/nats_exceptions.py`
- **test_nats_exceptions.py** (13 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **message_filtering.py** (12 connections) — `server/realtime/message_filtering.py`
- **NATSRequestError** (11 connections) — `server/services/nats_exceptions.py`
- **TestExceptionHierarchy** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **nats_service_connect.py** (11 connections) — `server/services/nats_service_connect.py`
- **nats_message_handler_subscriptions.py** (10 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **NatsConnectOptions** (9 connections) — `server/services/nats_service_connect.py`
- *... and 251 more nodes in this community*

## Relationships

- [NATS Configuration](NATS_Configuration.md) (67 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (31 shared connections)
- [Community 55](Community_55.md) (13 shared connections)
- [Community 451](Community_451.md) (13 shared connections)
- [Combat Events](Combat_Events.md) (12 shared connections)
- [Combat Cleanup & Results](Combat_Cleanup_&_Results.md) (11 shared connections)
- [Community 207](Community_207.md) (8 shared connections)
- [Community 524](Community_524.md) (8 shared connections)
- [Community 28](Community_28.md) (8 shared connections)
- [Community 46](Community_46.md) (7 shared connections)
- [Community 233](Community_233.md) (6 shared connections)
- [Community 291](Community_291.md) (6 shared connections)

## Source Files

- `server/realtime/message_filtering.py`
- `server/realtime/message_formatters.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/nats_message_handler_base.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/realtime/nats_message_handler_processing.py`
- `server/realtime/nats_message_handler_subscriptions.py`
- `server/services/nats_exceptions.py`
- `server/services/nats_metrics.py`
- `server/services/nats_service.py`
- `server/services/nats_service_connect.py`
- `server/services/nats_service_pool.py`
- `server/tests/unit/realtime/test_message_formatters.py`
- `server/tests/unit/services/test_nats_exceptions.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 631 (87%)
- INFERRED: 91 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*