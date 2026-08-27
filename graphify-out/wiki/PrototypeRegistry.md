# PrototypeRegistry

> 36 nodes

## Key Concepts

- **disconnect_grace_period.py** (27 connections) — `server/realtime/disconnect_grace_period.py`
- **start_grace_period()** (20 connections) — `server/realtime/disconnect_grace_period.py`
- **test_disconnect_grace_period.py** (19 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **cancel_grace_period()** (14 connections) — `server/realtime/disconnect_grace_period.py`
- **asyncio** (9 connections)
- **test_start_grace_period_reconnection_cancels()** (5 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_cancel_grace_period_cancels_task()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_cancel_grace_period_not_in_grace_period()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_grace_period_handles_errors_gracefully()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_grace_period_handles_player_not_found()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_start_grace_period_already_in_grace_period()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_start_grace_period_creates_task()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_start_grace_period_timer_expires()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **UUID** (4 connections)
- **mock_manager()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_is_player_in_grace_period_false()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_is_player_in_grace_period_no_manager_attribute()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_is_player_in_grace_period_true()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **Any** (3 connections)
- **fixture** (1 connections)
- **Disconnect grace period management for MythosMUD. This module handles the…** (1 connections) — `server/realtime/disconnect_grace_period.py`
- **Cancel grace period for a player (e.g., on reconnection). Args: player_id: The…** (1 connections) — `server/realtime/disconnect_grace_period.py`
- **Start a grace period for a disconnected player. During the grace period, the…** (1 connections) — `server/realtime/disconnect_grace_period.py`
- **Unit tests for disconnect grace period management. Tests the grace period…** (1 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **Test grace period is cancelled when player reconnects.** (1 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- *... and 11 more nodes in this community*

## Relationships

- [character-cleanup.ts](character-cleanup.ts.md) (10 shared connections)
- [TargetMatch](TargetMatch.md) (9 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (4 shared connections)
- [test_go_command.py](test_go_command.py.md) (3 shared connections)
- [utils/layout.ts](utils-layout.ts.md) (3 shared connections)
- [chatPanelRuntimeUtils.ts](chatPanelRuntimeUtils.ts.md) (3 shared connections)
- [test_container_persistence_extended_crud.py](test_container_persistence_extended_crud.py.md) (3 shared connections)
- [test_inventory_command_prototype.py](test_inventory_command_prototype.py.md) (2 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)
- [test_connection_statistics.py](test_connection_statistics.py.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [generate_invites.py](generate_invites.py.md) (1 shared connections)

## Source Files

- `server/realtime/disconnect_grace_period.py`
- `server/tests/unit/realtime/test_disconnect_grace_period.py`

## Audit Trail

- EXTRACTED: 101 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*