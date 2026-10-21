# send_system_message

> 25 nodes · cohesion 0.15

## Key Concepts

- **catalog_commands.py** (40 connections) — `server/commands/catalog_commands.py`
- **ItemCatalogResponse** (19 connections) — `server/schemas/item_catalog.py`
- **ItemCatalogPlayerItem** (17 connections) — `server/schemas/item_catalog.py`
- **ItemCatalogAdminItem** (13 connections) — `server/schemas/item_catalog.py`
- **format_catalog_output()** (12 connections) — `server/commands/catalog_commands.py`
- **schemas/item_catalog.py** (9 connections) — `server/schemas/item_catalog.py`
- **_append_admin_rows()** (5 connections) — `server/commands/catalog_commands.py`
- **_append_player_rows()** (4 connections) — `server/commands/catalog_commands.py`
- **test_format_catalog_output_admin_includes_prototype_id()** (4 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_format_catalog_output_next_page_hint()** (4 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **test_format_catalog_output_player()** (4 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **_truncate()** (3 connections) — `server/commands/catalog_commands.py`
- **_user_flag_true()** (3 connections) — `server/commands/catalog_commands.py`
- **BaseModel** (3 connections)
- **test_format_catalog_output_empty()** (3 connections) — `server/tests/unit/commands/test_catalog_commands.py`
- **_append_catalog_footer()** (2 connections) — `server/commands/catalog_commands.py`
- **_format_jsonish()** (2 connections) — `server/commands/catalog_commands.py`
- **_page_range()** (2 connections) — `server/commands/catalog_commands.py`
- **/catalog command: paginated text table of item prototypes.** (1 connections) — `server/commands/catalog_commands.py`
- **Format catalog page as a text table with showing header and footer hints.** (1 connections) — `server/commands/catalog_commands.py`
- **Read a boolean flag from a dict-shaped user or attribute-bearing object…** (1 connections) — `server/commands/catalog_commands.py`
- **Item catalog list schemas for GET /v1/api/item-catalog.** (1 connections) — `server/schemas/item_catalog.py`
- **Player-facing catalog row (P1 columns).** (1 connections) — `server/schemas/item_catalog.py`
- **Admin catalog row with all stored prototype columns (A3).** (1 connections) — `server/schemas/item_catalog.py`
- **Paginated item catalog response.** (1 connections) — `server/schemas/item_catalog.py`

## Relationships

- [properties](properties.md) (24 shared connections)
- [test_game_state_provider_hallucination.py](test_game_state_provider_hallucination.py.md) (11 shared connections)
- [NPCDefinitionCRUDMixin](NPCDefinitionCRUDMixin.md) (11 shared connections)
- [command_parser.py](command_parser.py.md) (6 shared connections)
- [MessageBatcher](MessageBatcher.md) (6 shared connections)
- [._get_npc_display_name](_get_npc_display_name.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [FollowService](FollowService.md) (2 shared connections)
- [CommandFactory](CommandFactory.md) (1 shared connections)

## Source Files

- `server/commands/catalog_commands.py`
- `server/schemas/item_catalog.py`
- `server/tests/unit/commands/test_catalog_commands.py`

## Audit Trail

- EXTRACTED: 99 (89%)
- INFERRED: 12 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*