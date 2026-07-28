# Message Broadcaster Core

> 18 nodes · cohesion 0.16

## Key Concepts

- **PartyService** (35 connections) — `server/game/party_service.py`
- **.accept_party_invite()** (8 connections) — `server/game/party_service.py`
- **._send_result_to_player()** (8 connections) — `server/game/party_service.py`
- **.decline_party_invite()** (7 connections) — `server/game/party_service.py`
- **._expire_pending_invites()** (7 connections) — `server/game/party_service.py`
- **.request_party_invite()** (7 connections) — `server/game/party_service.py`
- **._send_party_invite_to_target()** (5 connections) — `server/game/party_service.py`
- **.get_party()** (3 connections) — `server/game/party_service.py`
- **party_service()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **Remove expired pending invites and notify inviters.** (1 connections) — `server/game/party_service.py`
- **Send a command_response-style message to a single player.** (1 connections) — `server/game/party_service.py`
- **Send party_invite event to the target player only.** (1 connections) — `server/game/party_service.py`
- **Create a pending party invite and send party_invite event to target.         Tar** (1 connections) — `server/game/party_service.py`
- **Accept a party invite. Target is the player who accepted (the invitee).** (1 connections) — `server/game/party_service.py`
- **Decline a party invite.** (1 connections) — `server/game/party_service.py`
- **Return the party by id, or None.** (1 connections) — `server/game/party_service.py`
- **In-memory party management: create, disband, add/remove/kick members, leader che** (1 connections) — `server/game/party_service.py`
- **PartyService with no dependencies (in-memory only).** (1 connections) — `server/tests/unit/game/test_party_service.py`

## Relationships

- [Party Service Management](Party_Service_Management.md) (16 shared connections)
- [Realtime Conftest Mocks](Realtime_Conftest_Mocks.md) (11 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (9 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (3 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (2 shared connections)
- [Container Persistence Layer](Container_Persistence_Layer.md) (2 shared connections)
- [NPC Combat Handler Tests](NPC_Combat_Handler_Tests.md) (1 shared connections)

## Source Files

- `server/game/party_service.py`
- `server/tests/unit/game/test_party_service.py`

## Audit Trail

- EXTRACTED: 88 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*