# test_query_rooms_with_exits_async_table_not_found

> 4 nodes

## Key Concepts

- **_is_npc_follow_value()** (6 connections) — `server/game/follow_service.py`
- **_FollowTargetValue** (1 connections)
- **TypeGuard** (1 connections)
- **True when v is the 3-tuple (target_id, 'npc', display_name).** (1 connections) — `server/game/follow_service.py`

## Relationships

- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Player Respawn Handlers](Player_Respawn_Handlers.md) (1 shared connections)

## Source Files

- `server/game/follow_service.py`

## Audit Trail

- EXTRACTED: 9 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*