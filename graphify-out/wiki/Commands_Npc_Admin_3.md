# Commands Npc Admin

> 17 nodes

## Key Concepts

- **UUID** (17 connections)
- **_str_id()** (16 connections) — `server/game/party_service.py`
- **.get_party_for_player()** (8 connections) — `server/game/party_service.py`
- **.request_party_invite()** (7 connections) — `server/game/party_service.py`
- **.on_player_disconnect()** (6 connections) — `server/game/party_service.py`
- **._send_party_invite_to_target()** (5 connections) — `server/game/party_service.py`
- **.is_leader()** (5 connections) — `server/game/party_service.py`
- **.is_in_same_party()** (5 connections) — `server/game/party_service.py`
- **.get_party_members()** (4 connections) — `server/game/party_service.py`
- **Normalize ID to string for dict keys and membership sets.** (1 connections) — `server/game/party_service.py`
- **Send party_invite event to the target player only.** (1 connections) — `server/game/party_service.py`
- **Create a pending party invite and send party_invite event to target.         Tar** (1 connections) — `server/game/party_service.py`
- **Return the party the player is in, or None.** (1 connections) — `server/game/party_service.py`
- **Return True if the player is the leader of their current party.** (1 connections) — `server/game/party_service.py`
- **Return list of party member IDs for the given player (including themselves).** (1 connections) — `server/game/party_service.py`
- **Return True if both players are in the same party. For combat/validator hook:** (1 connections) — `server/game/party_service.py`
- **Remove player from any party and disband if they were leader.         Cancel any** (1 connections) — `server/game/party_service.py`

## Relationships

- [Combat DP Persistence Tests](Combat_DP_Persistence_Tests.md) (20 shared connections)
- [Invite Generate Invites](Invite_Generate_Invites.md) (7 shared connections)
- [Realtime Conftest Mocks](Realtime_Conftest_Mocks.md) (3 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)

## Source Files

- `server/game/party_service.py`

## Audit Trail

- EXTRACTED: 81 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*