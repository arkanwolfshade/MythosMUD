# server commands container helpers inventory

> 73 nodes

## Key Concepts

- **websocket_helpers.py** (39 connections) — `server/realtime/websocket_helpers.py`
- **.state()** (37 connections) — `server/realtime/connection_state_machine.py`
- **.app()** (34 connections) — `server/commands/look_helpers.py`
- **test_websocket_helpers_player.py** (24 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **check_shutdown_and_reject()** (13 connections) — `server/realtime/websocket_helpers.py`
- **get_player_and_room()** (12 connections) — `server/realtime/websocket_helpers.py`
- **_websocket_unified_command_result()** (11 connections) — `server/realtime/websocket_handler_commands.py`
- **prepare_player_data()** (10 connections) — `server/realtime/websocket_helpers.py`
- **get_player_service_from_connection_manager()** (9 connections) — `server/realtime/websocket_helpers.py`
- **get_player_stats_data()** (9 connections) — `server/realtime/websocket_helpers.py`
- **build_basic_player_data()** (7 connections) — `server/realtime/websocket_helpers.py`
- **convert_schema_to_dict()** (7 connections) — `server/realtime/websocket_helpers.py`
- **asyncio** (7 connections)
- **_ensure_player_in_room_occupancy()** (6 connections) — `server/realtime/websocket_helpers.py`
- **UUID** (6 connections)
- **_app_state_container_service()** (5 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_get_tracked_player_from_connection_manager()** (4 connections) — `server/realtime/websocket_helpers.py`
- **test_get_player_and_room_adds_player_to_room()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_and_room_player_not_found()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_and_room_room_not_found()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_and_room_success()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_prepare_player_data_no_service()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_prepare_player_data_service_error()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_prepare_player_data_with_service()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **_fetch_room_for_tracked_player()** (3 connections) — `server/realtime/websocket_helpers.py`
- *... and 48 more nodes in this community*

## Relationships

- [server realtime websocket handler](server_realtime_websocket_handler.md) (18 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (8 shared connections)
- [server realtime envelope build event](server_realtime_envelope_build_event.md) (6 shared connections)
- [server api real time](server_api_real_time.md) (4 shared connections)
- [server command handler command execution](server_command_handler_command_execution.md) (4 shared connections)
- [scripts add flavor text column](scripts_add_flavor_text_column.md) (4 shared connections)
- [object](object.md) (3 shared connections)
- [server commands communication commands flows](server_commands_communication_commands_flows.md) (3 shared connections)
- [room](room.md) (3 shared connections)
- [server npc combat integration base](server_npc_combat_integration_base.md) (3 shared connections)
- [server realtime integration game state](server_realtime_integration_game_state.md) (3 shared connections)
- [server commands admin summon command](server_commands_admin_summon_command.md) (2 shared connections)

## Source Files

- `server/commands/container_helpers_inventory_ops.py`
- `server/commands/look_helpers.py`
- `server/realtime/connection_state_machine.py`
- `server/realtime/websocket_handler_commands.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers_player.py`

## Audit Trail

- EXTRACTED: 159 (69%)
- INFERRED: 70 (31%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*