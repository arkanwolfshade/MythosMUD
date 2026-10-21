# test_look_player.py

> 203 nodes · cohesion 0.02

## Key Concepts

- **api/container_helpers.py** (45 connections) — `server/api/container_helpers.py`
- **test_container_helpers.py** (43 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TransferContainerRequest** (40 connections) — `server/api/container_models.py`
- **transfer_items()** (28 connections) — `server/api/container_endpoints_basic.py`
- **open_container()** (27 connections) — `server/api/container_endpoints_basic.py`
- **get_container_service()** (26 connections) — `server/api/container_helpers.py`
- **test_containers.py** (26 connections) — `server/tests/unit/api/test_containers.py`
- **close_container()** (23 connections) — `server/api/container_endpoints_basic.py`
- **handle_container_service_error()** (20 connections) — `server/api/container_helpers.py`
- **get_player_id_from_user()** (19 connections) — `server/api/container_helpers.py`
- **asyncio** (17 connections)
- **container_models.py** (16 connections) — `server/api/container_models.py`
- **OpenContainerRequest** (14 connections) — `server/api/container_models.py`
- **get_current_user()** (13 connections) — `docs/examples/logging/fastapi_integration.py`
- **execute_transfer()** (11 connections) — `server/api/container_helpers.py`
- **CloseContainerRequest** (11 connections) — `server/api/container_models.py`
- **TestOpenContainer** (11 connections) — `server/tests/unit/api/test_containers.py`
- **TestTransferItems** (11 connections) — `server/tests/unit/api/test_containers.py`
- **apply_rate_limiting_for_close_container()** (10 connections) — `server/api/container_helpers.py`
- **apply_rate_limiting_for_open_container()** (10 connections) — `server/api/container_helpers.py`
- **apply_rate_limiting_for_transfer()** (10 connections) — `server/api/container_helpers.py`
- **validate_user_for_close_container()** (10 connections) — `server/api/container_helpers.py`
- **validate_user_for_open_container()** (10 connections) — `server/api/container_helpers.py`
- **validate_user_for_transfer()** (10 connections) — `server/api/container_helpers.py`
- **test_container_models.py** (10 connections) — `server/tests/unit/api/test_container_models.py`
- *... and 178 more nodes in this community*

## Relationships

- [CombatParticipant](CombatParticipant.md) (27 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (24 shared connections)
- [generate_arkham_grid.py](generate_arkham_grid.py.md) (23 shared connections)
- [AttributeError](AttributeError.md) (20 shared connections)
- [test_command_factories.py](test_command_factories.py.md) (19 shared connections)
- [test_logging_handlers.py](test_logging_handlers.py.md) (18 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (16 shared connections)
- [useGameConnectionRefactored.ts](useGameConnectionRefactored.ts.md) (16 shared connections)
- [logging_file_setup.py](logging_file_setup.py.md) (12 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (10 shared connections)
- [test_npc_event_handlers.py](test_npc_event_handlers.py.md) (7 shared connections)
- [test_npc_startup_service.py](test_npc_startup_service.py.md) (6 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/api/container_endpoints_basic.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/services/container_service.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_models.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 528 (91%)
- INFERRED: 54 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*