# Ground and Rescue Commands

> 128 nodes

## Key Concepts

- **Profession** (54 connections) — `server/models/profession.py`
- **test_async_persistence_core.py** (40 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_profession.py** (30 connections) — `server/tests/unit/models/test_profession.py`
- **Any** (8 connections)
- **.get_stat_requirements()** (5 connections) — `server/models/profession.py`
- **.set_stat_requirements()** (3 connections) — `server/models/profession.py`
- **.get_mechanical_effects()** (3 connections) — `server/models/profession.py`
- **.set_mechanical_effects()** (3 connections) — `server/models/profession.py`
- **.get_stat_modifiers()** (3 connections) — `server/models/profession.py`
- **.set_stat_modifiers()** (3 connections) — `server/models/profession.py`
- **.get_skill_modifiers()** (3 connections) — `server/models/profession.py`
- **.set_skill_modifiers()** (3 connections) — `server/models/profession.py`
- **.meets_stat_requirements()** (3 connections) — `server/models/profession.py`
- **.get_requirement_display_text()** (3 connections) — `server/models/profession.py`
- **test_async_persistence_layer_init_skip_room_cache()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_async_persistence_layer_init_with_room_cache()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_async_persistence_layer_init_deprecated_params()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_user_by_username_case_insensitive_success()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_user_by_username_case_insensitive_database_error()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_professions_success()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_professions_database_error()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_professions_os_error()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_get_profession_by_id_delegates()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_profession_repr()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **test_profession_get_stat_requirements_valid_json()** (3 connections) — `server/tests/unit/models/test_profession.py`
- *... and 103 more nodes in this community*

## Relationships

- [Zone Config Loader](Zone_Config_Loader.md) (10 shared connections)
- [Realtime Conftest Mocks](Realtime_Conftest_Mocks.md) (6 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (4 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (3 shared connections)
- [Chat Logger Service Tests](Chat_Logger_Service_Tests.md) (2 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (1 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)

## Source Files

- `server/models/profession.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/models/test_profession.py`

## Audit Trail

- EXTRACTED: 354 (97%)
- INFERRED: 10 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*