# server tests integration test follow

> 16 nodes

## Key Concepts

- **test_follow_flow.py** (15 connections) — `server/tests/integration/test_follow_flow.py`
- **fixture** (5 connections)
- **event_bus()** (4 connections) — `server/tests/integration/test_follow_flow.py`
- **follow_service()** (4 connections) — `server/tests/integration/test_follow_flow.py`
- **test_follow_accept_then_move_propagates_then_restricted_exit_unfollows()** (4 connections) — `server/tests/integration/test_follow_flow.py`
- **connection_manager()** (3 connections) — `server/tests/integration/test_follow_flow.py`
- **movement_service()** (3 connections) — `server/tests/integration/test_follow_flow.py`
- **user_manager()** (3 connections) — `server/tests/integration/test_follow_flow.py`
- **asyncio** (2 connections)
- **Integration tests for follow feature. Flow: Player A requests follow B; B…** (1 connections) — `server/tests/integration/test_follow_flow.py`
- **Real EventBus for integration.** (1 connections) — `server/tests/integration/test_follow_flow.py`
- **Mock MovementService; move_player returns True then we can set False for…** (1 connections) — `server/tests/integration/test_follow_flow.py`
- **Mock UserManager; not muted.** (1 connections) — `server/tests/integration/test_follow_flow.py`
- **Mock ConnectionManager (optional for this flow).** (1 connections) — `server/tests/integration/test_follow_flow.py`
- **FollowService wired to real EventBus and mock MovementService.** (1 connections) — `server/tests/integration/test_follow_flow.py`
- **A requests follow B; B accepts. B moves room_a -> room_b: A moves too. B moves…** (1 connections) — `server/tests/integration/test_follow_flow.py`

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [moduletype](moduletype.md) (2 shared connections)
- [followtargetvalue](followtargetvalue.md) (2 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)

## Source Files

- `server/tests/integration/test_follow_flow.py`

## Audit Trail

- EXTRACTED: 27 (90%)
- INFERRED: 3 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*