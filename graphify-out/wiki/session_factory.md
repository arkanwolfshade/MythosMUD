# session_factory

> 16 nodes

## Key Concepts

- **session_factory()** (68 connections) — `server/tests/fixtures/integration/__init__.py`
- **test_calendar_procedures.py** (7 connections) — `server/tests/integration/test_calendar_procedures.py`
- **test_db_connectivity_create_and_read_user()** (6 connections) — `server/tests/integration/test_db_connectivity.py`
- **holiday_row()** (5 connections) — `server/tests/integration/test_calendar_procedures.py`
- **npc_schedule_row()** (5 connections) — `server/tests/integration/test_calendar_procedures.py`
- **test_get_calendar_holidays_includes_the_new_row()** (5 connections) — `server/tests/integration/test_calendar_procedures.py`
- **test_get_calendar_npc_schedules_includes_the_new_row()** (5 connections) — `server/tests/integration/test_calendar_procedures.py`
- **async_sessionmaker** (4 connections)
- **AsyncSession** (4 connections)
- **asyncio** (2 connections)
- **fixture** (2 connections)
- **asyncio** (1 connections)
- **serial** (1 connections)
- **Provide an async session factory for integration tests. CRITICAL: This fixture…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Integration tests for db/procedures/calendar.sql (#633). Replace raw SQL…** (1 connections) — `server/tests/integration/test_calendar_procedures.py`
- **Test that we can create and read a User from the database. CRITICAL: This test…** (1 connections) — `server/tests/integration/test_db_connectivity.py`

## Relationships

- [test_room_write_procedures.py](test_room_write_procedures.py.md) (12 shared connections)
- [test_exploration_procedures.py](test_exploration_procedures.py.md) (10 shared connections)
- [test_players_procedures.py](test_players_procedures.py.md) (9 shared connections)
- [fixtures/integration/__init__.py](fixtures-integration-__init__.py.md) (7 shared connections)
- [test_add_player_effect_generates_id](test_add_player_effect_generates_id.md) (5 shared connections)
- [test_containers_procedures.py](test_containers_procedures.py.md) (4 shared connections)
- [test_lucidity_procedures.py](test_lucidity_procedures.py.md) (4 shared connections)
- [test_emotes_procedures.py](test_emotes_procedures.py.md) (3 shared connections)
- [test_npcs_zone_config_procedures.py](test_npcs_zone_config_procedures.py.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (3 shared connections)
- [test_quest_instance_repository.py](test_quest_instance_repository.py.md) (2 shared connections)
- [LucidityService](LucidityService.md) (1 shared connections)

## Source Files

- `server/tests/fixtures/integration/__init__.py`
- `server/tests/integration/test_calendar_procedures.py`
- `server/tests/integration/test_db_connectivity.py`

## Audit Trail

- EXTRACTED: 31 (34%)
- INFERRED: 61 (66%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*