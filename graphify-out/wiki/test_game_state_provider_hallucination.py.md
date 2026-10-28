# test_game_state_provider_hallucination.py

> 20 nodes · cohesion 0.16

## Key Concepts

- **item_catalog_repository.py** (20 connections) — `server/persistence/repositories/item_catalog_repository.py`
- **item_catalog_service.py** (19 connections) — `server/game/item_catalog_service.py`
- **ItemPrototypeRow** (8 connections) — `server/persistence/repositories/item_catalog_repository.py`
- **project_admin_item()** (7 connections) — `server/game/item_catalog_service.py`
- **project_player_item()** (7 connections) — `server/game/item_catalog_service.py`
- **CatalogQuery** (6 connections) — `server/game/item_catalog_service.py`
- **.list_catalog()** (6 connections) — `server/game/item_catalog_service.py`
- **test_project_player_and_admin()** (6 connections) — `server/tests/unit/api/test_item_catalog.py`
- **_mappings_to_page()** (5 connections) — `server/persistence/repositories/item_catalog_repository.py`
- **_row_to_prototype()** (5 connections) — `server/persistence/repositories/item_catalog_repository.py`
- **_as_object_dict()** (2 connections) — `server/persistence/repositories/item_catalog_repository.py`
- **_as_object_list()** (2 connections) — `server/persistence/repositories/item_catalog_repository.py`
- **_coerce_int()** (2 connections) — `server/persistence/repositories/item_catalog_repository.py`
- **Item catalog service: filtered listing with player/admin column projection.** (1 connections) — `server/game/item_catalog_service.py`
- **Normalized catalog list query.** (1 connections) — `server/game/item_catalog_service.py`
- **P1 columns for non-admin viewers.** (1 connections) — `server/game/item_catalog_service.py`
- **A3 full stored prototype columns for admins.** (1 connections) — `server/game/item_catalog_service.py`
- **Fetch one page and project columns for the viewer role.** (1 connections) — `server/game/item_catalog_service.py`
- **Repository for paginated item_prototypes catalog listing.** (1 connections) — `server/persistence/repositories/item_catalog_repository.py`
- **One item_prototypes row from list_item_prototypes_page.** (1 connections) — `server/persistence/repositories/item_catalog_repository.py`

## Relationships

- [NPCDefinitionCRUDMixin](NPCDefinitionCRUDMixin.md) (16 shared connections)
- [send_system_message](send_system_message.md) (11 shared connections)
- [properties](properties.md) (4 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (2 shared connections)
- [endpoints.py](endpoints.py.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [._get_npc_display_name](_get_npc_display_name.md) (1 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (1 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (1 shared connections)

## Source Files

- `server/game/item_catalog_service.py`
- `server/persistence/repositories/item_catalog_repository.py`
- `server/tests/unit/api/test_item_catalog.py`

## Audit Trail

- EXTRACTED: 68 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*