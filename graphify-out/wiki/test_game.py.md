# test_game.py

> 130 nodes · cohesion 0.03

## Key Concepts

- **websocket_helpers.py** (38 connections) — `server/realtime/websocket_helpers.py`
- **test_websocket_helpers.py** (38 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_websocket_helpers_player.py** (28 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **validate_occupant_name()** (16 connections) — `server/realtime/websocket_helpers.py`
- **get_player_and_room()** (14 connections) — `server/realtime/websocket_helpers.py`
- **prepare_player_data()** (13 connections) — `server/realtime/websocket_helpers.py`
- **check_shutdown_and_reject()** (12 connections) — `server/realtime/websocket_helpers.py`
- **convert_uuids_to_strings()** (11 connections) — `server/realtime/websocket_helpers.py`
- **get_npc_name_from_instance()** (11 connections) — `server/realtime/websocket_helpers.py`
- **get_player_stats_data()** (9 connections) — `server/realtime/websocket_helpers.py`
- **is_client_disconnected_exception()** (9 connections) — `server/realtime/websocket_helpers.py`
- **get_player_service_from_connection_manager()** (8 connections) — `server/realtime/websocket_helpers.py`
- **_bind_get_stats()** (8 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **build_basic_player_data()** (7 connections) — `server/realtime/websocket_helpers.py`
- **convert_schema_to_dict()** (7 connections) — `server/realtime/websocket_helpers.py`
- **asyncio** (7 connections)
- **test_prepare_player_data_service_error()** (7 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **asyncio** (7 connections)
- **_ensure_player_in_room_occupancy()** (6 connections) — `server/realtime/websocket_helpers.py`
- **UUID** (6 connections)
- **test_get_player_and_room_adds_player_to_room()** (6 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_and_room_success()** (6 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_prepare_player_data_no_service()** (6 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_prepare_player_data_with_service()** (6 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **_connection_manager_with_app()** (5 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- *... and 105 more nodes in this community*

## Relationships

- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (19 shared connections)
- [resolve_weapon_attack_from_equipped](resolve_weapon_attack_from_equipped.md) (11 shared connections)
- [security.ts](security.ts.md) (6 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (4 shared connections)
- [test_room_system_message_categories.py](test_room_system_message_categories.py.md) (4 shared connections)
- [Room](Room.md) (2 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (2 shared connections)
- [command_parser.py](command_parser.py.md) (2 shared connections)
- [look_container.py](look_container.py.md) (2 shared connections)
- [test_combat_monitoring_service.py](test_combat_monitoring_service.py.md) (2 shared connections)
- [CombatConfiguration](CombatConfiguration.md) (1 shared connections)
- [coerce_int](coerce_int.md) (1 shared connections)

## Source Files

- `server/models/alias.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers_player.py`

## Audit Trail

- EXTRACTED: 278 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*