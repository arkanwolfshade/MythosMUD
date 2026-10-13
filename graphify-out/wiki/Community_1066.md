# Community 1066

> 13 nodes

## Key Concepts

- **_end_combat_for_grace_period()** (10 connections) — `server/api/players.py`
- **test_players_combat_grace.py** (10 connections) — `server/tests/unit/api/test_players_combat_grace.py`
- **test_grace_period_swallows_cleanup_errors()** (6 connections) — `server/tests/unit/api/test_players_combat_grace.py`
- **test_grace_period_removes_only_that_player_from_combat()** (5 connections) — `server/tests/unit/api/test_players_combat_grace.py`
- **_combat()** (4 connections) — `server/tests/unit/api/test_players_combat_grace.py`
- **_service()** (4 connections) — `server/tests/unit/api/test_players_combat_grace.py`
- **test_grace_period_is_a_no_op_without_a_combat()** (4 connections) — `server/tests/unit/api/test_players_combat_grace.py`
- **asyncio** (4 connections)
- **test_grace_period_is_a_no_op_without_a_combat_service()** (3 connections) — `server/tests/unit/api/test_players_combat_grace.py`
- **UUID** (2 connections)
- **End combat for player entering login grace period. Args: player_id: Player UUID** (1 connections) — `server/api/players.py`
- **Unit tests for the login-grace combat exit in server.api.players (#833: leave…** (1 connections) — `server/tests/unit/api/test_players_combat_grace.py`
- **Combat cleanup is best effort: a failing removal must not break the grace-…** (1 connections) — `server/tests/unit/api/test_players_combat_grace.py`

## Relationships

- [API Response Models](API_Response_Models.md) (5 shared connections)

## Source Files

- `server/api/players.py`
- `server/tests/unit/api/test_players_combat_grace.py`

## Audit Trail

- EXTRACTED: 30 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*