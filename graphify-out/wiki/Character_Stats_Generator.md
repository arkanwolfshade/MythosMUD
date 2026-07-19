# Character Stats Generator

> 45 nodes · cohesion 0.07

## Key Concepts

- **StatsGenerator** (29 connections) — `server/game/stats_generator.py`
- **Stats** (11 connections) — `server/game/stats_generator.py`
- **get_stats_generator()** (9 connections) — `server/dependencies.py`
- **TestGetRoomService** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **TestGetStatsGenerator** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **.roll_stats()** (6 connections) — `server/game/stats_generator.py`
- **.roll_stats_with_profession()** (6 connections) — `server/game/stats_generator.py`
- **.get_available_classes()** (5 connections) — `server/game/stats_generator.py`
- **._roll_3d6()** (5 connections) — `server/game/stats_generator.py`
- **._roll_size()** (5 connections) — `server/game/stats_generator.py`
- **.roll_stats_with_validation()** (5 connections) — `server/game/stats_generator.py`
- **._check_profession_requirements()** (4 connections) — `server/game/stats_generator.py`
- **.get_stat_summary()** (4 connections) — `server/game/stats_generator.py`
- **._roll_4d6_drop_lowest()** (4 connections) — `server/game/stats_generator.py`
- **._roll_point_buy()** (4 connections) — `server/game/stats_generator.py`
- **.validate_class_prerequisites()** (4 connections) — `server/game/stats_generator.py`
- **TestGetStatsGenerator** (4 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_stats_generator_returns_instance()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_room_service_not_initialized()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_room_service_success()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_stats_generator()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_stats_generator_stateless()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **Roll stats and validate against class requirements.          Args:             m** (2 connections) — `server/game/stats_generator.py`
- **.__init__()** (2 connections) — `server/game/stats_generator.py`
- **StatsGenerator** (2 connections) — `server/dependencies.py`
- *... and 20 more nodes in this community*

## Relationships

- [[Dependency Injection Tests]] (9 shared connections)
- [[NPC Admin API]] (5 shared connections)
- [[Character Creation Service]] (4 shared connections)
- [[Combat Command Handler]] (3 shared connections)
- [[Dependency Injection Dependencies]] (2 shared connections)
- [[Maps API Endpoints]] (2 shared connections)
- [[Character Creation API]] (1 shared connections)
- [[Players API Endpoints]] (1 shared connections)
- [[Async Persistence Layer]] (1 shared connections)

## Source Files

- `server/dependencies.py`
- `server/game/stats_generator.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 146 (90%)
- INFERRED: 16 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
