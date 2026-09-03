# Correlation Middleware

> 51 nodes

## Key Concepts

- **FastAPI** (31 connections)
- **server/main.py** (15 connections) — `server/main.py`
- **CorrelationMiddleware** (13 connections) — `server/middleware/correlation_middleware.py`
- **test_correlation_middleware.py** (13 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **correlation_middleware.py** (7 connections) — `server/middleware/correlation_middleware.py`
- **auth/conftest.py** (7 connections) — `server/tests/unit/auth/conftest.py`
- **test_auth()** (6 connections) — `server/main.py`
- **.__call__()** (6 connections) — `server/middleware/correlation_middleware.py`
- **create_correlation_middleware()** (6 connections) — `server/middleware/correlation_middleware.py`
- **_get_header()** (6 connections) — `server/middleware/correlation_middleware.py`
- **asyncio** (5 connections)
- **_create_get_app()** (3 connections) — `server/main.py`
- **main()** (3 connections) — `server/main.py`
- **read_root()** (3 connections) — `server/main.py`
- **.__init__()** (3 connections) — `server/middleware/correlation_middleware.py`
- **mock_request()** (3 connections) — `server/tests/unit/auth/conftest.py`
- **mock_session()** (3 connections) — `server/tests/unit/auth/conftest.py`
- **set_auth_epoch_for_tests()** (3 connections) — `server/tests/unit/auth/conftest.py`
- **test_correlation_middleware_adds_response_header()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_generates_correlation_id()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_passes_non_http()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_reraises_exception()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_uses_existing_header()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_create_correlation_middleware_factory()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **fixture** (3 connections)
- *... and 26 more nodes in this community*

## Relationships

- [WebSocket Message Handlers](WebSocket_Message_Handlers.md) (3 shared connections)
- [Test Websocket Helpers](Test_Websocket_Helpers.md) (3 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (3 shared connections)
- [Test Player Requests](Test_Player_Requests.md) (2 shared connections)
- [Test Websocket Initial State](Test_Websocket_Initial_State.md) (2 shared connections)
- [NPC Definitions API](NPC_Definitions_API.md) (2 shared connections)
- [Character Creation API](Character_Creation_API.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Subject Controller](Subject_Controller.md) (1 shared connections)
- [Maps](Maps.md) (1 shared connections)
- [Players](Players.md) (1 shared connections)
- [Real Time](Real_Time.md) (1 shared connections)

## Source Files

- `server/main.py`
- `server/middleware/correlation_middleware.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/middleware/test_correlation_middleware.py`

## Audit Trail

- EXTRACTED: 106 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*