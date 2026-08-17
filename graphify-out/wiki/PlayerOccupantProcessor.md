# PlayerOccupantProcessor

> 27 nodes

## Key Concepts

- **PlayerOccupantProcessor** (21 connections) — `server/realtime/player_occupant_processor.py`
- **asyncio** (8 connections)
- **._create_player_occupant_info()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **.process_players_for_occupants()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **test_both_linkdead_and_warded_indicators()** (7 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_warded_indicator_in_game_state_provider()** (6 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_warded_indicator_in_player_occupant_processor()** (6 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **.__init__()** (5 connections) — `server/realtime/player_occupant_processor.py`
- **test_warded_indicator_in_look_player()** (5 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_warded_indicator_in_look_room()** (5 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_warded_indicator_not_shown_for_reconnections()** (5 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **UUID** (5 connections)
- **._convert_player_ids_to_uuids()** (4 connections) — `server/realtime/player_occupant_processor.py`
- **._ensure_player_included_in_list()** (4 connections) — `server/realtime/player_occupant_processor.py`
- **Any** (3 connections)
- **Process players and convert to occupant information. Args: room_id: The room ID…** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Processes player occupants for rooms.** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Initialize player occupant processor. Args: connection_manager:…** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Ensure a player is included in the player ID strings list if specified. Args:…** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Convert player ID strings to UUIDs for batch loading. Args: player_id_strings:…** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Create occupant information dictionary for a single player. Args:…** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Test that look_player command adds '(warded)' indicator.** (1 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **Test that '(warded)' indicator is not shown for reconnections.** (1 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **Test that both '(linkdead)' and '(warded)' can appear together.** (1 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **Test that game state provider adds '(warded)' indicator.** (1 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- *... and 2 more nodes in this community*

## Relationships

- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (9 shared connections)
- [build_event](build_event.md) (8 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (5 shared connections)
- [test_look_player.py](test_look_player.py.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [test_player_occupant_processor.py](test_player_occupant_processor.py.md) (2 shared connections)
- [.__init__](__init__.md) (1 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (1 shared connections)
- [start_grace_period](start_grace_period.md) (1 shared connections)
- [GameStateProvider](GameStateProvider.md) (1 shared connections)
- [test_look_room.py](test_look_room.py.md) (1 shared connections)

## Source Files

- `server/realtime/player_occupant_processor.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`

## Audit Trail

- EXTRACTED: 61 (82%)
- INFERRED: 13 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*