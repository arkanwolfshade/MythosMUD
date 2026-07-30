# BaseCommand

> 207 nodes

## Key Concepts

- **TransferContainerRequest** (57 connections) — `server/api/container_models.py`
- **container_endpoints_basic.py** (50 connections) — `server/api/container_endpoints_basic.py`
- **container_helpers.py** (44 connections) — `server/api/container_helpers.py`
- **test_container_helpers.py** (43 connections) — `server/tests/unit/api/test_container_helpers.py`
- **transfer_items()** (25 connections) — `server/api/container_endpoints_basic.py`
- **open_container()** (23 connections) — `server/api/container_endpoints_basic.py`
- **TestTransferItems** (20 connections) — `server/tests/unit/api/test_containers.py`
- **close_container()** (19 connections) — `server/api/container_endpoints_basic.py`
- **get_player_id_from_user()** (19 connections) — `server/api/container_helpers.py`
- **handle_container_service_error()** (19 connections) — `server/api/container_helpers.py`
- **emit_transfer_event()** (17 connections) — `server/api/container_events.py`
- **get_container_service()** (16 connections) — `server/api/container_helpers.py`
- **CloseContainerRequest** (14 connections) — `server/api/container_models.py`
- **TestHandleContainerServiceError** (13 connections) — `server/tests/unit/api/test_container_helpers.py`
- **execute_transfer()** (12 connections) — `server/api/container_helpers.py`
- **container_models.py** (12 connections) — `server/api/container_models.py`
- **TestEmitTransferEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- **Request** (11 connections)
- **TestGetPlayerIdFromUser** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestValidateUserForOpenContainer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestApplyRateLimitingForOpenContainer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestValidateUserForTransfer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestApplyRateLimitingForTransfer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestExecuteTransfer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestValidateUserForCloseContainer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- *... and 182 more nodes in this community*

## Relationships

- [AbstractContextManager](AbstractContextManager.md) (128 shared connections)
- [. init ()](_init_%28%29.md) (36 shared connections)
- [APIRouter](APIRouter.md) (36 shared connections)
- [metrics](metrics.md) (34 shared connections)
- [DeadLetterMessage](DeadLetterMessage.md) (22 shared connections)
- [.get population stats()](get_population_stats%28%29.md) (20 shared connections)
- [test path validator](test_path_validator.md) (10 shared connections)
- [Player](Player.md) (7 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (5 shared connections)
- [test player event handlers state](test_player_event_handlers_state.md) (5 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (4 shared connections)
- [Lock](Lock.md) (3 shared connections)

## Source Files

- `server/api/container_endpoints_basic.py`
- `server/api/container_events.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 878 (82%)
- INFERRED: 187 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*