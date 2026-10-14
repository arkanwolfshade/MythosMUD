# handle_cleanse_command

> 17 nodes

## Key Concepts

- **handle_cleanse_command()** (14 connections) — `server/commands/cleanse_command.py`
- **test_cleanse_command.py** (13 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **CorruptionActionOnCooldownError** (10 connections) — `server/services/corruption_service.py`
- **asyncio** (5 connections)
- **test_handle_cleanse_command_cooldown()** (4 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **test_handle_cleanse_command_cooldown_no_expiry()** (4 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **mock_request()** (3 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **test_handle_cleanse_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **test_handle_cleanse_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **test_handle_cleanse_command_success()** (3 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **fixture** (3 connections)
- **mock_persistence()** (2 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **mock_player()** (2 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **Undertake a cleansing rite to pare back accrued corruption.** (1 connections) — `server/commands/cleanse_command.py`
- **Raised when a corruption recovery action is attempted during its cooldown.** (1 connections) — `server/services/corruption_service.py`
- **Unit tests for the cleanse command handler (#804).** (1 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **Create a mock request with app state and container.** (1 connections) — `server/tests/unit/commands/test_cleanse_command.py`

## Relationships

- [cleanse_command.py](cleanse_command.py.md) (5 shared connections)
- [CorruptionService](CorruptionService.md) (3 shared connections)
- [.apply_corruption_adjustment](apply_corruption_adjustment.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [command_service.py](command_service.py.md) (1 shared connections)

## Source Files

- `server/commands/cleanse_command.py`
- `server/services/corruption_service.py`
- `server/tests/unit/commands/test_cleanse_command.py`

## Audit Trail

- EXTRACTED: 39 (89%)
- INFERRED: 5 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*