# ._init_player_quest_layer

> 31 nodes

## Key Concepts

- **._init_player_quest_layer()** (16 connections) — `server/container/bundles/game.py`
- **.initialize()** (11 connections) — `server/container/bundles/game.py`
- **._initialize_item_services()** (8 connections) — `server/container/bundles/game.py`
- **decode_json_column()** (7 connections) — `server/container/utils.py`
- **._initialize_caching_services()** (6 connections) — `server/container/bundles/game.py`
- **._build_prototype_payload()** (5 connections) — `server/container/bundles/game.py`
- **._init_emote_service()** (5 connections) — `server/container/bundles/game.py`
- **._require_core_services()** (5 connections) — `server/container/bundles/game.py`
- **._handle_item_prototypes_db_error()** (4 connections) — `server/container/bundles/game.py`
- **._wire_user_manager_after_init()** (4 connections) — `server/container/bundles/game.py`
- **._decode_json_column()** (4 connections) — `server/container/main.py`
- **._wire_item_registry_to_player_service()** (3 connections) — `server/container/bundles/game.py`
- **.get_service()** (3 connections) — `server/container/main.py`
- **Any** (3 connections)
- **Any** (3 connections)
- **test_game_bundle_require_core_services_raises()** (2 connections) — `server/tests/unit/container/test_container_bundles.py`
- **Exception** (1 connections)
- **Any** (1 connections)
- **Wire user_manager into follow_service and nats_message_handler when present.** (1 connections) — `server/container/bundles/game.py`
- **Set item prototype registry on player service when both are available.** (1 connections) — `server/container/bundles/game.py`
- **Create room and profession cache services; set to None on RuntimeError.** (1 connections) — `server/container/bundles/game.py`
- **Wire player/room/user, container, skill, level, and quest services.** (1 connections) — `server/container/bundles/game.py`
- **Create the emote repository/service and load predefined emotes once, at…** (1 connections) — `server/container/bundles/game.py`
- **Initialize game services. Requires Core and Realtime.** (1 connections) — `server/container/bundles/game.py`
- **On SQLAlchemyError: log, optionally warn about schema/DDL, and clear item…** (1 connections) — `server/container/bundles/game.py`
- *... and 6 more nodes in this community*

## Relationships

- [test_container_bundles.py](test_container_bundles.py.md) (14 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (6 shared connections)
- [DatabaseError](DatabaseError.md) (4 shared connections)
- [ScheduleService](ScheduleService.md) (2 shared connections)
- [EmoteService](EmoteService.md) (1 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [RoomService](RoomService.md) (1 shared connections)
- [UserManager](UserManager.md) (1 shared connections)
- [ContainerService](ContainerService.md) (1 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (1 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/tests/unit/container/test_container_bundles.py`

## Audit Trail

- EXTRACTED: 72 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*