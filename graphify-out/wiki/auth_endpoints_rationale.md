# auth endpoints rationale

> 60 nodes

## Key Concepts

- **debrief_command.py** (26 connections) — `server/commands/debrief_command.py`
- **test_debrief_command.py** (25 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **active_lucidity_service.py** (23 connections) — `server/services/active_lucidity_service.py`
- **handle_debrief_command()** (19 connections) — `server/commands/debrief_command.py`
- **_generate_narrative_recap()** (10 connections) — `server/commands/debrief_command.py`
- **_perform_therapy_if_requested()** (9 connections) — `server/commands/debrief_command.py`
- **Any** (8 connections)
- **_validate_debrief_context()** (7 connections) — `server/commands/debrief_command.py`
- **_check_debrief_availability()** (7 connections) — `server/commands/debrief_command.py`
- **LucidityActionError** (7 connections) — `server/services/active_lucidity_service.py`
- **_get_persistence_from_app()** (6 connections) — `server/commands/debrief_command.py`
- **_get_catatonia_registry_from_app()** (6 connections) — `server/commands/debrief_command.py`
- **_complete_debrief()** (5 connections) — `server/commands/debrief_command.py`
- **.__init__()** (5 connections) — `server/services/active_lucidity_service.py`
- **test_perform_therapy_on_cooldown()** (4 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **EncounterProfile** (3 connections) — `server/services/active_lucidity_service.py`
- **RecoveryActionProfile** (3 connections) — `server/services/active_lucidity_service.py`
- **test_validate_debrief_context_no_persistence()** (3 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **test_validate_debrief_context_player_missing()** (3 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **test_get_persistence_from_app_container()** (3 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **test_get_catatonia_registry_from_state_fallback()** (3 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **test_check_debrief_availability_not_pending()** (3 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **test_perform_therapy_if_not_requested()** (3 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **test_perform_therapy_success()** (3 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **test_generate_narrative_recap_no_adjustments()** (3 connections) — `server/tests/unit/commands/test_debrief_command.py`
- *... and 35 more nodes in this community*

## Relationships

- [player room realtime](player_room_realtime.md) (18 shared connections)
- [realtime real time](realtime_real_time.md) (11 shared connections)
- [game models player](game_models_player.md) (8 shared connections)
- [Error Conversion](Error_Conversion.md) (6 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (3 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (2 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (1 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (1 shared connections)
- [npc population control](npc_population_control.md) (1 shared connections)
- [Spell Validation](Spell_Validation.md) (1 shared connections)

## Source Files

- `server/commands/debrief_command.py`
- `server/services/active_lucidity_service.py`
- `server/tests/unit/commands/test_debrief_command.py`

## Audit Trail

- EXTRACTED: 238 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*