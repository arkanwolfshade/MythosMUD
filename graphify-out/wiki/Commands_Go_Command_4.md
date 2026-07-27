# Commands Go Command

> 11 nodes · cohesion 0.20

## Key Concepts

- **_validate_player_posture()** (10 connections) — `server/commands/go_command.py`
- **test_validate_player_posture_get_stats_error()** (4 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_validate_player_posture_lying()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_validate_player_posture_no_get_stats()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_validate_player_posture_sitting()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_validate_player_posture_standing()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **Test _validate_player_posture returns False for sitting player.** (2 connections) — `server/tests/unit/commands/test_go_command.py`
- **Validate that player is in a valid posture for movement.** (1 connections) — `server/commands/go_command.py`
- **Test _validate_player_posture returns True for standing player.** (1 connections) — `server/tests/unit/commands/test_go_command.py`
- **Test _validate_player_posture handles player without get_stats.** (1 connections) — `server/tests/unit/commands/test_go_command.py`
- **Test _validate_player_posture handles get_stats errors.** (1 connections) — `server/tests/unit/commands/test_go_command.py`

## Relationships

- [[Commands Go Command]] (8 shared connections)
- [[Alias Expansion Logic]] (1 shared connections)
- [[Services Service Room]] (1 shared connections)

## Source Files

- `server/commands/go_command.py`
- `server/tests/unit/commands/test_go_command.py`

## Audit Trail

- EXTRACTED: 31 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
