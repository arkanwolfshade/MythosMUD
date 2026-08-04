# combat commands handler

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

- [command processor rationale](command_processor_rationale.md) (18 shared connections)
- [room validator path](room_validator_path.md) (8 shared connections)
- [Exception Containers](Exception_Containers.md) (6 shared connections)
- [Loot Generation](Loot_Generation.md) (5 shared connections)
- [combat schemas schema](combat_schemas_schema.md) (4 shared connections)
- [auth users rationale](auth_users_rationale.md) (4 shared connections)
- [command combat models](command_combat_models.md) (3 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (3 shared connections)
- [auth rationale access](auth_rationale_access.md) (3 shared connections)
- [nats services metrics](nats_services_metrics.md) (2 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 156 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*