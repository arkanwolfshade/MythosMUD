# ._init_player_quest_layer

> 18 nodes

## Key Concepts

- **._init_player_quest_layer()** (16 connections) — `server/container/bundles/game.py`
- **.event_bus()** (12 connections) — `server/realtime/connection_manager.py`
- **.initialize()** (11 connections) — `server/container/bundles/game.py`
- **._init_quest_service()** (7 connections) — `server/container/bundles/game.py`
- **._initialize_caching_services()** (6 connections) — `server/container/bundles/game.py`
- **._build_prototype_payload()** (5 connections) — `server/container/bundles/game.py`
- **._get_integration_dependencies()** (5 connections) — `server/npc/npc_base.py`
- **._wire_user_manager_after_init()** (4 connections) — `server/container/bundles/game.py`
- **._wire_item_registry_to_player_service()** (3 connections) — `server/container/bundles/game.py`
- **Any** (3 connections)
- **Wire user_manager into follow_service and nats_message_handler when present.** (1 connections) — `server/container/bundles/game.py`
- **Set item prototype registry on player service when both are available.** (1 connections) — `server/container/bundles/game.py`
- **Create room and profession cache services; set to None on RuntimeError.** (1 connections) — `server/container/bundles/game.py`
- **Wire player/room/user, container, skill, level, and quest services.** (1 connections) — `server/container/bundles/game.py`
- **Initialize game services. Requires Core and Realtime.** (1 connections) — `server/container/bundles/game.py`
- **Build a single item prototype payload from a DB row for validation.** (1 connections) — `server/container/bundles/game.py`
- **Return (event_bus, persistence) for movement integration, or (None, None).** (1 connections) — `server/npc/npc_base.py`
- **Get the event bus from connection manager.** (1 connections) — `server/realtime/connection_manager.py`

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (11 shared connections)
- [bundles/game.py](bundles-game.py.md) (3 shared connections)
- [._initialize_item_services](_initialize_item_services.md) (2 shared connections)
- [RoomCacheService](RoomCacheService.md) (2 shared connections)
- [NPCBase](NPCBase.md) (2 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [ExplorationService](ExplorationService.md) (1 shared connections)
- [UserManager](UserManager.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (1 shared connections)
- [SkillRepository](SkillRepository.md) (1 shared connections)
- [PlayerSkillRepository](PlayerSkillRepository.md) (1 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/npc/npc_base.py`
- `server/realtime/connection_manager.py`

## Audit Trail

- EXTRACTED: 53 (85%)
- INFERRED: 9 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*