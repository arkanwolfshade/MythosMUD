# analyze_file

> 11 nodes · cohesion 0.18

## Key Concepts

- **fixture** (5 connections)
- **follow_service()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **connection_manager()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **event_bus()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **movement_service()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **user_manager()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **No event bus so we don't need to run the loop; we call handlers directly.** (1 connections) — `server/tests/unit/game/test_follow_service.py`
- **Mock movement service; move_player returns True by default.** (1 connections) — `server/tests/unit/game/test_follow_service.py`
- **Mock user manager; not muted by default.** (1 connections) — `server/tests/unit/game/test_follow_service.py`
- **Mock connection manager (optional for most tests).** (1 connections) — `server/tests/unit/game/test_follow_service.py`
- **FollowService with mocks. connection_manager=None avoids scheduling real…** (1 connections) — `server/tests/unit/game/test_follow_service.py`

## Relationships

- [SchemaValidator](SchemaValidator.md) (6 shared connections)

## Source Files

- `server/tests/unit/game/test_follow_service.py`

## Audit Trail

- EXTRACTED: 16 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*