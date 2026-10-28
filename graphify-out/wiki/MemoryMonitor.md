# MemoryMonitor

> 61 nodes · cohesion 0.05

## Key Concepts

- **command_input.py** (18 connections) — `server/command_handler/command_input.py`
- **should_treat_as_emote()** (17 connections) — `server/command_handler/command_input.py`
- **command_handler/__init__.py** (14 connections) — `server/command_handler/__init__.py`
- **normalize_command()** (12 connections) — `server/command_handler/command_input.py`
- **TestCommandNormalization** (12 connections) — `server/tests/unit/commands/test_command_input.py`
- **_is_predefined_emote()** (11 connections) — `server/command_handler/command_input.py`
- **clean_command_input()** (10 connections) — `server/command_handler/command_input.py`
- **TestEmoteDetection** (10 connections) — `server/tests/unit/commands/test_command_input.py`
- **test_command_input.py** (9 connections) — `server/tests/unit/commands/test_command_input.py`
- **_mock_request()** (6 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_is_predefined_emote_false()** (4 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_is_predefined_emote_handles_error()** (4 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_is_predefined_emote_no_emote_service()** (4 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_is_predefined_emote_true()** (4 connections) — `server/tests/unit/commands/test_command_input.py`
- **test_a_combat_verb_is_never_mistaken_for_an_emote()** (3 connections) — `server/tests/unit/commands/test_assist_wiring.py`
- **.test_clean_command_input_basic()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_clean_command_input_leading_trailing_whitespace()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_clean_command_input_multiple_spaces()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_clean_command_input_tabs()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_empty()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_no_slash()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_slash_only()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_slash_with_spaces()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_whitespace_only()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- **.test_normalize_command_with_slash()** (3 connections) — `server/tests/unit/commands/test_command_input.py`
- *... and 36 more nodes in this community*

## Relationships

- [CommandFactory](CommandFactory.md) (6 shared connections)
- [QuestService](QuestService.md) (5 shared connections)
- [test_passive_corruption_flux_rate_overrides.py](test_passive_corruption_flux_rate_overrides.py.md) (4 shared connections)
- [test_logging_file_categories.py](test_logging_file_categories.py.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (2 shared connections)
- [DialogueService](DialogueService.md) (2 shared connections)
- [go_command.py](go_command.py.md) (2 shared connections)
- [ChatChannelLoggerMixin](ChatChannelLoggerMixin.md) (2 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (1 shared connections)
- [test_windows_safe_rotation.py](test_windows_safe_rotation.py.md) (1 shared connections)

## Source Files

- `server/command_handler/__init__.py`
- `server/command_handler/command_input.py`
- `server/tests/unit/commands/test_assist_wiring.py`
- `server/tests/unit/commands/test_command_input.py`
- `server/tests/unit/commands/test_protect_wiring.py`

## Audit Trail

- EXTRACTED: 124 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*