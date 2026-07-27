# Realtime Player Event

> 26 nodes · cohesion 0.09

## Key Concepts

- **Any** (8 connections) — `server/realtime/player_event_handlers_utils.py`
- **UUID** (7 connections) — `server/realtime/player_event_handlers_utils.py`
- **.get_player_info()** (5 connections) — `server/realtime/player_event_handlers_utils.py`
- **.process_dict_occupant()** (5 connections) — `server/realtime/player_event_handlers_utils.py`
- **.build_occupants_snapshot_data()** (4 connections) — `server/realtime/player_event_handlers_utils.py`
- **._extract_name_from_occupant()** (4 connections) — `server/realtime/player_event_handlers_utils.py`
- **.extract_occupant_names()** (4 connections) — `server/realtime/player_event_handlers_utils.py`
- **.__init__()** (4 connections) — `server/realtime/player_event_handlers_utils.py`
- **.normalize_player_id()** (4 connections) — `server/realtime/player_event_handlers_utils.py`
- **.add_valid_name_to_lists()** (3 connections) — `server/realtime/player_event_handlers_utils.py`
- **.count_occupants_by_type()** (3 connections) — `server/realtime/player_event_handlers_utils.py`
- **.is_player_disconnecting()** (3 connections) — `server/realtime/player_event_handlers_utils.py`
- **.is_player_in_grace_period()** (3 connections) — `server/realtime/player_event_handlers_utils.py`
- **.normalize_event_ids()** (3 connections) — `server/realtime/player_event_handlers_utils.py`
- **Process a dictionary occupant and add to appropriate lists if valid.          Ar** (2 connections) — `server/realtime/occupant_formatter.py`
- **PlayerNameExtractor** (2 connections) — `server/realtime/player_event_handlers_utils.py`
- **Extract occupant names from occupant information.          Args:             occ** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- **Add a valid name to the appropriate lists.          Args:             name: The** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- **Build structured occupants data from snapshot.          Args:             occupa** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- **Initialize utility functions.          Args:             connection_manager: Con** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- **Count NPCs and players in occupants snapshot.          Args:             occupan** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- **Check if a player is currently in grace period after disconnect.          Args:** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- **Normalize player ID to UUID format.          Args:             player_id: The pl** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- **Get player information and name (async version).          Args:             play** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- **Normalize event IDs to strings for comparison and logging.          Args:** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- *... and 1 more nodes in this community*

## Relationships

- [[Player Respawn Events]] (16 shared connections)
- [[Room Occupant Formatter]] (1 shared connections)
- [[Game Magic Casting]] (1 shared connections)

## Source Files

- `server/realtime/occupant_formatter.py`
- `server/realtime/player_event_handlers_utils.py`

## Audit Trail

- EXTRACTED: 71 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
