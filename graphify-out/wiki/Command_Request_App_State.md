# Command Request App State

> 34 nodes · cohesion 0.04

## Key Concepts

- **command_handler_unified.py** (52 connections) — `server/command_handler_unified.py`
- **_prepare_command_for_processing()** (21 connections) — `server/command_handler_unified.py`
- **_process_alias_expansion()** (19 connections) — `server/command_handler_unified.py`
- **process_command_unified()** (19 connections) — `server/command_handler_unified.py`
- **_check_casting_state()** (18 connections) — `server/command_handler_unified.py`
- **_handle_special_command_routing()** (18 connections) — `server/command_handler_unified.py`
- **_check_all_command_blocks()** (17 connections) — `server/command_handler_unified.py`
- **_ensure_alias_storage()** (14 connections) — `server/command_handler_unified.py`
- **Any** (14 connections) — `server/command_handler_unified.py`
- **_validate_command_basics()** (14 connections) — `server/command_handler_unified.py`
- **CommandExecutionRequest** (11 connections) — `server/command_handler_unified.py`
- **_check_rate_limit()** (10 connections) — `server/command_handler_unified.py`
- **handle_command()** (10 connections) — `server/command_handler_unified.py`
- **process_command()** (9 connections) — `server/command_handler_unified.py`
- **_get_grace_check_context()** (7 connections) — `server/command_handler_unified.py`
- **_get_casting_block_result()** (6 connections) — `server/command_handler_unified.py`
- **get_help_content()** (6 connections) — `server/command_handler_unified.py`
- **UUID** (3 connections) — `server/command_handler_unified.py`
- **Request** (2 connections) — `server/command_handler_unified.py`
- **Unified Command Handler for MythosMUD.  This module provides a single, unified c** (1 connections) — `server/command_handler_unified.py`
- **Handle special command routing (alias management, alias expansion, emote). Retur** (1 connections) — `server/command_handler_unified.py`
- **Unified command processing function for both HTTP and WebSocket.      This is th** (1 connections) — `server/command_handler_unified.py`
- **Check if player is rate limited. Returns result dict if blocked, None if allowed** (1 connections) — `server/command_handler_unified.py`
- **Validate basic command requirements. Returns result dict if invalid, None if val** (1 connections) — `server/command_handler_unified.py`
- **Ensure alias storage is initialized.** (1 connections) — `server/command_handler_unified.py`
- *... and 9 more nodes in this community*

## Relationships

- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (7 shared connections)
- [Stats Planning Archive](Stats_Planning_Archive.md) (5 shared connections)
- [Unified Command Handler](Unified_Command_Handler.md) (2 shared connections)

## Source Files

- `server/command_handler_unified.py`

## Audit Trail

- EXTRACTED: 279 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*