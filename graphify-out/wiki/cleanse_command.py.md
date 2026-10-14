# cleanse_command.py

> 31 nodes

## Key Concepts

- **cleanse_command.py** (23 connections) — `server/commands/cleanse_command.py`
- **CorruptionPersistencePlayer** (11 connections) — `server/services/corruption_service.py`
- **CleansePersistence** (8 connections) — `server/commands/cleanse_command.py`
- **Protocol** (6 connections)
- **CleanseTargetPlayer** (5 connections) — `server/commands/cleanse_command.py`
- **CleanseApp** (4 connections) — `server/commands/cleanse_command.py`
- **CleanseContainer** (4 connections) — `server/commands/cleanse_command.py`
- **CleanseRequest** (4 connections) — `server/commands/cleanse_command.py`
- **_format_cooldown_message()** (4 connections) — `server/commands/cleanse_command.py`
- **_resolve_persistence()** (4 connections) — `server/commands/cleanse_command.py`
- **CleanseAppState** (3 connections) — `server/commands/cleanse_command.py`
- **.get_player_by_id()** (3 connections) — `server/commands/cleanse_command.py`
- **.get_player_by_name()** (2 connections) — `server/commands/cleanse_command.py`
- **.save_player()** (2 connections) — `server/commands/cleanse_command.py`
- **.app()** (2 connections) — `server/commands/cleanse_command.py`
- **.save_player()** (2 connections) — `server/services/corruption_service.py`
- **datetime** (2 connections)
- **UUID** (2 connections)
- **Protocol** (2 connections)
- **.get_stats()** (1 connections) — `server/services/corruption_service.py`
- **.set_stats()** (1 connections) — `server/services/corruption_service.py`
- **Cleansing rite that pares back corruption's grip on the mind.** (1 connections) — `server/commands/cleanse_command.py`
- **Player surface needed by the cleanse command, beyond corruption stat access.** (1 connections) — `server/commands/cleanse_command.py`
- **Persistence surface the cleanse command and `CorruptionService` both need.…** (1 connections) — `server/commands/cleanse_command.py`
- **DI container surface exposing the async persistence layer.** (1 connections) — `server/commands/cleanse_command.py`
- *... and 6 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (6 shared connections)
- [handle_cleanse_command](handle_cleanse_command.md) (5 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (2 shared connections)
- [.apply_corruption_adjustment](apply_corruption_adjustment.md) (1 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [CorruptionService](CorruptionService.md) (1 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)
- [command_parser.py](command_parser.py.md) (1 shared connections)
- [command_service.py](command_service.py.md) (1 shared connections)

## Source Files

- `server/commands/cleanse_command.py`
- `server/services/corruption_service.py`

## Audit Trail

- EXTRACTED: 62 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*