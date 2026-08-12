# StatsGenerator

> 52 nodes

## Key Concepts

- **StatsGenerator** (34 connections) — `server/game/stats_generator.py`
- **Stats** (11 connections)
- **TestGetPlayerService** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **TestGetPlayerServiceForTesting** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **TestGetRoomService** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **TestGetStatsGenerator** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **.roll_stats_with_profession()** (7 connections) — `server/game/stats_generator.py`
- **.roll_stats()** (6 connections) — `server/game/stats_generator.py`
- **.get_available_classes()** (5 connections) — `server/game/stats_generator.py`
- **._roll_3d6()** (5 connections) — `server/game/stats_generator.py`
- **._roll_size()** (5 connections) — `server/game/stats_generator.py`
- **.roll_stats_with_validation()** (5 connections) — `server/game/stats_generator.py`
- **._check_profession_requirements()** (4 connections) — `server/game/stats_generator.py`
- **.get_stat_summary()** (4 connections) — `server/game/stats_generator.py`
- **._roll_4d6_drop_lowest()** (4 connections) — `server/game/stats_generator.py`
- **._roll_point_buy()** (4 connections) — `server/game/stats_generator.py`
- **.validate_class_prerequisites()** (4 connections) — `server/game/stats_generator.py`
- **.test_get_player_service_not_initialized()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_player_service_success()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_player_service_for_testing_with_injection()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_player_service_for_testing_without_injection()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_room_service_not_initialized()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_room_service_success()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_stats_generator()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_stats_generator_stateless()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- *... and 27 more nodes in this community*

## Relationships

- [server/dependencies.py](server-dependencies.py.md) (17 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (7 shared connections)
- [PlayerService](PlayerService.md) (6 shared connections)
- [RoomService](RoomService.md) (4 shared connections)
- [test_character_creation_service.py](test_character_creation_service.py.md) (2 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [Stats](Stats.md) (1 shared connections)

## Source Files

- `server/game/stats_generator.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 95 (87%)
- INFERRED: 14 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*