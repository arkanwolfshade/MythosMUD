# nats services metrics

> 27 nodes

## Key Concepts

- **real_time.py** (36 connections) — `server/api/real_time.py`
- **_resolve_player_id()** (11 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_token()** (10 connections) — `server/api/real_time.py`
- **websocket_endpoint()** (10 connections) — `server/api/real_time.py`
- **Any** (9 connections)
- **_resolve_player_id_from_test()** (9 connections) — `server/api/real_time.py`
- **websocket_endpoint_route()** (9 connections) — `server/api/real_time.py`
- **WebSocket** (8 connections)
- **_validate_websocket_connection_manager()** (8 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_path_or_token()** (8 connections) — `server/api/real_time.py`
- **_resolve_connection_manager_from_state()** (7 connections) — `server/api/real_time.py`
- **_validate_and_accept_websocket()** (7 connections) — `server/api/real_time.py`
- **UUID** (7 connections)
- **test_websocket_endpoint_route_unresolved_player()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_validate_and_accept_websocket_valid()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_validate_and_accept_websocket_unavailable()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_path_or_token_uuid()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_path_or_token_via_token()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **Real-time communication API endpoints for MythosMUD server.  This module handles** (1 connections) — `server/api/real_time.py`
- **Validate connection manager and accept WebSocket connection.     Returns True if** (1 connections) — `server/api/real_time.py`
- **Resolve player ID from test player_id query parameter.     Validates that the pl** (1 connections) — `server/api/real_time.py`
- **Resolve player ID from JWT token payload.     Validates that the user has a play** (1 connections) — `server/api/real_time.py`
- **Resolve player ID from token or test player_id parameter.     Handles both authe** (1 connections) — `server/api/real_time.py`
- **WebSocket endpoint for interactive commands and chat.     Supports session track** (1 connections) — `server/api/real_time.py`
- **Validate and resolve connection manager for WebSocket.      Args:         websoc** (1 connections) — `server/api/real_time.py`
- *... and 2 more nodes in this community*

## Relationships

- [cleanup combat handler](cleanup_combat_handler.md) (18 shared connections)
- [fixtures mock helpers](fixtures_mock_helpers.md) (8 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (6 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (4 shared connections)
- [command commands aliases](command_commands_aliases.md) (4 shared connections)
- [schedule services service](schedule_services_service.md) (4 shared connections)
- [Error Conversion](Error_Conversion.md) (4 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (3 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (2 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (1 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 156 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*