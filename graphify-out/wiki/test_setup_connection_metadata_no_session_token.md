# test_setup_connection_metadata_no_session_token

> 2 nodes

## Key Concepts

- **follow_service()** (3 connections) — `server/tests/integration/test_follow_flow.py`
- **FollowService wired to real EventBus and mock MovementService.** (1 connections) — `server/tests/integration/test_follow_flow.py`

## Relationships

- [Player Respawn Handlers](Player_Respawn_Handlers.md) (1 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (1 shared connections)

## Source Files

- `server/tests/integration/test_follow_flow.py`

## Audit Trail

- EXTRACTED: 4 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*