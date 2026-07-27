# Admin Summon Command

> 8 nodes · cohesion 0.08

## Key Concepts

- **CommandResponse** (9 connections) — `server/commands/inventory_get_command.py`
- **UUID** (7 connections) — `server/commands/inventory_get_command.py`
- **CommandResponse** (7 connections) — `server/commands/inventory_pickup_command.py`
- **Player** (6 connections) — `server/commands/inventory_get_command.py`
- **Player** (4 connections) — `server/commands/inventory_pickup_command.py`
- **UUID** (4 connections) — `server/commands/inventory_pickup_command.py`
- **UUID** (3 connections) — `server/commands/inventory_command_helpers.py`
- **_FloorPickupResolved** (2 connections) — `server/commands/inventory_pickup_command.py`

## Relationships

- No strong cross-community connections detected

## Source Files

- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_get_command.py`
- `server/commands/inventory_pickup_command.py`

## Audit Trail

- EXTRACTED: 26 (62%)
- INFERRED: 16 (38%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*