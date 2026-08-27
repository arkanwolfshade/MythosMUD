# test_combat_validator.py

> 82 nodes

## Key Concepts

- **real_time.py** (34 connections) — `server/api/real_time.py`
- **test_real_time_helpers.py** (34 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **asyncio** (20 connections)
- **_resolve_player_id()** (13 connections) — `server/api/real_time.py`
- **handle_new_game_session()** (11 connections) — `server/api/real_time.py`
- **_parse_websocket_token()** (10 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_path_or_token()** (10 connections) — `server/api/real_time.py`
- **_ensure_connection_manager()** (9 connections) — `server/api/real_time.py`
- **get_player_connections()** (9 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_token()** (9 connections) — `server/api/real_time.py`
- **websocket_endpoint()** (9 connections) — `server/api/real_time.py`
- **websocket_endpoint_route()** (9 connections) — `server/api/real_time.py`
- **Any** (9 connections)
- **WebSocket** (9 connections)
- **get_connection_statistics()** (8 connections) — `server/api/real_time.py`
- **_resolve_connection_manager_from_state()** (8 connections) — `server/api/real_time.py`
- **_resolve_player_id_from_test()** (8 connections) — `server/api/real_time.py`
- **UUID** (8 connections)
- **_validate_and_accept_websocket()** (7 connections) — `server/api/real_time.py`
- **_validate_websocket_connection_manager()** (7 connections) — `server/api/real_time.py`
- **_invoke_handle_websocket_connection()** (6 connections) — `server/api/real_time.py`
- **_extract_bearer_token()** (5 connections) — `server/api/real_time.py`
- **_parse_subprotocol_token()** (5 connections) — `server/api/real_time.py`
- **resolve_connection_manager()** (5 connections) — `server/api/real_time.py`
- **websocket_player_id_fallback_allowed()** (4 connections) — `server/api/real_time.py`
- *... and 57 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (10 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (4 shared connections)
- [field_validator](field_validator.md) (3 shared connections)
- [useRespawnHandlers.ts](useRespawnHandlers.ts.md) (2 shared connections)
- [run_extended_idle_memory_monitor.ps1](run_extended_idle_memory_monitor.ps1.md) (2 shared connections)
- [ChatMessage](ChatMessage.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 202 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*