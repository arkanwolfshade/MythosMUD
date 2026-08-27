# field_validator

> 104 nodes

## Key Concepts

- **test_websocket_initial_state.py** (45 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **websocket_initial_state.py** (41 connections) — `server/realtime/websocket_initial_state.py`
- **asyncio** (21 connections)
- **get_container_async_persistence()** (19 connections) — `server/async_persistence.py`
- **send_initial_room_state()** (18 connections) — `server/realtime/websocket_initial_state.py`
- **send_initial_game_state()** (14 connections) — `server/realtime/websocket_initial_state.py`
- **check_and_send_death_notification()** (12 connections) — `server/realtime/websocket_initial_state.py`
- **send_game_state_event_safely()** (10 connections) — `server/realtime/websocket_initial_state.py`
- **get_event_handler_for_initial_state()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **prepare_room_data_with_occupants()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **add_npc_occupants_to_list()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **send_occupants_snapshot_if_needed()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **Protocol** (7 connections)
- **get_npc_lifecycle_manager_from_connection_manager()** (6 connections) — `server/realtime/websocket_initial_state.py`
- **UUID** (6 connections)
- **_get_player_for_death_check()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **prepare_initial_room_data()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **mock_connection_manager()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **WebSocket** (5 connections)
- **_NpcLifecycleManagerForOccupants** (4 connections) — `server/realtime/websocket_initial_state.py`
- **test_add_npc_occupants_to_list_filters_dead_npcs()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_add_npc_occupants_to_list_no_app()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_add_npc_occupants_to_list_success()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_in_limbo()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_player_alive()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- *... and 79 more nodes in this community*

## Relationships

- [CombatAuditLogger](CombatAuditLogger.md) (8 shared connections)
- [test_room_subscription_manager_drops.py](test_room_subscription_manager_drops.py.md) (7 shared connections)
- [NPCDefinition](NPCDefinition.md) (7 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (6 shared connections)
- [test_error_logging.py](test_error_logging.py.md) (4 shared connections)
- [test_combat_validator.py](test_combat_validator.py.md) (3 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (3 shared connections)
- [test_user_manager.py](test_user_manager.py.md) (3 shared connections)
- [PopulationStats](PopulationStats.md) (3 shared connections)
- [ContainerComponent](ContainerComponent.md) (3 shared connections)
- [User](User.md) (2 shared connections)
- [Test Value Distribution Chart](Test_Value_Distribution_Chart.md) (2 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 241 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*