# cleanse_command.py

> 67 nodes

## Key Concepts

- **cleanse_command.py** (23 connections) — `server/commands/cleanse_command.py`
- **CorruptionPersistenceProtocol** (16 connections) — `server/services/corruption_service.py`
- **handle_cleanse_command()** (14 connections) — `server/commands/cleanse_command.py`
- **.apply_corruption_adjustment()** (13 connections) — `server/services/corruption_service.py`
- **test_cleanse_command.py** (13 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **CorruptionPersistencePlayer** (11 connections) — `server/services/corruption_service.py`
- **CorruptionActionOnCooldownError** (10 connections) — `server/services/corruption_service.py`
- **.perform_recovery_action()** (10 connections) — `server/services/corruption_service.py`
- **CleansePersistence** (8 connections) — `server/commands/cleanse_command.py`
- **.get_cooldown_expiry()** (7 connections) — `server/services/corruption_service.py`
- **UUID** (7 connections)
- **._notify_tier_crossing()** (6 connections) — `server/services/corruption_service.py`
- **Protocol** (6 connections)
- **CleanseTargetPlayer** (5 connections) — `server/commands/cleanse_command.py`
- **CorruptionActionError** (5 connections) — `server/services/corruption_service.py`
- **._send_corruption_update_event()** (5 connections) — `server/services/corruption_service.py`
- **asyncio** (5 connections)
- **CleanseApp** (4 connections) — `server/commands/cleanse_command.py`
- **CleanseContainer** (4 connections) — `server/commands/cleanse_command.py`
- **CleanseRequest** (4 connections) — `server/commands/cleanse_command.py`
- **_format_cooldown_message()** (4 connections) — `server/commands/cleanse_command.py`
- **_resolve_persistence()** (4 connections) — `server/commands/cleanse_command.py`
- **test_handle_cleanse_command_cooldown()** (4 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **test_handle_cleanse_command_cooldown_no_expiry()** (4 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **CleanseAppState** (3 connections) — `server/commands/cleanse_command.py`
- *... and 42 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (15 shared connections)
- [CorruptionService](CorruptionService.md) (10 shared connections)
- [PlayerService](PlayerService.md) (3 shared connections)
- [DatabaseManager](DatabaseManager.md) (3 shared connections)
- [CorruptionRepository](CorruptionRepository.md) (3 shared connections)
- [TargetResolutionResult](TargetResolutionResult.md) (2 shared connections)
- [TargetMatch](TargetMatch.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [command_service.py](command_service.py.md) (2 shared connections)
- [test_passive_corruption_flux_service.py](test_passive_corruption_flux_service.py.md) (2 shared connections)
- [admin_setstat_command.py](admin_setstat_command.py.md) (1 shared connections)
- [passive_corruption_flux/service.py](passive_corruption_flux-service.py.md) (1 shared connections)

## Source Files

- `server/commands/cleanse_command.py`
- `server/services/corruption_service.py`
- `server/tests/unit/commands/test_cleanse_command.py`

## Audit Trail

- EXTRACTED: 149 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*