# Test User Manager

> 32 nodes

## Key Concepts

- **asyncio** (15 connections)
- **Test is_player_muted() returns True when player is muted.** (4 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_add_admin_no_container_duplicate()** (3 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_add_admin_no_persistence()** (3 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_add_admin_player_not_found()** (3 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_add_admin_success()** (3 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_is_admin_cached()** (3 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_is_admin_no_persistence()** (3 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_is_admin_not_cached()** (3 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_is_player_muted_async_false()** (3 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_is_player_muted_async_true()** (3 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_load_player_mutes_async_cache_valid()** (3 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_load_player_mutes_batch_all_cached()** (3 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_load_player_mutes_batch_empty_list()** (3 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_remove_admin_no_persistence()** (3 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_remove_admin_player_not_found()** (3 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_remove_admin_success()** (3 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_is_player_muted_false()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **test_is_player_muted_true()** (2 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test add_admin() handles missing persistence (#679: injected, not via…** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test add_admin() handles player not found.** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test remove_admin() handles missing persistence (#679: injected, not via…** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test remove_admin() handles player not found.** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test is_admin() returns False when persistence not available (#679: injected).** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- **Test load_player_mutes_async() uses cache when valid.** (1 connections) — `server/tests/unit/services/test_user_manager.py`
- *... and 7 more nodes in this community*

## Relationships

- [Test User Manager](Test_User_Manager.md) (17 shared connections)

## Source Files

- `server/tests/unit/services/test_user_manager.py`

## Audit Trail

- EXTRACTED: 49 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*