# Community 623

> 27 nodes

## Key Concepts

- **test_talk_command.py** (14 connections) — `server/tests/unit/commands/test_talk_command.py`
- **DialoguePrompt** (10 connections) — `server/game/dialogue/dialogue_service.py`
- **_emit_prompt()** (8 connections) — `server/commands/talk_command.py`
- **_talk_with_npc()** (8 connections) — `server/commands/talk_command.py`
- **_resolve_player_id()** (6 connections) — `server/commands/talk_command.py`
- **_talk_by_option_index()** (6 connections) — `server/commands/talk_command.py`
- **_remainder_from_command_data()** (5 connections) — `server/commands/talk_command.py`
- **UUID** (5 connections)
- **test_talk_with_npc_success()** (4 connections) — `server/tests/unit/commands/test_talk_command.py`
- **asyncio** (4 connections)
- **test_emit_prompt_ended()** (3 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_emit_prompt_with_options()** (3 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_handle_talk_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_handle_talk_command_usage()** (3 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_talk_by_option_index_error_string()** (3 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_remainder_from_command_data_list()** (2 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_remainder_from_command_data_string()** (2 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_resolve_player_id_invalid()** (2 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_resolve_player_id_uuid()** (2 connections) — `server/tests/unit/commands/test_talk_command.py`
- **DialoguePrompt** (1 connections)
- **Extract player UUID from player model.** (1 connections) — `server/commands/talk_command.py`
- **Join talk args into a single remainder string.** (1 connections) — `server/commands/talk_command.py`
- **Send personal system message for a node; return short command result.** (1 connections) — `server/commands/talk_command.py`
- **Advance an active dialogue by numbered option.** (1 connections) — `server/commands/talk_command.py`
- **Start dialogue with a same-room NPC.** (1 connections) — `server/commands/talk_command.py`
- *... and 2 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (13 shared connections)
- [Community 243](Community_243.md) (6 shared connections)
- [Community 468](Community_468.md) (2 shared connections)

## Source Files

- `server/commands/talk_command.py`
- `server/game/dialogue/dialogue_service.py`
- `server/tests/unit/commands/test_talk_command.py`

## Audit Trail

- EXTRACTED: 60 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*