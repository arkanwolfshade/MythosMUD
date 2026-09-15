# ItemCatalogService

> 14 nodes

## Key Concepts

- **ItemCatalogService** (35 connections) — `server/game/item_catalog_service.py`
- **._init_player_quest_layer()** (18 connections) — `server/container/bundles/game.py`
- **ItemCatalogRepository** (16 connections) — `server/persistence/repositories/item_catalog_repository.py`
- **get_item_catalog_service()** (6 connections) — `server/dependencies.py`
- **_CatalogContainerStub** (4 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **.__init__()** (3 connections) — `server/game/item_catalog_service.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/item_catalog_repository.py`
- **.__init__()** (2 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **Wire player/room/user, container, skill, level, and quest services.** (1 connections) — `server/container/bundles/game.py`
- **Get ItemCatalogService for /catalog and GET /api/item-catalog.** (1 connections) — `server/dependencies.py`
- **List item prototypes with role-based projection.** (1 connections) — `server/game/item_catalog_service.py`
- **Create service with optional repository override for tests.** (1 connections) — `server/game/item_catalog_service.py`
- **Persistence for item catalog listing via list_item_prototypes_page().** (1 connections) — `server/persistence/repositories/item_catalog_repository.py`
- **Initialize the item catalog repository.** (1 connections) — `server/persistence/repositories/item_catalog_repository.py`

## Relationships

- [test_catalog_commands.py](test_catalog_commands.py.md) (10 shared connections)
- [test_item_catalog.py](test_item_catalog.py.md) (10 shared connections)
- [get_item_catalog](get_item_catalog.md) (8 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (4 shared connections)
- [catalog_commands.py](catalog_commands.py.md) (3 shared connections)
- [bundles/game.py](bundles-game.py.md) (3 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (2 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [RoomService](RoomService.md) (1 shared connections)
- [UserManager](UserManager.md) (1 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/dependencies.py`
- `server/game/item_catalog_service.py`
- `server/persistence/repositories/item_catalog_repository.py`
- `server/tests/unit/commands/test_catalog_commands.py`

## Audit Trail

- EXTRACTED: 55 (72%)
- INFERRED: 21 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*