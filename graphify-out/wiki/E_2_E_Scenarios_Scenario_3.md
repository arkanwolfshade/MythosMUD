# E 2 E Scenarios Scenario

> 4 nodes · cohesion 0.50

## Key Concepts

- **.async_heal_player()** (4 connections) — `server/async_persistence.py`
- **.heal_player()** (4 connections) — `server/async_persistence.py`
- **Heal a player. Delegates to HealthRepository.** (1 connections) — `server/async_persistence.py`
- **Async alias for heal_player. Delegates to HealthRepository.** (1 connections) — `server/async_persistence.py`

## Relationships

- [Combat Command Handler](Combat_Command_Handler.md) (2 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (2 shared connections)

## Source Files

- `server/async_persistence.py`

## Audit Trail

- EXTRACTED: 10 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*