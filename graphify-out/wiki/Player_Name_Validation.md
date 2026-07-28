# Player Name Validation

> 162 nodes · cohesion 0.02

## Key Concepts

- **PlayerNameExtractor** (104 connections) — `server/realtime/player_name_utils.py`
- **TestPlayerNameExtractor** (62 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **Any** (14 connections)
- **.extract_and_validate_player_name()** (8 connections) — `server/realtime/player_name_utils.py`
- **._validate_name_not_uuid()** (8 connections) — `server/realtime/player_name_utils.py`
- **UUID** (8 connections)
- **._try_fallback_name_sources()** (7 connections) — `server/realtime/player_name_utils.py`
- **._is_uuid_string()** (6 connections) — `server/realtime/player_name_utils.py`
- **._is_valid_name_string()** (6 connections) — `server/realtime/player_name_utils.py`
- **.extract_player_name()** (5 connections) — `server/realtime/player_name_utils.py`
- **._is_valid_name()** (5 connections) — `server/realtime/player_name_utils.py`
- **._log_uuid_validation_failure()** (5 connections) — `server/realtime/player_name_utils.py`
- **._try_player_username()** (5 connections) — `server/realtime/player_name_utils.py`
- **._try_user_object_name()** (5 connections) — `server/realtime/player_name_utils.py`
- **._validate_name_basic()** (5 connections) — `server/realtime/player_name_utils.py`
- **.validate_player_name_not_uuid()** (5 connections) — `server/realtime/player_name_utils.py`
- **._check_uuid_string_matches()** (4 connections) — `server/realtime/player_name_utils.py`
- **._extract_initial_player_name()** (4 connections) — `server/realtime/player_name_utils.py`
- **._get_name_from_user_object()** (4 connections) — `server/realtime/player_name_utils.py`
- **.is_valid_name_for_occupant()** (4 connections) — `server/realtime/player_name_utils.py`
- **test_player_name_utils.py** (4 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **.test_extract_player_name_user_exception()** (4 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **._check_uuid_pattern_match()** (3 connections) — `server/realtime/player_name_utils.py`
- **.__init__()** (3 connections) — `server/realtime/player_name_utils.py`
- **.test_check_uuid_pattern_match_invalid()** (3 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- *... and 137 more nodes in this community*

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (14 shared connections)
- [NPC Occupant Processor](NPC_Occupant_Processor.md) (4 shared connections)
- [NATS Subject Manager](NATS_Subject_Manager.md) (3 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (2 shared connections)
- [Realtime Player Event](Realtime_Player_Event.md) (2 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (1 shared connections)
- [Moderation Command Models](Moderation_Command_Models.md) (1 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (1 shared connections)

## Source Files

- `server/realtime/player_name_utils.py`
- `server/tests/unit/realtime/test_player_name_utils.py`

## Audit Trail

- EXTRACTED: 533 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*