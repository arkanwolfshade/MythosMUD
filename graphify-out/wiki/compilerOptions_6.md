# compilerOptions

> 9 nodes · cohesion 0.22

## Key Concepts

- **preferences_service()** (4 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **fixture** (4 connections)
- **sample_preferences()** (4 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **mock_session()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **sample_player_id()** (3 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **Create a PlayerPreferencesService instance.** (1 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **Create a mock async session.** (1 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **Create a sample player ID.** (1 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **Create sample player preferences.** (1 connections) — `server/tests/unit/services/test_player_preferences_service.py`

## Relationships

- [MessageQueue](MessageQueue.md) (4 shared connections)
- [server/tests/conftest.py](server-tests-conftest.py.md) (1 shared connections)
- [test_connection_event_helpers.py](test_connection_event_helpers.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_player_preferences_service.py`

## Audit Trail

- EXTRACTED: 12 (86%)
- INFERRED: 2 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*