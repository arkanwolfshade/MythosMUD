# message broadcaster realtime

> 15 nodes

## Key Concepts

- **talk_command.py** (26 connections) — `server/commands/talk_command.py`
- **handle_talk_command()** (11 connections) — `server/commands/talk_command.py`
- **_emit_prompt()** (8 connections) — `server/commands/talk_command.py`
- **_talk_with_npc()** (8 connections) — `server/commands/talk_command.py`
- **_talk_by_option_index()** (6 connections) — `server/commands/talk_command.py`
- **_resolve_player_id()** (5 connections) — `server/commands/talk_command.py`
- **UUID** (5 connections)
- **_remainder_from_command_data()** (3 connections) — `server/commands/talk_command.py`
- **talk / talk <n> command for NPC dialogue trees (#583).** (1 connections) — `server/commands/talk_command.py`
- **Extract player UUID from player model.** (1 connections) — `server/commands/talk_command.py`
- **Join talk args into a single remainder string.** (1 connections) — `server/commands/talk_command.py`
- **Send personal system message for a node; return short command result.** (1 connections) — `server/commands/talk_command.py`
- **Advance an active dialogue by numbered option.** (1 connections) — `server/commands/talk_command.py`
- **Start dialogue with a same-room NPC.** (1 connections) — `server/commands/talk_command.py`
- **Handle talk <npc> or talk <n> against same-room NPCs.** (1 connections) — `server/commands/talk_command.py`

## Relationships

- [npc commands admin](npc_commands_admin.md) (7 shared connections)
- [dialogue service game](dialogue_service_game.md) (7 shared connections)
- [commands admin mute](commands_admin_mute.md) (5 shared connections)
- [commands quest rationale](commands_quest_rationale.md) (5 shared connections)
- [quest chat game](quest_chat_game.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [command factories create](command_factories_create.md) (2 shared connections)

## Source Files

- `server/commands/talk_command.py`

## Audit Trail

- EXTRACTED: 78 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*