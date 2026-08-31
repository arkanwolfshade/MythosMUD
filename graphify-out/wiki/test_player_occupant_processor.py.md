# test_player_occupant_processor.py

> 79 nodes

## Key Concepts

- **test_player_occupant_processor.py** (27 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- **PlayerOccupantProcessor** (21 connections) — `server/realtime/player_occupant_processor.py`
- **player_occupant_processor.py** (15 connections) — `server/realtime/player_occupant_processor.py`
- **test_visual_indicator.py** (14 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **._create_player_occupant_info()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **.process_players_for_occupants()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **.__init__()** (5 connections) — `server/realtime/player_occupant_processor.py`
- **UUID** (5 connections)
- **._convert_player_ids_to_uuids()** (4 connections) — `server/realtime/player_occupant_processor.py`
- **._ensure_player_included_in_list()** (4 connections) — `server/realtime/player_occupant_processor.py`
- **processor()** (4 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- **test_filter_other_players_adds_linkdead_indicator()** (4 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **test_filter_other_players_no_linkdead_when_not_in_grace_period()** (4 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **asyncio** (4 connections)
- **mock_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- **mock_name_extractor()** (3 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- **test_process_players_for_occupants()** (3 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- **test_process_players_for_occupants_with_invalid_name()** (3 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- **test_process_players_for_occupants_with_player_not_found()** (3 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- **test_process_players_for_occupants_with_uuid_ensure_player()** (3 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- **test_format_player_look_display_adds_linkdead_indicator()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **test_format_player_look_display_no_linkdead_when_not_in_grace_period()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **test_player_occupant_processor_adds_linkdead_indicator()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **test_player_occupant_processor_no_linkdead_when_not_in_grace_period()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **Any** (3 connections)
- *... and 54 more nodes in this community*

## Relationships

- [test_websocket_room_updates.py](test_websocket_room_updates.py.md) (5 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (4 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (4 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (4 shared connections)
- [test_look_room.py](test_look_room.py.md) (4 shared connections)
- [test_look_player.py](test_look_player.py.md) (4 shared connections)
- [disconnect_grace_period.py](disconnect_grace_period.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)

## Source Files

- `server/realtime/player_occupant_processor.py`
- `server/tests/unit/realtime/test_player_occupant_processor.py`
- `server/tests/unit/realtime/test_visual_indicator.py`

## Audit Trail

- EXTRACTED: 125 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*