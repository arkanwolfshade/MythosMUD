# combat services persistence

> 135 nodes

## Key Concepts

- **test_active_lucidity_service.py** (34 connections) — `server/tests/unit/services/test_active_lucidity_service.py`
- **debrief_command.py** (26 connections) — `server/commands/debrief_command.py`
- **test_debrief_command.py** (25 connections) — `server/tests/unit/commands/test_debrief_command.py`
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
- **UUID** (4 connections)
- **.get_action_cooldown()** (4 connections) — `server/services/active_lucidity_service.py`
- **test_perform_therapy_on_cooldown()** (4 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **EncounterProfile** (3 connections) — `server/services/active_lucidity_service.py`
- *... and 110 more nodes in this community*

## Relationships

- [lucidity services helpers](lucidity_services_helpers.md) (17 shared connections)
- [realtime real time](realtime_real_time.md) (15 shared connections)
- [Loot Generation](Loot_Generation.md) (6 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (6 shared connections)
- [player room realtime](player_room_realtime.md) (6 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (6 shared connections)
- [command player state](command_player_state.md) (3 shared connections)
- [commands party examples](commands_party_examples.md) (2 shared connections)
- [commands admin mute](commands_admin_mute.md) (2 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (1 shared connections)

## Source Files

- `server/commands/debrief_command.py`
- `server/services/active_lucidity_service.py`
- `server/tests/unit/commands/test_debrief_command.py`
- `server/tests/unit/services/test_active_lucidity_service.py`

## Audit Trail

- EXTRACTED: 443 (96%)
- INFERRED: 17 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*