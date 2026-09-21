# _ExperienceEventBus

> 6 nodes

## Key Concepts

- **_ExperienceEventBus** (6 connections) — `server/persistence/repositories/experience_repository.py`
- **.__init__()** (4 connections) — `server/persistence/repositories/experience_repository.py`
- **.publish()** (2 connections) — `server/persistence/repositories/experience_repository.py`
- **Protocol** (1 connections)
- **Minimal event bus surface for XP award publishing.** (1 connections) — `server/persistence/repositories/experience_repository.py`
- **Initialize the experience repository. Args: event_bus: Optional EventBus for…** (1 connections) — `server/persistence/repositories/experience_repository.py`

## Relationships

- [EventBus](EventBus.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [ExperienceRepository](ExperienceRepository.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/experience_repository.py`

## Audit Trail

- EXTRACTED: 9 (90%)
- INFERRED: 1 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*