# test_command_admin.py

> 57 nodes · cohesion 0.05

## Key Concepts

- **_Transport** (27 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **PlayerRespawnedEvent** (25 connections) — `server/events/event_types.py`
- **Emitted** (17 connections)
- **_OfflineRespawnHandler** (14 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **_as()** (11 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **_drive_admin_broadcasts()** (10 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **_drive_combat_publisher()** (10 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **_drive_chat_segments()** (8 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **_drive_command_chokepoint()** (7 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **_drive_system_events()** (7 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **UUID** (7 connections)
- **_StatsPlayer** (7 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **_drive_dp_decay()** (6 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **_drive_npc_died()** (6 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **_drive_rest_countdown()** (6 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **_drive_direct_command_response()** (5 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **_drive_posture()** (5 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **_drive_respawn()** (5 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **_drive_combat_messaging()** (4 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **._record()** (4 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **.handle_player_respawned()** (3 connections) — `server/realtime/player_event_handlers.py`
- **_drive_rescue_update()** (3 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **._resolve_player_data_for_respawn_event()** (3 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **.get_player()** (3 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **.send_personal_message()** (3 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- *... and 32 more nodes in this community*

## Relationships

- [look_container.py](look_container.py.md) (25 shared connections)
- [ConnectionManager](ConnectionManager.md) (7 shared connections)
- [asyncio](asyncio.md) (6 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (5 shared connections)
- [WearableContainerServiceError](WearableContainerServiceError.md) (4 shared connections)
- [ChatService](ChatService.md) (4 shared connections)
- [ui-v2/types.ts](ui-v2-types.ts.md) (3 shared connections)
- [FollowService](FollowService.md) (2 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (2 shared connections)
- [._bind_event_type](_bind_event_type.md) (2 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (2 shared connections)
- [test_database_extended.py](test_database_extended.py.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/player_event_handlers.py`
- `server/tests/unit/realtime/test_message_category_invariants.py`

## Audit Trail

- EXTRACTED: 151 (92%)
- INFERRED: 13 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*