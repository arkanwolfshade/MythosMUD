# Protocols

> 64 nodes

## Key Concepts

- **PlayerRepositoryProtocol** (22 connections) — `server/persistence/protocols.py`
- **test_protocol_ellipsis_bodies_via_unbound_methods()** (22 connections) — `server/tests/unit/persistence/test_protocols.py`
- **_StubPlayerRepo** (16 connections) — `server/tests/unit/persistence/test_protocols.py`
- **Player** (11 connections)
- **test_protocols.py** (11 connections) — `server/tests/unit/persistence/test_protocols.py`
- **RoomRepositoryProtocol** (10 connections) — `server/persistence/protocols.py`
- **UUID** (6 connections)
- **UUID** (6 connections)
- **.get_players_batch()** (5 connections) — `server/persistence/protocols.py`
- **.update_player_last_active()** (5 connections) — `server/persistence/protocols.py`
- **test_player_repository_protocol_stub()** (5 connections) — `server/tests/unit/persistence/test_protocols.py`
- **_StubRoomRepo** (4 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.delete_player()** (4 connections) — `server/persistence/protocols.py`
- **.get_active_players_by_user_id()** (4 connections) — `server/persistence/protocols.py`
- **.get_player_by_id()** (4 connections) — `server/persistence/protocols.py`
- **.get_player_by_name()** (4 connections) — `server/persistence/protocols.py`
- **.get_player_by_user_id()** (4 connections) — `server/persistence/protocols.py`
- **.get_players_by_user_id()** (4 connections) — `server/persistence/protocols.py`
- **.get_players_in_room()** (4 connections) — `server/persistence/protocols.py`
- **.save_player()** (4 connections) — `server/persistence/protocols.py`
- **.save_players()** (4 connections) — `server/persistence/protocols.py`
- **.soft_delete_player()** (4 connections) — `server/persistence/protocols.py`
- **.validate_and_fix_player_room()** (4 connections) — `server/persistence/protocols.py`
- **.get_room_by_id()** (4 connections) — `server/persistence/protocols.py`
- **.list_rooms()** (4 connections) — `server/persistence/protocols.py`
- *... and 39 more nodes in this community*

## Relationships

- [Player Model & Migrations](Player_Model_&_Migrations.md) (6 shared connections)
- [Test Container Persistence Extended Crud](Test_Container_Persistence_Extended_Crud.md) (2 shared connections)
- [Retry](Retry.md) (2 shared connections)
- [Test Container Helpers Inventory Ops](Test_Container_Helpers_Inventory_Ops.md) (2 shared connections)
- [Room](Room.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/persistence/protocols.py`
- `server/tests/unit/persistence/test_protocols.py`

## Audit Trail

- EXTRACTED: 112 (93%)
- INFERRED: 8 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*