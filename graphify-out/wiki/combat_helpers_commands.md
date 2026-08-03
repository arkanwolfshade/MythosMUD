# combat helpers commands

> 18 nodes

## Key Concepts

- **test_user.py** (11 connections) — `server/tests/unit/models/test_user.py`
- **test_user_repr()** (3 connections) — `server/tests/unit/models/test_user.py`
- **test_user_is_authenticated_when_active()** (3 connections) — `server/tests/unit/models/test_user.py`
- **test_user_is_authenticated_when_inactive()** (3 connections) — `server/tests/unit/models/test_user.py`
- **test_user_get_display_name_with_display_name()** (3 connections) — `server/tests/unit/models/test_user.py`
- **test_user_get_display_name_with_empty_display_name()** (3 connections) — `server/tests/unit/models/test_user.py`
- **test_user_get_display_name_without_display_name()** (3 connections) — `server/tests/unit/models/test_user.py`
- **test_user_get_display_name_falls_back_to_id()** (3 connections) — `server/tests/unit/models/test_user.py`
- **test_user_get_display_name_all_empty()** (3 connections) — `server/tests/unit/models/test_user.py`
- **Unit tests for the User model.  Tests the User model methods including authentic** (1 connections) — `server/tests/unit/models/test_user.py`
- **Test __repr__ returns expected string format.** (1 connections) — `server/tests/unit/models/test_user.py`
- **Test is_authenticated returns True when user is active.** (1 connections) — `server/tests/unit/models/test_user.py`
- **Test is_authenticated returns False when user is inactive.** (1 connections) — `server/tests/unit/models/test_user.py`
- **Test get_display_name returns display_name when set.** (1 connections) — `server/tests/unit/models/test_user.py`
- **Test get_display_name falls back to username when display_name is empty.** (1 connections) — `server/tests/unit/models/test_user.py`
- **Test get_display_name falls back to username when display_name not set.** (1 connections) — `server/tests/unit/models/test_user.py`
- **Test get_display_name falls back to id when username is not set.** (1 connections) — `server/tests/unit/models/test_user.py`
- **Test get_display_name handles case where all fields are empty/missing.** (1 connections) — `server/tests/unit/models/test_user.py`

## Relationships

- [Exception Containers](Exception_Containers.md) (9 shared connections)
- [admin auth service](admin_auth_service.md) (1 shared connections)

## Source Files

- `server/tests/unit/models/test_user.py`

## Audit Trail

- EXTRACTED: 44 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*