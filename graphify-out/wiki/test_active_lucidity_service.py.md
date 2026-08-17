# test_active_lucidity_service.py

> 129 nodes

## Key Concepts

- **test_active_lucidity_service.py** (35 connections) — `server/tests/unit/services/test_active_lucidity_service.py`
- **debrief_command.py** (26 connections) — `server/commands/debrief_command.py`
- **test_debrief_command.py** (26 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **asyncio** (25 connections)
- **ActiveLucidityService** (23 connections) — `server/services/active_lucidity_service.py`
- **active_lucidity_service.py** (23 connections) — `server/services/active_lucidity_service.py`
- **handle_debrief_command()** (20 connections) — `server/commands/debrief_command.py`
- **UnknownEncounterCategoryError** (9 connections) — `server/services/active_lucidity_service.py`
- **_generate_narrative_recap()** (9 connections) — `server/commands/debrief_command.py`
- **_perform_therapy_if_requested()** (9 connections) — `server/commands/debrief_command.py`
- **asyncio** (9 connections)
- **Any** (8 connections)
- **_check_debrief_availability()** (7 connections) — `server/commands/debrief_command.py`
- **_validate_debrief_context()** (7 connections) — `server/commands/debrief_command.py`
- **_get_catatonia_registry_from_app()** (6 connections) — `server/commands/debrief_command.py`
- **_get_persistence_from_app()** (6 connections) — `server/commands/debrief_command.py`
- **_complete_debrief()** (5 connections) — `server/commands/debrief_command.py`
- **.apply_encounter_lucidity_loss()** (5 connections) — `server/services/active_lucidity_service.py`
- **.__init__()** (5 connections) — `server/services/active_lucidity_service.py`
- **test_handle_debrief_command_success()** (5 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **test_perform_therapy_on_cooldown()** (5 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **.get_action_cooldown()** (4 connections) — `server/services/active_lucidity_service.py`
- **test_check_debrief_availability_not_pending()** (4 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **test_handle_debrief_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **test_handle_debrief_command_not_available()** (4 connections) — `server/tests/unit/commands/test_debrief_command.py`
- *... and 104 more nodes in this community*

## Relationships

- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (18 shared connections)
- [LucidityService](LucidityService.md) (15 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [NPCCombatLucidity](NPCCombatLucidity.md) (6 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [command_service.py](command_service.py.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [.state](state.md) (1 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (1 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)

## Source Files

- `server/commands/debrief_command.py`
- `server/services/active_lucidity_service.py`
- `server/tests/unit/commands/test_debrief_command.py`
- `server/tests/unit/services/test_active_lucidity_service.py`

## Audit Trail

- EXTRACTED: 261 (95%)
- INFERRED: 15 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*