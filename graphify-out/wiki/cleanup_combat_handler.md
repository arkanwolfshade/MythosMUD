# cleanup combat handler

> 21 nodes

## Key Concepts

- **test_real_time_helpers.py** (31 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **_parse_websocket_token()** (9 connections) — `server/api/real_time.py`
- **_extract_bearer_token()** (6 connections) — `server/api/real_time.py`
- **_parse_subprotocol_token()** (5 connections) — `server/api/real_time.py`
- **test_resolve_player_id_from_token_no_player()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_missing_token_and_player_id()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_parse_websocket_token_header_parse_error()** (3 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_extract_bearer_token_with_marker()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_extract_bearer_token_last_part()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_extract_bearer_token_empty()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_parse_subprotocol_token()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_connection_manager_from_state()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_test()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_parse_websocket_token_from_query()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_parse_websocket_token_from_subprotocol()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_validate_websocket_connection_manager()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_player_id_from_token_with_character_id()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **Extract bearer token from parsed subprotocol parts.      If 'bearer' marker is p** (1 connections) — `server/api/real_time.py`
- **Parse token from WebSocket subprotocol header.      Example formats: "bearer, <t** (1 connections) — `server/api/real_time.py`
- **Parse token from WebSocket subprotocol (preferred) or query params (fallback).** (1 connections) — `server/api/real_time.py`
- **Unit tests for real_time API helper functions.** (1 connections) — `server/tests/unit/api/test_real_time_helpers.py`

## Relationships

- [nats services metrics](nats_services_metrics.md) (18 shared connections)
- [fixtures mock helpers](fixtures_mock_helpers.md) (5 shared connections)
- [schedule services service](schedule_services_service.md) (4 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (3 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (1 shared connections)
- [room sync service](room_sync_service.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 81 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*