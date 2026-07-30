# chat nats publisher

> 312 nodes

## Key Concepts

- **AsyncPersistenceLayer** (183 connections) — `server/async_persistence.py`
- **async_persistence.py** (73 connections) — `server/async_persistence.py`
- **test_async_persistence_core.py** (40 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **test_async_persistence_delegates.py** (35 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **room.py** (30 connections) — `server/models/room.py`
- **RoomCacheLoader** (29 connections) — `server/async_persistence_room_loader.py`
- **movement_service.py** (28 connections) — `server/game/movement_service.py`
- **Player** (22 connections)
- **UUID** (21 connections)
- **room_service.py** (21 connections) — `server/game/room_service.py`
- **PlayerRepositoryProtocol** (21 connections) — `server/persistence/protocols.py`
- **Any** (19 connections)
- **get_async_persistence()** (19 connections) — `server/async_persistence.py`
- **movement_integration.py** (18 connections) — `server/npc/movement_integration.py`
- **._ensure_room_cache_loaded()** (13 connections) — `server/async_persistence.py`
- **Any** (12 connections)
- **CreateItemInstanceInput** (11 connections) — `server/async_persistence_constants.py`
- **protocols.py** (11 connections) — `server/persistence/protocols.py`
- **Player** (11 connections)
- **.load()** (10 connections) — `server/async_persistence_room_loader.py`
- **RoomRepositoryProtocol** (9 connections) — `server/persistence/protocols.py`
- **._generate_room_id_from_zone_data()** (7 connections) — `server/async_persistence_room_loader.py`
- **datetime** (6 connections)
- **reset_async_persistence()** (6 connections) — `server/async_persistence.py`
- **._process_combined_rows()** (6 connections) — `server/async_persistence_room_loader.py`
- *... and 287 more nodes in this community*

## Relationships

- [real time](real_time.md) (38 shared connections)
- [. init ()](_init_%28%29.md) (31 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (23 shared connections)
- [close db()](close_db%28%29.md) (21 shared connections)
- [world](world.md) (15 shared connections)
- [parse jsonb column()](parse_jsonb_column%28%29.md) (14 shared connections)
- [spawn defaults](spawn_defaults.md) (12 shared connections)
- [CombatService](CombatService.md) (11 shared connections)
- [main()](main%28%29.md) (10 shared connections)
- [APIRouter](APIRouter.md) (8 shared connections)
- [HolidayCollection](HolidayCollection.md) (8 shared connections)
- [UUID](UUID.md) (7 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_constants.py`
- `server/async_persistence_room_loader.py`
- `server/game/movement_service.py`
- `server/game/room_service.py`
- `server/models/room.py`
- `server/npc/combat_integration_base.py`
- `server/npc/movement_integration.py`
- `server/persistence/protocols.py`
- `server/tests/unit/infrastructure/conftest.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/infrastructure/test_async_persistence_delegates.py`

## Audit Trail

- EXTRACTED: 1177 (93%)
- INFERRED: 93 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*