# Dependency Injection Tests

> 101 nodes

## Key Concepts

- **Room** (75 connections) — `server/models/room.py`
- **test_room_class.py** (29 connections) — `server/tests/unit/models/test_room_class.py`
- **movement_helpers.py** (16 connections) — `server/game/movement_helpers.py`
- **.to_dict()** (8 connections) — `server/models/room.py`
- **UUID** (6 connections)
- **.__init__()** (5 connections) — `server/models/room.py`
- **.player_entered()** (5 connections) — `server/models/room.py`
- **.get_containers()** (5 connections) — `server/models/room.py`
- **.player_left()** (4 connections) — `server/models/room.py`
- **.get_players()** (4 connections) — `server/models/room.py`
- **.get_npcs()** (4 connections) — `server/models/room.py`
- **.has_player()** (4 connections) — `server/models/room.py`
- **.get_occupant_count()** (4 connections) — `server/models/room.py`
- **Any** (3 connections)
- **.add_player_silently()** (3 connections) — `server/models/room.py`
- **.remove_player_silently()** (3 connections) — `server/models/room.py`
- **.object_added()** (3 connections) — `server/models/room.py`
- **.object_removed()** (3 connections) — `server/models/room.py`
- **.npc_left()** (3 connections) — `server/models/room.py`
- **.get_objects()** (3 connections) — `server/models/room.py`
- **.is_empty()** (3 connections) — `server/models/room.py`
- **test_room_init()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_init_defaults()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_player_entered()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- **test_room_player_entered_string_id()** (3 connections) — `server/tests/unit/models/test_room_class.py`
- *... and 76 more nodes in this community*

## Relationships

- [Calendar Holiday Schemas](Calendar_Holiday_Schemas.md) (8 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (8 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (5 shared connections)
- [Player Occupant Processor](Player_Occupant_Processor.md) (3 shared connections)
- [Integration DB Fixtures](Integration_DB_Fixtures.md) (3 shared connections)
- [Tailwind UI Migration Plan](Tailwind_UI_Migration_Plan.md) (3 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (2 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (2 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (2 shared connections)
- [Quest Instance Repository](Quest_Instance_Repository.md) (2 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (2 shared connections)
- [Character Creation Service](Character_Creation_Service.md) (2 shared connections)

## Source Files

- `server/game/movement_helpers.py`
- `server/models/room.py`
- `server/tests/unit/models/test_room_class.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 319 (97%)
- INFERRED: 11 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*