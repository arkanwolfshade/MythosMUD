# Command Parser

> 77 nodes

## Key Concepts

- **get_config()** (105 connections) — `server/config/__init__.py`
- **AppConfig** (31 connections) — `server/config/models/app.py`
- **__init__.py** (11 connections) — `server/config/__init__.py`
- **reset_config()** (9 connections) — `server/config/__init__.py`
- **test_config.py** (9 connections) — `server/tests/unit/config/test_config.py`
- **test_config_init.py** (9 connections) — `server/tests/unit/config/test_config_init.py`
- **.to_legacy_dict()** (7 connections) — `server/config/models/app.py`
- **Any** (6 connections)
- **_create_config_instance()** (5 connections) — `server/config/__init__.py`
- **_get_config_cached()** (5 connections) — `server/config/__init__.py`
- **_get_config_test()** (5 connections) — `server/config/__init__.py`
- **.__init__()** (5 connections) — `server/config/models/app.py`
- **._legacy_game_entries()** (5 connections) — `server/config/models/app.py`
- **._legacy_nats_dict()** (5 connections) — `server/config/models/app.py`
- **._legacy_chat_dict()** (5 connections) — `server/config/models/app.py`
- **._legacy_cors_dict()** (5 connections) — `server/config/models/app.py`
- **generate_unique_codes()** (5 connections) — `tools/invite_tools/generate_invites.py`
- **_is_test_mode()** (4 connections) — `server/config/__init__.py`
- **._sanitize_environment_for_nested_configs()** (4 connections) — `server/config/models/app.py`
- **test_reset_config_clears_state()** (4 connections) — `server/tests/unit/config/test_config.py`
- **test_reset_config_in_test_mode()** (4 connections) — `server/tests/unit/config/test_config_init.py`
- **generate_invites.py** (4 connections) — `tools/invite_tools/generate_invites.py`
- **._first_cors_origins_env()** (3 connections) — `server/config/models/app.py`
- **reset_config_singleton()** (3 connections) — `server/tests/conftest.py`
- **test_get_config_returns_app_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- *... and 52 more nodes in this community*

## Relationships

- [Pydantic Error Handlers](Pydantic_Error_Handlers.md) (10 shared connections)
- [NATS Metrics API](NATS_Metrics_API.md) (6 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (5 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (5 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (4 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (3 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (3 shared connections)
- [Commands Time](Commands_Time.md) (3 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (3 shared connections)
- [Map Editing Hooks](Map_Editing_Hooks.md) (3 shared connections)
- [Archive Planning E 2 E](Archive_Planning_E_2_E.md) (2 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (2 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/config/models/app.py`
- `server/tests/conftest.py`
- `server/tests/unit/config/test_config.py`
- `server/tests/unit/config/test_config_init.py`
- `server/tests/unit/test_config_smoke.py`
- `tools/invite_tools/generate_invites.py`

## Audit Trail

- EXTRACTED: 329 (97%)
- INFERRED: 11 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*