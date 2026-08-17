# server tests unit realtime integration

> 11 nodes

## Key Concepts

- **fixture** (5 connections)
- **game_state_provider()** (4 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **mock_get_app()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **mock_get_async_persistence()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **mock_room_manager()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **mock_send_personal_message()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Create a mock room manager.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Create a mock get_async_persistence callback.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Create a mock send_personal_message callback.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Create a mock get_app callback.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Create a GameStateProvider instance.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`

## Relationships

- [server tests unit realtime integration](server_tests_unit_realtime_integration.md) (5 shared connections)
- [server realtime integration game state](server_realtime_integration_game_state.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/integration/test_game_state_provider.py`

## Audit Trail

- EXTRACTED: 15 (94%)
- INFERRED: 1 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*