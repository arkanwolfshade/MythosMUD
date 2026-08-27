# _make_session_context

> 26 nodes

## Key Concepts

- **Any** (7 connections)
- **UUID** (6 connections)
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
- **Extract occupant names from occupant information. Args: occupants_info: List of…** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- **Add a valid name to the appropriate lists. Args: name: The name to validate and…** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- **Process a dictionary occupant and add to appropriate lists. Args: occ:…** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- **Build structured occupants data from snapshot. Args: occupants_snapshot: List…** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- **Initialize utility functions. Args: connection_manager: ConnectionManager…** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- **Count NPCs and players in occupants snapshot. Args: occupants_snapshot: List of…** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- **Check if a player is currently disconnecting. Args: player_id: The player's ID…** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- **Check if a player is currently in grace period after disconnect. Args:…** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- **Normalize player ID to UUID format. Args: player_id: The player's ID (UUID or…** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- **Get player information and name (async version). Args: player_id: The player's…** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- **Normalize event IDs to strings for comparison and logging. Args: player_id: The…** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- *... and 1 more nodes in this community*

## Relationships

- [InventoryCommandFactory](InventoryCommandFactory.md) (12 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (1 shared connections)
- [npc_database.py](npc_database.py.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_utils.py`

## Audit Trail

- EXTRACTED: 42 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*