# Community 1006

> 14 nodes

## Key Concepts

- **_cleanup_player_data()** (13 connections) — `server/realtime/connection_disconnection.py`
- **test_cleanup_player_data_clears_corruption_tier_cache()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_player_data_clears_phantoms()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_player_data_has_connection_does_not_clear_corruption_tier_cache()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_player_data_has_connection_does_not_clear_phantoms()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_player_data()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_player_data_has_connection()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **Clean up rate limiting, message, and session data for a player. Every…** (1 connections) — `server/realtime/connection_disconnection.py`
- **Test _cleanup_player_data() cleans up player data.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **Test _cleanup_player_data() does not clean up when has connection.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **#625: a player's last disconnect clears any lingering phantom hostiles.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **#625: phantoms are untouched while the player still has a live connection.** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **#804: a player's last disconnect clears their cached corruption tier (write-…** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **#804: the corruption tier cache is untouched while the player still has a live…** (1 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`

## Relationships

- [Community 532](Community_532.md) (7 shared connections)
- [Community 531](Community_531.md) (4 shared connections)
- [Community 38](Community_38.md) (4 shared connections)
- [Community 586](Community_586.md) (1 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`

## Audit Trail

- EXTRACTED: 25 (86%)
- INFERRED: 4 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*