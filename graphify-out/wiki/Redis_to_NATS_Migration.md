# Redis to NATS Migration

> 26 nodes

## Key Concepts

- **PlayerXPAwardEvent** (35 connections) — `server/services/player_combat_service.py`
- **.handle_player_xp_awarded()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_xp_awarded()** (3 connections) — `server/realtime/player_event_handlers.py`
- **test_event_handler_handle_player_xp_awarded()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_handle_player_xp_awarded_delegates_to_state_handler()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_handle_player_xp_awarded_error_handling()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_handle_player_xp_awarded_success()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_xp_awarded_no_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_xp_awarded_player_not_found()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_xp_awarded_error_handling()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_handle_player_xp_awarded_player_no_current_room_id()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **test_player_xp_award_event_init()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **.__post_init__()** (2 connections) — `server/services/player_combat_service.py`
- **Handle player XP award events by sending updates to the client.          Args:** (1 connections) — `server/realtime/player_event_handlers.py`
- **Handle player XP award events by sending updates to the client.          Args:** (1 connections) — `server/realtime/player_event_handlers_state.py`
- **Event published when a player receives XP.** (1 connections) — `server/services/player_combat_service.py`
- **Set event_type for serialization/deserialization.** (1 connections) — `server/services/player_combat_service.py`
- **Test RealTimeEventHandler._handle_player_xp_awarded() delegates to player_handle** (1 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **Test handle_player_xp_awarded() delegates to state handler.** (1 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **Test handle_player_xp_awarded() propagates errors from state handler.** (1 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **Test handle_player_xp_awarded() successfully sends XP update.** (1 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **Test handle_player_xp_awarded() skips when connection manager not available.** (1 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **Test handle_player_xp_awarded() handles player not found.** (1 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **Test handle_player_xp_awarded() handles errors.** (1 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **Test handle_player_xp_awarded() handles player without current_room_id.** (1 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- *... and 1 more nodes in this community*

## Relationships

- [Look Command Helpers](Look_Command_Helpers.md) (6 shared connections)
- [Tailwind UI Migration Plan](Tailwind_UI_Migration_Plan.md) (5 shared connections)
- [Character Creation E2E](Character_Creation_E2E.md) (4 shared connections)
- [Client Memory Leak Detector](Client_Memory_Leak_Detector.md) (4 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (3 shared connections)
- [Application Config Settings](Application_Config_Settings.md) (3 shared connections)
- [NPC Services Bundle](NPC_Services_Bundle.md) (3 shared connections)
- [Character Stats Generator](Character_Stats_Generator.md) (3 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (1 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (1 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_state.py`
- `server/services/player_combat_service.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_player_event_handlers.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`
- `server/tests/unit/services/test_player_combat_service.py`

## Audit Trail

- EXTRACTED: 75 (89%)
- INFERRED: 9 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*