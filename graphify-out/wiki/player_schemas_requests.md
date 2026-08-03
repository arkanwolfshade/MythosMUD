# player schemas requests

> 13 nodes

## Key Concepts

- **._is_valid_name_for_occupant()** (7 connections) — `server/realtime/occupant_formatter.py`
- **._process_dict_occupant_for_update()** (7 connections) — `server/realtime/occupant_formatter.py`
- **._process_player_name_for_update()** (6 connections) — `server/realtime/occupant_formatter.py`
- **._process_npc_name_for_update()** (6 connections) — `server/realtime/occupant_formatter.py`
- **Any** (5 connections)
- **.separate_occupants_by_type()** (5 connections) — `server/realtime/occupant_formatter.py`
- **._add_valid_name_to_lists()** (4 connections) — `server/realtime/occupant_formatter.py`
- **Check if a name is valid for use as an occupant name.          Args:** (1 connections) — `server/realtime/occupant_formatter.py`
- **Add a valid name to both target list and all occupants list.          Args:** (1 connections) — `server/realtime/occupant_formatter.py`
- **Process a player name and add to appropriate lists if valid.          Args:** (1 connections) — `server/realtime/occupant_formatter.py`
- **Process an NPC name and add to appropriate lists if valid.          Args:** (1 connections) — `server/realtime/occupant_formatter.py`
- **Process a dictionary occupant and add to appropriate lists if valid.          Ar** (1 connections) — `server/realtime/occupant_formatter.py`
- **Separate occupants into players, NPCs, and all occupants lists.          Args:** (1 connections) — `server/realtime/occupant_formatter.py`

## Relationships

- [container sql injection](container_sql_injection.md) (6 shared connections)
- [npc populate databases](npc_populate_databases.md) (2 shared connections)

## Source Files

- `server/realtime/occupant_formatter.py`

## Audit Trail

- EXTRACTED: 46 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*