# roll_character_stats

> 86 nodes

## Key Concepts

- **roll_character_stats()** (26 connections) — `server/api/character_creation.py`
- **test_character_creation.py** (24 connections) — `server/tests/unit/api/test_character_creation.py`
- **RollStatsRequest** (23 connections) — `server/schemas/players/player_requests.py`
- **validate_character_stats()** (15 connections) — `server/api/character_creation.py`
- **RollStatsResponse** (12 connections) — `server/schemas/players/character_creation.py`
- **TestRollCharacterStats** (12 connections) — `server/tests/unit/api/test_character_creation.py`
- **_roll_stats_with_profession_preview()** (12 connections) — `server/api/character_creation.py`
- **_convert_stat_summary_to_stat_summary_model()** (11 connections) — `server/api/character_creation.py`
- **get_stats_generator()** (11 connections) — `server/dependencies.py`
- **_dispatch_roll_stats()** (10 connections) — `server/api/character_creation.py`
- **get_current_user()** (9 connections) — `docs/examples/logging/fastapi_integration.py`
- **_raise_roll_stats_error()** (8 connections) — `server/api/character_creation.py`
- **_roll_stats_raw()** (8 connections) — `server/api/character_creation.py`
- **_roll_stats_with_class()** (8 connections) — `server/api/character_creation.py`
- **_raise_roll_stats_validation_error()** (7 connections) — `server/api/character_creation.py`
- **_stats_to_rolled_stats()** (7 connections) — `server/api/character_creation.py`
- **TestValidateCharacterStats** (6 connections) — `server/tests/unit/api/test_character_creation.py`
- **.test_roll_character_stats_profession_not_found()** (6 connections) — `server/tests/unit/api/test_character_creation.py`
- **.test_roll_character_stats_rate_limit()** (6 connections) — `server/tests/unit/api/test_character_creation.py`
- **TestGetStatsGenerator** (5 connections) — `server/tests/unit/test_dependency_injection.py`
- **_apply_rate_limiting_for_stats_roll()** (5 connections) — `server/api/character_creation.py`
- **.test_roll_character_stats_not_authenticated()** (5 connections) — `server/tests/unit/api/test_character_creation.py`
- **.test_roll_character_stats_persistence_not_available()** (5 connections) — `server/tests/unit/api/test_character_creation.py`
- **.test_roll_character_stats_shutdown_pending()** (5 connections) — `server/tests/unit/api/test_character_creation.py`
- **.test_roll_character_stats_with_class()** (5 connections) — `server/tests/unit/api/test_character_creation.py`
- *... and 61 more nodes in this community*

## Relationships

- [api/character_creation.py](api-character_creation.py.md) (46 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (11 shared connections)
- [Stats](Stats.md) (10 shared connections)
- [User](User.md) (9 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (6 shared connections)
- [test_player_requests.py](test_player_requests.py.md) (5 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (4 shared connections)
- [ValidationError](ValidationError.md) (3 shared connections)
- [ProfessionService](ProfessionService.md) (3 shared connections)
- [test_containers.py](test_containers.py.md) (2 shared connections)
- [http_exception_handler](http_exception_handler.md) (1 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (1 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/api/character_creation.py`
- `server/dependencies.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/player_requests.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/schemas/test_player_requests.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 225 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*