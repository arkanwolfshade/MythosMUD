# test_player_respawn_service.py

> 53 nodes · cohesion 0.07

## Key Concepts

- **PlayerRepositoryProtocol** (26 connections) — `server/persistence/protocols.py`
- **test_protocol_ellipsis_bodies_via_unbound_methods()** (22 connections) — `server/tests/unit/persistence/test_protocols.py`
- **protocols.py** (13 connections) — `server/persistence/protocols.py`
- **Player** (11 connections)
- **RoomRepositoryProtocol** (11 connections) — `server/persistence/protocols.py`
- **test_protocols.py** (10 connections) — `server/tests/unit/persistence/test_protocols.py`
- **UUID** (7 connections)
- **.get_players_batch()** (5 connections) — `server/persistence/protocols.py`
- **.update_player_last_active()** (5 connections) — `server/persistence/protocols.py`
- **test_player_repository_protocol_stub()** (5 connections) — `server/tests/unit/persistence/test_protocols.py`
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
- **_StubRoomRepo** (4 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.clear_player_inventory()** (3 connections) — `server/persistence/protocols.py`
- *... and 28 more nodes in this community*

## Relationships

- [.profession_to_dict](profession_to_dict.md) (3 shared connections)
- [Room](Room.md) (3 shared connections)
- [GameClientV2Dock.test.tsx](GameClientV2Dock.test.tsx.md) (3 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (2 shared connections)
- [test_combat_monitoring_service.py](test_combat_monitoring_service.py.md) (2 shared connections)
- [test_players_procedures.py](test_players_procedures.py.md) (2 shared connections)
- [inventory_item_matching.py](inventory_item_matching.py.md) (2 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (1 shared connections)
- [BaseEvent](BaseEvent.md) (1 shared connections)
- [ConnectionErrorHandler](ConnectionErrorHandler.md) (1 shared connections)

## Source Files

- `server/persistence/protocols.py`
- `server/tests/unit/persistence/test_protocols.py`

## Audit Trail

- EXTRACTED: 107 (93%)
- INFERRED: 8 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*