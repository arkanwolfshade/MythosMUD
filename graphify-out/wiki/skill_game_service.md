# skill game service

> 16 nodes

## Key Concepts

- **PartyService** (36 connections) — `server/game/party_service.py`
- **.get_party_for_player()** (8 connections) — `server/game/party_service.py`
- **.is_leader()** (5 connections) — `server/game/party_service.py`
- **.is_in_same_party()** (5 connections) — `server/game/party_service.py`
- **.get_party_members()** (4 connections) — `server/game/party_service.py`
- **test_party_invite_event_envelope_shape()** (4 connections) — `server/tests/unit/game/test_party_service.py`
- **.get_party()** (3 connections) — `server/game/party_service.py`
- **party_service()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **In-memory party management: create, disband, add/remove/kick members, leader che** (1 connections) — `server/game/party_service.py`
- **Return the party the player is in, or None.** (1 connections) — `server/game/party_service.py`
- **Return the party by id, or None.** (1 connections) — `server/game/party_service.py`
- **Return True if the player is the leader of their current party.** (1 connections) — `server/game/party_service.py`
- **Return list of party member IDs for the given player (including themselves).** (1 connections) — `server/game/party_service.py`
- **Return True if both players are in the same party. For combat/validator hook:** (1 connections) — `server/game/party_service.py`
- **PartyService with no dependencies (in-memory only).** (1 connections) — `server/tests/unit/game/test_party_service.py`
- **party_invite producer emits a build_event-shaped envelope.** (1 connections) — `server/tests/unit/game/test_party_service.py`

## Relationships

- [party game service](party_game_service.md) (16 shared connections)
- [Error Conversion](Error_Conversion.md) (9 shared connections)
- [player requests schemas](player_requests_schemas.md) (7 shared connections)
- [commands inventory helpers](commands_inventory_helpers.md) (3 shared connections)
- [room realtime occupant](room_realtime_occupant.md) (2 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (1 shared connections)
- [Room Broadcast](Room_Broadcast.md) (1 shared connections)
- [player room event](player_room_event.md) (1 shared connections)

## Source Files

- `server/game/party_service.py`
- `server/tests/unit/game/test_party_service.py`

## Audit Trail

- EXTRACTED: 72 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*