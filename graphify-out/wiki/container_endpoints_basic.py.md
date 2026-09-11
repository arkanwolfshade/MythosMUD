# container_endpoints_basic.py

> 507 nodes

## Key Concepts

- **container_endpoints_basic.py** (62 connections) — `server/api/container_endpoints_basic.py`
- **LootAllRequest** (59 connections) — `server/api/container_models.py`
- **RateLimitError** (44 connections) — `server/exceptions.py`
- **api/container_helpers.py** (42 connections) — `server/api/container_helpers.py`
- **test_container_helpers.py** (42 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TransferContainerRequest** (41 connections) — `server/api/container_models.py`
- **loot_all_items()** (34 connections) — `server/api/container_endpoints_loot.py`
- **container_endpoints_loot.py** (31 connections) — `server/api/container_endpoints_loot.py`
- **transfer_items()** (28 connections) — `server/api/container_endpoints_basic.py`
- **open_container()** (27 connections) — `server/api/container_endpoints_basic.py`
- **container_events.py** (26 connections) — `server/api/container_events.py`
- **test_containers.py** (26 connections) — `server/tests/unit/api/test_containers.py`
- **test_container_events.py** (25 connections) — `server/tests/unit/api/test_container_events.py`
- **close_container()** (23 connections) — `server/api/container_endpoints_basic.py`
- **test_container_helpers_loot.py** (22 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **transfer_all_items_from_container()** (21 connections) — `server/api/container_helpers.py`
- **asyncio** (21 connections)
- **get_player_id_from_user()** (19 connections) — `server/api/container_helpers.py`
- **handle_container_service_error()** (19 connections) — `server/api/container_helpers.py`
- **ConnectionManager** (19 connections)
- **emit_loot_all_event()** (17 connections) — `server/api/container_events.py`
- **emit_transfer_event()** (17 connections) — `server/api/container_events.py`
- **create_error_context()** (17 connections) — `server/api/container_helpers.py`
- **get_container_and_player_for_loot_all()** (17 connections) — `server/api/container_helpers.py`
- **asyncio** (17 connections)
- *... and 482 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (93 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (42 shared connections)
- [User](User.md) (30 shared connections)
- [get_logger](get_logger.md) (25 shared connections)
- [ContainerService](ContainerService.md) (25 shared connections)
- [PlayerService](PlayerService.md) (16 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (12 shared connections)
- [ConnectionManager](ConnectionManager.md) (12 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (10 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (8 shared connections)
- [test_rate_limiter_utils.py](test_rate_limiter_utils.py.md) (6 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (6 shared connections)

## Source Files

- `server/api/container_endpoints_basic.py`
- `server/api/container_endpoints_loot.py`
- `server/api/container_events.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/exceptions.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/api/test_container_events_loot.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/api/test_container_models.py`
- `server/tests/unit/api/test_containers.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/utils/rate_limiter.py`

## Audit Trail

- EXTRACTED: 1234 (91%)
- INFERRED: 118 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*