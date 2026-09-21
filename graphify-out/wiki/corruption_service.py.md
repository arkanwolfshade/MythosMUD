# corruption_service.py

> 76 nodes

## Key Concepts

- **corruption_service.py** (42 connections) — `server/services/corruption_service.py`
- **cleanse_command.py** (23 connections) — `server/commands/cleanse_command.py`
- **CorruptionPersistenceProtocol** (16 connections) — `server/services/corruption_service.py`
- **spell_costs.py** (16 connections) — `server/game/magic/spell_costs.py`
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
- **normalize_metadata()** (6 connections) — `server/services/lucidity_helpers.py`
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
- *... and 51 more nodes in this community*

## Relationships

- [CorruptionService](CorruptionService.md) (13 shared connections)
- [ValidationError](ValidationError.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [CorruptionTier](CorruptionTier.md) (5 shared connections)
- [DatabaseManager](DatabaseManager.md) (5 shared connections)
- [CorruptionRepository](CorruptionRepository.md) (5 shared connections)
- [command_service.py](command_service.py.md) (4 shared connections)
- [magic_service_completion.py](magic_service_completion.py.md) (4 shared connections)
- [test_passive_corruption_flux_service.py](test_passive_corruption_flux_service.py.md) (4 shared connections)
- [LucidityService](LucidityService.md) (4 shared connections)
- [Spell](Spell.md) (3 shared connections)
- [coerce_int](coerce_int.md) (3 shared connections)

## Source Files

- `server/commands/cleanse_command.py`
- `server/game/magic/spell_costs.py`
- `server/services/corruption_service.py`
- `server/services/lucidity_helpers.py`
- `server/tests/unit/commands/test_cleanse_command.py`

## Audit Trail

- EXTRACTED: 203 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*