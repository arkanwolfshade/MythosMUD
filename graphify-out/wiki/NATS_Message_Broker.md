# NATS Message Broker

> 75 nodes

## Key Concepts

- **test_player_disconnect_handlers.py** (34 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **player_disconnect_handlers.py** (27 connections) — `server/realtime/player_disconnect_handlers.py`
- **_collect_disconnect_keys()** (19 connections) — `server/realtime/player_disconnect_handlers.py`
- **handle_player_disconnect_broadcast()** (17 connections) — `server/realtime/player_disconnect_handlers.py`
- **_cleanup_player_references()** (11 connections) — `server/realtime/player_disconnect_handlers.py`
- **age_off_disconnected_sessions()** (11 connections) — `server/realtime/player_disconnect_handlers.py`
- **_remove_player_from_online_tracking()** (10 connections) — `server/realtime/player_disconnect_handlers.py`
- **UUID** (7 connections)
- **_get_session_maps_for_age_off()** (4 connections) — `server/realtime/player_disconnect_handlers.py`
- **_purge_expired_sessions_from_maps()** (4 connections) — `server/realtime/player_disconnect_handlers.py`
- **_session_ids_past_age_off()** (3 connections) — `server/realtime/player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_with_room()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_no_room()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_empty_player_name()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_collect_disconnect_keys_with_player()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_collect_disconnect_keys_no_player()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_remove_player_from_online_tracking()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_room_no_player()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_no_persistence()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_no_room_found()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_collect_disconnect_keys_with_user_id()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_collect_disconnect_keys_with_string_user_id()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_collect_disconnect_keys_with_player_name()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_collect_disconnect_keys_no_name()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_remove_player_from_online_tracking_not_in_online_players()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- *... and 50 more nodes in this community*

## Relationships

- [Container Persistence Queries](Container_Persistence_Queries.md) (9 shared connections)
- [Rescue Service Tests](Rescue_Service_Tests.md) (9 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (3 shared connections)
- [Player Command Developer Guide](Player_Command_Developer_Guide.md) (3 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (1 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (1 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (1 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (1 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (1 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (1 shared connections)

## Source Files

- `server/realtime/player_disconnect_handlers.py`
- `server/tests/unit/realtime/test_player_disconnect_handlers.py`

## Audit Trail

- EXTRACTED: 256 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*