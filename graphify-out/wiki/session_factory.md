# session_factory

> 20 nodes

## Key Concepts

- **session_factory()** (68 connections) — `server/tests/fixtures/integration/__init__.py`
- **test_db_connectivity_create_and_read_user()** (6 connections) — `server/tests/integration/test_db_connectivity.py`
- **emote_row()** (6 connections) — `server/tests/integration/test_emotes_procedures.py`
- **quest_seed_data()** (6 connections) — `server/tests/integration/test_quest_flow.py`
- **test_emotes_procedures.py** (6 connections) — `server/tests/integration/test_emotes_procedures.py`
- **test_get_emote_aliases_joins_owning_emote()** (5 connections) — `server/tests/integration/test_emotes_procedures.py`
- **test_get_emotes_includes_the_new_row()** (5 connections) — `server/tests/integration/test_emotes_procedures.py`
- **async_sessionmaker** (3 connections)
- **AsyncSession** (3 connections)
- **async_sessionmaker** (2 connections)
- **asyncio** (2 connections)
- **asyncio** (1 connections)
- **serial** (1 connections)
- **fixture** (1 connections)
- **fixture** (1 connections)
- **Provide an async session factory for integration tests. CRITICAL: This fixture…** (1 connections) — `server/tests/fixtures/integration/__init__.py`
- **Test that we can create and read a User from the database. CRITICAL: This test…** (1 connections) — `server/tests/integration/test_db_connectivity.py`
- **Integration tests for db/procedures/emotes.sql (#633). Replace raw SQL…** (1 connections) — `server/tests/integration/test_emotes_procedures.py`
- **Create one emote with one alias. Yields (stable_id, alias).** (1 connections) — `server/tests/integration/test_emotes_procedures.py`
- **Create User, Player, leave_the_tutorial QuestDefinition and QuestOffer. Quest…** (1 connections) — `server/tests/integration/test_quest_flow.py`

## Relationships

- [test_room_write_procedures.py](test_room_write_procedures.py.md) (12 shared connections)
- [test_exploration_procedures.py](test_exploration_procedures.py.md) (10 shared connections)
- [test_players_procedures.py](test_players_procedures.py.md) (9 shared connections)
- [fixtures/integration/__init__.py](fixtures-integration-__init__.py.md) (7 shared connections)
- [test_add_player_effect_generates_id](test_add_player_effect_generates_id.md) (5 shared connections)
- [sqlalchemy.md](sqlalchemy.md.md) (5 shared connections)
- [test_calendar_procedures.py](test_calendar_procedures.py.md) (4 shared connections)
- [test_containers_procedures.py](test_containers_procedures.py.md) (4 shared connections)
- [test_lucidity_procedures.py](test_lucidity_procedures.py.md) (4 shared connections)
- [pytest.md](pytest.md.md) (4 shared connections)
- [test_npcs_zone_config_procedures.py](test_npcs_zone_config_procedures.py.md) (3 shared connections)
- [LucidityService](LucidityService.md) (1 shared connections)

## Source Files

- `server/tests/fixtures/integration/__init__.py`
- `server/tests/integration/test_db_connectivity.py`
- `server/tests/integration/test_emotes_procedures.py`
- `server/tests/integration/test_quest_flow.py`

## Audit Trail

- EXTRACTED: 34 (36%)
- INFERRED: 61 (64%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*