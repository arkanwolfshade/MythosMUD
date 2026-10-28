# test_look_npc_helpers.py

> 51 nodes · cohesion 0.06

## Key Concepts

- **test_rest_and_grace_period.py** (25 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **is_player_in_grace_period()** (24 connections) — `server/realtime/disconnect_grace_period.py`
- **MockPersistenceFull** (14 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **asyncio** (13 connections)
- **test_intentional_disconnect_no_grace_period()** (5 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_command_blocks_during_combat()** (5 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_command_starts_countdown_not_in_combat()** (5 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_countdown_completes_disconnect()** (5 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_location_blocked_during_combat()** (5 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_location_instant_disconnect()** (5 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_unintentional_disconnect_starts_grace_period()** (5 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **mock_persistence_full()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_grace_period_player_can_auto_attack()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_grace_period_player_cannot_use_commands()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_reconnection_cancels_grace_period()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_interrupts_combat_action()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_visual_indicator_in_grace_period()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **mock_app_with_services()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **mock_connection_manager_full()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **fixture** (3 connections)
- **test_is_player_in_grace_period_false()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_is_player_in_grace_period_no_manager_attribute()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_is_player_in_grace_period_true()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **.get_player_by_name()** (2 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **.get_room_by_id()** (2 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- *... and 26 more nodes in this community*

## Relationships

- [player_connection_setup.py](player_connection_setup.py.md) (10 shared connections)
- [asyncio](asyncio.md) (7 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (4 shared connections)
- [setup_jwt_secret](setup_jwt_secret.md) (3 shared connections)
- [mapUtils.ts](mapUtils.ts.md) (2 shared connections)
- [FeatureFlagService](FeatureFlagService.md) (2 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (2 shared connections)
- [ResourceManager](ResourceManager.md) (2 shared connections)
- [ChatLogger](ChatLogger.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)

## Source Files

- `server/realtime/disconnect_grace_period.py`
- `server/tests/integration/test_rest_and_grace_period.py`
- `server/tests/unit/realtime/test_disconnect_grace_period.py`

## Audit Trail

- EXTRACTED: 109 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*