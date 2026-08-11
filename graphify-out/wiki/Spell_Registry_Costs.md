# Spell Registry Costs

> 298 nodes

## Key Concepts

- **.get_instance()** (88 connections) — `server/database.py`
- **.reset_instance()** (87 connections) — `server/database.py`
- **test_database_helpers.py** (46 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_database_extended.py** (43 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_error_handling.py** (41 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_init.py** (36 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **database_helpers.py** (30 connections) — `server/database_helpers.py`
- **DatabaseManager** (29 connections) — `server/database.py`
- **reset_database()** (16 connections) — `server/database.py`
- **get_database_path()** (16 connections) — `server/database_helpers.py`
- **get_database_path()** (12 connections) — `server/database.py`
- **get_async_session()** (12 connections) — `server/database_helpers.py`
- **close_db()** (9 connections) — `server/database.py`
- **get_engine()** (9 connections) — `server/database_helpers.py`
- **get_session_maker()** (9 connections) — `server/database_helpers.py`
- **close_db()** (9 connections) — `server/database_helpers.py`
- **get_engine()** (8 connections) — `server/database.py`
- **reset_database()** (8 connections) — `server/database_helpers.py`
- **init_db()** (8 connections) — `server/database_helpers.py`
- **test_database.py** (7 connections) — `server/tests/unit/infrastructure/test_database.py`
- **.get_database_path()** (6 connections) — `server/database.py`
- **Path** (6 connections)
- **get_database_url()** (6 connections) — `server/database.py`
- **get_database_url()** (6 connections) — `server/database_helpers.py`
- **ensure_database_directory()** (6 connections) — `server/database_helpers.py`
- *... and 273 more nodes in this community*

## Relationships

- [Command Parser Helpers](Command_Parser_Helpers.md) (39 shared connections)
- [NATS Subject Manager](NATS_Subject_Manager.md) (35 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (20 shared connections)
- [Profession Get Mechanical Effects](Profession_Get_Mechanical_Effects.md) (6 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (4 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (3 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (1 shared connections)
- [Container Persistence Ops](Container_Persistence_Ops.md) (1 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (1 shared connections)
- [Message Queue Cleanup](Message_Queue_Cleanup.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 1155 (96%)
- INFERRED: 52 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*