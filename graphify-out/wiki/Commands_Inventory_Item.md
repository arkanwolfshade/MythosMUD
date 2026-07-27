# Commands Inventory Item

> 10 nodes · cohesion 0.02

## Key Concepts

- **Any** (8 connections) — `server/services/equipment_service.py`
- **InventoryStack** (8 connections) — `server/services/equipment_service.py`
- **CommandResponse** (7 connections) — `server/commands/inventory_equip_command.py`
- **UUID** (7 connections) — `server/services/inventory_service.py`
- **InventoryStack** (4 connections) — `server/commands/equipment_helpers.py`
- **CommandResponse** (4 connections) — `server/commands/inventory_unequip_command.py`
- **AbstractContextManager** (3 connections) — `server/services/inventory_service.py`
- **Player** (3 connections) — `server/commands/equipment_helpers.py`
- **Player** (3 connections) — `server/commands/inventory_equip_command.py`
- **Player** (3 connections) — `server/commands/inventory_unequip_command.py`

## Relationships

- No strong cross-community connections detected

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_equip_command.py`
- `server/commands/inventory_unequip_command.py`
- `server/services/equipment_service.py`
- `server/services/inventory_service.py`

## Audit Trail

- EXTRACTED: 38 (76%)
- INFERRED: 12 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*