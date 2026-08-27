# test_persistence_container_persistence.py

> 15 nodes

## Key Concepts

- **fixture** (7 connections)
- **player_death_service()** (4 connections) — `server/tests/unit/services/test_player_death_service.py`
- **player_death_service_no_dependencies()** (4 connections) — `server/tests/unit/services/test_player_death_service.py`
- **mock_event_bus()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **mock_player()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **mock_player_combat_service()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **mock_session()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **sample_player_id()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Create a mock event bus.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Create a mock player combat service.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Create a PlayerDeathService instance.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Create a PlayerDeathService instance without dependencies.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Create a mock async session.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Create a sample player ID.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`
- **Create a mock player.** (1 connections) — `server/tests/unit/services/test_player_death_service.py`

## Relationships

- [Polish Systematically](Polish_Systematically.md) (7 shared connections)
- [3. REFACTOR Findings (935 findings)](3._REFACTOR_Findings_935_findings.md) (2 shared connections)

## Source Files

- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 21 (91%)
- INFERRED: 2 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*