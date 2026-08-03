# combat services persistence

> 123 nodes

## Key Concepts

- **LucidityService** (88 connections) — `server/services/lucidity_service.py`
- **debrief_command.py** (26 connections) — `server/commands/debrief_command.py`
- **test_debrief_command.py** (25 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **test_lucidity_service.py** (24 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **active_lucidity_service.py** (23 connections) — `server/services/active_lucidity_service.py`
- **ActiveLucidityService** (20 connections) — `server/services/active_lucidity_service.py`
- **handle_debrief_command()** (19 connections) — `server/commands/debrief_command.py`
- **LucidityActionOnCooldownError** (18 connections) — `server/services/active_lucidity_service.py`
- **UnknownLucidityActionError** (12 connections) — `server/services/active_lucidity_service.py`
- **_generate_narrative_recap()** (10 connections) — `server/commands/debrief_command.py`
- **UnknownEncounterCategoryError** (10 connections) — `server/services/active_lucidity_service.py`
- **_perform_therapy_if_requested()** (9 connections) — `server/commands/debrief_command.py`
- **Any** (8 connections)
- **_validate_debrief_context()** (7 connections) — `server/commands/debrief_command.py`
- **_check_debrief_availability()** (7 connections) — `server/commands/debrief_command.py`
- **LucidityActionError** (7 connections) — `server/services/active_lucidity_service.py`
- **_get_persistence_from_app()** (6 connections) — `server/commands/debrief_command.py`
- **_get_catatonia_registry_from_app()** (6 connections) — `server/commands/debrief_command.py`
- **.perform_recovery_action()** (6 connections) — `server/services/active_lucidity_service.py`
- **_complete_debrief()** (5 connections) — `server/commands/debrief_command.py`
- **.__init__()** (5 connections) — `server/services/active_lucidity_service.py`
- **.apply_encounter_lucidity_loss()** (5 connections) — `server/services/active_lucidity_service.py`
- **._max_lcd_from_stats()** (5 connections) — `server/services/lucidity_service.py`
- **UUID** (4 connections)
- **.get_action_cooldown()** (4 connections) — `server/services/active_lucidity_service.py`
- *... and 98 more nodes in this community*

## Relationships

- [lucidity services helpers](lucidity_services_helpers.md) (27 shared connections)
- [realtime real time](realtime_real_time.md) (15 shared connections)
- [world models rationale](world_models_rationale.md) (12 shared connections)
- [lucidity active service](lucidity_active_service.md) (12 shared connections)
- [combat models rationale](combat_models_rationale.md) (9 shared connections)
- [models npc rationale](models_npc_rationale.md) (8 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (6 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (6 shared connections)
- [command helpers functions](command_helpers_functions.md) (5 shared connections)
- [commands position system](commands_position_system.md) (3 shared connections)
- [combat npc services](combat_npc_services.md) (3 shared connections)
- [command player state](command_player_state.md) (3 shared connections)

## Source Files

- `server/commands/debrief_command.py`
- `server/services/active_lucidity_service.py`
- `server/services/lucidity_service.py`
- `server/tests/unit/commands/test_debrief_command.py`
- `server/tests/unit/services/test_lucidity_service.py`

## Audit Trail

- EXTRACTED: 505 (94%)
- INFERRED: 34 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*