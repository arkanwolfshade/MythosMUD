# LoggedHTTPException

> 110 nodes

## Key Concepts

- **LoggedHTTPException** (358 connections) — `server/exceptions.py`
- **api/player_respawn.py** (29 connections) — `server/api/player_respawn.py`
- **test_auth_dependencies.py** (26 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_player_respawn_api.py** (18 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_player_respawn_handlers.py** (16 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **respawn_player()** (15 connections) — `server/api/player_respawn.py`
- **test_professions_endpoints.py** (15 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **asyncio** (14 connections)
- **respawn_player_from_delirium()** (13 connections) — `server/api/player_respawn.py`
- **_handle_delirium_respawn_validation_error()** (12 connections) — `server/api/player_respawn.py`
- **get_current_superuser()** (12 connections) — `server/auth/dependencies.py`
- **_handle_respawn_validation_error()** (11 connections) — `server/api/player_respawn.py`
- **get_all_professions()** (11 connections) — `server/api/professions.py`
- **get_profession_by_id()** (11 connections) — `server/api/professions.py`
- **require_invite_code()** (11 connections) — `server/auth/dependencies.py`
- **validate_user_for_loot_all()** (10 connections) — `server/api/container_helpers.py`
- **_run_player_respawn()** (10 connections) — `server/api/player_respawn.py`
- **RespawnResponse** (9 connections) — `server/schemas/players/player_respawn.py`
- **_user()** (9 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **get_current_verified_user()** (8 connections) — `server/auth/dependencies.py`
- **_user()** (8 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **player_router.py** (8 connections) — `server/api/player_router.py`
- **asyncio** (8 connections)
- **get_optional_current_user()** (6 connections) — `server/auth/dependencies.py`
- **test_respawn_player_from_delirium_not_found()** (6 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- *... and 85 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (78 shared connections)
- [PlayerService](PlayerService.md) (43 shared connections)
- [User](User.md) (41 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (37 shared connections)
- [test_monitoring_endpoints.py](test_monitoring_endpoints.py.md) (18 shared connections)
- [test_metrics_endpoints.py](test_metrics_endpoints.py.md) (15 shared connections)
- [handle_transfer_items_exceptions](handle_transfer_items_exceptions.md) (14 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (13 shared connections)
- [login_user](login_user.md) (13 shared connections)
- [ValidationError](ValidationError.md) (13 shared connections)
- [ExplorationService](ExplorationService.md) (11 shared connections)
- [dialogue_definitions_api.py](dialogue_definitions_api.py.md) (10 shared connections)

## Source Files

- `server/api/container_helpers.py`
- `server/api/player_respawn.py`
- `server/api/player_router.py`
- `server/api/professions.py`
- `server/auth/dependencies.py`
- `server/exceptions.py`
- `server/schemas/players/player_respawn.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_player_respawn_api.py`
- `server/tests/unit/api/test_player_respawn_handlers.py`
- `server/tests/unit/api/test_professions_endpoints.py`
- `server/tests/unit/auth/test_auth_dependencies.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`

## Audit Trail

- EXTRACTED: 499 (76%)
- INFERRED: 158 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*