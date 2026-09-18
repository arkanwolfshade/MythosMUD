# Community 783

> 21 nodes

## Key Concepts

- **handle_cleanse_command()** (14 connections) — `server/commands/cleanse_command.py`
- **test_cleanse_command.py** (13 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **CorruptionActionOnCooldownError** (10 connections) — `server/services/corruption_service.py`
- **CorruptionActionError** (5 connections) — `server/services/corruption_service.py`
- **test_handle_cleanse_command_cooldown()** (5 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **test_handle_cleanse_command_cooldown_no_expiry()** (5 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **asyncio** (5 connections)
- **test_handle_cleanse_command_success()** (4 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **mock_request()** (3 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **test_handle_cleanse_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **test_handle_cleanse_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **fixture** (3 connections)
- **mock_persistence()** (2 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **mock_player()** (2 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **AliasStorage** (1 connections)
- **RuntimeError** (1 connections)
- **Undertake a cleansing rite to pare back accrued corruption.** (1 connections) — `server/commands/cleanse_command.py`
- **Base error for corruption action operations.** (1 connections) — `server/services/corruption_service.py`
- **Raised when a corruption recovery action is attempted during its cooldown.** (1 connections) — `server/services/corruption_service.py`
- **Unit tests for the cleanse command handler (#804).** (1 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **Create a mock request with app state and container.** (1 connections) — `server/tests/unit/commands/test_cleanse_command.py`

## Relationships

- [Community 514](Community_514.md) (5 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (4 shared connections)
- [Community 520](Community_520.md) (3 shared connections)
- [Community 38](Community_38.md) (3 shared connections)
- [Community 297](Community_297.md) (2 shared connections)
- [Community 442](Community_442.md) (1 shared connections)

## Source Files

- `server/commands/cleanse_command.py`
- `server/services/corruption_service.py`
- `server/tests/unit/commands/test_cleanse_command.py`

## Audit Trail

- EXTRACTED: 43 (84%)
- INFERRED: 8 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*