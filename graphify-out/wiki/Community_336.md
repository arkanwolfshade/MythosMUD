# Community 336

> 50 nodes

## Key Concepts

- **test_debrief_command.py** (25 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **debrief_command.py** (23 connections) — `server/commands/debrief_command.py`
- **handle_debrief_command()** (18 connections) — `server/commands/debrief_command.py`
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
- *... and 25 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (6 shared connections)
- [Community 138](Community_138.md) (5 shared connections)
- [Community 122](Community_122.md) (5 shared connections)
- [DB Seed & Migration Scripts](DB_Seed_&_Migration_Scripts.md) (2 shared connections)
- [Channel Commands](Channel_Commands.md) (2 shared connections)
- [Community 222](Community_222.md) (2 shared connections)
- [Community 78](Community_78.md) (1 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (1 shared connections)
- [Community 207](Community_207.md) (1 shared connections)

## Source Files

- `server/commands/debrief_command.py`
- `server/tests/unit/commands/test_debrief_command.py`

## Audit Trail

- EXTRACTED: 114 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*