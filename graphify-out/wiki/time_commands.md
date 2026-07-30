# time commands

> 12 nodes

## Key Concepts

- **CreateItemInstanceInput** (11 connections) — `server/async_persistence_constants.py`
- **Profession** (5 connections)
- **.get_professions()** (4 connections) — `server/async_persistence.py`
- **.get_profession_by_id()** (3 connections) — `server/async_persistence.py`
- **.create_item_instance()** (3 connections) — `server/async_persistence.py`
- **async_persistence_constants.py** (3 connections) — `server/async_persistence_constants.py`
- **Get all available professions using SQLAlchemy ORM.** (1 connections) — `server/async_persistence.py`
- **Get a profession by ID. Delegates to ProfessionRepository.** (1 connections) — `server/async_persistence.py`
- **Create a new item instance. Delegates to ItemRepository.** (1 connections) — `server/async_persistence.py`
- **TypedDict** (1 connections)
- **Constants and shared types for async persistence layer.  Extracted to keep async** (1 connections) — `server/async_persistence_constants.py`
- **Optional fields for create_item_instance. owner_type, owner_id, etc. with defaul** (1 connections) — `server/async_persistence_constants.py`

## Relationships

- [chat nats publisher](chat_nats_publisher.md) (4 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (2 shared connections)
- [test player preferences service](test_player_preferences_service.md) (1 shared connections)
- [Protocol](Protocol.md) (1 shared connections)
- [real time](real_time.md) (1 shared connections)
- [PlayerChannelPreferences](PlayerChannelPreferences.md) (1 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (1 shared connections)
- [init](init.md) (1 shared connections)
- [find dead connections()](find_dead_connections%28%29.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_constants.py`

## Audit Trail

- EXTRACTED: 26 (74%)
- INFERRED: 9 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*