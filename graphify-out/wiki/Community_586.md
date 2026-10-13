# Community 586

> 29 nodes

## Key Concepts

- **test_real_time_helpers.py** (40 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **asyncio** (20 connections)
- **_resolve_player_id_from_path_or_token()** (9 connections) — `server/api/real_time.py`
- **test_resolve_player_id_query_rejected_when_fallback_off()** (5 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_ensure_connection_manager_missing()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_handle_new_game_session_invalid_json()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_handle_new_game_session_missing_session_id()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_parse_websocket_token_header_parse_error()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_token_no_player()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_missing_token_and_player_id()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_query_allowed_when_fallback_on()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_validate_websocket_connection_manager()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_websocket_endpoint_route_unresolved_player()** (4 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_get_player_connections()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_handle_new_game_session()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_path_or_token_uuid_jwt_match()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_path_or_token_uuid_jwt_mismatch_rejected()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_path_or_token_uuid_without_jwt_rejected()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_path_or_token_via_token()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_test()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_token_with_character_id()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_validate_and_accept_websocket_unavailable()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_validate_and_accept_websocket_valid()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_websocket_player_id_fallback_allowed_default_off()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **MonkeyPatch** (3 connections)
- *... and 4 more nodes in this community*

## Relationships

- [Community 643](Community_643.md) (14 shared connections)
- [Container API Models](Container_API_Models.md) (12 shared connections)
- [Community 672](Community_672.md) (6 shared connections)
- [Community 1020](Community_1020.md) (3 shared connections)
- [Community 1389](Community_1389.md) (3 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (2 shared connections)
- [Community 1583](Community_1583.md) (2 shared connections)
- [Community 1219](Community_1219.md) (1 shared connections)
- [API Response Models](API_Response_Models.md) (1 shared connections)
- [Community 170](Community_170.md) (1 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 91 (92%)
- INFERRED: 8 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*