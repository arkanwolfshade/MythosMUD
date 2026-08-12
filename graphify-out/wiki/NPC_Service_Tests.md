# NPC Service Tests

> 187 nodes

## Key Concepts

- **TransferContainerRequest** (57 connections) — `server/api/container_models.py`
- **container_endpoints_basic.py** (49 connections) — `server/api/container_endpoints_basic.py`
- **container_helpers.py** (44 connections) — `server/api/container_helpers.py`
- **test_container_helpers.py** (43 connections) — `server/tests/unit/api/test_container_helpers.py`
- **transfer_items()** (25 connections) — `server/api/container_endpoints_basic.py`
- **open_container()** (23 connections) — `server/api/container_endpoints_basic.py`
- **close_container()** (19 connections) — `server/api/container_endpoints_basic.py`
- **get_player_id_from_user()** (19 connections) — `server/api/container_helpers.py`
- **handle_container_service_error()** (19 connections) — `server/api/container_helpers.py`
- **emit_transfer_event()** (17 connections) — `server/api/container_events.py`
- **get_container_service()** (16 connections) — `server/api/container_helpers.py`
- **_emit_close_container_event()** (14 connections) — `server/api/container_events.py`
- **TestHandleContainerServiceError** (13 connections) — `server/tests/unit/api/test_container_helpers.py`
- **_convert_container_dict_to_container_data()** (12 connections) — `server/api/container_endpoints_basic.py`
- **execute_transfer()** (12 connections) — `server/api/container_helpers.py`
- **_convert_inventory_list_to_inventory_stacks()** (11 connections) — `server/api/container_endpoints_basic.py`
- **Request** (11 connections)
- **ContainerLootAllResponse** (11 connections) — `server/schemas/containers/container.py`
- **TestApplyRateLimitingForTransfer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestExecuteTransfer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **validate_user_for_open_container()** (10 connections) — `server/api/container_helpers.py`
- **apply_rate_limiting_for_open_container()** (10 connections) — `server/api/container_helpers.py`
- **validate_user_for_transfer()** (10 connections) — `server/api/container_helpers.py`
- **apply_rate_limiting_for_transfer()** (10 connections) — `server/api/container_helpers.py`
- **validate_user_for_close_container()** (10 connections) — `server/api/container_helpers.py`
- *... and 162 more nodes in this community*

## Relationships

- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (98 shared connections)
- [Combat Player Broadcasts](Combat_Player_Broadcasts.md) (63 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (49 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (25 shared connections)
- [Player Effects API](Player_Effects_API.md) (13 shared connections)
- [Magic Command Handlers](Magic_Command_Handlers.md) (5 shared connections)
- [Client Event Store](Client_Event_Store.md) (5 shared connections)
- [Game Terminal Panels](Game_Terminal_Panels.md) (5 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (4 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (4 shared connections)
- [Combat NPC Lookup](Combat_NPC_Lookup.md) (3 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (3 shared connections)

## Source Files

- `server/api/container_endpoints_basic.py`
- `server/api/container_endpoints_loot.py`
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

- EXTRACTED: 831 (89%)
- INFERRED: 98 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*