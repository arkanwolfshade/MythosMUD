# LoggedHTTPException

> 80 nodes

## Key Concepts

- **LoggedHTTPException** (359 connections) — `server/exceptions.py`
- **test_player_respawn_api.py** (18 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_player_respawn_handlers.py** (16 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **respawn_player()** (15 connections) — `server/api/player_respawn.py`
- **test_npc_admin_mgmt_api.py** (15 connections) — `server/tests/unit/api/admin/test_npc_admin_mgmt_api.py`
- **test_professions_endpoints.py** (15 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **get_admin_sessions()** (13 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **respawn_player_from_delirium()** (13 connections) — `server/api/player_respawn.py`
- **_handle_delirium_respawn_validation_error()** (12 connections) — `server/api/player_respawn.py`
- **cleanup_admin_sessions()** (11 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **_handle_respawn_validation_error()** (11 connections) — `server/api/player_respawn.py`
- **get_all_professions()** (11 connections) — `server/api/professions.py`
- **get_profession_by_id()** (11 connections) — `server/api/professions.py`
- **get_admin_audit_log()** (10 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **_run_player_respawn()** (10 connections) — `server/api/player_respawn.py`
- **RespawnResponse** (9 connections) — `server/schemas/players/player_respawn.py`
- **_user()** (9 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **_user()** (8 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **asyncio** (8 connections)
- **test_respawn_player_from_delirium_not_found()** (6 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_not_found()** (6 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_validation_error()** (6 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_delirium_unexpected_error()** (5 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_from_delirium_success()** (5 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_no_session()** (5 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- *... and 55 more nodes in this community*

## Relationships

- [container_endpoints_basic.py](container_endpoints_basic.py.md) (52 shared connections)
- [User](User.md) (49 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (38 shared connections)
- [get_logger](get_logger.md) (37 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (26 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (18 shared connections)
- [maps.py](maps.py.md) (16 shared connections)
- [test_metrics_endpoints.py](test_metrics_endpoints.py.md) (15 shared connections)
- [real_time.py](real_time.py.md) (15 shared connections)
- [login_user](login_user.md) (13 shared connections)
- [test_auth_dependencies.py](test_auth_dependencies.py.md) (12 shared connections)
- [ValidationError](ValidationError.md) (12 shared connections)

## Source Files

- `server/api/admin/npc_admin_mgmt_api.py`
- `server/api/player_respawn.py`
- `server/api/professions.py`
- `server/exceptions.py`
- `server/schemas/players/player_respawn.py`
- `server/tests/unit/api/admin/test_npc_admin_mgmt_api.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/api/test_player_respawn_api.py`
- `server/tests/unit/api/test_player_respawn_handlers.py`
- `server/tests/unit/api/test_professions_endpoints.py`

## Audit Trail

- EXTRACTED: 440 (76%)
- INFERRED: 140 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*