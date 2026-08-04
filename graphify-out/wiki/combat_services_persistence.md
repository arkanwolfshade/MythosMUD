# combat services persistence

> 124 nodes

## Key Concepts

- **test_active_lucidity_service.py** (34 connections) — `server/tests/unit/services/test_active_lucidity_service.py`
- **debrief_command.py** (26 connections) — `server/commands/debrief_command.py`
- **test_debrief_command.py** (25 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **active_lucidity_service.py** (23 connections) — `server/services/active_lucidity_service.py`
- **ActiveLucidityService** (20 connections) — `server/services/active_lucidity_service.py`
- **handle_debrief_command()** (19 connections) — `server/commands/debrief_command.py`
- **_generate_narrative_recap()** (10 connections) — `server/commands/debrief_command.py`
- **UnknownEncounterCategoryError** (10 connections) — `server/services/active_lucidity_service.py`
- **_perform_therapy_if_requested()** (9 connections) — `server/commands/debrief_command.py`
- **Any** (8 connections)
- **_validate_debrief_context()** (7 connections) — `server/commands/debrief_command.py`
- **_check_debrief_availability()** (7 connections) — `server/commands/debrief_command.py`
- **_get_persistence_from_app()** (6 connections) — `server/commands/debrief_command.py`
- **_get_catatonia_registry_from_app()** (6 connections) — `server/commands/debrief_command.py`
- **.perform_recovery_action()** (6 connections) — `server/services/active_lucidity_service.py`
- **_complete_debrief()** (5 connections) — `server/commands/debrief_command.py`
- **.__init__()** (5 connections) — `server/services/active_lucidity_service.py`
- **.apply_encounter_lucidity_loss()** (5 connections) — `server/services/active_lucidity_service.py`
- **UUID** (4 connections)
- **.get_action_cooldown()** (4 connections) — `server/services/active_lucidity_service.py`
- **test_perform_therapy_on_cooldown()** (4 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **EncounterProfile** (3 connections) — `server/services/active_lucidity_service.py`
- **RecoveryActionProfile** (3 connections) — `server/services/active_lucidity_service.py`
- **Any** (3 connections)
- **test_validate_debrief_context_no_persistence()** (3 connections) — `server/tests/unit/commands/test_debrief_command.py`
- *... and 99 more nodes in this community*

## Relationships

- [realtime real time](realtime_real_time.md) (17 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (14 shared connections)
- [NPC Combat](NPC_Combat.md) (9 shared connections)
- [player room realtime](player_room_realtime.md) (5 shared connections)
- [commands whisper command](commands_whisper_command.md) (3 shared connections)
- [command player state](command_player_state.md) (3 shared connections)
- [Exception Containers](Exception_Containers.md) (3 shared connections)
- [commands npc admin](commands_npc_admin.md) (2 shared connections)
- [game models enums](game_models_enums.md) (1 shared connections)
- [services service phantom](services_service_phantom.md) (1 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (1 shared connections)

## Source Files

- `server/commands/debrief_command.py`
- `server/services/active_lucidity_service.py`
- `server/tests/unit/commands/test_debrief_command.py`
- `server/tests/unit/services/test_active_lucidity_service.py`

## Audit Trail

- EXTRACTED: 400 (98%)
- INFERRED: 10 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*