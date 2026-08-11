# Phase Three Complete Summary

> 14 nodes

## Key Concepts

- **test_security_headers.py** (20 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **mock_app()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_to_response()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_to_response_hsts_with_subdomains()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_to_response_hsts_without_subdomains()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_dispatch_method()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_dispatch_method_error_handling()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Unit tests for security headers middleware.  Tests the SecurityHeadersMiddleware** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Create a mock ASGI app.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test _add_security_headers_to_response adds headers to Response.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test _add_security_headers_to_response includes subdomains in HSTS.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test _add_security_headers_to_response without subdomains in HSTS.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test dispatch method (backward compatibility).** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test dispatch method error handling.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`

## Relationships

- [Realtime Message Builders](Realtime_Message_Builders.md) (5 shared connections)
- [Game Profession Service](Game_Profession_Service.md) (4 shared connections)
- [Graceful Degradation Plan](Graceful_Degradation_Plan.md) (3 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (1 shared connections)

## Source Files

- `server/tests/unit/middleware/test_security_headers.py`

## Audit Trail

- EXTRACTED: 39 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*