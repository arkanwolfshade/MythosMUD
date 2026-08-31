# _str_id

> 27 nodes

## Key Concepts

- **_str_id()** (17 connections) — `server/game/party_service.py`
- **UUID** (15 connections)
- **.accept_party_invite()** (8 connections) — `server/game/party_service.py`
- **.get_party_for_player()** (8 connections) — `server/game/party_service.py`
- **._send_result_to_player()** (8 connections) — `server/game/party_service.py`
- **.add_member()** (7 connections) — `server/game/party_service.py`
- **.decline_party_invite()** (7 connections) — `server/game/party_service.py`
- **._expire_pending_invites()** (7 connections) — `server/game/party_service.py`
- **.request_party_invite()** (7 connections) — `server/game/party_service.py`
- **.on_player_disconnect()** (6 connections) — `server/game/party_service.py`
- **.is_in_same_party()** (5 connections) — `server/game/party_service.py`
- **.is_leader()** (5 connections) — `server/game/party_service.py`
- **.get_party_members()** (4 connections) — `server/game/party_service.py`
- **test_str_id_accepts_uuid()** (3 connections) — `server/tests/unit/game/test_follow_service.py`
- **Add a player to a party. Fails if party does not exist or player is already in…** (1 connections) — `server/game/party_service.py`
- **Remove expired pending invites and notify inviters.** (1 connections) — `server/game/party_service.py`
- **Send a command_response-style message to a single player.** (1 connections) — `server/game/party_service.py`
- **Create a pending party invite and send party_invite event to target. Target…** (1 connections) — `server/game/party_service.py`
- **Normalize ID to string for dict keys and membership sets.** (1 connections) — `server/game/party_service.py`
- **Accept a party invite. Target is the player who accepted (the invitee).** (1 connections) — `server/game/party_service.py`
- **Decline a party invite.** (1 connections) — `server/game/party_service.py`
- **Return the party the player is in, or None.** (1 connections) — `server/game/party_service.py`
- **Return True if the player is the leader of their current party.** (1 connections) — `server/game/party_service.py`
- **Return list of party member IDs for the given player (including themselves).…** (1 connections) — `server/game/party_service.py`
- **Return True if both players are in the same party. For combat/validator hook:…** (1 connections) — `server/game/party_service.py`
- *... and 2 more nodes in this community*

## Relationships

- [PartyService](PartyService.md) (14 shared connections)
- [Any](Any.md) (13 shared connections)
- [Party](Party.md) (3 shared connections)
- [magic_service.py](magic_service.py.md) (1 shared connections)
- [test_follow_service.py](test_follow_service.py.md) (1 shared connections)

## Source Files

- `server/game/party_service.py`
- `server/tests/unit/game/test_follow_service.py`

## Audit Trail

- EXTRACTED: 75 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*