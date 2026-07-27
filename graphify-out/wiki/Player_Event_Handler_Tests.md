# Player Event Handler Tests

> 122 nodes · cohesion 0.02

## Key Concepts

- **PlayerDPUpdated** (36 connections) — `server/events/event_types.py`
- **test_player_event_handlers.py** (30 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_player_event_handlers_state.py** (29 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **combat_hp_sync.py** (14 connections) — `server/services/combat_hp_sync.py`
- **CombatDPSync** (11 connections) — `server/services/combat_hp_sync.py`
- **UUID** (9 connections) — `server/services/combat_hp_sync.py`
- **._persist_player_dp_sync()** (7 connections) — `server/services/combat_hp_sync.py`
- **Test handle_player_entered() skips when connection manager not available.** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **Test handle_player_entered() handles errors.** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **._publish_player_dp_correction_event()** (5 connections) — `server/services/combat_hp_sync.py`
- **._publish_player_dp_update_event()** (5 connections) — `server/services/combat_hp_sync.py`
- **._update_and_save_player_dp()** (5 connections) — `server/services/combat_hp_sync.py`
- **._get_persistence()** (4 connections) — `server/services/combat_hp_sync.py`
- **._log_death_threshold_events()** (4 connections) — `server/services/combat_hp_sync.py`
- **._verify_player_save()** (4 connections) — `server/services/combat_hp_sync.py`
- **test_handle_player_left_no_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **test_handle_player_entered_error_handling()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **test_handle_player_entered_no_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_room.py`
- **mock_utils()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_error_handling()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_no_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_player_no_get_stats()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_player_not_found()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_dp_updated_success()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_xp_awarded_error_handling()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- *... and 97 more nodes in this community*

## Relationships

- [[Distributed Event Bus]] (13 shared connections)
- [[Player Combat XP]] (9 shared connections)
- [[Player Respawn Events]] (8 shared connections)
- [[NPC Services Bundle]] (6 shared connections)
- [[Services Combat Persistence]] (6 shared connections)
- [[Player Left Room Tests]] (5 shared connections)
- [[NPC Admin API]] (5 shared connections)
- [[Magic Game Healing]] (4 shared connections)
- [[Realtime Player Event]] (2 shared connections)
- [[Realtime Event Delegation]] (2 shared connections)
- [[Game Tick Processing]] (1 shared connections)
- [[App Game Tick]] (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/services/combat_hp_sync.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_player_event_handlers.py`
- `server/tests/unit/realtime/test_player_event_handlers_room.py`
- `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils.py`

## Audit Trail

- EXTRACTED: 357 (98%)
- INFERRED: 7 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
