# combat models rationale

> 6 nodes

## Key Concepts

- **TestGetPlayerServiceForTesting** (5 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_player_service_for_testing_creates_mock()** (4 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_player_service_for_testing_with_provided_service()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Tests for get_player_service_for_testing helper function.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_player_service_for_testing returns provided service.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_player_service_for_testing creates PlayerService when None provided.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`

## Relationships

- [NPC Definitions Admin](NPC_Definitions_Admin.md) (3 shared connections)
- [Player Stats](Player_Stats.md) (2 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_dependencies.py`

## Audit Trail

- EXTRACTED: 13 (87%)
- INFERRED: 2 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*