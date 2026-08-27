# npc_database.py

> 86 nodes

## Key Concepts

- **test_player_event_handlers_state.py** (34 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **PlayerDPUpdated** (33 connections) — `server/events/event_types.py`
- **PlayerXPAwardEvent** (30 connections) — `server/services/player_combat_service.py`
- **player_event_handlers_state.py** (23 connections) — `server/realtime/player_event_handlers_state.py`
- **asyncio** (19 connections)
- **player_event_handlers_utils.py** (16 connections) — `server/realtime/player_event_handlers_utils.py`
- **PlayerStateEventHandler** (14 connections) — `server/realtime/player_event_handlers_state.py`
- **_dispatch_player_dp_updated_payload()** (11 connections) — `server/realtime/player_event_handlers_state.py`
- **_send_player_death_notification()** (8 connections) — `server/realtime/player_event_handlers_state.py`
- **_player_snapshot_for_dp()** (6 connections) — `server/realtime/player_event_handlers_state.py`
- **.__init__()** (5 connections) — `server/realtime/player_event_handlers_state.py`
- **_dp_player_update_payload()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_died()** (4 connections) — `server/realtime/player_event_handlers_state.py`
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
- *... and 61 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (19 shared connections)
- [InventoryCommandFactory](InventoryCommandFactory.md) (12 shared connections)
- [MovementService](MovementService.md) (6 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (6 shared connections)
- [test_spell_effects.py](test_spell_effects.py.md) (6 shared connections)
- [test_player_occupant_processor.py](test_player_occupant_processor.py.md) (4 shared connections)
- [PopulationStats](PopulationStats.md) (4 shared connections)
- [ContainerComponent](ContainerComponent.md) (4 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (3 shared connections)
- [SessionManager](SessionManager.md) (3 shared connections)
- [CombatInstance](CombatInstance.md) (3 shared connections)
- [ChatLogger](ChatLogger.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_state.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/services/player_combat_service.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`

## Audit Trail

- EXTRACTED: 198 (88%)
- INFERRED: 26 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*