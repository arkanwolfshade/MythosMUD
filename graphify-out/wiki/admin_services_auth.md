# admin services auth

> 4 nodes

## Key Concepts

- **_is_npc_follow_value()** (6 connections) — `server/game/follow_service.py`
- **_FollowTargetValue** (1 connections)
- **TypeGuard** (1 connections)
- **True when v is the 3-tuple (target_id, 'npc', display_name).** (1 connections) — `server/game/follow_service.py`

## Relationships

- [combat services messaging](combat_services_messaging.md) (1 shared connections)
- [follow game service](follow_game_service.md) (1 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)

## Source Files

- `server/game/follow_service.py`

## Audit Trail

- EXTRACTED: 9 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*