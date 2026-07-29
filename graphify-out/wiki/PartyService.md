# PartyService

> 29 nodes

## Key Concepts

- **PartyService** (35 connections) — `server/game/party_service.py`
- **UUID** (17 connections)
- **_str_id()** (16 connections) — `server/game/party_service.py`
- **._send_result_to_player()** (8 connections) — `server/game/party_service.py`
- **.accept_party_invite()** (8 connections) — `server/game/party_service.py`
- **.get_party_for_player()** (8 connections) — `server/game/party_service.py`
- **.add_member()** (7 connections) — `server/game/party_service.py`
- **._expire_pending_invites()** (7 connections) — `server/game/party_service.py`
- **.request_party_invite()** (7 connections) — `server/game/party_service.py`
- **.decline_party_invite()** (7 connections) — `server/game/party_service.py`
- **.on_player_disconnect()** (6 connections) — `server/game/party_service.py`
- **._send_party_invite_to_target()** (5 connections) — `server/game/party_service.py`
- **.is_leader()** (5 connections) — `server/game/party_service.py`
- **.is_in_same_party()** (5 connections) — `server/game/party_service.py`
- **.get_party_members()** (4 connections) — `server/game/party_service.py`
- **Normalize ID to string for dict keys and membership sets.** (1 connections) — `server/game/party_service.py`
- **In-memory party management: create, disband, add/remove/kick members, leader che** (1 connections) — `server/game/party_service.py`
- **Add a player to a party. Fails if party does not exist or player is already in a** (1 connections) — `server/game/party_service.py`
- **Remove expired pending invites and notify inviters.** (1 connections) — `server/game/party_service.py`
- **Send a command_response-style message to a single player.** (1 connections) — `server/game/party_service.py`
- **Send party_invite event to the target player only.** (1 connections) — `server/game/party_service.py`
- **Create a pending party invite and send party_invite event to target.         Tar** (1 connections) — `server/game/party_service.py`
- **Accept a party invite. Target is the player who accepted (the invitee).** (1 connections) — `server/game/party_service.py`
- **Decline a party invite.** (1 connections) — `server/game/party_service.py`
- **Return the party the player is in, or None.** (1 connections) — `server/game/party_service.py`
- *... and 4 more nodes in this community*

## Relationships

- [.create party()](create_party%28%29.md) (24 shared connections)
- [PartyUpdated](PartyUpdated.md) (8 shared connections)
- [Any](Any.md) (3 shared connections)
- [Party](Party.md) (2 shared connections)
- [test party service](test_party_service.md) (2 shared connections)
- [UUID](UUID.md) (2 shared connections)
- [.initialize()](initialize%28%29.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)

## Source Files

- `server/game/party_service.py`

## Audit Trail

- EXTRACTED: 155 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*