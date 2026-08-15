# PlayerOccupantProcessor

> 18 nodes

## Key Concepts

- **PlayerOccupantProcessor** (21 connections) — `server/realtime/player_occupant_processor.py`
- **._create_player_occupant_info()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **.process_players_for_occupants()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **.__init__()** (5 connections) — `server/realtime/player_occupant_processor.py`
- **UUID** (5 connections)
- **._convert_player_ids_to_uuids()** (4 connections) — `server/realtime/player_occupant_processor.py`
- **._ensure_player_included_in_list()** (4 connections) — `server/realtime/player_occupant_processor.py`
- **test_player_occupant_processor_adds_linkdead_indicator()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **test_player_occupant_processor_no_linkdead_when_not_in_grace_period()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **Any** (3 connections)
- **Process players and convert to occupant information. Args: room_id: The room ID…** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Processes player occupants for rooms.** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Initialize player occupant processor. Args: connection_manager:…** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Ensure a player is included in the player ID strings list if specified. Args:…** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Convert player ID strings to UUIDs for batch loading. Args: player_id_strings:…** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Create occupant information dictionary for a single player. Args:…** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Test PlayerOccupantProcessor adds (linkdead) indicator for grace period players.** (1 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **Test PlayerOccupantProcessor does not add (linkdead) when player not in grace…** (1 connections) — `server/tests/unit/realtime/test_visual_indicator.py`

## Relationships

- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (6 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [test_look_player.py](test_look_player.py.md) (3 shared connections)
- [test_player_occupant_processor.py](test_player_occupant_processor.py.md) (2 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (2 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (1 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (1 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (1 shared connections)

## Source Files

- `server/realtime/player_occupant_processor.py`
- `server/tests/unit/realtime/test_visual_indicator.py`

## Audit Trail

- EXTRACTED: 36 (80%)
- INFERRED: 9 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*