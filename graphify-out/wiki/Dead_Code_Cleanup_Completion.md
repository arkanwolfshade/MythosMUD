# Dead Code Cleanup Completion

> 4 nodes

## Key Concepts

- **_is_npc_follow_value()** (6 connections) — `server/game/follow_service.py`
- **_FollowTargetValue** (1 connections)
- **TypeGuard** (1 connections)
- **True when v is the 3-tuple (target_id, 'npc', display_name).** (1 connections) — `server/game/follow_service.py`

## Relationships

- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [NATSError](NATSError.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)

## Source Files

- `server/game/follow_service.py`

## Audit Trail

- EXTRACTED: 6 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*