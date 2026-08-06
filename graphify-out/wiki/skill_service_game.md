# skill service game

> 14 nodes

## Key Concepts

- **RoomOccupantManager** (22 connections) — `server/realtime/room_occupant_manager.py`
- **.__init__()** (9 connections) — `server/realtime/room_occupant_manager.py`
- **.get_room_occupants()** (4 connections) — `server/realtime/room_occupant_manager.py`
- **Any** (3 connections)
- **.separate_occupants_by_type()** (3 connections) — `server/realtime/room_occupant_manager.py`
- **occupant_manager()** (3 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **test_get_room_occupants_no_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **UUID** (2 connections)
- **Manages room occupant queries and processing.      Handles both players and NPCs** (1 connections) — `server/realtime/room_occupant_manager.py`
- **Initialize the room occupant manager.          Args:             connection_mana** (1 connections) — `server/realtime/room_occupant_manager.py`
- **Get the list of occupants in a room.          Args:             room_id: The roo** (1 connections) — `server/realtime/room_occupant_manager.py`
- **Separate occupants into players, NPCs, and all occupants lists.          Args:** (1 connections) — `server/realtime/room_occupant_manager.py`
- **Create RoomOccupantManager instance.** (1 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`
- **Test get_room_occupants returns empty when no connection manager.** (1 connections) — `server/tests/unit/realtime/test_room_occupant_manager.py`

## Relationships

- [inventory mutation guard](inventory_mutation_guard.md) (6 shared connections)
- [schemas players profession](schemas_players_profession.md) (6 shared connections)
- [profession models rationale](profession_models_rationale.md) (3 shared connections)
- [player occupant processor](player_occupant_processor.md) (3 shared connections)
- [occupant formatter realtime](occupant_formatter_realtime.md) (2 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (2 shared connections)
- [room realtime rationale](room_realtime_rationale.md) (2 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (1 shared connections)

## Source Files

- `server/realtime/room_occupant_manager.py`
- `server/tests/unit/realtime/test_room_occupant_manager.py`

## Audit Trail

- EXTRACTED: 47 (85%)
- INFERRED: 8 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*