# PlayerOccupantProcessor

> 31 nodes

## Key Concepts

- **PlayerOccupantProcessor** (21 connections) — `server/realtime/player_occupant_processor.py`
- **player_occupant_processor.py** (15 connections) — `server/realtime/player_occupant_processor.py`
- **test_visual_indicator.py** (13 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **._create_player_occupant_info()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **.process_players_for_occupants()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **.__init__()** (5 connections) — `server/realtime/player_occupant_processor.py`
- **UUID** (5 connections)
- **._convert_player_ids_to_uuids()** (4 connections) — `server/realtime/player_occupant_processor.py`
- **._ensure_player_included_in_list()** (4 connections) — `server/realtime/player_occupant_processor.py`
- **test_filter_other_players_adds_linkdead_indicator()** (4 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **test_filter_other_players_no_linkdead_when_not_in_grace_period()** (4 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **test_format_player_look_display_adds_linkdead_indicator()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **test_format_player_look_display_no_linkdead_when_not_in_grace_period()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **test_player_occupant_processor_adds_linkdead_indicator()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **test_player_occupant_processor_no_linkdead_when_not_in_grace_period()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **Any** (3 connections)
- **asyncio** (2 connections)
- **Player occupant processing utilities. This module handles querying and…** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Process players and convert to occupant information. Args: room_id: The room ID…** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Processes player occupants for rooms.** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Initialize player occupant processor. Args: connection_manager:…** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Ensure a player is included in the player ID strings list if specified. Args:…** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Convert player ID strings to UUIDs for batch loading. Args: player_id_strings:…** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Create occupant information dictionary for a single player. Args:…** (1 connections) — `server/realtime/player_occupant_processor.py`
- **Unit tests for visual indicator (linkdead) display. Tests that "(linkdead)"…** (1 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- *... and 6 more nodes in this community*

## Relationships

- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (9 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (4 shared connections)
- [test_look_room.py](test_look_room.py.md) (4 shared connections)
- [test_look_player.py](test_look_player.py.md) (4 shared connections)
- [test_player_occupant_processor.py](test_player_occupant_processor.py.md) (3 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (3 shared connections)
- [disconnect_grace_period.py](disconnect_grace_period.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)

## Source Files

- `server/realtime/player_occupant_processor.py`
- `server/tests/unit/realtime/test_visual_indicator.py`

## Audit Trail

- EXTRACTED: 70 (91%)
- INFERRED: 7 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*