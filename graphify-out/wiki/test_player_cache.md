# test player cache

> 23 nodes

## Key Concepts

- **channel_commands.py** (16 connections) — `server/commands/channel_commands.py`
- **handle_channel_command()** (10 connections) — `server/commands/channel_commands.py`
- **_handle_default_channel_setting()** (6 connections) — `server/commands/channel_commands.py`
- **Any** (6 connections)
- **_get_persistence_and_player()** (5 connections) — `server/commands/channel_commands.py`
- **.handle_attack_command()** (5 connections) — `server/commands/combat_handler.py`
- **.handle_taunt_command()** (5 connections) — `server/commands/combat_handler.py`
- **Any** (4 connections)
- **_extract_channel_from_command()** (4 connections) — `server/commands/channel_commands.py`
- **.extract_combat_command_data()** (4 connections) — `server/commands/combat_handler.py`
- **.handle_flee_command()** (4 connections) — `server/commands/combat_handler.py`
- **_validate_channel_name()** (3 connections) — `server/commands/channel_commands.py`
- **Channel management commands for Advanced Chat Channels.  This module provides ha** (1 connections) — `server/commands/channel_commands.py`
- **Get persistence and player. Returns (persistence, player) or (None, None) if not** (1 connections) — `server/commands/channel_commands.py`
- **Extract channel name from command_data. Returns channel name or None.** (1 connections) — `server/commands/channel_commands.py`
- **Handle setting default channel. Returns result dict or None if not a default com** (1 connections) — `server/commands/channel_commands.py`
- **Validate channel name. Returns error dict if invalid, None if valid.** (1 connections) — `server/commands/channel_commands.py`
- **Handle the channel command for switching channels or setting default channel.** (1 connections) — `server/commands/channel_commands.py`
- **Extract command type and target name from command_data. Public API.** (1 connections) — `server/commands/combat_handler.py`
- **Extract command type and target name from command_data.** (1 connections) — `server/commands/combat_handler.py`
- **Handle attack commands (attack, punch, kick, etc.).** (1 connections) — `server/commands/combat_handler.py`
- **Handle /flee command: leave combat and move to random adjacent room.** (1 connections) — `server/commands/combat_handler.py`
- **Handle taunt command: draw NPC aggro (ADR-016). Room-local only.** (1 connections) — `server/commands/combat_handler.py`

## Relationships

- [Any](Any.md) (7 shared connections)
- [Player Position Service](Player_Position_Service.md) (4 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [close db()](close_db%28%29.md) (3 shared connections)
- [test player preferences service](test_player_preferences_service.md) (2 shared connections)
- [world](world.md) (2 shared connections)
- [main()](main%28%29.md) (1 shared connections)
- [Spell Targeting](Spell_Targeting.md) (1 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (1 shared connections)
- [combat attack](combat_attack.md) (1 shared connections)
- [test player event handlers room](test_player_event_handlers_room.md) (1 shared connections)

## Source Files

- `server/commands/channel_commands.py`
- `server/commands/combat_handler.py`

## Audit Trail

- EXTRACTED: 79 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*