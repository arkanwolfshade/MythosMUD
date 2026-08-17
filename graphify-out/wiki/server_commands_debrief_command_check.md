# server commands debrief command check

> 48 nodes

## Key Concepts

- **test_debrief_command.py** (26 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **handle_debrief_command()** (20 connections) — `server/commands/debrief_command.py`
- **_generate_narrative_recap()** (9 connections) — `server/commands/debrief_command.py`
- **_perform_therapy_if_requested()** (9 connections) — `server/commands/debrief_command.py`
- **asyncio** (9 connections)
- **Any** (8 connections)
- **_check_debrief_availability()** (7 connections) — `server/commands/debrief_command.py`
- **_validate_debrief_context()** (7 connections) — `server/commands/debrief_command.py`
- **_get_catatonia_registry_from_app()** (6 connections) — `server/commands/debrief_command.py`
- **_get_persistence_from_app()** (6 connections) — `server/commands/debrief_command.py`
- **_complete_debrief()** (5 connections) — `server/commands/debrief_command.py`
- **test_handle_debrief_command_success()** (5 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **test_perform_therapy_on_cooldown()** (5 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **test_check_debrief_availability_not_pending()** (4 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **test_handle_debrief_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **test_handle_debrief_command_not_available()** (4 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **test_perform_therapy_if_not_requested()** (4 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **test_perform_therapy_success()** (4 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **test_validate_debrief_context_no_persistence()** (4 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **test_validate_debrief_context_player_missing()** (4 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **test_generate_narrative_recap_exception_fallback()** (3 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **test_generate_narrative_recap_no_adjustments()** (3 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **test_generate_narrative_recap_with_adjustments()** (3 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **test_get_catatonia_registry_from_state_fallback()** (3 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **test_get_persistence_from_app_container()** (3 connections) — `server/tests/unit/commands/test_debrief_command.py`
- *... and 23 more nodes in this community*

## Relationships

- [server commands admin setlucidity command](server_commands_admin_setlucidity_command.md) (16 shared connections)
- [scripts add flavor text column](scripts_add_flavor_text_column.md) (2 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (2 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (1 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (1 shared connections)
- [object](object.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/commands/debrief_command.py`
- `server/tests/unit/commands/test_debrief_command.py`

## Audit Trail

- EXTRACTED: 101 (95%)
- INFERRED: 5 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*