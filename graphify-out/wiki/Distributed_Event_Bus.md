# Distributed Event Bus

> 201 nodes

## Key Concepts

- **connection_manager.py** (134 connections) — `server/realtime/connection_manager.py`
- **connection_manager_methods.py** (69 connections) — `server/realtime/connection_manager_methods.py`
- **Any** (45 connections)
- **test_connection_statistics.py** (24 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **UUID** (20 connections)
- **canonical_room_id_impl()** (17 connections) — `server/realtime/connection_room_utils.py`
- **test_connection_room_utils.py** (16 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **subscribe_to_room_events_impl()** (13 connections) — `server/realtime/connection_event_helpers.py`
- **unsubscribe_from_room_events_impl()** (13 connections) — `server/realtime/connection_event_helpers.py`
- **test_connection_event_helpers.py** (13 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **delegate_game_state_provider()** (12 connections) — `server/realtime/connection_delegates.py`
- **connection_statistics.py** (11 connections) — `server/realtime/connection_statistics.py`
- **validate_player_presence_impl()** (11 connections) — `server/realtime/connection_statistics.py`
- **connection_room_utils.py** (10 connections) — `server/realtime/connection_room_utils.py`
- **get_online_player_by_display_name_impl()** (10 connections) — `server/realtime/connection_statistics.py`
- **get_player_presence_info_impl()** (9 connections) — `server/realtime/connection_statistics.py`
- **get_session_stats_impl()** (9 connections) — `server/realtime/connection_statistics.py`
- **broadcast_to_room_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_room_event_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_global_event_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **get_presence_statistics_impl()** (8 connections) — `server/realtime/connection_statistics.py`
- **get_message_delivery_stats_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **get_player_presence_info_method()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **validate_player_presence_method()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_global_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- *... and 176 more nodes in this community*

## Relationships

- [Archive Bug Fix](Archive_Bug_Fix.md) (50 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (36 shared connections)
- [Client Event Store](Client_Event_Store.md) (18 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (16 shared connections)
- [NATS Subject Patterns](NATS_Subject_Patterns.md) (9 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (8 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (8 shared connections)
- [Combat Turn Processor](Combat_Turn_Processor.md) (5 shared connections)
- [WebSocket Connection Setup](WebSocket_Connection_Setup.md) (4 shared connections)
- [Playwright E2E Specs](Playwright_E2E_Specs.md) (4 shared connections)
- [Rescue Service Tests](Rescue_Service_Tests.md) (4 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (3 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_event_helpers.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/connection_room_utils.py`
- `server/realtime/connection_statistics.py`
- `server/tests/unit/realtime/test_connection_event_helpers.py`
- `server/tests/unit/realtime/test_connection_room_utils.py`
- `server/tests/unit/realtime/test_connection_statistics.py`

## Audit Trail

- EXTRACTED: 937 (99%)
- INFERRED: 13 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*