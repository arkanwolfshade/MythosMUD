# _CombatServiceDeps

> 36 nodes · cohesion 0.07

## Key Concepts

- **follow_service.py** (31 connections) — `server/game/follow_service.py`
- **follow_types.py** (12 connections) — `server/game/follow_types.py`
- **FollowPersistence** (12 connections) — `server/game/follow_types.py`
- **FollowStatePayload** (11 connections) — `server/game/follow_types.py`
- **.get_following_display()** (8 connections) — `server/game/follow_service.py`
- **.__init__()** (8 connections) — `server/game/follow_service.py`
- **FollowPlayerView** (8 connections) — `server/game/follow_types.py`
- **is_npc_follow_value()** (8 connections) — `server/game/follow_types.py`
- **PendingFollowRequest** (7 connections) — `server/game/follow_types.py`
- **._resolve_follow_target_label()** (6 connections) — `server/game/follow_service.py`
- **._followers_display_line()** (4 connections) — `server/game/follow_service.py`
- **.get_followers()** (4 connections) — `server/game/follow_service.py`
- **test_send_follow_state_skips_without_manager()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **.get_player_by_id()** (3 connections) — `server/game/follow_types.py`
- **TypedDict** (3 connections)
- **UUID** (3 connections)
- **._send_follow_state_to_player()** (2 connections) — `server/game/follow_movement.py`
- **Protocol** (2 connections)
- **ConnectionManager** (1 connections)
- **FollowTargetValue** (1 connections)
- **UserManager** (1 connections)
- **Follow service for MythosMUD. In-memory follow state: who is following whom…** (1 connections) — `server/game/follow_service.py`
- **Return list of follower player IDs (for movement propagation).** (1 connections) — `server/game/follow_service.py`
- **Human-readable label for the entity this player is following.** (1 connections) — `server/game/follow_service.py`
- **One line listing who follows the player (or none).** (1 connections) — `server/game/follow_service.py`
- *... and 11 more nodes in this community*

## Relationships

- [SchemaValidator](SchemaValidator.md) (16 shared connections)
- [ManualPage.tsx](ManualPage.tsx.md) (12 shared connections)
- [.initialize](initialize.md) (10 shared connections)
- [Room](Room.md) (4 shared connections)
- [CombatInstance](CombatInstance.md) (2 shared connections)
- [BaseEvent](BaseEvent.md) (2 shared connections)
- [get_username_from_user](get_username_from_user.md) (2 shared connections)
- [_find_item_in_equipped](_find_item_in_equipped.md) (2 shared connections)
- [RoomDataCache](RoomDataCache.md) (2 shared connections)
- [.publish_with_pool](publish_with_pool.md) (1 shared connections)
- [test_database_extended.py](test_database_extended.py.md) (1 shared connections)
- [ChatService](ChatService.md) (1 shared connections)

## Source Files

- `server/game/follow_movement.py`
- `server/game/follow_service.py`
- `server/game/follow_types.py`
- `server/tests/unit/game/test_follow_service.py`

## Audit Trail

- EXTRACTED: 96 (89%)
- INFERRED: 12 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*