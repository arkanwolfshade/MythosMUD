# config rationale config()

> 6 nodes

## Key Concepts

- **TestGetPlayerServiceForTesting** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_player_service_for_testing_with_injection()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_player_service_for_testing_without_injection()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_player_service_for_testing() function.** (1 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_player_service_for_testing() with injected service.** (1 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_player_service_for_testing() creates mock when None.** (1 connections) — `server/tests/unit/test_dependency_injection.py`

## Relationships

- [Player Stats](Player_Stats.md) (3 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (3 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (1 shared connections)
- [System Metrics](System_Metrics.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 13 (72%)
- INFERRED: 5 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*