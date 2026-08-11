# Game Profession Service

> 8 nodes

## Key Concepts

- **middleware()** (6 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_non_http_scope()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_adds_headers()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_error_handling()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Create SecurityHeadersMiddleware instance.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test middleware passes through non-HTTP connections.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test middleware adds security headers to HTTP responses.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test middleware error handling.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`

## Relationships

- [Phase Three Complete Summary](Phase_Three_Complete_Summary.md) (4 shared connections)
- [Graceful Degradation Plan](Graceful_Degradation_Plan.md) (1 shared connections)

## Source Files

- `server/tests/unit/middleware/test_security_headers.py`

## Audit Trail

- EXTRACTED: 19 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*