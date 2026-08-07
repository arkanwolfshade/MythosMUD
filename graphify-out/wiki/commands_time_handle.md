# commands time handle

> 12 nodes

## Key Concepts

- **TestCatatoniaRegistry** (26 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_on_catatonia_entered_with_string()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_on_catatonia_cleared_with_uuid()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_on_sanitarium_failover_callback_exception()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_get_snapshot_with_players()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **.test_multiple_players_catatonic()** (3 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **Test suite for CatatoniaRegistry class.** (1 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **Test on_catatonia_entered with string player_id.** (1 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **Test on_catatonia_cleared removes player from registry.** (1 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **Test on_sanitarium_failover handles callback exceptions.** (1 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **Test get_snapshot returns copy of catatonic players.** (1 connections) — `server/tests/unit/services/test_catatonia_registry.py`
- **Test registry can track multiple catatonic players.** (1 connections) — `server/tests/unit/services/test_catatonia_registry.py`

## Relationships

- [catatonia registry services](catatonia_registry_services.md) (6 shared connections)
- [skill game service](skill_game_service.md) (4 shared connections)
- [game room service](game_room_service.md) (3 shared connections)
- [infrastructure persistence room](infrastructure_persistence_room.md) (3 shared connections)
- [room game service](room_game_service.md) (3 shared connections)
- [room infrastructure persistence](room_infrastructure_persistence.md) (3 shared connections)
- [infrastructure persistence core](infrastructure_persistence_core.md) (1 shared connections)
- [room service game](room_service_game.md) (1 shared connections)
- [game skill service](game_skill_service.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_catatonia_registry.py`

## Audit Trail

- EXTRACTED: 46 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*