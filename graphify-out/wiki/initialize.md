# .initialize

> 21 nodes

## Key Concepts

- **.initialize()** (11 connections) — `server/container/bundles/game.py`
- **._init_temporal_layer()** (9 connections) — `server/container/bundles/game.py`
- **._initialize_item_services()** (8 connections) — `server/container/bundles/game.py`
- **._initialize_caching_services()** (6 connections) — `server/container/bundles/game.py`
- **._build_prototype_payload()** (5 connections) — `server/container/bundles/game.py`
- **._require_core_services()** (5 connections) — `server/container/bundles/game.py`
- **._handle_item_prototypes_db_error()** (4 connections) — `server/container/bundles/game.py`
- **._wire_user_manager_after_init()** (4 connections) — `server/container/bundles/game.py`
- **._wire_item_registry_to_player_service()** (3 connections) — `server/container/bundles/game.py`
- **Any** (3 connections)
- **test_game_bundle_require_core_services_raises()** (2 connections) — `server/tests/unit/container/test_container_bundles.py`
- **Exception** (1 connections)
- **Wire user_manager into follow_service and nats_message_handler when present.** (1 connections) — `server/container/bundles/game.py`
- **Set item prototype registry on player service when both are available.** (1 connections) — `server/container/bundles/game.py`
- **Create room and profession cache services; set to None on RuntimeError.** (1 connections) — `server/container/bundles/game.py`
- **Wire holiday/schedule services and Mythos tick scheduler.** (1 connections) — `server/container/bundles/game.py`
- **Initialize game services. Requires Core and Realtime.** (1 connections) — `server/container/bundles/game.py`
- **On SQLAlchemyError: log, optionally warn about schema/DDL, and clear item…** (1 connections) — `server/container/bundles/game.py`
- **Build a single item prototype payload from a DB row for validation.** (1 connections) — `server/container/bundles/game.py`
- **Load item prototypes from PostgreSQL and create item factory.** (1 connections) — `server/container/bundles/game.py`
- **Raise if core services are missing (required before GameBundle init).** (1 connections) — `server/container/bundles/game.py`

## Relationships

- [test_container_bundles.py](test_container_bundles.py.md) (11 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (4 shared connections)
- [validate_calendar.py](validate_calendar.py.md) (2 shared connections)
- [SkillService](SkillService.md) (2 shared connections)
- [HolidayService](HolidayService.md) (1 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (1 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (1 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (1 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (1 shared connections)
- [RoomCacheService](RoomCacheService.md) (1 shared connections)
- [ProfessionCacheService](ProfessionCacheService.md) (1 shared connections)
- [PrototypeRegistry](PrototypeRegistry.md) (1 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/tests/unit/container/test_container_bundles.py`

## Audit Trail

- EXTRACTED: 49 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*