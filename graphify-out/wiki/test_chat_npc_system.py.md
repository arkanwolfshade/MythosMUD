# test_chat_npc_system.py

> 92 nodes

## Key Concepts

- **test_security_headers.py** (21 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **middleware()** (19 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_correlation_middleware.py** (18 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **CorrelationMiddleware** (12 connections) — `server/middleware/correlation_middleware.py`
- **SecurityHeadersMiddleware** (11 connections) — `server/middleware/security_headers.py`
- **correlation_middleware.py** (10 connections) — `server/middleware/correlation_middleware.py`
- **WebSocketCorrelationMiddleware** (9 connections) — `server/middleware/correlation_middleware.py`
- **.__call__()** (8 connections) — `server/middleware/correlation_middleware.py`
- **asyncio** (7 connections)
- **create_correlation_middleware()** (6 connections) — `server/middleware/correlation_middleware.py`
- **_get_header()** (6 connections) — `server/middleware/correlation_middleware.py`
- **MutableHeaders** (6 connections)
- **create_websocket_correlation_middleware()** (5 connections) — `server/middleware/correlation_middleware.py`
- **.__call__()** (5 connections) — `server/middleware/security_headers.py`
- **.dispatch()** (5 connections) — `server/middleware/security_headers.py`
- **asyncio** (5 connections)
- **._add_security_headers_to_response()** (4 connections) — `server/middleware/security_headers.py`
- **test_correlation_middleware_adds_response_header()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_generates_correlation_id()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_passes_non_http()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_reraises_exception()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_uses_existing_header()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_websocket_correlation_middleware()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_websocket_correlation_middleware_generates_id()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_security_headers_middleware_adds_headers()** (4 connections) — `server/tests/unit/middleware/test_security_headers.py`
- *... and 67 more nodes in this community*

## Relationships

- [SkillAssignmentScreen.tsx](SkillAssignmentScreen.tsx.md) (5 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (4 shared connections)
- [Persistence Layer Extraction - COMPLETE ✅](Persistence_Layer_Extraction_-_COMPLETE_✅.md) (3 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)
- [Profession](Profession.md) (1 shared connections)
- [Test Coverage Summary: Disconnect Grace Period & Rest Command](Test_Coverage_Summary-_Disconnect_Grace_Period_&_Rest_Command.md) (1 shared connections)

## Source Files

- `server/middleware/correlation_middleware.py`
- `server/middleware/security_headers.py`
- `server/tests/unit/middleware/test_correlation_middleware.py`
- `server/tests/unit/middleware/test_security_headers.py`

## Audit Trail

- EXTRACTED: 131 (83%)
- INFERRED: 27 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*