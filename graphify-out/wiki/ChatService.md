# ChatService

> 128 nodes

## Key Concepts

- **container_endpoints_basic.py** (64 connections) — `server/api/container_endpoints_basic.py`
- **test_container_helpers.py** (44 connections) — `server/tests/unit/api/test_container_helpers.py`
- **api/container_helpers.py** (43 connections) — `server/api/container_helpers.py`
- **test_containers.py** (29 connections) — `server/tests/unit/api/test_containers.py`
- **transfer_items()** (28 connections) — `server/api/container_endpoints_basic.py`
- **open_container()** (27 connections) — `server/api/container_endpoints_basic.py`
- **close_container()** (23 connections) — `server/api/container_endpoints_basic.py`
- **get_player_id_from_user()** (19 connections) — `server/api/container_helpers.py`
- **asyncio** (17 connections)
- **get_container_service()** (16 connections) — `server/api/container_helpers.py`
- **OpenContainerRequest** (13 connections) — `server/api/container_models.py`
- **_convert_container_dict_to_container_data()** (12 connections) — `server/api/container_endpoints_basic.py`
- **get_async_persistence()** (12 connections) — `server/dependencies.py`
- **TestOpenContainer** (11 connections) — `server/tests/unit/api/test_containers.py`
- **TestTransferItems** (11 connections) — `server/tests/unit/api/test_containers.py`
- **execute_transfer()** (11 connections) — `server/api/container_helpers.py`
- **Request** (11 connections)
- **CloseContainerRequest** (10 connections) — `server/api/container_models.py`
- **_build_container_data_from_dict()** (10 connections) — `server/api/container_endpoints_basic.py`
- **apply_rate_limiting_for_close_container()** (10 connections) — `server/api/container_helpers.py`
- **apply_rate_limiting_for_loot_all()** (10 connections) — `server/api/container_helpers.py`
- **apply_rate_limiting_for_open_container()** (10 connections) — `server/api/container_helpers.py`
- **apply_rate_limiting_for_transfer()** (10 connections) — `server/api/container_helpers.py`
- **validate_user_for_close_container()** (10 connections) — `server/api/container_helpers.py`
- **validate_user_for_loot_all()** (10 connections) — `server/api/container_helpers.py`
- *... and 103 more nodes in this community*

## Relationships

- [ValidationError](ValidationError.md) (34 shared connections)
- [test_nats_service.py](test_nats_service.py.md) (19 shared connections)
- [NATSServicePoolMixin](NATSServicePoolMixin.md) (16 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (15 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (15 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (15 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (15 shared connections)
- [ContainerComponent](ContainerComponent.md) (12 shared connections)
- [dialogue_definitions_api.py](dialogue_definitions_api.py.md) (10 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (9 shared connections)
- [_handle_admin_set_stat_command](_handle_admin_set_stat_command.md) (9 shared connections)
- [P7 · Rulings — complete](P7_·_Rulings_—_complete.md) (6 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/api/container_endpoints_basic.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/dependencies.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 471 (96%)
- INFERRED: 21 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*