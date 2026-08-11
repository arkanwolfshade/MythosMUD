# Player Command Developer Guide

> 15 nodes

## Key Concepts

- **player_presence_utils.py** (16 connections) — `server/realtime/player_presence_utils.py`
- **extract_player_name()** (16 connections) — `server/realtime/player_presence_utils.py`
- **get_player_position()** (7 connections) — `server/realtime/player_presence_utils.py`
- **_get_name_from_user()** (5 connections) — `server/realtime/player_presence_utils.py`
- **_is_valid_name()** (4 connections) — `server/realtime/player_presence_utils.py`
- **_is_uuid_string()** (3 connections) — `server/realtime/player_presence_utils.py`
- **Player** (3 connections)
- **UUID** (3 connections)
- **Any** (1 connections)
- **Utility functions for player presence tracking.  This module provides helper fun** (1 connections) — `server/realtime/player_presence_utils.py`
- **Check if a value is a valid non-empty string name.      Args:         name: Valu** (1 connections) — `server/realtime/player_presence_utils.py`
- **Check if a string is a UUID format.      Args:         value: String to check** (1 connections) — `server/realtime/player_presence_utils.py`
- **Attempt to get player name from related User object.      Args:         player:** (1 connections) — `server/realtime/player_presence_utils.py`
- **Extract and validate player name, ensuring it's never a UUID.      Args:** (1 connections) — `server/realtime/player_presence_utils.py`
- **Get player position from stats.      Args:         player: The player object** (1 connections) — `server/realtime/player_presence_utils.py`

## Relationships

- [Rescue Service Tests](Rescue_Service_Tests.md) (6 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (3 shared connections)
- [Container Persistence Queries](Container_Persistence_Queries.md) (3 shared connections)
- [Chat Rate Limiter](Chat_Rate_Limiter.md) (3 shared connections)
- [NATS Message Broker](NATS_Message_Broker.md) (3 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (1 shared connections)

## Source Files

- `server/realtime/player_presence_utils.py`

## Audit Trail

- EXTRACTED: 62 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*