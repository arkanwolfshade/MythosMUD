# Realtime Connection Impl

> 8 nodes

## Key Concepts

- **_setup_session_tracking()** (9 connections) — `server/realtime/connection_establishment.py`
- **test_setup_session_tracking_no_session_id()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_session_tracking_new_session()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_session_tracking_existing_session()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Track connection in session.      Args:         connection_id: The connection ID** (1 connections) — `server/realtime/connection_establishment.py`
- **Test _setup_session_tracking() handles None session_id.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_session_tracking() creates new session entry.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_session_tracking() adds to existing session.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`

## Relationships

- [Logging Structured Setup](Logging_Structured_Setup.md) (4 shared connections)
- [WebSocket Connection Setup](WebSocket_Connection_Setup.md) (4 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`
- `server/tests/unit/realtime/test_connection_establishment.py`

## Audit Trail

- EXTRACTED: 22 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*