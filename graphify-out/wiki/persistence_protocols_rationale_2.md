# persistence protocols rationale

> 49 nodes

## Key Concepts

- **PlayerRepositoryProtocol** (25 connections) — `server/persistence/protocols.py`
- **test_protocol_ellipsis_bodies_via_unbound_methods()** (18 connections) — `server/tests/unit/persistence/test_protocols.py`
- **RoomRepositoryProtocol** (13 connections) — `server/persistence/protocols.py`
- **protocols.py** (12 connections) — `server/persistence/protocols.py`
- **Player** (11 connections)
- **test_protocols.py** (10 connections) — `server/tests/unit/persistence/test_protocols.py`
- **UUID** (6 connections)
- **_StubRoomRepo** (6 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.get_players_batch()** (5 connections) — `server/persistence/protocols.py`
- **.update_player_last_active()** (5 connections) — `server/persistence/protocols.py`
- **test_room_repository_protocol_stub()** (5 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.get_player_by_id()** (4 connections) — `server/persistence/protocols.py`
- **.get_player_by_user_id()** (4 connections) — `server/persistence/protocols.py`
- **.get_players_by_user_id()** (4 connections) — `server/persistence/protocols.py`
- **.get_active_players_by_user_id()** (4 connections) — `server/persistence/protocols.py`
- **.get_player_by_name()** (4 connections) — `server/persistence/protocols.py`
- **.save_player()** (4 connections) — `server/persistence/protocols.py`
- **.save_players()** (4 connections) — `server/persistence/protocols.py`
- **.get_players_in_room()** (4 connections) — `server/persistence/protocols.py`
- **.soft_delete_player()** (4 connections) — `server/persistence/protocols.py`
- **.delete_player()** (4 connections) — `server/persistence/protocols.py`
- **.validate_and_fix_player_room()** (4 connections) — `server/persistence/protocols.py`
- **.get_room_by_id()** (4 connections) — `server/persistence/protocols.py`
- **.list_rooms()** (4 connections) — `server/persistence/protocols.py`
- **.list_players()** (3 connections) — `server/persistence/protocols.py`
- *... and 24 more nodes in this community*

## Relationships

- [retry rationale transient()](retry_rationale_transient%28%29.md) (6 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (3 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (3 shared connections)
- [room models instance](room_models_instance.md) (3 shared connections)
- [auth users rationale](auth_users_rationale.md) (3 shared connections)
- [player room realtime](player_room_realtime.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)

## Source Files

- `server/persistence/protocols.py`
- `server/tests/unit/persistence/test_protocols.py`

## Audit Trail

- EXTRACTED: 187 (94%)
- INFERRED: 13 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*