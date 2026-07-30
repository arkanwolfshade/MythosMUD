# chat nats publisher

> 116 nodes

## Key Concepts

- **AsyncPersistenceLayer** (183 connections) — `server/async_persistence.py`
- **test_async_persistence_delegates.py** (35 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **schedule_service.py** (25 connections) — `server/services/schedule_service.py`
- **.__init__()** (13 connections) — `server/async_persistence.py`
- **RoomRepository** (12 connections) — `server/persistence/repositories/room_repository.py`
- **ProfessionRepository** (11 connections) — `server/persistence/repositories/profession_repository.py`
- **_schedule_entry_from_row()** (8 connections) — `server/services/schedule_service.py`
- **test_schedule_service.py** (8 connections) — `server/tests/unit/services/test_schedule_service.py`
- **reset_async_persistence()** (6 connections) — `server/async_persistence.py`
- **.__init__()** (5 connections) — `server/npc/combat_integration_base.py`
- **normalize_weekday_names()** (5 connections) — `server/services/schedule_service.py`
- **_DatabaseLoadResult** (5 connections) — `server/services/schedule_service.py`
- **conftest.py** (5 connections) — `server/tests/unit/infrastructure/conftest.py`
- **_string_list_from_row()** (4 connections) — `server/services/schedule_service.py`
- **_lower_string_list_from_row()** (4 connections) — `server/services/schedule_service.py`
- **test_validate_and_fix_player_room_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_apply_lucidity_loss_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_apply_fear_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_apply_corruption_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_heal_player_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_async_heal_player_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_damage_player_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_async_damage_player_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_create_container_with_params()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_create_container_with_kwargs()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- *... and 91 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (35 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (18 shared connections)
- [. init ()](_init_%28%29.md) (14 shared connections)
- [real time](real_time.md) (13 shared connections)
- [PlayerChannelPreferences](PlayerChannelPreferences.md) (12 shared connections)
- [parse jsonb column()](parse_jsonb_column%28%29.md) (11 shared connections)
- [init](init.md) (10 shared connections)
- [UUID](UUID.md) (7 shared connections)
- [Formatter](Formatter.md) (7 shared connections)
- [CombatService](CombatService.md) (6 shared connections)
- [Any](Any.md) (6 shared connections)
- [.model dump()](model_dump%28%29.md) (6 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/npc/combat_integration_base.py`
- `server/persistence/repositories/profession_repository.py`
- `server/persistence/repositories/room_repository.py`
- `server/services/schedule_service.py`
- `server/tests/unit/infrastructure/conftest.py`
- `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- `server/tests/unit/services/test_schedule_service.py`

## Audit Trail

- EXTRACTED: 464 (89%)
- INFERRED: 55 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*