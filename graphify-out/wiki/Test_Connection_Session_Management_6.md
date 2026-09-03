# Test Connection Session Management

> 15 nodes

## Key Concepts

- **_as_ws()** (14 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **_is_websocket_connected()** (9 connections) — `server/realtime/connection_session_management.py`
- **test_is_websocket_connected_connected()** (5 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_is_websocket_connected_disconnected()** (5 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_is_websocket_connected_no_client_state()** (5 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_is_websocket_connected_no_name()** (5 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **_WsMissingClientState** (3 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **WebSocket** (1 connections)
- **WebSocket** (1 connections)
- **Check if a WebSocket is connected. Args: websocket: The WebSocket to check…** (1 connections) — `server/realtime/connection_session_management.py`
- **Test _is_websocket_connected() returns True for connected websocket.** (1 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **Test _is_websocket_connected() returns False for disconnected websocket.** (1 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **Test _is_websocket_connected() handles missing client_state.** (1 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **Test _is_websocket_connected() handles missing name attribute.** (1 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **Stand-in whose missing client_state trips AttributeError in the helper.** (1 connections) — `server/tests/unit/realtime/test_connection_session_management.py`

## Relationships

- [Test Connection Session Management](Test_Connection_Session_Management.md) (18 shared connections)
- [Connection Session Management](Connection_Session_Management.md) (1 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)

## Source Files

- `server/realtime/connection_session_management.py`
- `server/tests/unit/realtime/test_connection_session_management.py`

## Audit Trail

- EXTRACTED: 37 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*