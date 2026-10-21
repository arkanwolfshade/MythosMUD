# reset_database

> 58 nodes · cohesion 0.07

## Key Concepts

- **CorruptionService** (42 connections) — `server/services/corruption_service.py`
- **test_corruption_service.py** (25 connections) — `server/tests/unit/services/test_corruption_service.py`
- **CorruptionPersistenceProtocol** (16 connections) — `server/services/corruption_service.py`
- **_async_session_gen()** (14 connections) — `server/tests/unit/services/test_corruption_service.py`
- **.apply_corruption_adjustment()** (13 connections) — `server/services/corruption_service.py`
- **_player()** (13 connections) — `server/tests/unit/services/test_corruption_service.py`
- **asyncio** (13 connections)
- **CorruptionPersistencePlayer** (11 connections) — `server/services/corruption_service.py`
- **.perform_recovery_action()** (10 connections) — `server/services/corruption_service.py`
- **.get_cooldown_expiry()** (7 connections) — `server/services/corruption_service.py`
- **UUID** (7 connections)
- **test_apply_corruption_adjustment_bypass_permanence_floor_allows_zero()** (7 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_floors_at_1_once_touched()** (7 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_notifies_on_first_taint()** (7 connections) — `server/tests/unit/services/test_corruption_service.py`
- **._notify_tier_crossing()** (6 connections) — `server/services/corruption_service.py`
- **test_apply_corruption_adjustment_notifies_on_tier_crossing()** (6 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_pushes_a_player_update_event()** (6 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_stays_at_0_when_never_touched()** (6 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_writes_through_the_tier_cache()** (6 connections) — `server/tests/unit/services/test_corruption_service.py`
- **CorruptionActionError** (5 connections) — `server/services/corruption_service.py`
- **._send_corruption_update_event()** (5 connections) — `server/services/corruption_service.py`
- **test_apply_corruption_adjustment_clamps_to_100()** (5 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_no_notification_within_a_tier()** (5 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_positive_delta()** (5 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_perform_recovery_action_allows_after_cooldown_expires()** (5 connections) — `server/tests/unit/services/test_corruption_service.py`
- *... and 33 more nodes in this community*

## Relationships

- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (14 shared connections)
- [test_player_respawn_api.py](test_player_respawn_api.py.md) (10 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (5 shared connections)
- [retry.py](retry.py.md) (4 shared connections)
- [test_command_communication.py](test_command_communication.py.md) (3 shared connections)
- [RoomService](RoomService.md) (3 shared connections)
- [cleanse_command.py](cleanse_command.py.md) (3 shared connections)
- [_str_id](_str_id.md) (3 shared connections)
- [ItemFactory](ItemFactory.md) (3 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)

## Source Files

- `server/services/corruption_service.py`
- `server/tests/unit/services/test_corruption_service.py`

## Audit Trail

- EXTRACTED: 161 (87%)
- INFERRED: 24 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*