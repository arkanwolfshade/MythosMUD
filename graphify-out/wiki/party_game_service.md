# party game service

> 21 nodes

## Key Concepts

- **UUID** (17 connections)
- **_str_id()** (16 connections) — `server/game/party_service.py`
- **._send_result_to_player()** (8 connections) — `server/game/party_service.py`
- **.accept_party_invite()** (8 connections) — `server/game/party_service.py`
- **.create_party()** (7 connections) — `server/game/party_service.py`
- **.add_member()** (7 connections) — `server/game/party_service.py`
- **._expire_pending_invites()** (7 connections) — `server/game/party_service.py`
- **.request_party_invite()** (7 connections) — `server/game/party_service.py`
- **.decline_party_invite()** (7 connections) — `server/game/party_service.py`
- **.on_player_disconnect()** (6 connections) — `server/game/party_service.py`
- **._send_party_invite_to_target()** (5 connections) — `server/game/party_service.py`
- **Normalize ID to string for dict keys and membership sets.** (1 connections) — `server/game/party_service.py`
- **Create a new party with the given player as leader.          Returns dict with s** (1 connections) — `server/game/party_service.py`
- **Add a player to a party. Fails if party does not exist or player is already in a** (1 connections) — `server/game/party_service.py`
- **Remove expired pending invites and notify inviters.** (1 connections) — `server/game/party_service.py`
- **Send a command_response-style message to a single player.** (1 connections) — `server/game/party_service.py`
- **Send party_invite event to the target player only.** (1 connections) — `server/game/party_service.py`
- **Create a pending party invite and send party_invite event to target.         Tar** (1 connections) — `server/game/party_service.py`
- **Accept a party invite. Target is the player who accepted (the invitee).** (1 connections) — `server/game/party_service.py`
- **Decline a party invite.** (1 connections) — `server/game/party_service.py`
- **Remove player from any party and disband if they were leader.         Cancel any** (1 connections) — `server/game/party_service.py`

## Relationships

- [player requests schemas](player_requests_schemas.md) (16 shared connections)
- [skill game service](skill_game_service.md) (16 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)
- [lucidity npc combat](lucidity_npc_combat.md) (1 shared connections)
- [combat services messaging](combat_services_messaging.md) (1 shared connections)

## Source Files

- `server/game/party_service.py`

## Audit Trail

- EXTRACTED: 105 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*