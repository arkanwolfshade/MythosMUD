# npc combat services

> 19 nodes

## Key Concepts

- **main.py** (15 connections) — `server/main.py`
- **create_app()** (14 connections) — `server/app/factory.py`
- **main()** (4 connections) — `scripts/generate_openapi_spec.py`
- **main()** (4 connections) — `server/main.py`
- **_create_get_app()** (4 connections) — `server/main.py`
- **generate_openapi_spec.py** (3 connections) — `scripts/generate_openapi_spec.py`
- **_sanitize_token_examples()** (3 connections) — `scripts/generate_openapi_spec.py`
- **FastAPI** (3 connections)
- **test_auth()** (3 connections) — `server/main.py`
- **read_root()** (2 connections) — `server/main.py`
- **Replace auth token examples with clearly fake placeholders.** (1 connections) — `scripts/generate_openapi_spec.py`
- **Generate and write OpenAPI spec to docs/openapi/openapi.json.** (1 connections) — `scripts/generate_openapi_spec.py`
- **Create and configure the FastAPI application.      This function sets up the Fas** (1 connections) — `server/app/factory.py`
- **Any** (1 connections)
- **MythosMUD Server - Main Application Entry Point  This module serves as the prima** (1 connections) — `server/main.py`
- **Main entry point for the MythosMUD server.** (1 connections) — `server/main.py`
- **Factory function that creates the get_app function with encapsulated cache.** (1 connections) — `server/main.py`
- **Root endpoint providing basic server information.** (1 connections) — `server/main.py`
- **Test endpoint to verify JWT authentication is working.** (1 connections) — `server/main.py`

## Relationships

- [player service game](player_service_game.md) (5 shared connections)
- [Loot Generation](Loot_Generation.md) (3 shared connections)
- [app factory rationale](app_factory_rationale.md) (2 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (1 shared connections)
- [middleware comprehensive logging](middleware_comprehensive_logging.md) (1 shared connections)
- [middleware error handling](middleware_error_handling.md) (1 shared connections)
- [persistence rationale player](persistence_rationale_player.md) (1 shared connections)
- [auth users rationale](auth_users_rationale.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)

## Source Files

- `scripts/generate_openapi_spec.py`
- `server/app/factory.py`
- `server/main.py`

## Audit Trail

- EXTRACTED: 61 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*