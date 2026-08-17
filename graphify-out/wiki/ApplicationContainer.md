# ApplicationContainer

> 817 nodes

## Key Concepts

- **ApplicationContainer** (157 connections) — `server/container/main.py`
- **server/dependencies.py** (107 connections) — `server/dependencies.py`
- **time.py** (97 connections) — `server/container/bundles/time.py`
- **LucidityService** (79 connections) — `server/services/lucidity_service.py`
- **PlayerLucidity** (69 connections) — `server/models/lucidity.py`
- **lifespan_startup.py** (64 connections) — `server/app/lifespan_startup.py`
- **test_player_respawn_service.py** (55 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **lucidity_service.py** (52 connections) — `server/services/lucidity_service.py`
- **lifecycle_manager.py** (49 connections) — `server/npc/lifecycle_manager.py`
- **threading.py** (47 connections) — `server/npc/threading.py`
- **bundles/game.py** (44 connections) — `server/container/bundles/game.py`
- **lifespan.py** (43 connections) — `server/app/lifespan.py`
- **test_lifespan_startup.py** (41 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **player_respawn_service.py** (40 connections) — `server/services/player_respawn_service.py`
- **service.py** (36 connections) — `server/services/passive_lucidity_flux/service.py`
- **lucidity.py** (35 connections) — `server/models/lucidity.py`
- **server/models/game.py** (33 connections) — `server/models/game.py`
- **MemoryLeakMetricsCollector** (30 connections) — `server/monitoring/memory_leak_metrics.py`
- **LRUCache** (29 connections) — `server/caching/lru_cache.py`
- **ScheduleEntry** (29 connections) — `server/schemas/calendar/calendar.py`
- **api/game.py** (29 connections) — `server/api/game.py`
- **ScheduleService** (28 connections) — `server/services/schedule_service.py`
- **get_mythos_chronicle()** (27 connections) — `server/time/time_service.py`
- **asyncio** (27 connections)
- **time_service.py** (27 connections) — `server/time/time_service.py`
- *... and 792 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (154 shared connections)
- [DatabaseError](DatabaseError.md) (99 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (74 shared connections)
- [ConnectionManager](ConnectionManager.md) (58 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (56 shared connections)
- [AliasStorage](AliasStorage.md) (37 shared connections)
- [test_application_container.py](test_application_container.py.md) (27 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (21 shared connections)
- [test_lifespan_helpers.py](test_lifespan_helpers.py.md) (20 shared connections)
- [PlayerService](PlayerService.md) (20 shared connections)
- [RoomCacheService](RoomCacheService.md) (18 shared connections)
- [NPCDied](NPCDied.md) (18 shared connections)

## Source Files

- `server/api/game.py`
- `server/api/system_monitoring.py`
- `server/app/game_tick_corpses.py`
- `server/app/lifespan.py`
- `server/app/lifespan_magic.py`
- `server/app/lifespan_startup.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/caching/__init__.py`
- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/commands/shutdown_process_termination.py`
- `server/container/__init__.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/game.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/dependencies.py`

## Audit Trail

- EXTRACTED: 2678 (94%)
- INFERRED: 162 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*