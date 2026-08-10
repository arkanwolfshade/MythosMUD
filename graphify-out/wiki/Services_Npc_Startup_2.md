# Services Npc Startup

> 8 nodes

## Key Concepts

- **_cleanup_failed_connection()** (10 connections) — `server/realtime/connection_establishment.py`
- **test_cleanup_failed_connection_none()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_failed_connection_success()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_failed_connection_error()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Cleanup connection on failure.      Args:         connection_id: The connection** (1 connections) — `server/realtime/connection_establishment.py`
- **Test _cleanup_failed_connection() handles None connection_id.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _cleanup_failed_connection() cleans up connection.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _cleanup_failed_connection() handles errors during cleanup.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`

## Relationships

- [Logging Structured Setup](Logging_Structured_Setup.md) (4 shared connections)
- [WebSocket Connection Setup](WebSocket_Connection_Setup.md) (4 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (1 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`
- `server/tests/unit/realtime/test_connection_establishment.py`

## Audit Trail

- EXTRACTED: 22 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*