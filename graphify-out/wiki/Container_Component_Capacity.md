# Container Component Capacity

> 9 nodes · cohesion 0.01

## Key Concepts

- **Any** (8 connections) — `server/models/container.py`
- **UUID** (7 connections) — `server/api/container_events.py`
- **Any** (6 connections) — `server/api/container_events.py`
- **UUID** (5 connections) — `server/models/container.py`
- **ContainerComponent** (3 connections) — `server/api/container_events.py`
- **datetime** (3 connections) — `server/models/container.py`
- **InventoryStack** (3 connections) — `server/models/container.py`
- **Request** (2 connections) — `server/api/container_endpoints_loot.py`
- **ValidationInfo** (2 connections) — `server/models/container.py`

## Relationships

- No strong cross-community connections detected

## Source Files

- `server/api/container_endpoints_loot.py`
- `server/api/container_events.py`
- `server/models/container.py`

## Audit Trail

- EXTRACTED: 32 (82%)
- INFERRED: 7 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*