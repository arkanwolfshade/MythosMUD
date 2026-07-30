# get item prototype count()

> 4 nodes

## Key Concepts

- **.damage_player()** (4 connections) — `server/async_persistence.py`
- **.async_damage_player()** (4 connections) — `server/async_persistence.py`
- **Damage a player. Delegates to HealthRepository.** (1 connections) — `server/async_persistence.py`
- **Async alias for damage_player. Delegates to HealthRepository.** (1 connections) — `server/async_persistence.py`

## Relationships

- [chat nats publisher](chat_nats_publisher.md) (2 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (2 shared connections)

## Source Files

- `server/async_persistence.py`

## Audit Trail

- EXTRACTED: 10 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*