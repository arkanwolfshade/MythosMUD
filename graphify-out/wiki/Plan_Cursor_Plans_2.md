# Plan Cursor Plans

> 43 nodes

## Key Concepts

- **factory.py** (37 connections) — `server/app/factory.py`
- **create_app()** (16 connections) — `server/app/factory.py`
- **main.py** (15 connections) — `server/main.py`
- **__init__.py** (10 connections) — `server/api/__init__.py`
- **containers.py** (6 connections) — `server/api/containers.py`
- **CORSConfigDict** (6 connections) — `server/app/factory.py`
- **_get_cors_config_from_app_config()** (6 connections) — `server/app/factory.py`
- **_configure_cors()** (6 connections) — `server/app/factory.py`
- **base.py** (5 connections) — `server/api/base.py`
- **main()** (4 connections) — `scripts/generate_openapi_spec.py`
- **__init__.py** (4 connections) — `server/api/admin/__init__.py`
- **_get_default_cors_config()** (4 connections) — `server/app/factory.py`
- **_parse_cors_env_vars()** (4 connections) — `server/app/factory.py`
- **main()** (4 connections) — `server/main.py`
- **_create_get_app()** (4 connections) — `server/main.py`
- **generate_openapi_spec.py** (3 connections) — `scripts/generate_openapi_spec.py`
- **_sanitize_token_examples()** (3 connections) — `scripts/generate_openapi_spec.py`
- **FastAPI** (3 connections)
- **test_auth()** (3 connections) — `server/main.py`
- **FastAPI** (2 connections)
- **read_root()** (2 connections) — `server/main.py`
- **Replace auth token examples with clearly fake placeholders.** (1 connections) — `scripts/generate_openapi_spec.py`
- **Generate and write OpenAPI spec to docs/openapi/openapi.json.** (1 connections) — `scripts/generate_openapi_spec.py`
- **API module for MythosMUD.  This module provides REST API endpoints for the Mytho** (1 connections) — `server/api/__init__.py`
- **Admin API module for MythosMUD.  This module provides administrative API endpoin** (1 connections) — `server/api/admin/__init__.py`
- *... and 18 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (12 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (8 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (7 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (3 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (3 shared connections)
- [Error Handling Middleware](Error_Handling_Middleware.md) (3 shared connections)
- [Command Field Validators](Command_Field_Validators.md) (2 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (2 shared connections)
- [Memory Threshold Monitor](Memory_Threshold_Monitor.md) (2 shared connections)
- [Game Terminal Panels](Game_Terminal_Panels.md) (2 shared connections)
- [Room Occupant Manager Tests](Room_Occupant_Manager_Tests.md) (2 shared connections)
- [Commands Npc Admin](Commands_Npc_Admin.md) (2 shared connections)

## Source Files

- `scripts/generate_openapi_spec.py`
- `server/api/__init__.py`
- `server/api/admin/__init__.py`
- `server/api/base.py`
- `server/api/containers.py`
- `server/app/factory.py`
- `server/main.py`

## Audit Trail

- EXTRACTED: 163 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*