# is_player_in_grace_period

> 28 nodes

## Key Concepts

- **is_player_in_grace_period()** (24 connections) — `server/realtime/disconnect_grace_period.py`
- **PlayerOccupantProcessor** (21 connections) — `server/realtime/player_occupant_processor.py`
- **occupant_display.py** (11 connections) — `server/realtime/occupant_display.py`
- **format_occupant_display_name()** (10 connections) — `server/realtime/occupant_display.py`
- **._create_player_occupant_info()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **.process_players_for_occupants()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **_apply_grace_badges()** (6 connections) — `server/realtime/occupant_display.py`
- **.__init__()** (5 connections) — `server/realtime/player_occupant_processor.py`
- **UUID** (5 connections)
- **._convert_player_ids_to_uuids()** (4 connections) — `server/realtime/player_occupant_processor.py`
- **._ensure_player_included_in_list()** (4 connections) — `server/realtime/player_occupant_processor.py`
- **UUID** (4 connections)
- **_parse_occupant_player_id()** (3 connections) — `server/realtime/occupant_display.py`
- **test_player_occupant_processor_adds_linkdead_indicator()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **test_player_occupant_processor_no_linkdead_when_not_in_grace_period()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **Any** (3 connections)
- **Any** (2 connections)
- **Check if a player is currently in grace period. Args: player_id: The player's…** (1 connections) — `server/realtime/disconnect_grace_period.py`
- **Shared occupant display names for look text and Occupants panel events.** (1 connections) — `server/realtime/occupant_display.py`
- **Format an in-room player's Occupants/look name. Always list; grace badges only.** (1 connections) — `server/realtime/occupant_display.py`
- **Process players and convert to occupant information. Args: room_id: The room ID…** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Processes player occupants for rooms.** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Initialize player occupant processor. Args: connection_manager:…** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Ensure a player is included in the player ID strings list if specified. Args:…** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Convert player ID strings to UUIDs for batch loading. Args: player_id_strings:…** (1 connections) — `server/realtime/player_occupant_processor.py`
- *... and 3 more nodes in this community*

## Relationships

- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (13 shared connections)
- [disconnect_grace_period.py](disconnect_grace_period.py.md) (8 shared connections)
- [test_look_player.py](test_look_player.py.md) (5 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (4 shared connections)
- [PlayerLeftRoom](PlayerLeftRoom.md) (3 shared connections)
- [test_look_room.py](test_look_room.py.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [test_player_occupant_processor.py](test_player_occupant_processor.py.md) (2 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (2 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (2 shared connections)
- [GameStateProvider](GameStateProvider.md) (2 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (1 shared connections)

## Source Files

- `server/realtime/disconnect_grace_period.py`
- `server/realtime/occupant_display.py`
- `server/realtime/player_occupant_processor.py`
- `server/tests/unit/realtime/test_visual_indicator.py`

## Audit Trail

- EXTRACTED: 84 (92%)
- INFERRED: 7 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*