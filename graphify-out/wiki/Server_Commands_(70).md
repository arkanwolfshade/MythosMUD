# Server Commands (70)

> 12 nodes

## Key Concepts

- **_get_profession_info()** (10 connections) — `server/commands/status_commands.py`
- **test_get_profession_info_error_handling()** (4 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_profession_info_no_profession_id()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_profession_info_player_dict_no_profession_id()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_profession_info_with_profession()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_profession_info_profession_not_found()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **Get profession information for a player.      Args:         player: Player objec** (1 connections) — `server/commands/status_commands.py`
- **Test _get_profession_info returns None values when profession_id is 0.** (1 connections) — `server/tests/unit/commands/test_status_commands.py`
- **Test _get_profession_info handles player as dict with no profession_id.** (1 connections) — `server/tests/unit/commands/test_status_commands.py`
- **Test _get_profession_info returns profession info when profession exists.** (1 connections) — `server/tests/unit/commands/test_status_commands.py`
- **Test _get_profession_info returns None values when profession not found.** (1 connections) — `server/tests/unit/commands/test_status_commands.py`
- **Test _get_profession_info handles errors gracefully.** (1 connections) — `server/tests/unit/commands/test_status_commands.py`

## Relationships

- [Server Commands (52)](Server_Commands_%2852%29.md) (6 shared connections)
- [Server Commands (69)](Server_Commands_%2869%29.md) (3 shared connections)
- [Server Services (35)](Server_Services_%2835%29.md) (1 shared connections)

## Source Files

- `server/commands/status_commands.py`
- `server/tests/unit/commands/test_status_commands.py`

## Audit Trail

- EXTRACTED: 31 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*