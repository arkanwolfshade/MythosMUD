# _str_id

> 17 nodes

## Key Concepts

- **_str_id()** (16 connections) — `server/game/party_service.py`
- **UUID** (15 connections)
- **.get_party_for_player()** (8 connections) — `server/game/party_service.py`
- **.remove_member()** (8 connections) — `server/game/party_service.py`
- **.create_party()** (7 connections) — `server/game/party_service.py`
- **.on_player_disconnect()** (6 connections) — `server/game/party_service.py`
- **.is_in_same_party()** (5 connections) — `server/game/party_service.py`
- **.is_leader()** (5 connections) — `server/game/party_service.py`
- **.get_party_members()** (4 connections) — `server/game/party_service.py`
- **Create a new party with the given player as leader. Returns dict with success…** (1 connections) — `server/game/party_service.py`
- **Normalize ID to string for dict keys and membership sets.** (1 connections) — `server/game/party_service.py`
- **Remove a player from a party (leave or internal remove). If leader leaves,…** (1 connections) — `server/game/party_service.py`
- **Return the party the player is in, or None.** (1 connections) — `server/game/party_service.py`
- **Return True if the player is the leader of their current party.** (1 connections) — `server/game/party_service.py`
- **Return list of party member IDs for the given player (including themselves).…** (1 connections) — `server/game/party_service.py`
- **Return True if both players are in the same party. For combat/validator hook:…** (1 connections) — `server/game/party_service.py`
- **Remove player from any party and disband if they were leader. Cancel any…** (1 connections) — `server/game/party_service.py`

## Relationships

- [Any](Any.md) (13 shared connections)
- [PartyService](PartyService.md) (9 shared connections)
- [.accept_party_invite](accept_party_invite.md) (8 shared connections)
- [Party](Party.md) (2 shared connections)

## Source Files

- `server/game/party_service.py`

## Audit Trail

- EXTRACTED: 57 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*