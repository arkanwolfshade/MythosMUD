# Architecture Decisions Adr

> 7 nodes

## Key Concepts

- **ItemInstance** (7 connections) — `server/game/items/item_instance.py`
- **item_instance.py** (4 connections) — `server/game/items/item_instance.py`
- **.to_inventory_stack()** (3 connections) — `server/game/items/item_instance.py`
- **Any** (1 connections)
- **Item instance model for runtime item representation.  This module defines the It** (1 connections) — `server/game/items/item_instance.py`
- **Runtime representation of an item created from a prototype.** (1 connections) — `server/game/items/item_instance.py`
- **Convert the instance into an inventory stack payload understood by legacy servic** (1 connections) — `server/game/items/item_instance.py`

## Relationships

- [NATS Retry Handler](NATS_Retry_Handler.md) (5 shared connections)
- [Npc Services Combat](Npc_Services_Combat.md) (1 shared connections)

## Source Files

- `server/game/items/item_instance.py`

## Audit Trail

- EXTRACTED: 16 (89%)
- INFERRED: 2 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*