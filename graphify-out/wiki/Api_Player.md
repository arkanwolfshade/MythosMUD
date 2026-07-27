# Api Player

> 12 nodes · cohesion 0.20

## Key Concepts

- **create_error_context()** (10 connections) — `server/api/player_helpers.py`
- **test_player_helpers.py** (4 connections) — `server/tests/unit/api/test_player_helpers.py`
- **test_create_error_context_with_user_sets_user_id_and_metadata()** (3 connections) — `server/tests/unit/api/test_player_helpers.py`
- **test_create_error_context_without_user_sets_metadata()** (3 connections) — `server/tests/unit/api/test_player_helpers.py`
- **Create error context from request and user.      Helper function to reduce dupli** (2 connections) — `server/api/player_helpers.py`
- **Unit tests for server.api.player_helpers (error context helper).** (1 connections) — `server/tests/unit/api/test_player_helpers.py`
- **When current_user is None, context gets metadata only.** (1 connections) — `server/tests/unit/api/test_player_helpers.py`
- **When current_user is set, user_id is populated and metadata merged.** (1 connections) — `server/tests/unit/api/test_player_helpers.py`
- **Any** (1 connections) — `server/api/player_helpers.py`
- **ErrorContext** (1 connections) — `server/api/player_helpers.py`
- **Request** (1 connections) — `server/api/player_helpers.py`
- **User** (1 connections) — `server/api/player_helpers.py`

## Relationships

- [[NPC Admin API]] (1 shared connections)
- [[Error Logging Enhanced]] (1 shared connections)
- [[Container Exception Handlers]] (1 shared connections)

## Source Files

- `server/api/player_helpers.py`
- `server/tests/unit/api/test_player_helpers.py`

## Audit Trail

- EXTRACTED: 29 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
