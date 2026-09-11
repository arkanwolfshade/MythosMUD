# test_lucidity_recovery_commands.py

> 105 nodes

## Key Concepts

- **test_lucidity_recovery_commands.py** (34 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **lucidity_recovery_commands.py** (26 connections) — `server/commands/lucidity_recovery_commands.py`
- **ActiveLucidityService** (23 connections) — `server/services/active_lucidity_service.py`
- **active_lucidity_service.py** (23 connections) — `server/services/active_lucidity_service.py`
- **handle_pray_command()** (21 connections) — `server/commands/lucidity_recovery_commands.py`
- **asyncio** (21 connections)
- **LucidityActionOnCooldownError** (17 connections) — `server/services/active_lucidity_service.py`
- **UnknownLucidityActionError** (11 connections) — `server/services/active_lucidity_service.py`
- **_perform_recovery_action()** (11 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_meditate_command()** (10 connections) — `server/commands/lucidity_recovery_commands.py`
- **UnknownEncounterCategoryError** (9 connections) — `server/services/active_lucidity_service.py`
- **handle_group_solace_command()** (9 connections) — `server/commands/lucidity_recovery_commands.py`
- **Any** (9 connections)
- **handle_folk_tonic_command()** (8 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_therapy_command()** (8 connections) — `server/commands/lucidity_recovery_commands.py`
- **_run_recovery_session()** (8 connections) — `server/commands/lucidity_recovery_commands.py`
- **LucidityActionError** (6 connections) — `server/services/active_lucidity_service.py`
- **.perform_recovery_action()** (6 connections) — `server/services/active_lucidity_service.py`
- **_restore_mp_for_action()** (5 connections) — `server/commands/lucidity_recovery_commands.py`
- **_validate_recovery_context()** (5 connections) — `server/commands/lucidity_recovery_commands.py`
- **.apply_encounter_lucidity_loss()** (5 connections) — `server/services/active_lucidity_service.py`
- **.__init__()** (5 connections) — `server/services/active_lucidity_service.py`
- **test_handle_group_solace_command_unknown_action()** (5 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_meditate_command_cooldown()** (5 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_cooldown()** (5 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- *... and 80 more nodes in this community*

## Relationships

- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (12 shared connections)
- [LucidityService](LucidityService.md) (10 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [AliasStorage](AliasStorage.md) (7 shared connections)
- [NPCCombatLucidity](NPCCombatLucidity.md) (6 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (6 shared connections)
- [command_service.py](command_service.py.md) (6 shared connections)
- [Player](Player.md) (4 shared connections)
- [get_async_session](get_async_session.md) (2 shared connections)
- [mp_regeneration_service](mp_regeneration_service.md) (1 shared connections)
- [CatatoniaObserverProtocol](CatatoniaObserverProtocol.md) (1 shared connections)

## Source Files

- `server/commands/lucidity_recovery_commands.py`
- `server/services/active_lucidity_service.py`
- `server/tests/unit/commands/test_lucidity_recovery_commands.py`

## Audit Trail

- EXTRACTED: 237 (90%)
- INFERRED: 25 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*