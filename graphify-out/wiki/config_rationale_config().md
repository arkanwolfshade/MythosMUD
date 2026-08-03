# config rationale config()

> 6 nodes

## Key Concepts

- **TestGetPlayerService** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_player_service_success()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_player_service_not_initialized()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_player_service() function.** (1 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_player_service() returns player service from container.** (1 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_player_service() raises error when service not initialized.** (1 connections) — `server/tests/unit/test_dependency_injection.py`

## Relationships

- [NPC Definitions Admin](NPC_Definitions_Admin.md) (3 shared connections)
- [command inventory models](command_inventory_models.md) (2 shared connections)
- [room game service](room_game_service.md) (1 shared connections)
- [profession game service](profession_game_service.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 13 (76%)
- INFERRED: 4 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*