# persistence protocols rationale

> 66 nodes

## Key Concepts

- **PlayerRepositoryProtocol** (25 connections) — `server/persistence/protocols.py`
- **_StubPlayerRepo** (18 connections) — `server/tests/unit/persistence/test_protocols.py`
- **test_protocol_ellipsis_bodies_via_unbound_methods()** (18 connections) — `server/tests/unit/persistence/test_protocols.py`
- **test_player_repository_protocol_stub()** (17 connections) — `server/tests/unit/persistence/test_protocols.py`
- **RoomRepositoryProtocol** (13 connections) — `server/persistence/protocols.py`
- **protocols.py** (12 connections) — `server/persistence/protocols.py`
- **Player** (11 connections)
- **test_protocols.py** (10 connections) — `server/tests/unit/persistence/test_protocols.py`
- **UUID** (6 connections)
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
- *... and 41 more nodes in this community*

## Relationships

- [websocket helpers realtime](websocket_helpers_realtime.md) (3 shared connections)
- [game weapon player](game_weapon_player.md) (3 shared connections)
- [room models instance](room_models_instance.md) (3 shared connections)
- [commands party examples](commands_party_examples.md) (3 shared connections)
- [player room realtime](player_room_realtime.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [retry rationale transient()](retry_rationale_transient%28%29.md) (1 shared connections)

## Source Files

- `server/persistence/protocols.py`
- `server/tests/unit/persistence/test_protocols.py`

## Audit Trail

- EXTRACTED: 258 (94%)
- INFERRED: 17 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*