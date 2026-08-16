# Client

> 15 nodes

## Key Concepts

- **Client** (7 connections)
- **WebSocket** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **WebSocket** (5 connections) — `docs/examples/logging/websocket_integration.py`
- **_NatsConnectFn** (3 connections) — `server/services/nats_service_pool.py`
- **.__call__()** (3 connections) — `server/services/nats_service_pool.py`
- **.client()** (2 connections) — `docs/examples/logging/fastapi_integration.py`
- **.client()** (2 connections) — `docs/examples/logging/websocket_integration.py`
- **.accept()** (1 connections) — `docs/examples/logging/fastapi_integration.py`
- **.receive_text()** (1 connections) — `docs/examples/logging/fastapi_integration.py`
- **.send_text()** (1 connections) — `docs/examples/logging/fastapi_integration.py`
- **.accept()** (1 connections) — `docs/examples/logging/websocket_integration.py`
- **.receive_text()** (1 connections) — `docs/examples/logging/websocket_integration.py`
- **.send_text()** (1 connections) — `docs/examples/logging/websocket_integration.py`
- **Protocol** (1 connections)
- **SSLContext** (1 connections)

## Relationships

- [NATSSubjectManager](NATSSubjectManager.md) (2 shared connections)
- [NATSServicePoolMixin](NATSServicePoolMixin.md) (2 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (1 shared connections)
- [websocket_integration.py](websocket_integration.py.md) (1 shared connections)
- [testing_examples.py](testing_examples.py.md) (1 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `docs/examples/logging/websocket_integration.py`
- `server/services/nats_service_pool.py`

## Audit Trail

- EXTRACTED: 18 (86%)
- INFERRED: 3 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*