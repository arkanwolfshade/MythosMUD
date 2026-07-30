# UUID

> 348 nodes

## Key Concepts

- **websocket_initial_state.py** (45 connections) — `server/realtime/websocket_initial_state.py`
- **test_websocket_initial_state.py** (45 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **RealTimeEventHandler** (44 connections) — `server/realtime/event_handler.py`
- **AttributeError** (37 connections)
- **websocket_helpers.py** (37 connections) — `server/realtime/websocket_helpers.py`
- **websocket_room_updates.py** (35 connections) — `server/realtime/websocket_room_updates.py`
- **test_websocket_helpers.py** (34 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_websocket_room_updates.py** (32 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **broadcast_room_update()** (24 connections) — `server/realtime/websocket_room_updates.py`
- **test_websocket_helpers_player.py** (23 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **get_async_persistence()** (19 connections) — `server/async_persistence.py`
- **send_initial_room_state()** (19 connections) — `server/realtime/websocket_initial_state.py`
- **send_initial_game_state()** (15 connections) — `server/realtime/websocket_initial_state.py`
- **validate_occupant_name()** (14 connections) — `server/realtime/websocket_helpers.py`
- **get_player_and_room()** (14 connections) — `server/realtime/websocket_helpers.py`
- **check_and_send_death_notification()** (14 connections) — `server/realtime/websocket_initial_state.py`
- **build_room_update_event()** (13 connections) — `server/realtime/websocket_room_updates.py`
- **get_npc_name_from_instance()** (12 connections) — `server/realtime/websocket_helpers.py`
- **check_shutdown_and_reject()** (12 connections) — `server/realtime/websocket_helpers.py`
- **prepare_player_data()** (12 connections) — `server/realtime/websocket_helpers.py`
- **get_occupant_names()** (11 connections) — `server/realtime/websocket_helpers.py`
- **convert_uuids_to_strings()** (11 connections) — `server/realtime/websocket_helpers.py`
- **get_player_occupants()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **get_npc_occupants_from_lifecycle_manager()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **send_game_state_event_safely()** (10 connections) — `server/realtime/websocket_initial_state.py`
- *... and 323 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (35 shared connections)
- [Player](Player.md) (19 shared connections)
- [.is required()](is_required%28%29.md) (19 shared connections)
- [Any](Any.md) (15 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (14 shared connections)
- [. init ()](_init_%28%29.md) (14 shared connections)
- [spawn defaults](spawn_defaults.md) (6 shared connections)
- [login grace period](login_grace_period.md) (6 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (5 shared connections)
- [test build room drop summary](test_build_room_drop_summary.md) (5 shared connections)
- [clean command input()](clean_command_input%28%29.md) (4 shared connections)
- [follow commands](follow_commands.md) (3 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/realtime/event_handler.py`
- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_initial_state.py`
- `server/realtime/websocket_room_updates.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers_player.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`
- `server/tests/unit/realtime/test_websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 1207 (93%)
- INFERRED: 95 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*