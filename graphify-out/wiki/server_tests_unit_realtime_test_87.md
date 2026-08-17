# server tests unit realtime test

> 49 nodes

## Key Concepts

- **test_event_handler.py** (42 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **asyncio** (15 connections)
- **Test RealTimeEventHandler._handle_player_entered() delegates to player_handler.** (8 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **event_handler()** (7 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_npc_entered()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_npc_left()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_delirium_respawned()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_died()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_dp_decay()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_dp_updated()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_entered()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_left()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_respawned()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_xp_awarded()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **fixture** (4 connections)
- **mock_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **mock_event_bus()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **mock_task_registry()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_create_player_entered_message()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_create_player_left_message()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_get_room_occupants()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_init()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_init_no_event_bus()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_send_occupants_snapshot_to_player()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_send_room_occupants_update()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- *... and 24 more nodes in this community*

## Relationships

- [server realtime event handler py](server_realtime_event_handler_py.md) (4 shared connections)
- [baseevent](baseevent.md) (4 shared connections)
- [server events event types playerdiedevent](server_events_event_types_playerdiedevent.md) (4 shared connections)
- [server events event types playerdpupdated](server_events_event_types_playerdpupdated.md) (4 shared connections)
- [server events event types playerenteredroom](server_events_event_types_playerenteredroom.md) (3 shared connections)
- [server events event types playerleftroom](server_events_event_types_playerleftroom.md) (3 shared connections)
- [server events event bus](server_events_event_bus.md) (3 shared connections)
- [moduletype](moduletype.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (1 shared connections)
- [server realtime player connection setup](server_realtime_player_connection_setup.md) (1 shared connections)
- [server realtime envelope build event](server_realtime_envelope_build_event.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_event_handler.py`

## Audit Trail

- EXTRACTED: 87 (83%)
- INFERRED: 18 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*