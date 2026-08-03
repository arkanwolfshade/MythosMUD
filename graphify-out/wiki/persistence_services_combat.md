# persistence services combat

> 14 nodes

## Key Concepts

- **test_follow_flow.py** (13 connections) — `server/tests/integration/test_follow_flow.py`
- **event_bus()** (3 connections) — `server/tests/integration/test_follow_flow.py`
- **follow_service()** (3 connections) — `server/tests/integration/test_follow_flow.py`
- **test_follow_accept_then_move_propagates_then_restricted_exit_unfollows()** (3 connections) — `server/tests/integration/test_follow_flow.py`
- **movement_service()** (2 connections) — `server/tests/integration/test_follow_flow.py`
- **user_manager()** (2 connections) — `server/tests/integration/test_follow_flow.py`
- **connection_manager()** (2 connections) — `server/tests/integration/test_follow_flow.py`
- **Integration tests for follow feature.  Flow: Player A requests follow B; B accep** (1 connections) — `server/tests/integration/test_follow_flow.py`
- **Real EventBus for integration.** (1 connections) — `server/tests/integration/test_follow_flow.py`
- **Mock MovementService; move_player returns True then we can set False for restric** (1 connections) — `server/tests/integration/test_follow_flow.py`
- **Mock UserManager; not muted.** (1 connections) — `server/tests/integration/test_follow_flow.py`
- **Mock ConnectionManager (optional for this flow).** (1 connections) — `server/tests/integration/test_follow_flow.py`
- **FollowService wired to real EventBus and mock MovementService.** (1 connections) — `server/tests/integration/test_follow_flow.py`
- **A requests follow B; B accepts. B moves room_a -> room_b: A moves too.     B mov** (1 connections) — `server/tests/integration/test_follow_flow.py`

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (3 shared connections)
- [item models rationale](item_models_rationale.md) (3 shared connections)
- [follow game service](follow_game_service.md) (3 shared connections)

## Source Files

- `server/tests/integration/test_follow_flow.py`

## Audit Trail

- EXTRACTED: 35 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*