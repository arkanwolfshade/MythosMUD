# _parse_equip_selector

> 4 nodes

## Key Concepts

- **_parse_equip_selector()** (5 connections) — `server/utils/command_factories_inventory.py`
- **_maybe_extract_equip_slot()** (3 connections) — `server/utils/command_factories_inventory.py`
- **If last token is a known slot, return (remaining tokens, slot); else (tokens,…** (1 connections) — `server/utils/command_factories_inventory.py`
- **Parse selector tokens into (index, search_term, target_slot); may raise…** (1 connections) — `server/utils/command_factories_inventory.py`

## Relationships

- [get_logger](get_logger.md) (2 shared connections)
- [InventoryCommandFactory](InventoryCommandFactory.md) (1 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)

## Source Files

- `server/utils/command_factories_inventory.py`

## Audit Trail

- EXTRACTED: 7 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*