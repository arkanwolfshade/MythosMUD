# Cache and NPC Cache

> 122 nodes

## Key Concepts

- **GameBundle** (45 connections) — `server/container/bundles/game.py`
- **LRUCache** (27 connections) — `server/caching/lru_cache.py`
- **RoomCacheService** (17 connections) — `server/caching/cache_service.py`
- **get_cache_manager()** (16 connections) — `server/caching/lru_cache.py`
- **._init_player_quest_layer()** (16 connections) — `server/container/bundles/game.py`
- **ProfessionCacheService** (15 connections) — `server/caching/cache_service.py`
- **cache_service.py** (13 connections) — `server/caching/cache_service.py`
- **Any** (13 connections)
- **LevelService** (13 connections) — `server/game/level_service.py`
- **__init__.py** (12 connections) — `server/caching/__init__.py`
- **lru_cache.py** (12 connections) — `server/caching/lru_cache.py`
- **CacheManager** (12 connections) — `server/caching/lru_cache.py`
- **.initialize()** (11 connections) — `server/container/bundles/game.py`
- **CacheService** (8 connections) — `server/caching/cache_service.py`
- **.items()** (8 connections) — `server/caching/lru_cache.py`
- **.__init__()** (7 connections) — `server/caching/cache_service.py`
- **K** (7 connections)
- **.get_or_set()** (7 connections) — `server/caching/lru_cache.py`
- **._init_quest_service()** (7 connections) — `server/container/bundles/game.py`
- **.get()** (6 connections) — `server/caching/lru_cache.py`
- **.put()** (6 connections) — `server/caching/lru_cache.py`
- **._initialize_caching_services()** (6 connections) — `server/container/bundles/game.py`
- **cached()** (5 connections) — `server/caching/cache_service.py`
- **.get_all_professions()** (5 connections) — `server/caching/cache_service.py`
- **V** (5 connections)
- *... and 97 more nodes in this community*

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (21 shared connections)
- [Grace Period Blocking Tests](Grace_Period_Blocking_Tests.md) (8 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (7 shared connections)
- [Monitoring Response Models](Monitoring_Response_Models.md) (5 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (5 shared connections)
- [Realtime Visual Indicator](Realtime_Visual_Indicator.md) (4 shared connections)
- [Game Magic Spell](Game_Magic_Spell.md) (3 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (3 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (3 shared connections)
- [Status Effect Model](Status_Effect_Model.md) (3 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (3 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (2 shared connections)

## Source Files

- `server/caching/__init__.py`
- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/container/bundles/game.py`
- `server/game/level_service.py`

## Audit Trail

- EXTRACTED: 448 (91%)
- INFERRED: 44 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*