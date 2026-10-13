# Community 1440

> 6 nodes

## Key Concepts

- **_ContainerWithPersistence** (5 connections) — `server/container/async_persistence_access.py`
- **_ApplicationContainerType** (4 connections) — `server/container/async_persistence_access.py`
- **.get_instance()** (2 connections) — `server/container/async_persistence_access.py`
- **Protocol** (2 connections)
- **Container singleton surface needed for persistence lookup.** (1 connections) — `server/container/async_persistence_access.py`
- **ApplicationContainer.get_instance without importing container.main.** (1 connections) — `server/container/async_persistence_access.py`

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (3 shared connections)

## Source Files

- `server/container/async_persistence_access.py`

## Audit Trail

- EXTRACTED: 8 (89%)
- INFERRED: 1 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*