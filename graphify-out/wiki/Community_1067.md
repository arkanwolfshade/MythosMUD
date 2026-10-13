# Community 1067

> 13 nodes

## Key Concepts

- **_compute_admin_status()** (12 connections) — `server/commands/admin_commands.py`
- **TestComputeAdminStatus** (7 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **.test_database_admin_with_no_user_manager()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **.test_falls_back_to_player_id_when_id_is_missing()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **.test_runtime_admin_overrides_database_false()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **.test_user_manager_lookup_error_falls_back_to_database_only()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **.test_not_admin_in_either_source()** (2 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **Determine (is_admin_database, is_admin_runtime, is_admin_effective) for a…** (1 connections) — `server/commands/admin_commands.py`
- **_compute_admin_status: extracted from _handle_admin_status_command in issue…** (1 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **No user_manager means runtime status can't be checked; effective follows…** (1 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **Effective status is true if EITHER source says so (session cache can grant it).** (1 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **A cache lookup failure must not crash the status command.** (1 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **Some player records expose player_id instead of id (see the getattr fallback).** (1 connections) — `server/tests/unit/commands/test_admin_commands.py`

## Relationships

- [Community 109](Community_109.md) (4 shared connections)
- [Community 42](Community_42.md) (1 shared connections)
- [Community 207](Community_207.md) (1 shared connections)
- [Community 136](Community_136.md) (1 shared connections)

## Source Files

- `server/commands/admin_commands.py`
- `server/tests/unit/commands/test_admin_commands.py`

## Audit Trail

- EXTRACTED: 21 (91%)
- INFERRED: 2 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*