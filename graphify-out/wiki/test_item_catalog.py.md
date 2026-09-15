# test_item_catalog.py

> 31 nodes

## Key Concepts

- **test_item_catalog.py** (38 connections) — `server/tests/unit/api/test_item_catalog.py`
- **item_catalog_service.py** (19 connections) — `server/game/item_catalog_service.py`
- **ItemCatalogPlayerItem** (17 connections) — `server/schemas/item_catalog.py`
- **ItemCatalogAdminItem** (13 connections) — `server/schemas/item_catalog.py`
- **normalize_catalog_query()** (12 connections) — `server/game/item_catalog_service.py`
- **ItemCatalogPage** (10 connections) — `server/persistence/repositories/item_catalog_repository.py`
- **schemas/item_catalog.py** (9 connections) — `server/schemas/item_catalog.py`
- **ItemPrototypeRow** (8 connections) — `server/persistence/repositories/item_catalog_repository.py`
- **project_admin_item()** (7 connections) — `server/game/item_catalog_service.py`
- **project_player_item()** (7 connections) — `server/game/item_catalog_service.py`
- **test_service_list_catalog_admin_projection()** (7 connections) — `server/tests/unit/api/test_item_catalog.py`
- **test_service_list_catalog_player_projection()** (7 connections) — `server/tests/unit/api/test_item_catalog.py`
- **CatalogQuery** (6 connections) — `server/game/item_catalog_service.py`
- **.list_catalog()** (6 connections) — `server/game/item_catalog_service.py`
- **test_project_player_and_admin()** (6 connections) — `server/tests/unit/api/test_item_catalog.py`
- **_sample_row()** (5 connections) — `server/tests/unit/api/test_item_catalog.py`
- **BaseModel** (3 connections)
- **test_normalize_catalog_query_blank_filters_become_none()** (2 connections) — `server/tests/unit/api/test_item_catalog.py`
- **test_normalize_catalog_query_clamps_and_strips()** (2 connections) — `server/tests/unit/api/test_item_catalog.py`
- **Item catalog service: filtered listing with player/admin column projection.** (1 connections) — `server/game/item_catalog_service.py`
- **Normalized catalog list query.** (1 connections) — `server/game/item_catalog_service.py`
- **Clamp pagination and blank filters to None.** (1 connections) — `server/game/item_catalog_service.py`
- **P1 columns for non-admin viewers.** (1 connections) — `server/game/item_catalog_service.py`
- **A3 full stored prototype columns for admins.** (1 connections) — `server/game/item_catalog_service.py`
- **Fetch one page and project columns for the viewer role.** (1 connections) — `server/game/item_catalog_service.py`
- *... and 6 more nodes in this community*

## Relationships

- [get_item_catalog](get_item_catalog.md) (17 shared connections)
- [catalog_commands.py](catalog_commands.py.md) (15 shared connections)
- [ItemCatalogService](ItemCatalogService.md) (10 shared connections)
- [test_catalog_commands.py](test_catalog_commands.py.md) (9 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (4 shared connections)
- [_ExecuteResult](_ExecuteResult.md) (2 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (1 shared connections)

## Source Files

- `server/game/item_catalog_service.py`
- `server/persistence/repositories/item_catalog_repository.py`
- `server/schemas/item_catalog.py`
- `server/tests/unit/api/test_item_catalog.py`

## Audit Trail

- EXTRACTED: 118 (89%)
- INFERRED: 14 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*