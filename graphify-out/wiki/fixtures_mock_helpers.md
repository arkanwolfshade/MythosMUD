# fixtures mock helpers

> 14 nodes

## Key Concepts

- **handle_new_game_session()** (11 connections) — `server/api/real_time.py`
- **_ensure_connection_manager()** (10 connections) — `server/api/real_time.py`
- **get_player_connections()** (9 connections) — `server/api/real_time.py`
- **get_connection_statistics()** (7 connections) — `server/api/real_time.py`
- **Request** (4 connections)
- **test_ensure_connection_manager_missing()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_handle_new_game_session_missing_session_id()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_handle_new_game_session_invalid_json()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_get_player_connections()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_handle_new_game_session()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **Ensure connection manager is available.     Raises LoggedHTTPException with prop** (1 connections) — `server/api/real_time.py`
- **Get connection information for a player.     Returns detailed connection metadat** (1 connections) — `server/api/real_time.py`
- **Handle a new game session for a player.     This will disconnect existing connec** (1 connections) — `server/api/real_time.py`
- **Get comprehensive connection statistics.     Returns detailed statistics about a** (1 connections) — `server/api/real_time.py`

## Relationships

- [nats services metrics](nats_services_metrics.md) (8 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (5 shared connections)
- [schedule services service](schedule_services_service.md) (5 shared connections)
- [cleanup combat handler](cleanup_combat_handler.md) (5 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 55 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*