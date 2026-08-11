# Combat DP Persistence Tests

> 28 nodes

## Key Concepts

- **UUID** (17 connections)
- **_str_id()** (16 connections) — `server/game/party_service.py`
- **Any** (10 connections)
- **._emit_party_updated()** (9 connections) — `server/game/party_service.py`
- **.disband_party()** (8 connections) — `server/game/party_service.py`
- **._send_result_to_player()** (8 connections) — `server/game/party_service.py`
- **.accept_party_invite()** (8 connections) — `server/game/party_service.py`
- **.remove_member()** (8 connections) — `server/game/party_service.py`
- **.kick_member()** (8 connections) — `server/game/party_service.py`
- **.create_party()** (7 connections) — `server/game/party_service.py`
- **.add_member()** (7 connections) — `server/game/party_service.py`
- **._notify_player_removed_from_party()** (7 connections) — `server/game/party_service.py`
- **.decline_party_invite()** (7 connections) — `server/game/party_service.py`
- **._schedule_notification()** (6 connections) — `server/game/party_service.py`
- **.on_player_disconnect()** (6 connections) — `server/game/party_service.py`
- **Normalize ID to string for dict keys and membership sets.** (1 connections) — `server/game/party_service.py`
- **Emit PartyUpdated event if event_bus is set.** (1 connections) — `server/game/party_service.py`
- **Create a new party with the given player as leader.          Returns dict with s** (1 connections) — `server/game/party_service.py`
- **Disband a party. If by_player_id is given, only the leader may disband.** (1 connections) — `server/game/party_service.py`
- **Add a player to a party. Fails if party does not exist or player is already in a** (1 connections) — `server/game/party_service.py`
- **Send a command_response-style message to a single player.** (1 connections) — `server/game/party_service.py`
- **Safely schedule an async notification, handling cases where no event loop is run** (1 connections) — `server/game/party_service.py`
- **Notify a player they have been removed from a party. Resolves leader name.** (1 connections) — `server/game/party_service.py`
- **Accept a party invite. Target is the player who accepted (the invitee).** (1 connections) — `server/game/party_service.py`
- **Decline a party invite.** (1 connections) — `server/game/party_service.py`
- *... and 3 more nodes in this community*

## Relationships

- [Commands Npc Admin](Commands_Npc_Admin.md) (19 shared connections)
- [Invite Generate Invites](Invite_Generate_Invites.md) (8 shared connections)
- [Client Event Store](Client_Event_Store.md) (5 shared connections)
- [Combat Turn Processor](Combat_Turn_Processor.md) (1 shared connections)

## Source Files

- `server/game/party_service.py`

## Audit Trail

- EXTRACTED: 145 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*