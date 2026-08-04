# player cache rationale

> 21 nodes

## Key Concepts

- **talk_command.py** (27 connections) — `server/commands/talk_command.py`
- **handle_talk_command()** (11 connections) — `server/commands/talk_command.py`
- **get_dialogue_service()** (9 connections) — `server/game/dialogue/dialogue_service.py`
- **_emit_prompt()** (8 connections) — `server/commands/talk_command.py`
- **_talk_with_npc()** (8 connections) — `server/commands/talk_command.py`
- **format_dialogue_prompt()** (7 connections) — `server/game/dialogue/dialogue_service.py`
- **_talk_by_option_index()** (6 connections) — `server/commands/talk_command.py`
- **_resolve_player_id()** (5 connections) — `server/commands/talk_command.py`
- **UUID** (5 connections)
- **_remainder_from_command_data()** (3 connections) — `server/commands/talk_command.py`
- **test_format_dialogue_prompt_numbers_options()** (3 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **talk / talk <n> command for NPC dialogue trees (#583).** (1 connections) — `server/commands/talk_command.py`
- **Extract player UUID from player model.** (1 connections) — `server/commands/talk_command.py`
- **Join talk args into a single remainder string.** (1 connections) — `server/commands/talk_command.py`
- **Send personal system message for a node; return short command result.** (1 connections) — `server/commands/talk_command.py`
- **Advance an active dialogue by numbered option.** (1 connections) — `server/commands/talk_command.py`
- **Start dialogue with a same-room NPC.** (1 connections) — `server/commands/talk_command.py`
- **Handle talk <npc> or talk <n> against same-room NPCs.** (1 connections) — `server/commands/talk_command.py`
- **Build personal-system message body for a dialogue node.** (1 connections) — `server/game/dialogue/dialogue_service.py`
- **Return process-wide DialogueService singleton.** (1 connections) — `server/game/dialogue/dialogue_service.py`
- **Prompt includes NPC line and numbered options.** (1 connections) — `server/tests/unit/game/test_dialogue_service.py`

## Relationships

- [dialogue service game](dialogue_service_game.md) (10 shared connections)
- [rate limiter services](rate_limiter_services.md) (6 shared connections)
- [commands quest rationale](commands_quest_rationale.md) (5 shared connections)
- [Loot Generation](Loot_Generation.md) (4 shared connections)
- [quest chat game](quest_chat_game.md) (3 shared connections)
- [commands party examples](commands_party_examples.md) (2 shared connections)
- [commands admin mute](commands_admin_mute.md) (2 shared connections)
- [commands command rationale](commands_command_rationale.md) (2 shared connections)
- [commands communication flows](commands_communication_flows.md) (1 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (1 shared connections)

## Source Files

- `server/commands/talk_command.py`
- `server/game/dialogue/dialogue_service.py`
- `server/tests/unit/game/test_dialogue_service.py`

## Audit Trail

- EXTRACTED: 101 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*