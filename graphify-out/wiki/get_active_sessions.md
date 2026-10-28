# .get_active_sessions

> 8 nodes · cohesion 0.32

## Key Concepts

- **async_persistence_access.py** (7 connections) — `server/container/async_persistence_access.py`
- **_ContainerWithPersistence** (5 connections) — `server/container/async_persistence_access.py`
- **_ApplicationContainerType** (4 connections) — `server/container/async_persistence_access.py`
- **.get_instance()** (2 connections) — `server/container/async_persistence_access.py`
- **Protocol** (2 connections)
- **Access the DI container's live AsyncPersistenceLayer singleton.** (1 connections) — `server/container/async_persistence_access.py`
- **Container singleton surface needed for persistence lookup.** (1 connections) — `server/container/async_persistence_access.py`
- **ApplicationContainer.get_instance without importing container.main.** (1 connections) — `server/container/async_persistence_access.py`

## Relationships

- [test_party_service.py](test_party_service.py.md) (3 shared connections)
- [Room](Room.md) (1 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (1 shared connections)

## Source Files

- `server/container/async_persistence_access.py`

## Audit Trail

- EXTRACTED: 13 (93%)
- INFERRED: 1 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*