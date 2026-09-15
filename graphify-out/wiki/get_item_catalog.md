# get_item_catalog

> 25 nodes

## Key Concepts

- **get_item_catalog()** (22 connections) — `server/api/item_catalog.py`
- **asyncio** (10 connections)
- **_repo_list_page()** (8 connections) — `server/tests/unit/api/test_item_catalog.py`
- **_SessionCM** (7 connections) — `server/tests/unit/api/test_item_catalog.py`
- **test_get_item_catalog_endpoint_player()** (7 connections) — `server/tests/unit/api/test_item_catalog.py`
- **test_get_item_catalog_endpoint_admin()** (6 connections) — `server/tests/unit/api/test_item_catalog.py`
- **test_get_item_catalog_endpoint_error()** (6 connections) — `server/tests/unit/api/test_item_catalog.py`
- **test_get_item_catalog_endpoint_superuser_is_admin()** (6 connections) — `server/tests/unit/api/test_item_catalog.py`
- **_mock_user()** (5 connections) — `server/tests/unit/api/test_item_catalog.py`
- **test_repository_list_page_db_error()** (5 connections) — `server/tests/unit/api/test_item_catalog.py`
- **test_repository_list_page_invalid_total_count()** (4 connections) — `server/tests/unit/api/test_item_catalog.py`
- **_user_is_admin()** (3 connections) — `server/api/item_catalog.py`
- **test_repository_list_page_empty()** (3 connections) — `server/tests/unit/api/test_item_catalog.py`
- **test_repository_list_page_success()** (3 connections) — `server/tests/unit/api/test_item_catalog.py`
- **.__aenter__()** (1 connections) — `server/tests/unit/api/test_item_catalog.py`
- **.__aexit__()** (1 connections) — `server/tests/unit/api/test_item_catalog.py`
- **.__init__()** (1 connections) — `server/tests/unit/api/test_item_catalog.py`
- **ge** (1 connections)
- **le** (1 connections)
- **Query** (1 connections)
- **Depends** (1 connections)
- **get** (1 connections)
- **Request** (1 connections)
- **Return a paginated item prototype catalog with role-based columns.** (1 connections) — `server/api/item_catalog.py`
- **Typed async context manager for session_maker().** (1 connections) — `server/tests/unit/api/test_item_catalog.py`

## Relationships

- [test_item_catalog.py](test_item_catalog.py.md) (17 shared connections)
- [ItemCatalogService](ItemCatalogService.md) (8 shared connections)
- [catalog_commands.py](catalog_commands.py.md) (4 shared connections)
- [User](User.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [alias_schema.json](alias_schema.json.md) (1 shared connections)
- [_ExecuteResult](_ExecuteResult.md) (1 shared connections)

## Source Files

- `server/api/item_catalog.py`
- `server/tests/unit/api/test_item_catalog.py`

## Audit Trail

- EXTRACTED: 60 (82%)
- INFERRED: 13 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*