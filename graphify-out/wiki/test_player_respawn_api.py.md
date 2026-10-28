# test_player_respawn_api.py

> 42 nodes · cohesion 0.08

## Key Concepts

- **cleanse_command.py** (23 connections) — `server/commands/cleanse_command.py`
- **handle_cleanse_command()** (14 connections) — `server/commands/cleanse_command.py`
- **test_cleanse_command.py** (13 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **CorruptionActionOnCooldownError** (10 connections) — `server/services/corruption_service.py`
- **CleansePersistence** (8 connections) — `server/commands/cleanse_command.py`
- **Protocol** (6 connections)
- **CleanseTargetPlayer** (5 connections) — `server/commands/cleanse_command.py`
- **asyncio** (5 connections)
- **CleanseApp** (4 connections) — `server/commands/cleanse_command.py`
- **CleanseContainer** (4 connections) — `server/commands/cleanse_command.py`
- **CleanseRequest** (4 connections) — `server/commands/cleanse_command.py`
- **_format_cooldown_message()** (4 connections) — `server/commands/cleanse_command.py`
- **_resolve_persistence()** (4 connections) — `server/commands/cleanse_command.py`
- **test_handle_cleanse_command_cooldown()** (4 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **test_handle_cleanse_command_cooldown_no_expiry()** (4 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **CleanseAppState** (3 connections) — `server/commands/cleanse_command.py`
- **.get_player_by_id()** (3 connections) — `server/commands/cleanse_command.py`
- **mock_request()** (3 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **fixture** (3 connections)
- **test_handle_cleanse_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **test_handle_cleanse_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **test_handle_cleanse_command_success()** (3 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **.get_player_by_name()** (2 connections) — `server/commands/cleanse_command.py`
- **.save_player()** (2 connections) — `server/commands/cleanse_command.py`
- **.app()** (2 connections) — `server/commands/cleanse_command.py`
- *... and 17 more nodes in this community*

## Relationships

- [reset_database](reset_database.md) (10 shared connections)
- [command_parser.py](command_parser.py.md) (5 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [NPCCombatLucidity](NPCCombatLucidity.md) (2 shared connections)
- [CommandFactory](CommandFactory.md) (1 shared connections)
- [.load_room_data](load_room_data.md) (1 shared connections)

## Source Files

- `server/commands/cleanse_command.py`
- `server/services/corruption_service.py`
- `server/tests/unit/commands/test_cleanse_command.py`

## Audit Trail

- EXTRACTED: 87 (95%)
- INFERRED: 5 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*