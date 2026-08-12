# MutableHeaders

> 13 nodes

## Key Concepts

- **MutableHeaders** (6 connections)
- **._add_security_headers()** (3 connections) — `server/middleware/security_headers.py`
- **test_add_security_headers()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_csp_policy()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_hsts_value()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_permissions_policy()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_referrer_policy()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Add all security headers to the response.** (1 connections) — `server/middleware/security_headers.py`
- **Test _add_security_headers adds all security headers.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test _add_security_headers sets correct HSTS value.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test _add_security_headers includes Permissions-Policy.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test _add_security_headers uses configured CSP policy.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test _add_security_headers uses configured referrer policy.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`

## Relationships

- [test_security_headers.py](test_security_headers.py.md) (5 shared connections)
- [SecurityHeadersMiddleware](SecurityHeadersMiddleware.md) (1 shared connections)

## Source Files

- `server/middleware/security_headers.py`
- `server/tests/unit/middleware/test_security_headers.py`

## Audit Trail

- EXTRACTED: 13 (72%)
- INFERRED: 5 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*