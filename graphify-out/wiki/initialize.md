# .initialize

> 21 nodes

## Key Concepts

- **.initialize()** (11 connections) — `server/container/bundles/game.py`
- **._initialize_item_services()** (8 connections) — `server/container/bundles/game.py`
- **._initialize_caching_services()** (6 connections) — `server/container/bundles/game.py`
- **._build_prototype_payload()** (5 connections) — `server/container/bundles/game.py`
- **._init_emote_service()** (5 connections) — `server/container/bundles/game.py`
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
- **Create the emote repository/service and load predefined emotes once, at…** (1 connections) — `server/container/bundles/game.py`
- **Initialize game services. Requires Core and Realtime.** (1 connections) — `server/container/bundles/game.py`
- **On SQLAlchemyError: log, optionally warn about schema/DDL, and clear item…** (1 connections) — `server/container/bundles/game.py`
- **Build a single item prototype payload from a DB row for validation.** (1 connections) — `server/container/bundles/game.py`
- **Load item prototypes from PostgreSQL and create item factory.** (1 connections) — `server/container/bundles/game.py`
- **Raise if core services are missing (required before GameBundle init).** (1 connections) — `server/container/bundles/game.py`

## Relationships

- [test_container_bundles.py](test_container_bundles.py.md) (11 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [PlayerService](PlayerService.md) (2 shared connections)
- [test_emote_repository.py](test_emote_repository.py.md) (1 shared connections)
- [EmoteService](EmoteService.md) (1 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (1 shared connections)
- [InstanceManager](InstanceManager.md) (1 shared connections)
- [RoomCacheService](RoomCacheService.md) (1 shared connections)
- [ProfessionCacheService](ProfessionCacheService.md) (1 shared connections)
- [PrototypeRegistry](PrototypeRegistry.md) (1 shared connections)
- [PrototypeRegistryError](PrototypeRegistryError.md) (1 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/tests/unit/container/test_container_bundles.py`

## Audit Trail

- EXTRACTED: 45 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*