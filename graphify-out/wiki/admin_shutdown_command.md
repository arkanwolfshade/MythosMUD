# admin shutdown command

> 112 nodes

## Key Concepts

- **character_creation.py** (47 connections) — `server/api/character_creation.py`
- **roll_character_stats()** (23 connections) — `server/api/character_creation.py`
- **test_character_creation.py** (22 connections) — `server/tests/unit/api/test_character_creation.py`
- **RollStatsRequest** (20 connections) — `server/schemas/players/player_requests.py`
- **create_character_with_stats()** (18 connections) — `server/api/character_creation.py`
- **ProfessionService** (17 connections) — `server/game/profession_service.py`
- **CreateCharacterRequest** (17 connections) — `server/schemas/players/player_requests.py`
- **_roll_stats_with_profession_preview()** (14 connections) — `server/api/character_creation.py`
- **_execute_create_character()** (13 connections) — `server/api/character_creation.py`
- **validate_character_stats()** (13 connections) — `server/api/character_creation.py`
- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **TestRollCharacterStats** (13 connections) — `server/tests/unit/api/test_character_creation.py`
- **character_creation.py** (10 connections) — `server/schemas/players/character_creation.py`
- **CreateCharacterResponse** (10 connections) — `server/schemas/players/character_creation.py`
- **RolledStats** (10 connections) — `server/schemas/players/stat_values.py`
- **TestCreateCharacterWithStats** (10 connections) — `server/tests/unit/api/test_character_creation.py`
- **_convert_stat_summary_to_stat_summary_model()** (9 connections) — `server/api/character_creation.py`
- **RollStatsResponse** (9 connections) — `server/schemas/players/character_creation.py`
- **ValidateStatsResponse** (9 connections) — `server/schemas/players/character_creation.py`
- **TestValidateCharacterStats** (9 connections) — `server/tests/unit/api/test_character_creation.py`
- **_check_shutdown_status()** (8 connections) — `server/api/character_creation.py`
- **_roll_stats_raw()** (8 connections) — `server/api/character_creation.py`
- **_roll_stats_with_class()** (8 connections) — `server/api/character_creation.py`
- **StatSummary** (8 connections) — `server/schemas/players/character_creation.py`
- **_stats_to_rolled_stats()** (7 connections) — `server/api/character_creation.py`
- *... and 87 more nodes in this community*

## Relationships

- [AbstractContextManager](AbstractContextManager.md) (22 shared connections)
- [metrics](metrics.md) (17 shared connections)
- [test player event handlers state](test_player_event_handlers_state.md) (13 shared connections)
- [append unique valid occupant()](append_unique_valid_occupant%28%29.md) (12 shared connections)
- [. init ()](_init_%28%29.md) (11 shared connections)
- [Room](Room.md) (11 shared connections)
- [.initialize()](initialize%28%29.md) (7 shared connections)
- [Player](Player.md) (6 shared connections)
- [character creation](character_creation.md) (6 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (5 shared connections)
- [emit close container event()](emit_close_container_event%28%29.md) (4 shared connections)
- [Any](Any.md) (4 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/commands/admin_shutdown_command.py`
- `server/game/profession_service.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/stat_values.py`
- `server/tests/unit/api/test_character_creation.py`

## Audit Trail

- EXTRACTED: 501 (94%)
- INFERRED: 33 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*