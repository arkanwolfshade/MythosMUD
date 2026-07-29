# disconnect grace period

> 95 nodes

## Key Concepts

- **test_login_grace_period_visual_indicator.py** (28 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **disconnect_grace_period.py** (24 connections) — `server/realtime/disconnect_grace_period.py`
- **is_player_in_grace_period()** (24 connections) — `server/realtime/disconnect_grace_period.py`
- **test_rest_and_grace_period.py** (24 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **start_grace_period()** (18 connections) — `server/realtime/disconnect_grace_period.py`
- **test_disconnect_grace_period.py** (17 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **player_event_handlers_utils.py** (16 connections) — `server/realtime/player_event_handlers_utils.py`
- **player_occupant_processor.py** (15 connections) — `server/realtime/player_occupant_processor.py`
- **MockPersistenceFull** (14 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **player_name_utils.py** (13 connections) — `server/realtime/player_name_utils.py`
- **cancel_grace_period()** (12 connections) — `server/realtime/disconnect_grace_period.py`
- **test_both_linkdead_and_warded_indicators()** (6 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **UUID** (4 connections)
- **test_unintentional_disconnect_starts_grace_period()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_intentional_disconnect_no_grace_period()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_command_blocks_during_combat()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_command_starts_countdown_not_in_combat()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_location_instant_disconnect()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_location_blocked_during_combat()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_countdown_completes_disconnect()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_start_grace_period_reconnection_cancels()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_warded_indicator_in_look_room()** (4 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_warded_indicator_in_look_player()** (4 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_warded_indicator_in_websocket_room_updates()** (4 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **Any** (3 connections)
- *... and 70 more nodes in this community*

## Relationships

- [Any](Any.md) (13 shared connections)
- [login grace period](login_grace_period.md) (12 shared connections)
- [main()](main%28%29.md) (10 shared connections)
- [player disconnect handlers](player_disconnect_handlers.md) (9 shared connections)
- [.check and interrupt rest()](check_and_interrupt_rest%28%29.md) (9 shared connections)
- [look room](look_room.md) (7 shared connections)
- [PlayerOccupantProcessor](PlayerOccupantProcessor.md) (7 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (7 shared connections)
- [look player](look_player.md) (6 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (4 shared connections)
- [check alias safety()](check_alias_safety%28%29.md) (3 shared connections)
- [.state()](state%28%29.md) (3 shared connections)

## Source Files

- `server/realtime/disconnect_grace_period.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/realtime/player_name_utils.py`
- `server/realtime/player_occupant_processor.py`
- `server/tests/integration/test_rest_and_grace_period.py`
- `server/tests/unit/realtime/test_disconnect_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`

## Audit Trail

- EXTRACTED: 371 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*