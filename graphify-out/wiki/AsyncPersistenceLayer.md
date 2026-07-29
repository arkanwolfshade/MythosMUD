# AsyncPersistenceLayer

> 206 nodes

## Key Concepts

- **AsyncPersistenceLayer** (183 connections) — `server/async_persistence.py`
- **test_async_persistence_delegates.py** (35 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **RoomCacheLoader** (29 connections) — `server/async_persistence_room_loader.py`
- **Player** (22 connections)
- **UUID** (21 connections)
- **Any** (19 connections)
- **._ensure_room_cache_loaded()** (13 connections) — `server/async_persistence.py`
- **Any** (12 connections)
- **CreateItemInstanceInput** (11 connections) — `server/async_persistence_constants.py`
- **.load()** (10 connections) — `server/async_persistence_room_loader.py`
- **Delegate to room loader; exposed for unit tests.** (8 connections) — `server/async_persistence.py`
- **._generate_room_id_from_zone_data()** (7 connections) — `server/async_persistence_room_loader.py`
- **datetime** (6 connections)
- **reset_async_persistence()** (6 connections) — `server/async_persistence.py`
- **._process_combined_rows()** (6 connections) — `server/async_persistence_room_loader.py`
- **.get_player_by_id()** (5 connections) — `server/async_persistence.py`
- **.get_players_batch()** (5 connections) — `server/async_persistence.py`
- **Profession** (5 connections)
- **._build_room_data_from_row()** (5 connections) — `server/async_persistence_room_loader.py`
- **._process_exit_rows()** (5 connections) — `server/async_persistence_room_loader.py`
- **.__init__()** (5 connections) — `server/npc/combat_integration_base.py`
- **.__init__()** (5 connections) — `server/npc/movement_integration.py`
- **_DatabaseLoadResult** (5 connections) — `server/services/schedule_service.py`
- **conftest.py** (5 connections) — `server/tests/unit/infrastructure/conftest.py`
- **.get_player_by_name()** (4 connections) — `server/async_persistence.py`
- *... and 181 more nodes in this community*

## Relationships

- [main()](main%28%29.md) (40 shared connections)
- [. init ()](_init_%28%29.md) (20 shared connections)
- [.initialize()](initialize%28%29.md) (9 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (8 shared connections)
- [Any](Any.md) (8 shared connections)
- [APIRouter](APIRouter.md) (7 shared connections)
- [Player Position Service](Player_Position_Service.md) (7 shared connections)
- [real time](real_time.md) (5 shared connections)
- [. repr ()](_repr_%28%29.md) (5 shared connections)
- [get skill repository()](get_skill_repository%28%29.md) (4 shared connections)
- [combat](combat.md) (4 shared connections)
- [datetime](datetime.md) (4 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_constants.py`
- `server/async_persistence_room_loader.py`
- `server/npc/combat_integration_base.py`
- `server/npc/movement_integration.py`
- `server/services/schedule_service.py`
- `server/tests/unit/infrastructure/conftest.py`
- `server/tests/unit/infrastructure/test_async_persistence_delegates.py`

## Audit Trail

- EXTRACTED: 761 (90%)
- INFERRED: 83 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*