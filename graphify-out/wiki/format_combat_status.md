# format_combat_status

> 15 nodes

## Key Concepts

- **format_combat_status()** (6 connections) — `server/commands/combat_helpers.py`
- **get_combat_target()** (6 connections) — `server/commands/combat_helpers.py`
- **test_combat_helpers.py** (6 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **test_format_combat_status_in_combat()** (3 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **test_format_combat_status_not_in_combat()** (3 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **test_get_combat_target()** (3 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **test_get_combat_target_not_found()** (3 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **Any** (2 connections)
- **Produce a human-readable combat status string. This helper is retained for…** (1 connections) — `server/commands/combat_helpers.py`
- **Resolve a combat target by name. The current implementation is intentionally…** (1 connections) — `server/commands/combat_helpers.py`
- **Unit tests for combat command helper functions. Tests helper functions in…** (1 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **Test format_combat_status() formats combat status.** (1 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **Test format_combat_status() handles player not in combat.** (1 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **Test get_combat_target() finds target.** (1 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **Test get_combat_target() returns None when target not found.** (1 connections) — `server/tests/unit/commands/test_combat_helpers.py`

## Relationships

- [CombatCommandHandler](CombatCommandHandler.md) (3 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (2 shared connections)

## Source Files

- `server/commands/combat_helpers.py`
- `server/tests/unit/commands/test_combat_helpers.py`

## Audit Trail

- EXTRACTED: 18 (82%)
- INFERRED: 4 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*