# Commands Go Command

> 10 nodes · cohesion 0.20

## Key Concepts

- **_execute_movement()** (10 connections) — `server/commands/go_command.py`
- **test_execute_movement_error_handling()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_execute_movement_failure()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_execute_movement_fallback_service()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_execute_movement_success()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **Execute player movement using movement service.** (1 connections) — `server/commands/go_command.py`
- **Test _execute_movement successfully moves player.** (1 connections) — `server/tests/unit/commands/test_go_command.py`
- **Test _execute_movement handles movement failure.** (1 connections) — `server/tests/unit/commands/test_go_command.py`
- **Test _execute_movement handles errors gracefully.** (1 connections) — `server/tests/unit/commands/test_go_command.py`
- **Test _execute_movement uses fallback service when container not available.** (1 connections) — `server/tests/unit/commands/test_go_command.py`

## Relationships

- [[Commands Go Command]] (8 shared connections)
- [[Alias Expansion Logic]] (1 shared connections)

## Source Files

- `server/commands/go_command.py`
- `server/tests/unit/commands/test_go_command.py`

## Audit Trail

- EXTRACTED: 27 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
