# Room Broadcast

> 450 nodes

## Key Concepts

- **ConnectionManager** (233 connections) — `server/realtime/connection_manager.py`
- **connection_manager.py** (161 connections) — `server/realtime/connection_manager.py`
- **connection_manager_methods.py** (80 connections) — `server/realtime/connection_manager_methods.py`
- **UUID** (41 connections)
- **test_connection_helpers_impl.py** (35 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_connection_statistics.py** (24 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **connection_helpers.py** (21 connections) — `server/realtime/connection_helpers.py`
- **UUID** (21 connections)
- **convert_uuids_to_strings()** (18 connections) — `server/realtime/connection_helpers.py`
- **canonical_room_id_impl()** (17 connections) — `server/realtime/connection_room_utils.py`
- **test_connection_room_utils.py** (16 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **test_connection_manager_class.py** (15 connections) — `server/tests/unit/realtime/test_connection_manager_class.py`
- **send_personal_message_old_impl()** (13 connections) — `server/realtime/connection_helpers.py`
- **resolve_connection_manager()** (13 connections) — `server/realtime/connection_manager.py`
- **delegate_game_state_provider()** (12 connections) — `server/realtime/connection_delegates.py`
- **force_disconnect_player_impl()** (12 connections) — `server/realtime/connection_manager_methods.py`
- **_optimize_payload()** (11 connections) — `server/realtime/connection_helpers.py`
- **_send_to_websockets()** (11 connections) — `server/realtime/connection_helpers.py`
- **connection_statistics.py** (11 connections) — `server/realtime/connection_statistics.py`
- **validate_player_presence_impl()** (11 connections) — `server/realtime/connection_statistics.py`
- **Any** (10 connections)
- **safe_close_websocket_impl()** (10 connections) — `server/realtime/connection_manager_methods.py`
- **connection_room_utils.py** (10 connections) — `server/realtime/connection_room_utils.py`
- **get_online_player_by_display_name_impl()** (10 connections) — `server/realtime/connection_statistics.py`
- **handle_new_login_impl()** (9 connections) — `server/realtime/connection_helpers.py`
- *... and 425 more nodes in this community*

## Relationships

- [connection disconnection realtime](connection_disconnection_realtime.md) (39 shared connections)
- [connection realtime delegates](connection_realtime_delegates.md) (25 shared connections)
- [models npc rationale](models_npc_rationale.md) (24 shared connections)
- [combat services messaging](combat_services_messaging.md) (22 shared connections)
- [Database Config](Database_Config.md) (15 shared connections)
- [container service services](container_service_services.md) (13 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (13 shared connections)
- [NATS Messaging](NATS_Messaging.md) (12 shared connections)
- [NPC Combat](NPC_Combat.md) (11 shared connections)
- [connection realtime error](connection_realtime_error.md) (11 shared connections)
- [Exception Containers](Exception_Containers.md) (8 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (7 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_helpers.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/connection_room_utils.py`
- `server/realtime/connection_statistics.py`
- `server/tests/unit/realtime/test_connection_helpers.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`
- `server/tests/unit/realtime/test_connection_manager_class.py`
- `server/tests/unit/realtime/test_connection_room_utils.py`
- `server/tests/unit/realtime/test_connection_statistics.py`

## Audit Trail

- EXTRACTED: 1872 (98%)
- INFERRED: 44 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*