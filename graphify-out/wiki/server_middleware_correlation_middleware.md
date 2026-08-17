# server middleware correlation middleware

> 37 nodes

## Key Concepts

- **middleware()** (19 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_correlation_middleware.py** (18 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **CorrelationMiddleware** (13 connections) — `server/middleware/correlation_middleware.py`
- **correlation_middleware.py** (10 connections) — `server/middleware/correlation_middleware.py`
- **WebSocketCorrelationMiddleware** (9 connections) — `server/middleware/correlation_middleware.py`
- **.__call__()** (8 connections) — `server/middleware/correlation_middleware.py`
- **asyncio** (7 connections)
- **create_correlation_middleware()** (6 connections) — `server/middleware/correlation_middleware.py`
- **_get_header()** (6 connections) — `server/middleware/correlation_middleware.py`
- **create_websocket_correlation_middleware()** (5 connections) — `server/middleware/correlation_middleware.py`
- **test_correlation_middleware_adds_response_header()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_generates_correlation_id()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_passes_non_http()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_reraises_exception()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_uses_existing_header()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_websocket_correlation_middleware()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_websocket_correlation_middleware_generates_id()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **.__init__()** (3 connections) — `server/middleware/correlation_middleware.py`
- **test_create_correlation_middleware_factory()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_create_websocket_correlation_middleware()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **.__init__()** (2 connections) — `server/middleware/correlation_middleware.py`
- **test_get_header_case_insensitive()** (2 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **Scope** (2 connections)
- **ASGIApp** (1 connections)
- **Receive** (1 connections)
- *... and 12 more nodes in this community*

## Relationships

- [mutableheaders](mutableheaders.md) (6 shared connections)
- [docs examples logging correct patterns](docs_examples_logging_correct_patterns.md) (5 shared connections)
- [server middleware comprehensive logging](server_middleware_comprehensive_logging.md) (3 shared connections)
- [scripts generate openapi spec](scripts_generate_openapi_spec.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/middleware/correlation_middleware.py`
- `server/tests/unit/middleware/test_correlation_middleware.py`
- `server/tests/unit/middleware/test_security_headers.py`

## Audit Trail

- EXTRACTED: 67 (75%)
- INFERRED: 22 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*