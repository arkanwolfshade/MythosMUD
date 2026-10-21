# Async Persistence Migration Tracker

> 22 nodes · cohesion 0.13

## Key Concepts

- **test_game_state_provider_hallucination.py** (12 connections) — `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`
- **test_send_initial_game_state_hallucinates_exits_for_deranged_viewer()** (6 connections) — `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`
- **test_send_initial_game_state_includes_viewer_phantom()** (6 connections) — `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`
- **fixture** (5 connections)
- **game_state_provider()** (4 connections) — `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`
- **_no_lucidity_row_session()** (4 connections) — `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`
- **_wire_room()** (4 connections) — `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`
- **mock_get_app()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`
- **mock_get_async_persistence()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`
- **mock_room_manager()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`
- **mock_send_personal_message()** (3 connections) — `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`
- **asyncio** (2 connections)
- **Unit tests for hallucination-related additions to GameStateProvider (#625,…** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`
- **#626/#714: a deranged connecting player's initial game_state shows the seeded…** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`
- **Fake get_async_session() yielding a session whose PlayerLucidity lookup misses.…** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`
- **Create a mock room manager.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`
- **Create a mock get_async_persistence callback.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`
- **Create a mock send_personal_message callback.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`
- **Create a mock get_app callback.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`
- **Create a GameStateProvider instance.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`
- **Wire the fixtures so send_initial_game_state resolves a minimal, real room dict.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`
- **#625/#714: the game_state room payload includes this viewer's own active…** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`

## Relationships

- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (4 shared connections)
- [ChatLogger](ChatLogger.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`

## Audit Trail

- EXTRACTED: 33 (94%)
- INFERRED: 2 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*