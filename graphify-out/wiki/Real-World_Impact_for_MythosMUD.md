# Real-World Impact for MythosMUD

> 6 nodes · cohesion 0.40

## Key Concepts

- **_AsyncPersistenceRoomFacadeBase** (7 connections) — `server/async_persistence_room_facade.py`
- **._ensure_room_cache_loaded()** (3 connections) — `server/async_persistence_room_facade.py`
- **._load_room_cache_async()** (3 connections) — `server/async_persistence_room_facade.py`
- **Attrs provided by AsyncPersistenceLayer when mixed in.** (1 connections) — `server/async_persistence_room_facade.py`
- **Ensure room cache is loaded (lazy loading with lock).** (1 connections) — `server/async_persistence_room_facade.py`
- **Load rooms from PostgreSQL via RoomCacheLoader.** (1 connections) — `server/async_persistence_room_facade.py`

## Relationships

- [FastAPI Code Review - Anti-Patterns and Best Practices](FastAPI_Code_Review_-_Anti-Patterns_and_Best_Practices.md) (2 shared connections)
- [Async Remediation Final Report](Async_Remediation_Final_Report.md) (1 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (1 shared connections)

## Source Files

- `server/async_persistence_room_facade.py`

## Audit Trail

- EXTRACTED: 8 (80%)
- INFERRED: 2 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*