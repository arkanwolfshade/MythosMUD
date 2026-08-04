# commands follow rationale

> 196 nodes

## Key Concepts

- **RateLimitError** (76 connections) — `server/exceptions.py`
- **TransferContainerRequest** (57 connections) — `server/api/container_models.py`
- **container_endpoints_basic.py** (50 connections) — `server/api/container_endpoints_basic.py`
- **container_helpers.py** (44 connections) — `server/api/container_helpers.py`
- **test_container_helpers.py** (43 connections) — `server/tests/unit/api/test_container_helpers.py`
- **container_endpoints_loot.py** (36 connections) — `server/api/container_endpoints_loot.py`
- **transfer_items()** (25 connections) — `server/api/container_endpoints_basic.py`
- **open_container()** (23 connections) — `server/api/container_endpoints_basic.py`
- **close_container()** (19 connections) — `server/api/container_endpoints_basic.py`
- **get_player_id_from_user()** (19 connections) — `server/api/container_helpers.py`
- **handle_container_service_error()** (19 connections) — `server/api/container_helpers.py`
- **get_container_service()** (16 connections) — `server/api/container_helpers.py`
- **TestHandleContainerServiceError** (13 connections) — `server/tests/unit/api/test_container_helpers.py`
- **_convert_container_dict_to_container_data()** (12 connections) — `server/api/container_endpoints_basic.py`
- **execute_transfer()** (12 connections) — `server/api/container_helpers.py`
- **TestCreateErrorContext** (12 connections) — `server/tests/unit/api/test_container_helpers.py`
- **_convert_inventory_list_to_inventory_stacks()** (11 connections) — `server/api/container_endpoints_basic.py`
- **Request** (11 connections)
- **TestGetPlayerIdFromUser** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestValidateUserForOpenContainer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestApplyRateLimitingForOpenContainer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestValidateUserForTransfer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestApplyRateLimitingForTransfer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestExecuteTransfer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestValidateUserForCloseContainer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- *... and 171 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (190 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (43 shared connections)
- [player requests schemas](player_requests_schemas.md) (36 shared connections)
- [auth rationale access](auth_rationale_access.md) (31 shared connections)
- [NPC Combat](NPC_Combat.md) (8 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (7 shared connections)
- [Room Broadcast](Room_Broadcast.md) (7 shared connections)
- [command handler unified](command_handler_unified.md) (7 shared connections)
- [profession game service](profession_game_service.md) (7 shared connections)
- [Loot Generation](Loot_Generation.md) (6 shared connections)
- [Player Stats](Player_Stats.md) (5 shared connections)
- [Spell Validation](Spell_Validation.md) (4 shared connections)

## Source Files

- `server/api/container_endpoints_basic.py`
- `server/api/container_endpoints_loot.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/api/containers.py`
- `server/exceptions.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_containers.py`
- `server/tests/unit/test_exceptions.py`

## Audit Trail

- EXTRACTED: 892 (81%)
- INFERRED: 203 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*