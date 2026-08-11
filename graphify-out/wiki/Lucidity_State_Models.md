# Lucidity State Models

> 41 nodes

## Key Concepts

- **PlayerRepositoryProtocol** (21 connections) — `server/persistence/protocols.py`
- **protocols.py** (11 connections) — `server/persistence/protocols.py`
- **Player** (11 connections)
- **RoomRepositoryProtocol** (9 connections) — `server/persistence/protocols.py`
- **UUID** (6 connections)
- **.get_players_batch()** (4 connections) — `server/persistence/protocols.py`
- **.update_player_last_active()** (4 connections) — `server/persistence/protocols.py`
- **.get_player_by_id()** (3 connections) — `server/persistence/protocols.py`
- **.get_player_by_user_id()** (3 connections) — `server/persistence/protocols.py`
- **.get_players_by_user_id()** (3 connections) — `server/persistence/protocols.py`
- **.get_active_players_by_user_id()** (3 connections) — `server/persistence/protocols.py`
- **.get_player_by_name()** (3 connections) — `server/persistence/protocols.py`
- **.save_player()** (3 connections) — `server/persistence/protocols.py`
- **.save_players()** (3 connections) — `server/persistence/protocols.py`
- **.get_players_in_room()** (3 connections) — `server/persistence/protocols.py`
- **.soft_delete_player()** (3 connections) — `server/persistence/protocols.py`
- **.delete_player()** (3 connections) — `server/persistence/protocols.py`
- **.validate_and_fix_player_room()** (3 connections) — `server/persistence/protocols.py`
- **.get_room_by_id()** (3 connections) — `server/persistence/protocols.py`
- **.list_rooms()** (3 connections) — `server/persistence/protocols.py`
- **Protocol** (2 connections)
- **.list_players()** (2 connections) — `server/persistence/protocols.py`
- **datetime** (2 connections)
- **Room** (2 connections)
- **Repository protocols for MythosMUD persistence layer.  Explicit typing.Protocol** (1 connections) — `server/persistence/protocols.py`
- *... and 16 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (4 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (3 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (3 shared connections)

## Source Files

- `server/persistence/protocols.py`

## Audit Trail

- EXTRACTED: 126 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*