# OccupantFormatter

> 29 nodes

## Key Concepts

- **OccupantFormatter** (41 connections) — `server/realtime/occupant_formatter.py`
- **._is_uuid_string()** (8 connections) — `server/realtime/occupant_formatter.py`
- **._is_valid_name_for_occupant()** (7 connections) — `server/realtime/occupant_formatter.py`
- **._process_dict_occupant_for_update()** (7 connections) — `server/realtime/occupant_formatter.py`
- **._process_npc_name_for_update()** (6 connections) — `server/realtime/occupant_formatter.py`
- **._process_player_name_for_update()** (6 connections) — `server/realtime/occupant_formatter.py`
- **.separate_occupants_by_type()** (5 connections) — `server/realtime/occupant_formatter.py`
- **Any** (5 connections)
- **._add_valid_name_to_lists()** (4 connections) — `server/realtime/occupant_formatter.py`
- **._process_string_occupant_for_update()** (4 connections) — `server/realtime/occupant_formatter.py`
- **test_occupant_formatter_is_uuid_string_invalid_chars()** (4 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_is_uuid_string_invalid_dashes()** (4 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_is_uuid_string_invalid_length()** (4 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_is_uuid_string_valid()** (4 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **.__init__()** (3 connections) — `server/realtime/occupant_formatter.py`
- **Process a dictionary occupant and add to appropriate lists if valid. Args: occ:…** (1 connections) — `server/realtime/occupant_formatter.py`
- **Process a string occupant (legacy format) and add to list if valid. Args: occ:…** (1 connections) — `server/realtime/occupant_formatter.py`
- **Separate occupants into players, NPCs, and all occupants lists. Args:…** (1 connections) — `server/realtime/occupant_formatter.py`
- **Formats and separates occupants by type.** (1 connections) — `server/realtime/occupant_formatter.py`
- **Initialize occupant formatter.** (1 connections) — `server/realtime/occupant_formatter.py`
- **Check if a string looks like a UUID. Args: value: The string to check Returns:…** (1 connections) — `server/realtime/occupant_formatter.py`
- **Check if a name is valid for use as an occupant name. Args: name: The name to…** (1 connections) — `server/realtime/occupant_formatter.py`
- **Add a valid name to both target list and all occupants list. Args: name: The…** (1 connections) — `server/realtime/occupant_formatter.py`
- **Process a player name and add to appropriate lists if valid. Args: player_name:…** (1 connections) — `server/realtime/occupant_formatter.py`
- **Process an NPC name and add to appropriate lists if valid. Args: npc_name: The…** (1 connections) — `server/realtime/occupant_formatter.py`
- *... and 4 more nodes in this community*

## Relationships

- [test_occupant_formatter.py](test_occupant_formatter.py.md) (27 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [.__init__](__init__.md) (1 shared connections)

## Source Files

- `server/realtime/occupant_formatter.py`
- `server/tests/unit/realtime/test_occupant_formatter.py`

## Audit Trail

- EXTRACTED: 52 (66%)
- INFERRED: 27 (34%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*