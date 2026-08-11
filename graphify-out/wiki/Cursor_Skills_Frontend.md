# Cursor Skills Frontend

> 20 nodes

## Key Concepts

- **create_app()** (16 connections) — `server/app/factory.py`
- **main.py** (15 connections) — `server/main.py`
- **main()** (4 connections) — `scripts/generate_openapi_spec.py`
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
- **Create and configure the FastAPI application.      This function sets up the Fas** (1 connections) — `server/app/factory.py`
- **Any** (1 connections)
- **MythosMUD Server - Main Application Entry Point  This module serves as the prima** (1 connections) — `server/main.py`
- **Main entry point for the MythosMUD server.** (1 connections) — `server/main.py`
- **Factory function that creates the get_app function with encapsulated cache.** (1 connections) — `server/main.py`
- **Root endpoint providing basic server information.** (1 connections) — `server/main.py`
- **Test endpoint to verify JWT authentication is working.** (1 connections) — `server/main.py`

## Relationships

- [Combat Command Handler](Combat_Command_Handler.md) (5 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (3 shared connections)
- [Docker PostgreSQL Typo Bug](Docker_PostgreSQL_Typo_Bug.md) (1 shared connections)
- [Commands Npc Admin](Commands_Npc_Admin.md) (1 shared connections)
- [Error Handling Middleware](Error_Handling_Middleware.md) (1 shared connections)
- [Graceful Degradation Plan](Graceful_Degradation_Plan.md) (1 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (1 shared connections)
- [Player Movement Service](Player_Movement_Service.md) (1 shared connections)

## Source Files

- `scripts/generate_openapi_spec.py`
- `server/app/factory.py`
- `server/main.py`

## Audit Trail

- EXTRACTED: 62 (91%)
- INFERRED: 6 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*