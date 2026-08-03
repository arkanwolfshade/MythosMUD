# config models game

> 31 nodes

## Key Concepts

- **_StubPlayerRepo** (18 connections) — `server/tests/unit/persistence/test_protocols.py`
- **test_player_repository_protocol_stub()** (17 connections) — `server/tests/unit/persistence/test_protocols.py`
- **RoomRepositoryProtocol** (13 connections) — `server/persistence/protocols.py`
- **test_protocols.py** (10 connections) — `server/tests/unit/persistence/test_protocols.py`
- **UUID** (6 connections)
- **_StubRoomRepo** (6 connections) — `server/tests/unit/persistence/test_protocols.py`
- **test_room_repository_protocol_stub()** (5 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.get_room_by_id()** (4 connections) — `server/persistence/protocols.py`
- **.list_rooms()** (4 connections) — `server/persistence/protocols.py`
- **.get_player_by_id()** (3 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.get_players_batch()** (3 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.soft_delete_player()** (3 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.delete_player()** (3 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.update_player_last_active()** (3 connections) — `server/tests/unit/persistence/test_protocols.py`
- **Protocol** (2 connections)
- **Room** (2 connections)
- **.get_player_by_user_id()** (2 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.get_players_by_user_id()** (2 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.get_active_players_by_user_id()** (2 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.get_player_by_name()** (2 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.save_player()** (2 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.save_players()** (2 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.list_players()** (2 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.get_players_in_room()** (2 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.validate_and_fix_player_room()** (2 connections) — `server/tests/unit/persistence/test_protocols.py`
- *... and 6 more nodes in this community*

## Relationships

- [persistence protocols rationale](persistence_protocols_rationale.md) (10 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [world models rationale](world_models_rationale.md) (1 shared connections)
- [room models instance](room_models_instance.md) (1 shared connections)
- [persistence container item](persistence_container_item.md) (1 shared connections)

## Source Files

- `server/persistence/protocols.py`
- `server/tests/unit/persistence/test_protocols.py`

## Audit Trail

- EXTRACTED: 117 (91%)
- INFERRED: 11 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*