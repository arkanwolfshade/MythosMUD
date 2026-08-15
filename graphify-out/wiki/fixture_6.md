# fixture

> 9 nodes

## Key Concepts

- **fixture** (5 connections)
- **follow_service()** (4 connections) — `server/tests/integration/test_follow_flow.py`
- **connection_manager()** (3 connections) — `server/tests/integration/test_follow_flow.py`
- **movement_service()** (3 connections) — `server/tests/integration/test_follow_flow.py`
- **user_manager()** (3 connections) — `server/tests/integration/test_follow_flow.py`
- **Mock MovementService; move_player returns True then we can set False for…** (1 connections) — `server/tests/integration/test_follow_flow.py`
- **Mock UserManager; not muted.** (1 connections) — `server/tests/integration/test_follow_flow.py`
- **Mock ConnectionManager (optional for this flow).** (1 connections) — `server/tests/integration/test_follow_flow.py`
- **FollowService wired to real EventBus and mock MovementService.** (1 connections) — `server/tests/integration/test_follow_flow.py`

## Relationships

- [get_logger](get_logger.md) (5 shared connections)
- [FollowService](FollowService.md) (1 shared connections)

## Source Files

- `server/tests/integration/test_follow_flow.py`

## Audit Trail

- EXTRACTED: 13 (93%)
- INFERRED: 1 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*