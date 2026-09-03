# Test Connection Establishment

> 12 nodes

## Key Concepts

- **_find_dead_connections()** (11 connections) — `server/realtime/connection_establishment.py`
- **test_find_dead_connections_all_active()** (7 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_find_dead_connections_not_connected()** (7 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_find_dead_connections_no_player()** (5 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_find_dead_connections_none_websocket()** (5 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_find_dead_connections_not_in_active()** (5 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Find dead WebSocket connections for a player before acquiring lock. Args:…** (1 connections) — `server/realtime/connection_establishment.py`
- **Test _find_dead_connections() returns empty list when player not found.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _find_dead_connections() returns empty list when all connections are…** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _find_dead_connections() skips connections not in active_websockets.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _find_dead_connections() raises ConnectionError when websocket is None.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _find_dead_connections() finds dead connections.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`

## Relationships

- [Test Connection Establishment](Test_Connection_Establishment.md) (16 shared connections)
- [Test Connection Establishment Ws](Test_Connection_Establishment_Ws.md) (5 shared connections)
- [Connection Establishment](Connection_Establishment.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`
- `server/tests/unit/realtime/test_connection_establishment.py`

## Audit Trail

- EXTRACTED: 35 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*