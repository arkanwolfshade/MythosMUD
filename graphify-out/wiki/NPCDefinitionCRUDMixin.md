# NPCDefinitionCRUDMixin

> 35 nodes · cohesion 0.11

## Key Concepts

- **test_item_catalog.py** (38 connections) — `server/tests/unit/api/test_item_catalog.py`
- **ItemCatalogRepository** (16 connections) — `server/persistence/repositories/item_catalog_repository.py`
- **normalize_catalog_query()** (12 connections) — `server/game/item_catalog_service.py`
- **ItemCatalogPage** (10 connections) — `server/persistence/repositories/item_catalog_repository.py`
- **asyncio** (10 connections)
- **_repo_list_page()** (8 connections) — `server/tests/unit/api/test_item_catalog.py`
- **_SessionCM** (7 connections) — `server/tests/unit/api/test_item_catalog.py`
- **test_get_item_catalog_endpoint_player()** (7 connections) — `server/tests/unit/api/test_item_catalog.py`
- **test_service_list_catalog_admin_projection()** (7 connections) — `server/tests/unit/api/test_item_catalog.py`
- **test_service_list_catalog_player_projection()** (7 connections) — `server/tests/unit/api/test_item_catalog.py`
- **.list_page()** (6 connections) — `server/persistence/repositories/item_catalog_repository.py`
- **test_get_item_catalog_endpoint_admin()** (6 connections) — `server/tests/unit/api/test_item_catalog.py`
- **test_get_item_catalog_endpoint_error()** (6 connections) — `server/tests/unit/api/test_item_catalog.py`
- **test_get_item_catalog_endpoint_superuser_is_admin()** (6 connections) — `server/tests/unit/api/test_item_catalog.py`
- **_mock_user()** (5 connections) — `server/tests/unit/api/test_item_catalog.py`
- **_sample_row()** (5 connections) — `server/tests/unit/api/test_item_catalog.py`
- **test_repository_list_page_db_error()** (5 connections) — `server/tests/unit/api/test_item_catalog.py`
- **test_repository_list_page_invalid_total_count()** (4 connections) — `server/tests/unit/api/test_item_catalog.py`
- **.__init__()** (3 connections) — `server/game/item_catalog_service.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/item_catalog_repository.py`
- **test_repository_list_page_empty()** (3 connections) — `server/tests/unit/api/test_item_catalog.py`
- **test_repository_list_page_success()** (3 connections) — `server/tests/unit/api/test_item_catalog.py`
- **test_normalize_catalog_query_blank_filters_become_none()** (2 connections) — `server/tests/unit/api/test_item_catalog.py`
- **test_normalize_catalog_query_clamps_and_strips()** (2 connections) — `server/tests/unit/api/test_item_catalog.py`
- **Clamp pagination and blank filters to None.** (1 connections) — `server/game/item_catalog_service.py`
- *... and 10 more nodes in this community*

## Relationships

- [test_game_state_provider_hallucination.py](test_game_state_provider_hallucination.py.md) (16 shared connections)
- [properties](properties.md) (11 shared connections)
- [send_system_message](send_system_message.md) (11 shared connections)
- [._get_npc_display_name](_get_npc_display_name.md) (9 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (4 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (3 shared connections)
- [TestHorizontalExitCharBetween](TestHorizontalExitCharBetween.md) (3 shared connections)
- [endpoints.py](endpoints.py.md) (2 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (2 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (1 shared connections)
- [Room](Room.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)

## Source Files

- `server/game/item_catalog_service.py`
- `server/persistence/repositories/item_catalog_repository.py`
- `server/tests/unit/api/test_item_catalog.py`

## Audit Trail

- EXTRACTED: 107 (84%)
- INFERRED: 21 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*