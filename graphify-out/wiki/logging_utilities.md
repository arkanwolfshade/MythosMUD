# logging utilities

> 13 nodes

## Key Concepts

- **handle_status_command()** (18 connections) — `server/commands/status_commands.py`
- **status_commands.py** (16 connections) — `server/commands/status_commands.py`
- **handle_whoami_command()** (12 connections) — `server/commands/status_commands.py`
- **_build_base_status_lines()** (11 connections) — `server/commands/status_commands.py`
- **_get_combat_status()** (9 connections) — `server/commands/status_commands.py`
- **Any** (7 connections)
- **test_build_base_status_lines_in_combat()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **Status command handlers for MythosMUD.  This module contains handlers for status** (1 connections) — `server/commands/status_commands.py`
- **Check if player is in combat.      Args:         app: FastAPI app instance** (1 connections) — `server/commands/status_commands.py`
- **Build base status lines for the status command.      Args:         player: Playe** (1 connections) — `server/commands/status_commands.py`
- **Handle the status command for showing player status.      Args:         command_** (1 connections) — `server/commands/status_commands.py`
- **Handle the whoami command as an alias for status.      Mirrors handle_status_com** (1 connections) — `server/commands/status_commands.py`
- **Test _build_base_status_lines shows combat status correctly.** (1 connections) — `server/tests/unit/commands/test_status_commands.py`

## Relationships

- [status commands](status_commands.md) (16 shared connections)
- [HallucinationFrequencyService](HallucinationFrequencyService.md) (8 shared connections)
- [Any](Any.md) (7 shared connections)
- [MutableHeaders](MutableHeaders.md) (3 shared connections)
- [disconnect player connections()](disconnect_player_connections%28%29.md) (3 shared connections)
- [Player Position Service](Player_Position_Service.md) (3 shared connections)
- [skills commands](skills_commands.md) (3 shared connections)
- [world](world.md) (2 shared connections)
- [Spell Targeting](Spell_Targeting.md) (1 shared connections)

## Source Files

- `server/commands/status_commands.py`
- `server/tests/unit/commands/test_status_commands.py`

## Audit Trail

- EXTRACTED: 76 (93%)
- INFERRED: 6 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*