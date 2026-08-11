# Realtime WebSocket Auth

> 41 nodes

## Key Concepts

- **test_rest_and_grace_period.py** (24 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **MockPersistenceFull** (14 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_unintentional_disconnect_starts_grace_period()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_intentional_disconnect_no_grace_period()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_command_blocks_during_combat()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_command_starts_countdown_not_in_combat()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_location_instant_disconnect()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_location_blocked_during_combat()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_countdown_completes_disconnect()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **mock_persistence_full()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_interrupts_combat_action()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_reconnection_cancels_grace_period()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_grace_period_player_can_auto_attack()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_grace_period_player_cannot_use_commands()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_visual_indicator_in_grace_period()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **mock_app_with_services()** (2 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **mock_connection_manager_full()** (2 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **.get_player_by_name()** (2 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **.get_room_by_id()** (2 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **.__setattr__()** (2 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **.__init__()** (1 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **Integration tests for rest command and disconnect grace period.  Tests the integ** (1 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **Create a mock app with all required services.** (1 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **Create a fully configured mock connection manager.** (1 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **Mock persistence layer with async methods for integration tests.** (1 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- *... and 16 more nodes in this community*

## Relationships

- [NATS Message Broker](NATS_Message_Broker.md) (7 shared connections)
- [Party Service Management](Party_Service_Management.md) (5 shared connections)
- [Player State Factories](Player_State_Factories.md) (4 shared connections)
- [Rescue Service Tests](Rescue_Service_Tests.md) (3 shared connections)

## Source Files

- `server/tests/integration/test_rest_and_grace_period.py`

## Audit Trail

- EXTRACTED: 115 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*