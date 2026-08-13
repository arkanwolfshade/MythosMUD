# test_player_occupant_processor.py

> 72 nodes

## Key Concepts

- **test_player_occupant_processor.py** (26 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- **PlayerOccupantProcessor** (21 connections) — `server/realtime/player_occupant_processor.py`
- **player_occupant_processor.py** (15 connections) — `server/realtime/player_occupant_processor.py`
- **.__init__()** (9 connections) — `server/realtime/room_occupant_manager.py`
- **._create_player_occupant_info()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **.process_players_for_occupants()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **.__init__()** (5 connections) — `server/realtime/player_occupant_processor.py`
- **UUID** (5 connections)
- **._convert_player_ids_to_uuids()** (4 connections) — `server/realtime/player_occupant_processor.py`
- **._ensure_player_included_in_list()** (4 connections) — `server/realtime/player_occupant_processor.py`
- **processor()** (4 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- **asyncio** (4 connections)
- **mock_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- **mock_name_extractor()** (3 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- **test_create_player_occupant_info_grace_period_exception()** (3 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- **test_process_players_for_occupants()** (3 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- **test_process_players_for_occupants_with_invalid_name()** (3 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- **test_process_players_for_occupants_with_player_not_found()** (3 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- **test_process_players_for_occupants_with_uuid_ensure_player()** (3 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- **test_player_occupant_processor_adds_linkdead_indicator()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **test_player_occupant_processor_no_linkdead_when_not_in_grace_period()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **Any** (3 connections)
- **fixture** (3 connections)
- **test_convert_player_ids_to_uuids()** (2 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- **test_convert_player_ids_to_uuids_already_uuid()** (2 connections) — `server/tests/unit/realtime/test_player_occupant_processor.py`
- *... and 47 more nodes in this community*

## Relationships

- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (9 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (6 shared connections)
- [test_look_player.py](test_look_player.py.md) (4 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [is_player_in_grace_period](is_player_in_grace_period.md) (2 shared connections)
- [RoomIDUtils](RoomIDUtils.md) (2 shared connections)
- [OccupantFormatter](OccupantFormatter.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)
- [test_player_disconnect_handlers.py](test_player_disconnect_handlers.py.md) (1 shared connections)

## Source Files

- `server/realtime/player_occupant_processor.py`
- `server/realtime/room_occupant_manager.py`
- `server/tests/unit/realtime/test_player_occupant_processor.py`
- `server/tests/unit/realtime/test_visual_indicator.py`

## Audit Trail

- EXTRACTED: 118 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*