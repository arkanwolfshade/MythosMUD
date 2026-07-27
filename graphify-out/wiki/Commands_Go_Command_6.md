# Commands Go Command

> 10 nodes · cohesion 0.20

## Key Concepts

- **_validate_exit()** (9 connections) — `server/commands/go_command.py`
- **test_validate_exit_direction_not_found()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_validate_exit_no_exits()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_validate_exit_success()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_validate_exit_target_room_not_found()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **Validate that exit exists and target room is valid.** (1 connections) — `server/commands/go_command.py`
- **Test _validate_exit returns None when room has no exits.** (1 connections) — `server/tests/unit/commands/test_go_command.py`
- **Test _validate_exit returns None when direction not in exits.** (1 connections) — `server/tests/unit/commands/test_go_command.py`
- **Test _validate_exit returns None when target room doesn't exist.** (1 connections) — `server/tests/unit/commands/test_go_command.py`
- **Test _validate_exit returns target room ID on success.** (1 connections) — `server/tests/unit/commands/test_go_command.py`

## Relationships

- [[Commands Go Command]] (7 shared connections)
- [[Alias Expansion Logic]] (1 shared connections)

## Source Files

- `server/commands/go_command.py`
- `server/tests/unit/commands/test_go_command.py`

## Audit Trail

- EXTRACTED: 26 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
