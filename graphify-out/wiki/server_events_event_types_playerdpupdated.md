# server events event types playerdpupdated

> 84 nodes

## Key Concepts

- **PlayerDPUpdated** (34 connections) — `server/events/event_types.py`
- **test_player_event_handlers_state.py** (34 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **PlayerXPAwardEvent** (28 connections) — `server/services/player_combat_service.py`
- **player_event_handlers_state.py** (23 connections) — `server/realtime/player_event_handlers_state.py`
- **asyncio** (19 connections)
- **PlayerStateEventHandler** (11 connections) — `server/realtime/player_event_handlers_state.py`
- **_dispatch_player_dp_updated_payload()** (11 connections) — `server/realtime/player_event_handlers_state.py`
- **_send_player_death_notification()** (8 connections) — `server/realtime/player_event_handlers_state.py`
- **_player_snapshot_for_dp()** (6 connections) — `server/realtime/player_event_handlers_state.py`
- **.__init__()** (5 connections) — `server/realtime/player_event_handlers_state.py`
- **_dp_player_update_payload()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_died()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_dp_decay()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_dp_updated()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_xp_awarded()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **mock_utils()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **player_state_event_handler()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_error_handling()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_no_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_player_no_get_stats()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_player_not_found()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_success()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_xp_awarded_error_handling()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_xp_awarded_no_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_xp_awarded_player_no_current_room_id()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- *... and 59 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (14 shared connections)
- [server tests unit realtime test](server_tests_unit_realtime_test.md) (10 shared connections)
- [moduletype](moduletype.md) (5 shared connections)
- [server realtime player event handlers](server_realtime_player_event_handlers.md) (5 shared connections)
- [server realtime envelope build event](server_realtime_envelope_build_event.md) (5 shared connections)
- [server events event types playerdiedevent](server_events_event_types_playerdiedevent.md) (5 shared connections)
- [server services combat persistence handler](server_services_combat_persistence_handler.md) (4 shared connections)
- [server events event bus](server_events_event_bus.md) (4 shared connections)
- [playercombatservice](playercombatservice.md) (4 shared connections)
- [server game magic magic healing](server_game_magic_magic_healing.md) (3 shared connections)
- [server game magic spell targeting](server_game_magic_spell_targeting.md) (3 shared connections)
- [server services combat hp sync](server_services_combat_hp_sync.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/event_handler.py`
- `server/realtime/player_event_handlers_state.py`
- `server/services/player_combat_service.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`

## Audit Trail

- EXTRACTED: 179 (86%)
- INFERRED: 28 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*