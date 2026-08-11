# Playwright E2E Specs

> 442 nodes

## Key Concepts

- **connection_manager.py** (124 connections) — `server/realtime/connection_manager.py`
- **RateLimiter** (54 connections) — `server/realtime/rate_limiter.py`
- **connection_manager_methods.py** (52 connections) — `server/realtime/connection_manager_methods.py`
- **MessageQueue** (52 connections) — `server/realtime/message_queue.py`
- **AttributeError** (38 connections)
- **test_connection_helpers_impl.py** (35 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_connection_disconnection.py** (34 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_connection_rate_limiter.py** (33 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **connection_disconnection.py** (32 connections) — `server/realtime/connection_disconnection.py`
- **Any** (32 connections)
- **connection_cleaner.py** (22 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **connection_helpers.py** (21 connections) — `server/realtime/connection_helpers.py`
- **_DisconnectConnectionManager** (20 connections) — `server/realtime/connection_disconnection.py`
- **statistics_aggregator.py** (19 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **test_connection_disconnection_websockets.py** (19 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **convert_uuids_to_strings()** (18 connections) — `server/realtime/connection_helpers.py`
- **canonical_room_id_impl()** (17 connections) — `server/realtime/connection_room_utils.py`
- **room_subscription_manager.py** (17 connections) — `server/realtime/room_subscription_manager.py`
- **test_connection_room_utils.py** (16 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **validate_token_impl()** (13 connections) — `server/realtime/connection_delegates.py`
- **disconnect_all_websockets_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **_track_disconnect_if_needed()** (13 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_room_subscriptions()** (13 connections) — `server/realtime/connection_disconnection.py`
- **cleanup_websocket_disconnect()** (13 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_connection_by_id_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- *... and 417 more nodes in this community*

## Relationships

- [Room Occupant Events](Room_Occupant_Events.md) (45 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (40 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (32 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (30 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (23 shared connections)
- [Game State Provider Tests](Game_State_Provider_Tests.md) (18 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (10 shared connections)
- [Async Persistence Migration](Async_Persistence_Migration.md) (9 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (7 shared connections)
- [JSONB Column Parsing](JSONB_Column_Parsing.md) (7 shared connections)
- [Connection Health Monitor](Connection_Health_Monitor.md) (6 shared connections)
- [Player Combat XP](Player_Combat_XP.md) (6 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_disconnection.py`
- `server/realtime/connection_event_helpers.py`
- `server/realtime/connection_helpers.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/connection_room_utils.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/realtime/message_queue.py`
- `server/realtime/messaging/personal_message_sender.py`
- `server/realtime/monitoring/statistics_aggregator.py`
- `server/realtime/payload_optimizer.py`
- `server/realtime/rate_limiter.py`
- `server/realtime/room_subscription_manager.py`
- `server/tests/unit/realtime/test_connection_delegates.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- `server/tests/unit/realtime/test_connection_event_helpers.py`
- `server/tests/unit/realtime/test_connection_helpers.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 1820 (96%)
- INFERRED: 81 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*