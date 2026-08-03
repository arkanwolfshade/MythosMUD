# grace period disconnect

> 111 nodes

## Key Concepts

- **test_login_grace_period_visual_indicator.py** (28 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **disconnect_grace_period.py** (26 connections) — `server/realtime/disconnect_grace_period.py`
- **is_player_in_grace_period()** (26 connections) — `server/realtime/disconnect_grace_period.py`
- **test_rest_and_grace_period.py** (24 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **game_state_provider.py** (21 connections) — `server/realtime/integration/game_state_provider.py`
- **PlayerOccupantProcessor** (21 connections) — `server/realtime/player_occupant_processor.py`
- **start_grace_period()** (20 connections) — `server/realtime/disconnect_grace_period.py`
- **test_disconnect_grace_period.py** (17 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **player_occupant_processor.py** (15 connections) — `server/realtime/player_occupant_processor.py`
- **MockPersistenceFull** (14 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **cancel_grace_period()** (12 connections) — `server/realtime/disconnect_grace_period.py`
- **._create_player_occupant_info()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **.process_players_for_occupants()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **test_both_linkdead_and_warded_indicators()** (6 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **.__init__()** (5 connections) — `server/realtime/player_occupant_processor.py`
- **UUID** (5 connections)
- **test_warded_indicator_in_player_occupant_processor()** (5 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **UUID** (4 connections)
- **._ensure_player_included_in_list()** (4 connections) — `server/realtime/player_occupant_processor.py`
- **._convert_player_ids_to_uuids()** (4 connections) — `server/realtime/player_occupant_processor.py`
- **test_unintentional_disconnect_starts_grace_period()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_intentional_disconnect_no_grace_period()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_command_blocks_during_combat()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_command_starts_countdown_not_in_combat()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_location_instant_disconnect()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- *... and 86 more nodes in this community*

## Relationships

- [grace period login](grace_period_login.md) (18 shared connections)
- [NATS Messaging](NATS_Messaging.md) (17 shared connections)
- [player disconnect handlers](player_disconnect_handlers.md) (9 shared connections)
- [rest grace period](rest_grace_period.md) (9 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (7 shared connections)
- [look helpers commands](look_helpers_commands.md) (6 shared connections)
- [room look commands](room_look_commands.md) (6 shared connections)
- [realtime player connection](realtime_player_connection.md) (6 shared connections)
- [player presence tracker](player_presence_tracker.md) (6 shared connections)
- [room websocket updates](room_websocket_updates.md) (6 shared connections)
- [realtime game state](realtime_game_state.md) (6 shared connections)
- [player look commands](player_look_commands.md) (4 shared connections)

## Source Files

- `server/realtime/disconnect_grace_period.py`
- `server/realtime/integration/game_state_provider.py`
- `server/realtime/player_occupant_processor.py`
- `server/tests/integration/test_rest_and_grace_period.py`
- `server/tests/unit/realtime/test_disconnect_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`

## Audit Trail

- EXTRACTED: 439 (100%)
- INFERRED: 2 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*