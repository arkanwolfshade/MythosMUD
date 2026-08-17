# LoggedHTTPException

> 129 nodes

## Key Concepts

- **LoggedHTTPException** (358 connections) — `server/exceptions.py`
- **test_metrics_endpoints.py** (39 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **api/metrics.py** (31 connections) — `server/api/metrics.py`
- **test_player_respawn_api.py** (18 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_player_respawn_handlers.py** (16 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **respawn_player()** (15 connections) — `server/api/player_respawn.py`
- **replay_dlq_message()** (14 connections) — `server/api/metrics.py`
- **_admin_user()** (14 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **asyncio** (14 connections)
- **respawn_player_from_delirium()** (13 connections) — `server/api/player_respawn.py`
- **metrics/metrics.py** (13 connections) — `server/schemas/metrics/metrics.py`
- **get_metrics()** (12 connections) — `server/api/metrics.py`
- **_handle_delirium_respawn_validation_error()** (12 connections) — `server/api/player_respawn.py`
- **delete_dlq_message()** (11 connections) — `server/api/metrics.py`
- **reset_circuit_breaker()** (11 connections) — `server/api/metrics.py`
- **_handle_respawn_validation_error()** (11 connections) — `server/api/player_respawn.py`
- **DLQReplayResponse** (10 connections) — `server/schemas/metrics/metrics.py`
- **get_dlq_messages()** (10 connections) — `server/api/metrics.py`
- **get_metrics_summary()** (10 connections) — `server/api/metrics.py`
- **_load_dlq_message()** (10 connections) — `server/api/metrics.py`
- **_run_player_respawn()** (10 connections) — `server/api/player_respawn.py`
- **StatusMessageResponse** (9 connections) — `server/schemas/metrics/metrics.py`
- **RespawnResponse** (9 connections) — `server/schemas/players/player_respawn.py`
- **reset_metrics()** (9 connections) — `server/api/metrics.py`
- **verify_admin_access()** (9 connections) — `server/api/metrics.py`
- *... and 104 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (56 shared connections)
- [User](User.md) (45 shared connections)
- [PlayerService](PlayerService.md) (34 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (24 shared connections)
- [models/user.py](models-user.py.md) (22 shared connections)
- [pytest.md](pytest.md.md) (22 shared connections)
- [Invite](Invite.md) (19 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (17 shared connections)
- [maps.py](maps.py.md) (16 shared connections)
- [test_monitoring_endpoints.py](test_monitoring_endpoints.py.md) (16 shared connections)
- [handle_transfer_items_exceptions](handle_transfer_items_exceptions.md) (14 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (13 shared connections)

## Source Files

- `server/api/metrics.py`
- `server/api/player_respawn.py`
- `server/exceptions.py`
- `server/schemas/metrics/__init__.py`
- `server/schemas/metrics/metrics.py`
- `server/schemas/metrics/metrics_data.py`
- `server/schemas/players/player_respawn.py`
- `server/tests/unit/api/test_metrics_endpoints.py`
- `server/tests/unit/api/test_player_respawn_api.py`
- `server/tests/unit/api/test_player_respawn_handlers.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`

## Audit Trail

- EXTRACTED: 567 (78%)
- INFERRED: 156 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*