# Contexts Themecontext Hooks

> 29 nodes

## Key Concepts

- **OccupantFormatter** (37 connections) — `server/realtime/occupant_formatter.py`
- **._is_uuid_string()** (8 connections) — `server/realtime/occupant_formatter.py`
- **._is_valid_name_for_occupant()** (7 connections) — `server/realtime/occupant_formatter.py`
- **._process_dict_occupant_for_update()** (7 connections) — `server/realtime/occupant_formatter.py`
- **._process_player_name_for_update()** (6 connections) — `server/realtime/occupant_formatter.py`
- **._process_npc_name_for_update()** (6 connections) — `server/realtime/occupant_formatter.py`
- **Any** (5 connections)
- **.separate_occupants_by_type()** (5 connections) — `server/realtime/occupant_formatter.py`
- **._add_valid_name_to_lists()** (4 connections) — `server/realtime/occupant_formatter.py`
- **._process_string_occupant_for_update()** (4 connections) — `server/realtime/occupant_formatter.py`
- **.__init__()** (3 connections) — `server/realtime/occupant_formatter.py`
- **test_occupant_formatter_is_uuid_string_invalid_dashes()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_is_valid_name_for_occupant_uuid()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_separate_occupants_by_type_dict_npcs()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_separate_occupants_by_type_empty()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Formats and separates occupants by type.** (1 connections) — `server/realtime/occupant_formatter.py`
- **Initialize occupant formatter.** (1 connections) — `server/realtime/occupant_formatter.py`
- **Check if a string looks like a UUID.          Args:             value: The strin** (1 connections) — `server/realtime/occupant_formatter.py`
- **Check if a name is valid for use as an occupant name.          Args:** (1 connections) — `server/realtime/occupant_formatter.py`
- **Add a valid name to both target list and all occupants list.          Args:** (1 connections) — `server/realtime/occupant_formatter.py`
- **Process a player name and add to appropriate lists if valid.          Args:** (1 connections) — `server/realtime/occupant_formatter.py`
- **Process an NPC name and add to appropriate lists if valid.          Args:** (1 connections) — `server/realtime/occupant_formatter.py`
- **Process a dictionary occupant and add to appropriate lists if valid.          Ar** (1 connections) — `server/realtime/occupant_formatter.py`
- **Process a string occupant (legacy format) and add to list if valid.          Arg** (1 connections) — `server/realtime/occupant_formatter.py`
- **Separate occupants into players, NPCs, and all occupants lists.          Args:** (1 connections) — `server/realtime/occupant_formatter.py`
- *... and 4 more nodes in this community*

## Relationships

- [Room Occupant Formatter](Room_Occupant_Formatter.md) (26 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (2 shared connections)
- [NATS Retry Handler](NATS_Retry_Handler.md) (1 shared connections)
- [Manual Dependency Analysis](Manual_Dependency_Analysis.md) (1 shared connections)

## Source Files

- `server/realtime/occupant_formatter.py`
- `server/tests/unit/realtime/test_occupant_formatter.py`

## Audit Trail

- EXTRACTED: 117 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*