# npc combat base

> 44 nodes

## Key Concepts

- **disconnect_grace_period.py** (26 connections) — `server/realtime/disconnect_grace_period.py`
- **is_player_in_grace_period()** (26 connections) — `server/realtime/disconnect_grace_period.py`
- **start_grace_period()** (20 connections) — `server/realtime/disconnect_grace_period.py`
- **test_disconnect_grace_period.py** (17 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **cancel_grace_period()** (12 connections) — `server/realtime/disconnect_grace_period.py`
- **UUID** (4 connections)
- **test_start_grace_period_reconnection_cancels()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **Any** (3 connections)
- **test_reconnection_cancels_grace_period()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_grace_period_player_can_auto_attack()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_grace_period_player_cannot_use_commands()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_visual_indicator_in_grace_period()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_start_grace_period_creates_task()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_start_grace_period_already_in_grace_period()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_start_grace_period_timer_expires()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_cancel_grace_period_not_in_grace_period()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_cancel_grace_period_cancels_task()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_is_player_in_grace_period_true()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_is_player_in_grace_period_false()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_is_player_in_grace_period_no_manager_attribute()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_grace_period_handles_player_not_found()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_grace_period_handles_errors_gracefully()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **mock_manager()** (2 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **Disconnect grace period management for MythosMUD.  This module handles the 30-se** (1 connections) — `server/realtime/disconnect_grace_period.py`
- **Start a grace period for a disconnected player.      During the grace period, th** (1 connections) — `server/realtime/disconnect_grace_period.py`
- *... and 19 more nodes in this community*

## Relationships

- [player disconnect handlers](player_disconnect_handlers.md) (9 shared connections)
- [command utility models](command_utility_models.md) (7 shared connections)
- [rest grace period](rest_grace_period.md) (7 shared connections)
- [player model models](player_model_models.md) (3 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (3 shared connections)
- [look helpers commands](look_helpers_commands.md) (3 shared connections)
- [command commands talk](command_commands_talk.md) (3 shared connections)
- [help content websocket](help_content_websocket.md) (3 shared connections)
- [movement monitor game](movement_monitor_game.md) (3 shared connections)
- [command models moderation](command_models_moderation.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [profession models rationale](profession_models_rationale.md) (2 shared connections)

## Source Files

- `server/realtime/disconnect_grace_period.py`
- `server/tests/integration/test_rest_and_grace_period.py`
- `server/tests/unit/realtime/test_disconnect_grace_period.py`

## Audit Trail

- EXTRACTED: 177 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*