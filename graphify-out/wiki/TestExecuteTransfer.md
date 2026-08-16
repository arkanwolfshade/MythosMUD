# TestExecuteTransfer

> 13 nodes

## Key Concepts

- **TestExecuteTransfer** (6 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_execute_transfer_to_container()** (6 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_execute_transfer_to_player()** (6 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestGetPlayerIdFromUser** (5 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_get_player_id_from_user_not_found()** (4 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_get_player_id_from_user_success()** (4 connections) — `server/tests/unit/api/test_container_helpers.py`
- **asyncio** (4 connections)
- **Test get_player_id_from_user raises exception when player not found.** (1 connections) — `server/tests/unit/api/test_container_helpers.py`
- **Test execute_transfer function.** (1 connections) — `server/tests/unit/api/test_container_helpers.py`
- **Test execute_transfer calls transfer_to_container for to_container direction.** (1 connections) — `server/tests/unit/api/test_container_helpers.py`
- **Test execute_transfer calls transfer_from_container for to_player direction.** (1 connections) — `server/tests/unit/api/test_container_helpers.py`
- **Test get_player_id_from_user function.** (1 connections) — `server/tests/unit/api/test_container_helpers.py`
- **Test get_player_id_from_user returns player ID.** (1 connections) — `server/tests/unit/api/test_container_helpers.py`

## Relationships

- [LootAllRequest](LootAllRequest.md) (6 shared connections)
- [ContainerService](ContainerService.md) (3 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (1 shared connections)

## Source Files

- `server/tests/unit/api/test_container_helpers.py`

## Audit Trail

- EXTRACTED: 24 (89%)
- INFERRED: 3 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*