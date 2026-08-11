# Commands Npc Admin

> 12 nodes

## Key Concepts

- **PartyService** (35 connections) — `server/game/party_service.py`
- **.get_party_for_player()** (8 connections) — `server/game/party_service.py`
- **.is_leader()** (5 connections) — `server/game/party_service.py`
- **.is_in_same_party()** (5 connections) — `server/game/party_service.py`
- **.get_party_members()** (4 connections) — `server/game/party_service.py`
- **party_service()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **In-memory party management: create, disband, add/remove/kick members, leader che** (1 connections) — `server/game/party_service.py`
- **Return the party the player is in, or None.** (1 connections) — `server/game/party_service.py`
- **Return True if the player is the leader of their current party.** (1 connections) — `server/game/party_service.py`
- **Return list of party member IDs for the given player (including themselves).** (1 connections) — `server/game/party_service.py`
- **Return True if both players are in the same party. For combat/validator hook:** (1 connections) — `server/game/party_service.py`
- **PartyService with no dependencies (in-memory only).** (1 connections) — `server/tests/unit/game/test_party_service.py`

## Relationships

- [Combat DP Persistence Tests](Combat_DP_Persistence_Tests.md) (19 shared connections)
- [Client Event Store](Client_Event_Store.md) (9 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (3 shared connections)
- [Invite Generate Invites](Invite_Generate_Invites.md) (3 shared connections)
- [Command Alias Model](Command_Alias_Model.md) (2 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (1 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (1 shared connections)

## Source Files

- `server/game/party_service.py`
- `server/tests/unit/game/test_party_service.py`

## Audit Trail

- EXTRACTED: 62 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*