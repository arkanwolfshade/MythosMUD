# Server Realtime (20)

> 73 nodes

## Key Concepts

- **is_player_in_grace_period()** (26 connections) — `server/realtime/disconnect_grace_period.py`
- **test_rest_and_grace_period.py** (24 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_disconnect_grace_period.py** (17 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **MockPersistenceFull** (14 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **cancel_grace_period()** (12 connections) — `server/realtime/disconnect_grace_period.py`
- **UUID** (4 connections)
- **test_unintentional_disconnect_starts_grace_period()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_intentional_disconnect_no_grace_period()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_command_blocks_during_combat()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_command_starts_countdown_not_in_combat()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_location_instant_disconnect()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_location_blocked_during_combat()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_countdown_completes_disconnect()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_start_grace_period_reconnection_cancels()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **Any** (3 connections)
- **mock_persistence_full()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_interrupts_combat_action()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_reconnection_cancels_grace_period()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_grace_period_player_can_auto_attack()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_grace_period_player_cannot_use_commands()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_visual_indicator_in_grace_period()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_start_grace_period_creates_task()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_start_grace_period_already_in_grace_period()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_start_grace_period_timer_expires()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_cancel_grace_period_not_in_grace_period()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- *... and 48 more nodes in this community*

## Relationships

- [Server Realtime (3)](Server_Realtime_%283%29.md) (17 shared connections)
- [Server Commands (15)](Server_Commands_%2815%29.md) (9 shared connections)
- [Server Realtime (67)](Server_Realtime_%2867%29.md) (2 shared connections)
- [Server Commands (3)](Server_Commands_%283%29.md) (2 shared connections)
- [Server Commands (17)](Server_Commands_%2817%29.md) (2 shared connections)
- [Server Commands (13)](Server_Commands_%2813%29.md) (2 shared connections)
- [Server Realtime (44)](Server_Realtime_%2844%29.md) (2 shared connections)
- [Server Realtime (62)](Server_Realtime_%2862%29.md) (2 shared connections)
- [Server Realtime (2)](Server_Realtime_%282%29.md) (1 shared connections)
- [Server Realtime (35)](Server_Realtime_%2835%29.md) (1 shared connections)
- [Server Realtime (9)](Server_Realtime_%289%29.md) (1 shared connections)
- [Server Realtime (8)](Server_Realtime_%288%29.md) (1 shared connections)

## Source Files

- `server/realtime/disconnect_grace_period.py`
- `server/tests/integration/test_rest_and_grace_period.py`
- `server/tests/unit/realtime/test_disconnect_grace_period.py`

## Audit Trail

- EXTRACTED: 228 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*