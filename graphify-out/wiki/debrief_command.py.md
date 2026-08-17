# debrief_command.py

> 53 nodes

## Key Concepts

- **debrief_command.py** (26 connections) — `server/commands/debrief_command.py`
- **test_debrief_command.py** (26 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **handle_debrief_command()** (20 connections) — `server/commands/debrief_command.py`
- **_generate_narrative_recap()** (9 connections) — `server/commands/debrief_command.py`
- **_perform_therapy_if_requested()** (9 connections) — `server/commands/debrief_command.py`
- **asyncio** (9 connections)
- **Any** (8 connections)
- **_check_debrief_availability()** (7 connections) — `server/commands/debrief_command.py`
- **_validate_debrief_context()** (7 connections) — `server/commands/debrief_command.py`
- **LucidityActionCode** (6 connections) — `server/models/lucidity.py`
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
- *... and 28 more nodes in this community*

## Relationships

- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (7 shared connections)
- [LucidityService](LucidityService.md) (6 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [lucidity.py](lucidity.py.md) (3 shared connections)
- [get_session_maker](get_session_maker.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [command_service.py](command_service.py.md) (2 shared connections)
- [test_hallucination_services.py](test_hallucination_services.py.md) (1 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [.app](app.md) (1 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)

## Source Files

- `server/commands/debrief_command.py`
- `server/models/lucidity.py`
- `server/tests/unit/commands/test_debrief_command.py`

## Audit Trail

- EXTRACTED: 123 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*