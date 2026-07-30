# connection manager api

> 15 nodes

## Key Concepts

- **Any** (7 connections)
- **.process_dict_occupant()** (5 connections) — `server/realtime/player_event_handlers_utils.py`
- **.__init__()** (4 connections) — `server/realtime/player_event_handlers_utils.py`
- **._extract_name_from_occupant()** (4 connections) — `server/realtime/player_event_handlers_utils.py`
- **.extract_occupant_names()** (4 connections) — `server/realtime/player_event_handlers_utils.py`
- **.build_occupants_snapshot_data()** (4 connections) — `server/realtime/player_event_handlers_utils.py`
- **.add_valid_name_to_lists()** (3 connections) — `server/realtime/player_event_handlers_utils.py`
- **.count_occupants_by_type()** (3 connections) — `server/realtime/player_event_handlers_utils.py`
- **Initialize utility functions.          Args:             connection_manager: Con** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- **Extract name from a single occupant entry.          Args:             occ: Occup** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- **Extract occupant names from occupant information.          Args:             occ** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- **Add a valid name to the appropriate lists.          Args:             name: The** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- **Process a dictionary occupant and add to appropriate lists.          Args:** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- **Build structured occupants data from snapshot.          Args:             occupa** (1 connections) — `server/realtime/player_event_handlers_utils.py`
- **Count NPCs and players in occupants snapshot.          Args:             occupan** (1 connections) — `server/realtime/player_event_handlers_utils.py`

## Relationships

- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (8 shared connections)
- [container websocket events](container_websocket_events.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_utils.py`

## Audit Trail

- EXTRACTED: 41 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*