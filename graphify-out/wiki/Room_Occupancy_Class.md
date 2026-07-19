# Room Occupancy Class

> 128 nodes · cohesion 0.02

## Key Concepts

- **Room** (88 connections) — `server/models/room.py`
- **test_room_class.py** (28 connections) — `server/tests/unit/models/test_room_class.py`
- **PlayerRepositoryProtocol** (21 connections) — `server/persistence/protocols.py`
- **Player** (13 connections) — `server/persistence/protocols.py`
- **protocols.py** (9 connections) — `server/persistence/protocols.py`
- **RoomRepositoryProtocol** (9 connections) — `server/persistence/protocols.py`
- **.to_dict()** (8 connections) — `server/models/room.py`
- **UUID** (8 connections) — `server/persistence/protocols.py`
- **UUID** (6 connections) — `server/models/room.py`
- **.get_containers()** (5 connections) — `server/models/room.py`
- **.__init__()** (5 connections) — `server/models/room.py`
- **.get_npcs()** (4 connections) — `server/models/room.py`
- **.get_occupant_count()** (4 connections) — `server/models/room.py`
- **.get_players()** (4 connections) — `server/models/room.py`
- **.player_entered()** (4 connections) — `server/models/room.py`
- **.player_left()** (4 connections) — `server/models/room.py`
- **.get_players_batch()** (4 connections) — `server/persistence/protocols.py`
- **.update_player_last_active()** (4 connections) — `server/persistence/protocols.py`
- **datetime** (4 connections) — `server/persistence/protocols.py`
- **Room** (4 connections) — `server/persistence/protocols.py`
- **.add_player_silently()** (3 connections) — `server/models/room.py`
- **.get_objects()** (3 connections) — `server/models/room.py`
- **.has_player()** (3 connections) — `server/models/room.py`
- **.is_empty()** (3 connections) — `server/models/room.py`
- **.remove_player_silently()** (3 connections) — `server/models/room.py`
- *... and 103 more nodes in this community*

## Relationships

- [[NPC Admin API]] (16 shared connections)
- [[NPC Services Bundle]] (9 shared connections)
- [[Player Domain Model]] (7 shared connections)
- [[Distributed Event Bus]] (6 shared connections)
- [[Persistence Item Instance]] (3 shared connections)
- [[Game Instance Manager]] (2 shared connections)
- [[Movement Service Tests]] (2 shared connections)
- [[WebSocket Initial State]] (2 shared connections)
- [[Combat Command Handler]] (2 shared connections)
- [[Player Combat XP]] (2 shared connections)
- [[Async Persistence Types]] (1 shared connections)
- [[NPC Death Lifecycle]] (1 shared connections)

## Source Files

- `server/models/room.py`
- `server/persistence/protocols.py`
- `server/tests/unit/models/test_room_class.py`

## Audit Trail

- EXTRACTED: 405 (93%)
- INFERRED: 32 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
