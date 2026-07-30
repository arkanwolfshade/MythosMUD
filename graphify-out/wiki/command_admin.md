# command admin

> 25 nodes

## Key Concepts

- **MockPersistenceFull** (14 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_unintentional_disconnect_starts_grace_period()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_intentional_disconnect_no_grace_period()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_command_blocks_during_combat()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_command_starts_countdown_not_in_combat()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_location_instant_disconnect()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_location_blocked_during_combat()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_countdown_completes_disconnect()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **mock_persistence_full()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **.get_player_by_name()** (2 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **.get_room_by_id()** (2 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **.__setattr__()** (2 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **.__init__()** (1 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **Mock persistence layer with async methods for integration tests.** (1 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **Mock async method that uses configured mock.** (1 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **Mock method that uses configured mock.** (1 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **Allow setting get_player_by_name and get_room_by_id to mocks.** (1 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **Create a fully configured mock persistence layer.** (1 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **Test that unintentional disconnect starts grace period.** (1 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **Test that intentional disconnect does NOT start grace period.** (1 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **Test that /rest command is blocked during combat.** (1 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **Test that /rest command starts countdown when not in combat.** (1 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **Test that rest location provides instant disconnect when not in combat.** (1 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **Test that /rest in rest location is still blocked during combat.** (1 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **Test that rest countdown completes and disconnects player.** (1 connections) — `server/tests/integration/test_rest_and_grace_period.py`

## Relationships

- [player disconnect handlers](player_disconnect_handlers.md) (9 shared connections)
- [.check and interrupt rest()](check_and_interrupt_rest%28%29.md) (5 shared connections)
- [player presence tracker](player_presence_tracker.md) (2 shared connections)

## Source Files

- `server/tests/integration/test_rest_and_grace_period.py`

## Audit Trail

- EXTRACTED: 64 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*