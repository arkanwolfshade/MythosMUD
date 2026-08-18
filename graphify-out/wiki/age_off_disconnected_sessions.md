# age_off_disconnected_sessions

> 14 nodes

## Key Concepts

- **age_off_disconnected_sessions()** (13 connections) — `server/realtime/player_disconnect_handlers.py`
- **_get_session_maps_for_age_off()** (4 connections) — `server/realtime/player_disconnect_handlers.py`
- **_purge_expired_sessions_from_maps()** (4 connections) — `server/realtime/player_disconnect_handlers.py`
- **_session_ids_past_age_off()** (3 connections) — `server/realtime/player_disconnect_handlers.py`
- **test_age_off_disconnected_sessions_keeps_recent()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_age_off_disconnected_sessions_missing_attrs_returns_zero()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_age_off_disconnected_sessions_removes_expired()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **Return typed session maps for age-off, or None if the manager is not ready.…** (1 connections) — `server/realtime/player_disconnect_handlers.py`
- **Session ids whose disconnect timestamp is older than SESSION_AGE_OFF_SECONDS.** (1 connections) — `server/realtime/player_disconnect_handlers.py`
- **Remove expired session ids from disconnect_times, connections, and…** (1 connections) — `server/realtime/player_disconnect_handlers.py`
- **Remove sessions that have been disconnected for more than…** (1 connections) — `server/realtime/player_disconnect_handlers.py`
- **Test age_off_disconnected_sessions removes sessions older than 5 minutes.** (1 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **Test age_off_disconnected_sessions keeps sessions disconnected less than 5…** (1 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **Test age_off_disconnected_sessions returns 0 when manager lacks session attrs.** (1 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`

## Relationships

- [test_player_disconnect_handlers.py](test_player_disconnect_handlers.py.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [connection_manager_health_cleanup.py](connection_manager_health_cleanup.py.md) (2 shared connections)
- [test_connection_cleanup_methods.py](test_connection_cleanup_methods.py.md) (1 shared connections)

## Source Files

- `server/realtime/player_disconnect_handlers.py`
- `server/tests/unit/realtime/test_player_disconnect_handlers.py`

## Audit Trail

- EXTRACTED: 27 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*