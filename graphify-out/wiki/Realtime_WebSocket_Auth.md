# Realtime WebSocket Auth

> 79 nodes

## Key Concepts

- **is_player_in_grace_period()** (26 connections) — `server/realtime/disconnect_grace_period.py`
- **test_rest_and_grace_period.py** (24 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **game_state_provider.py** (22 connections) — `server/realtime/integration/game_state_provider.py`
- **start_grace_period()** (20 connections) — `server/realtime/disconnect_grace_period.py`
- **test_disconnect_grace_period.py** (17 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **MockPersistenceFull** (14 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **cancel_grace_period()** (12 connections) — `server/realtime/disconnect_grace_period.py`
- **__init__.py** (5 connections) — `server/realtime/integration/__init__.py`
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
- *... and 54 more nodes in this community*

## Relationships

- [NATS Message Broker](NATS_Message_Broker.md) (19 shared connections)
- [Client Event Store](Client_Event_Store.md) (10 shared connections)
- [Spell Effects Tests](Spell_Effects_Tests.md) (5 shared connections)
- [Game State Provider](Game_State_Provider.md) (5 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (4 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (3 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (3 shared connections)
- [Look Player Command](Look_Player_Command.md) (2 shared connections)
- [Room Look Formatting](Room_Look_Formatting.md) (2 shared connections)
- [Message Broadcaster Core](Message_Broadcaster_Core.md) (2 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (2 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)

## Source Files

- `server/realtime/disconnect_grace_period.py`
- `server/realtime/integration/__init__.py`
- `server/realtime/integration/game_state_provider.py`
- `server/tests/integration/test_rest_and_grace_period.py`
- `server/tests/unit/realtime/test_disconnect_grace_period.py`

## Audit Trail

- EXTRACTED: 278 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*