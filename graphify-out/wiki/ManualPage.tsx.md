# ManualPage.tsx

> 41 nodes · cohesion 0.07

## Key Concepts

- **FollowActionResult** (15 connections) — `server/game/follow_types.py`
- **str_id()** (15 connections) — `server/game/follow_types.py`
- **.request_follow()** (10 connections) — `server/game/follow_service.py`
- **UUID** (9 connections)
- **._send_result_to_player()** (8 connections) — `server/game/follow_service.py`
- **.accept_follow()** (7 connections) — `server/game/follow_service.py`
- **.decline_follow()** (7 connections) — `server/game/follow_service.py`
- **._send_follow_state_to_player()** (7 connections) — `server/game/follow_service.py`
- **.unfollow()** (7 connections) — `server/game/follow_service.py`
- **._create_pending_follow_request()** (6 connections) — `server/game/follow_service.py`
- **._expire_pending_requests()** (6 connections) — `server/game/follow_service.py`
- **._schedule_coro()** (6 connections) — `server/game/follow_service.py`
- **.get_following()** (5 connections) — `server/game/follow_service.py`
- **.get_following_display_name()** (5 connections) — `server/game/follow_service.py`
- **._notify_followee_of_unfollow()** (5 connections) — `server/game/follow_service.py`
- **._start_following_npc()** (5 connections) — `server/game/follow_service.py`
- **._follow_request_mute_failure()** (4 connections) — `server/game/follow_service.py`
- **.on_player_disconnect()** (4 connections) — `server/game/follow_service.py`
- **._send_follow_request_to_target()** (4 connections) — `server/game/follow_service.py`
- **._send_unfollow_notice()** (4 connections) — `server/game/follow_service.py`
- **test_str_id_accepts_uuid()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **Fire-and-forget; close coro if no running event loop (e.g. sync unit tests).…** (1 connections) — `server/game/follow_service.py`
- **Send a command_response-style message to a single player.** (1 connections) — `server/game/follow_service.py`
- **Send follow_state event so client can update title panel (who I am following).** (1 connections) — `server/game/follow_service.py`
- **Immediately attach follow state for an NPC target.** (1 connections) — `server/game/follow_service.py`
- *... and 16 more nodes in this community*

## Relationships

- [SchemaValidator](SchemaValidator.md) (20 shared connections)
- [_CombatServiceDeps](_CombatServiceDeps.md) (12 shared connections)
- [.initialize](initialize.md) (3 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (2 shared connections)
- [test_database_extended.py](test_database_extended.py.md) (2 shared connections)
- [.publish_with_pool](publish_with_pool.md) (1 shared connections)

## Source Files

- `server/game/follow_service.py`
- `server/game/follow_types.py`
- `server/tests/unit/game/test_follow_service.py`

## Audit Trail

- EXTRACTED: 98 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*