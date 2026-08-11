# Components Map Layout

> 6 nodes

## Key Concepts

- **.dispatch()** (5 connections) — `server/middleware/security_headers.py`
- **._add_security_headers_to_response()** (4 connections) — `server/middleware/security_headers.py`
- **Any** (2 connections)
- **Request** (1 connections)
- **Backward-compatible dispatch method for BaseHTTPMiddleware interface.          T** (1 connections) — `server/middleware/security_headers.py`
- **Add security headers to Response object (compatibility method).** (1 connections) — `server/middleware/security_headers.py`

## Relationships

- [Graceful Degradation Plan](Graceful_Degradation_Plan.md) (2 shared connections)

## Source Files

- `server/middleware/security_headers.py`

## Audit Trail

- EXTRACTED: 14 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*