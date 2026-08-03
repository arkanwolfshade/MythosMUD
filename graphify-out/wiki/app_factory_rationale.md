# app factory rationale

> 41 nodes

## Key Concepts

- **factory.py** (45 connections) — `server/app/factory.py`
- **error_handling_middleware.py** (19 connections) — `server/middleware/error_handling_middleware.py`
- **register_error_handlers()** (11 connections) — `server/middleware/error_handling_middleware.py`
- **setup_error_handling()** (8 connections) — `server/middleware/error_handling_middleware.py`
- **CORSConfigDict** (7 connections) — `server/app/factory.py`
- **_register_v1_routers()** (7 connections) — `server/app/factory.py`
- **_get_cors_config_from_app_config()** (6 connections) — `server/app/factory.py`
- **_parse_cors_env_vars()** (6 connections) — `server/app/factory.py`
- **_configure_cors()** (6 connections) — `server/app/factory.py`
- **UserRead** (6 connections) — `server/auth/endpoints.py`
- **UserUpdate** (6 connections) — `server/auth/endpoints.py`
- **__init__.py** (6 connections) — `server/middleware/__init__.py`
- **add_error_handling_middleware()** (6 connections) — `server/middleware/error_handling_middleware.py`
- **_apply_cors_env_overrides()** (5 connections) — `server/app/factory.py`
- **CORSConfigOverrides** (4 connections) — `server/app/factory.py`
- **_get_default_cors_config()** (4 connections) — `server/app/factory.py`
- **_parse_cors_origin_list()** (4 connections) — `server/app/factory.py`
- **FastAPI** (4 connections)
- **_first_set_env()** (3 connections) — `server/app/factory.py`
- **_try_json_str_list()** (3 connections) — `server/app/factory.py`
- **FastAPI** (3 connections)
- **TypedDict** (2 connections)
- **FastAPI application factory for MythosMUD server.  This module handles FastAPI a** (1 connections) — `server/app/factory.py`
- **Type definition for CORS configuration dictionary.** (1 connections) — `server/app/factory.py`
- **Partial CORS overrides from environment variables.** (1 connections) — `server/app/factory.py`
- *... and 16 more nodes in this community*

## Relationships

- [auth users rationale](auth_users_rationale.md) (10 shared connections)
- [NATS Messaging](NATS_Messaging.md) (8 shared connections)
- [middleware error handling](middleware_error_handling.md) (7 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (7 shared connections)
- [command commands talk](command_commands_talk.md) (5 shared connections)
- [Exception Containers](Exception_Containers.md) (3 shared connections)
- [Player Stats](Player_Stats.md) (3 shared connections)
- [health models rationale](health_models_rationale.md) (2 shared connections)
- [System Metrics](System_Metrics.md) (2 shared connections)
- [Item Instances](Item_Instances.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (1 shared connections)

## Source Files

- `server/app/factory.py`
- `server/auth/endpoints.py`
- `server/middleware/__init__.py`
- `server/middleware/error_handling_middleware.py`

## Audit Trail

- EXTRACTED: 175 (92%)
- INFERRED: 15 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*