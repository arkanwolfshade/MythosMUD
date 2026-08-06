# admin command setstat

> 12 nodes

## Key Concepts

- **create_error_context()** (10 connections) — `server/api/player_helpers.py`
- **player_helpers.py** (9 connections) — `server/api/player_helpers.py`
- **test_player_helpers.py** (5 connections) — `server/tests/unit/api/test_player_helpers.py`
- **test_create_error_context_without_user_sets_metadata()** (3 connections) — `server/tests/unit/api/test_player_helpers.py`
- **test_create_error_context_with_user_sets_user_id_and_metadata()** (3 connections) — `server/tests/unit/api/test_player_helpers.py`
- **Request** (1 connections)
- **Any** (1 connections)
- **Shared helper functions for player API endpoints.** (1 connections) — `server/api/player_helpers.py`
- **Create error context from request and user.      Helper function to reduce dupli** (1 connections) — `server/api/player_helpers.py`
- **Unit tests for server.api.player_helpers (error context helper).** (1 connections) — `server/tests/unit/api/test_player_helpers.py`
- **When current_user is None, context gets metadata only.** (1 connections) — `server/tests/unit/api/test_player_helpers.py`
- **When current_user is set, user_id is populated and metadata merged.** (1 connections) — `server/tests/unit/api/test_player_helpers.py`

## Relationships

- [commands shutdown process](commands_shutdown_process.md) (2 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (2 shared connections)
- [player requests schemas](player_requests_schemas.md) (2 shared connections)
- [player game schema](player_game_schema.md) (2 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (1 shared connections)

## Source Files

- `server/api/player_helpers.py`
- `server/tests/unit/api/test_player_helpers.py`

## Audit Trail

- EXTRACTED: 37 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*