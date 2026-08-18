# server tests integration test login

> 5 nodes

## Key Concepts

- **mock_async_persistence()** (3 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **mock_combat_service()** (3 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **fixture** (3 connections)
- **Create a mock async persistence layer.** (1 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **Create a mock combat service.** (1 connections) — `server/tests/integration/test_login_grace_period_flow.py`

## Relationships

- [server realtime integration game state](server_realtime_integration_game_state.md) (3 shared connections)

## Source Files

- `server/tests/integration/test_login_grace_period_flow.py`

## Audit Trail

- EXTRACTED: 7 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*