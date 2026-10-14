# ItemCatalogResponse

> 14 nodes

## Key Concepts

- **ItemCatalogResponse** (19 connections) — `server/schemas/item_catalog.py`
- **ItemCatalogPlayerItem** (17 connections) — `server/schemas/item_catalog.py`
- **format_catalog_output()** (12 connections) — `server/commands/catalog_commands.py`
- **schemas/item_catalog.py** (9 connections) — `server/schemas/item_catalog.py`
- **test_format_catalog_output_admin_includes_prototype_id()** (4 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_format_catalog_output_next_page_hint()** (4 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_format_catalog_output_empty()** (3 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **BaseModel** (3 connections)
- **_append_catalog_footer()** (2 connections) — `server/commands/catalog_commands.py`
- **_page_range()** (2 connections) — `server/commands/catalog_commands.py`
- **Format catalog page as a text table with showing header and footer hints.** (1 connections) — `server/commands/catalog_commands.py`
- **Item catalog list schemas for GET /v1/api/item-catalog.** (1 connections) — `server/schemas/item_catalog.py`
- **Player-facing catalog row (P1 columns).** (1 connections) — `server/schemas/item_catalog.py`
- **Paginated item catalog response.** (1 connections) — `server/schemas/item_catalog.py`

## Relationships

- [ItemCatalogService](ItemCatalogService.md) (13 shared connections)
- [catalog_commands.py](catalog_commands.py.md) (10 shared connections)
- [item_catalog_repository.py](item_catalog_repository.py.md) (9 shared connections)
- [test_item_catalog.py](test_item_catalog.py.md) (9 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)

## Source Files

- `server/commands/catalog_commands.py`
- `server/schemas/item_catalog.py`
- `server/tests/unit/commands/test_catalog_commands.py`

## Audit Trail

- EXTRACTED: 52 (85%)
- INFERRED: 9 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*