# asyncio

> 111 nodes · cohesion 0.04

## Key Concepts

- **PlayerRespawnEventHandler** (57 connections) — `server/realtime/player_event_handlers_respawn.py`
- **test_player_event_handlers_respawn.py** (39 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **asyncio** (23 connections)
- **RespawnPlayerEventPayload** (13 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **_async_persistence()** (11 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **._fetch_delirium_respawn_player_snapshot()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_respawned()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_player_data_for_respawn()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_delirium_respawned()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._resolve_player_data_for_respawn_event()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_player_respawned_event()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_respawn_player_payload()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_fallback_player_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.send_respawn_event_with_retry()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **UUID** (7 connections)
- **_logger_method()** (7 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **_send_personal_message()** (7 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **test_get_player_data_for_delirium_respawn_error_handling()** (7 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **._build_fallback_respawn_player_payload()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._emit_respawn_room_posture()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._send_room_occupants_after_respawn()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **test_get_player_data_for_respawn_error_handling()** (6 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **test_get_player_data_for_respawn_no_get_stats()** (6 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **test_handle_player_delirium_respawned_includes_room_data()** (6 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **test_handle_player_delirium_respawned_success()** (6 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- *... and 86 more nodes in this community*

## Relationships

- [ConnectionManager](ConnectionManager.md) (8 shared connections)
- [look_container.py](look_container.py.md) (7 shared connections)
- [test_command_admin.py](test_command_admin.py.md) (6 shared connections)
- [FollowService](FollowService.md) (4 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (3 shared connections)
- [.publish_with_pool](publish_with_pool.md) (3 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (2 shared connections)
- [test_room_system_message_categories.py](test_room_system_message_categories.py.md) (2 shared connections)
- [WearableContainerServiceError](WearableContainerServiceError.md) (1 shared connections)
- [ItemFactory](ItemFactory.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/player_event_handlers_respawn_types.py`
- `server/tests/unit/realtime/test_player_event_handlers_respawn.py`

## Audit Trail

- EXTRACTED: 229 (87%)
- INFERRED: 33 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*