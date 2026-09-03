# Test Security Headers

> 21 nodes

## Key Concepts

- **test_security_headers.py** (21 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **MutableHeaders** (6 connections)
- **._add_security_headers()** (3 connections) — `server/middleware/security_headers.py`
- **test_add_security_headers()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_csp_policy()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_hsts_value()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_permissions_policy()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_referrer_policy()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_to_response()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_to_response_hsts_with_subdomains()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_to_response_hsts_without_subdomains()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Add all security headers to the response.** (1 connections) — `server/middleware/security_headers.py`
- **Unit tests for security headers middleware. Tests the SecurityHeadersMiddleware…** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test _add_security_headers_to_response adds headers to Response.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test _add_security_headers_to_response includes subdomains in HSTS.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test _add_security_headers_to_response without subdomains in HSTS.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test _add_security_headers adds all security headers.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test _add_security_headers sets correct HSTS value.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test _add_security_headers includes Permissions-Policy.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test _add_security_headers uses configured CSP policy.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test _add_security_headers uses configured referrer policy.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`

## Relationships

- [Test Security Headers](Test_Security_Headers.md) (7 shared connections)
- [Security Headers](Security_Headers.md) (4 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)

## Source Files

- `server/middleware/security_headers.py`
- `server/tests/unit/middleware/test_security_headers.py`

## Audit Trail

- EXTRACTED: 32 (86%)
- INFERRED: 5 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*