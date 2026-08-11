# Invite Generate Invites

> 6 nodes

## Key Concepts

- **._expire_pending_invites()** (7 connections) — `server/game/party_service.py`
- **.request_party_invite()** (7 connections) — `server/game/party_service.py`
- **._send_party_invite_to_target()** (5 connections) — `server/game/party_service.py`
- **Remove expired pending invites and notify inviters.** (1 connections) — `server/game/party_service.py`
- **Send party_invite event to the target player only.** (1 connections) — `server/game/party_service.py`
- **Create a pending party invite and send party_invite event to target.         Tar** (1 connections) — `server/game/party_service.py`

## Relationships

- [Combat DP Persistence Tests](Combat_DP_Persistence_Tests.md) (8 shared connections)
- [Commands Npc Admin](Commands_Npc_Admin.md) (3 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (1 shared connections)

## Source Files

- `server/game/party_service.py`

## Audit Trail

- EXTRACTED: 22 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*