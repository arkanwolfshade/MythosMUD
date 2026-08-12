# NATS Subject Validator

> 40 nodes

## Key Concepts

- **test_room_subscription_manager_helpers.py** (22 connections) — `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- **subscription_manager()** (3 connections) — `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- **test_remove_player_from_all_rooms()** (2 connections) — `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- **test_reconcile_room_presence()** (2 connections) — `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- **test_canonical_room_id()** (2 connections) — `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- **test_canonical_room_id_no_persistence()** (2 connections) — `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- **test_get_stats()** (2 connections) — `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- **test_remove_player_from_all_rooms_no_subscriptions()** (2 connections) — `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- **test_remove_player_from_all_rooms_with_subscriptions()** (2 connections) — `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- **test_remove_player_from_all_rooms_error()** (2 connections) — `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- **test_reconcile_room_presence_no_online_players()** (2 connections) — `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- **test_reconcile_room_presence_error()** (2 connections) — `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- **test_canonical_room_id_none()** (2 connections) — `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- **test_canonical_room_id_empty_string()** (2 connections) — `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- **test_canonical_room_id_with_persistence()** (2 connections) — `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- **test_canonical_room_id_no_room_id_attr()** (2 connections) — `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- **test_canonical_room_id_error()** (2 connections) — `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- **test_get_stats_empty()** (2 connections) — `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- **test_get_stats_with_data()** (2 connections) — `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- **test_get_stats_error()** (2 connections) — `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- **Unit tests for room subscription manager helper functions.  Tests the helper fun** (1 connections) — `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- **Create a RoomSubscriptionManager instance.** (1 connections) — `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- **Test remove_player_from_all_rooms() removes player from all rooms.** (1 connections) — `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- **Test reconcile_room_presence() removes offline players.** (1 connections) — `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- **Test _canonical_room_id() resolves canonical ID.** (1 connections) — `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`
- *... and 15 more nodes in this community*

## Relationships

- [JSONB Column Parsing](JSONB_Column_Parsing.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_room_subscription_manager_helpers.py`

## Audit Trail

- EXTRACTED: 81 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*