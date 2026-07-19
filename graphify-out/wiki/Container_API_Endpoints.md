# Container API Endpoints

> 250 nodes · cohesion 0.02

## Key Concepts

- **TransferContainerRequest** (82 connections) — `server/api/container_models.py`
- **container_endpoints_basic.py** (50 connections) — `server/api/container_endpoints_basic.py`
- **container_helpers.py** (42 connections) — `server/api/container_helpers.py`
- **test_container_helpers.py** (39 connections) — `server/tests/unit/api/test_container_helpers.py`
- **container_endpoints_loot.py** (35 connections) — `server/api/container_endpoints_loot.py`
- **OpenContainerRequest** (30 connections) — `server/api/container_models.py`
- **CloseContainerRequest** (27 connections) — `server/api/container_models.py`
- **transfer_items()** (25 connections) — `server/api/container_endpoints_basic.py`
- **open_container()** (23 connections) — `server/api/container_endpoints_basic.py`
- **container_events.py** (20 connections) — `server/api/container_events.py`
- **TestTransferItems** (20 connections) — `server/tests/unit/api/test_containers.py`
- **close_container()** (19 connections) — `server/api/container_endpoints_basic.py`
- **get_player_id_from_user()** (19 connections) — `server/api/container_helpers.py`
- **handle_container_service_error()** (19 connections) — `server/api/container_helpers.py`
- **emit_loot_all_event()** (17 connections) — `server/api/container_events.py`
- **emit_transfer_event()** (17 connections) — `server/api/container_events.py`
- **get_container_and_player_for_loot_all()** (17 connections) — `server/api/container_helpers.py`
- **get_container_service()** (17 connections) — `server/api/container_helpers.py`
- **_emit_close_container_event()** (14 connections) — `server/api/container_events.py`
- **User** (14 connections) — `server/api/container_helpers.py`
- **TestHandleContainerServiceError** (13 connections) — `server/tests/unit/api/test_container_helpers.py`
- **Request** (13 connections) — `server/api/container_helpers.py`
- **_convert_container_dict_to_container_data()** (12 connections) — `server/api/container_endpoints_basic.py`
- **TestEmitCloseContainerEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitTransferEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- *... and 225 more nodes in this community*

## Relationships

- [[Container Exception Handlers]] (116 shared connections)
- [[Loot All Endpoint]] (45 shared connections)
- [[Standardized Error Responses]] (36 shared connections)
- [[Container Loot Helpers]] (28 shared connections)
- [[NPC Admin API]] (25 shared connections)
- [[Container Open Events]] (23 shared connections)
- [[API Test Fixtures]] (17 shared connections)
- [[Admin NPC Schemas]] (16 shared connections)
- [[Inventory Service Helpers]] (9 shared connections)
- [[Container Component Capacity]] (6 shared connections)
- [[Room Occupant Events]] (4 shared connections)
- [[Database Manager Tests]] (3 shared connections)

## Source Files

- `server/api/container_endpoints_basic.py`
- `server/api/container_endpoints_loot.py`
- `server/api/container_events.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/schemas/game/weapon.py`
- `server/services/container_websocket_events.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 1126 (80%)
- INFERRED: 290 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
