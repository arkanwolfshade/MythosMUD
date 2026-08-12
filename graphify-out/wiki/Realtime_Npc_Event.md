# Realtime Npc Event

> 13 nodes

## Key Concepts

- **channel_commands.py** (16 connections) — `server/commands/channel_commands.py`
- **handle_channel_command()** (10 connections) — `server/commands/channel_commands.py`
- **_handle_default_channel_setting()** (6 connections) — `server/commands/channel_commands.py`
- **_get_persistence_and_player()** (5 connections) — `server/commands/channel_commands.py`
- **Any** (4 connections)
- **_extract_channel_from_command()** (4 connections) — `server/commands/channel_commands.py`
- **_validate_channel_name()** (3 connections) — `server/commands/channel_commands.py`
- **Channel management commands for Advanced Chat Channels.  This module provides ha** (1 connections) — `server/commands/channel_commands.py`
- **Get persistence and player. Returns (persistence, player) or (None, None) if not** (1 connections) — `server/commands/channel_commands.py`
- **Extract channel name from command_data. Returns channel name or None.** (1 connections) — `server/commands/channel_commands.py`
- **Handle setting default channel. Returns result dict or None if not a default com** (1 connections) — `server/commands/channel_commands.py`
- **Validate channel name. Returns error dict if invalid, None if valid.** (1 connections) — `server/commands/channel_commands.py`
- **Handle the channel command for switching channels or setting default channel.** (1 connections) — `server/commands/channel_commands.py`

## Relationships

- [Player Schema Converter](Player_Schema_Converter.md) (3 shared connections)
- [Realtime Conftest Mocks](Realtime_Conftest_Mocks.md) (3 shared connections)
- [Character Selection Screens](Character_Selection_Screens.md) (3 shared connections)
- [Container Open Events](Container_Open_Events.md) (3 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (1 shared connections)
- [Rate Limiter Utilities](Rate_Limiter_Utilities.md) (1 shared connections)

## Source Files

- `server/commands/channel_commands.py`

## Audit Trail

- EXTRACTED: 52 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*