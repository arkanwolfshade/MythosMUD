# Container Exception Handlers

> 89 nodes

## Key Concepts

- **connection_manager.py** (124 connections) — `server/realtime/connection_manager.py`
- **connection_manager_methods.py** (52 connections) — `server/realtime/connection_manager_methods.py`
- **Any** (32 connections)
- **connection_delegates.py** (21 connections) — `server/realtime/connection_delegates.py`
- **delegate_game_state_provider()** (12 connections) — `server/realtime/connection_delegates.py`
- **UUID** (12 connections)
- **delegate_message_broadcaster()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_room_event_handler()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_game_state_provider_sync()** (8 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender_sync()** (8 connections) — `server/realtime/connection_delegates.py`
- **broadcast_to_room_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_room_event_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_global_event_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **get_message_delivery_stats_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_global_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **force_disconnect_player_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **disconnect_websocket_connection_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **get_player_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **get_players_batch_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **send_initial_game_state_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **send_personal_message_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **is_websocket_open_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **get_player_websocket_connection_id_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **get_connection_id_from_websocket_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- *... and 64 more nodes in this community*

## Relationships

- [Archive Bug Fix](Archive_Bug_Fix.md) (32 shared connections)
- [Command Helper Utilities](Command_Helper_Utilities.md) (28 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (26 shared connections)
- [Client Event Store](Client_Event_Store.md) (12 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (12 shared connections)
- [Playwright E2E Specs](Playwright_E2E_Specs.md) (9 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (6 shared connections)
- [ASCII Map API](ASCII_Map_API.md) (6 shared connections)
- [Follow Service Tests](Follow_Service_Tests.md) (5 shared connections)
- [NATS Subject Manager](NATS_Subject_Manager.md) (4 shared connections)
- [Rescue Service Tests](Rescue_Service_Tests.md) (4 shared connections)
- [Commands Look Item](Commands_Look_Item.md) (4 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`

## Audit Trail

- EXTRACTED: 542 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*