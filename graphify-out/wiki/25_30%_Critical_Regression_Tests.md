# 25 30% Critical Regression Tests

> 16 nodes

## Key Concepts

- **test_lucidity_event_dispatcher.py** (34 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_catatonia_event_with_current_lcd()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_catatonia_event_with_message()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_catatonia_event_with_rescuer_and_target()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_rescue_update_event_basic()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_rescue_update_event_with_progress_only()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_dispatch_player_event_import_error()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **mock_send_game_event()** (2 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **Unit tests for lucidity event dispatcher.  Tests the lucidity event broadcasting** (1 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **Create a mock send_game_event function.** (1 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **Test send_catatonia_event with current_lcd.** (1 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **Test send_catatonia_event with message.** (1 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **Test send_catatonia_event with rescuer and target names.** (1 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **Test send_rescue_update_event with basic parameters.** (1 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **Test send_rescue_update_event with progress only.** (1 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **Test _dispatch_player_event handles import errors gracefully.** (1 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`

## Relationships

- [local channel isolation.spec](local_channel_isolation.spec.md) (12 shared connections)
- [LiabilityStackEntry](LiabilityStackEntry.md) (9 shared connections)
- [seed e2e users](seed_e2e_users.md) (7 shared connections)
- [test_dispatch_player_event_uuid_conversion](test_dispatch_player_event_uuid_conversion.md) (1 shared connections)
- [test_send_catatonia_event_basic](test_send_catatonia_event_basic.md) (1 shared connections)
- [test_send_rescue_update_event_dispatch_error](test_send_rescue_update_event_dispatch_error.md) (1 shared connections)
- [main()](main%28%29.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_lucidity_event_dispatcher.py`

## Audit Trail

- EXTRACTED: 62 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*