# npc idle movement

> 14 nodes

## Key Concepts

- **TestEmoteDetection** (8 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_is_predefined_emote_true()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_is_predefined_emote_false()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_is_predefined_emote_handles_error()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_should_treat_as_emote_system_command()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_should_treat_as_emote_unknown_word()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_should_treat_as_emote_predefined_emote()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test emote detection functions.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test _is_predefined_emote() returns True for predefined emote.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test _is_predefined_emote() returns False for non-emote.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test _is_predefined_emote() handles errors gracefully.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test should_treat_as_emote() returns False for system commands.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test should_treat_as_emote() returns False for unknown words.** (1 connections) — `server/tests/unit/commands/test_command_input.py`
- **Test should_treat_as_emote() returns True for predefined emotes.** (1 connections) — `server/tests/unit/commands/test_command_input.py`

## Relationships

- [websocket helpers realtime](websocket_helpers_realtime.md) (3 shared connections)
- [player model models](player_model_models.md) (3 shared connections)
- [commands recovery lucidity](commands_recovery_lucidity.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_command_input.py`

## Audit Trail

- EXTRACTED: 33 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*