# test_message_handler_factory.py

> 115 nodes

## Key Concepts

- **ConnectionManager** (63 connections) — `server/realtime/connection_manager_methods.py`
- **test_connection_manager_methods.py** (50 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **UUID** (23 connections)
- **get_player_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **get_players_batch_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **get_message_delivery_stats_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **get_player_presence_info_method()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **send_initial_game_state_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **send_personal_message_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **validate_player_presence_method()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **check_connection_health_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **convert_uuids_to_strings_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **disconnect_websocket_connection_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_connection_count_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_connection_id_from_websocket_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_error_statistics_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_npcs_batch_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_pending_messages_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_player_session_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_player_websocket_connection_id_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_rate_limit_info_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **has_websocket_connection_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **start_health_checks_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **subscribe_to_room_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **validate_session_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- *... and 90 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (37 shared connections)
- [test_chat_logger.py](test_chat_logger.py.md) (27 shared connections)
- [security.ts](security.ts.md) (9 shared connections)
- [test_shutdown_sequence.py](test_shutdown_sequence.py.md) (4 shared connections)
- [_parse_env_list](_parse_env_list.md) (3 shared connections)
- [🔴 CRITICAL ISSUES](🔴_CRITICAL_ISSUES.md) (1 shared connections)
- [P3 · realtime-connection + events-nats](P3_·_realtime-connection_+_events-nats.md) (1 shared connections)
- [TestHelperFunctions](TestHelperFunctions.md) (1 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (1 shared connections)
- [chat_service.py](chat_service.py.md) (1 shared connections)
- [setup_jwt_secret](setup_jwt_secret.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager_methods.py`
- `server/tests/unit/realtime/test_connection_manager_methods.py`

## Audit Trail

- EXTRACTED: 250 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*