# _apply_stat_change_and_build_result

> 16 nodes

## Key Concepts

- **validate_admin_permission()** (20 connections) — `server/commands/admin_permission_utils.py`
- **test_admin_permission_utils.py** (12 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- **asyncio** (6 connections)
- **_BrokenAdminPlayer** (4 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- **test_validate_admin_permission_attribute_error()** (4 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- **test_validate_admin_permission_logs_secondary_failure()** (4 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- **test_validate_admin_permission_missing_is_admin_attr()** (4 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- **test_validate_admin_permission_granted()** (3 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- **test_validate_admin_permission_is_admin_false()** (3 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- **test_validate_admin_permission_no_player()** (3 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- **.is_admin()** (2 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- **mock_admin_logger()** (2 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- **Any** (1 connections)
- **fixture** (1 connections)
- **Validate that a player has admin permissions. Args: player: Player object to…** (1 connections) — `server/commands/admin_permission_utils.py`
- **Unit tests for admin permission validation.** (1 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`

## Relationships

- [pytest.md](pytest.md.md) (7 shared connections)
- [ConnectionCleaner](ConnectionCleaner.md) (3 shared connections)
- [RoomService](RoomService.md) (1 shared connections)
- [player_effect_repository.py](player_effect_repository.py.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [test_character_creation_service.py](test_character_creation_service.py.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/commands/admin_permission_utils.py`
- `server/tests/unit/commands/test_admin_permission_utils.py`

## Audit Trail

- EXTRACTED: 41 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*