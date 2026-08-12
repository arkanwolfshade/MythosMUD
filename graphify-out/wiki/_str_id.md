# _str_id

> 15 nodes

## Key Concepts

- **_str_id()** (16 connections) — `server/game/party_service.py`
- **UUID** (15 connections)
- **.get_party_for_player()** (8 connections) — `server/game/party_service.py`
- **.add_member()** (7 connections) — `server/game/party_service.py`
- **.on_player_disconnect()** (6 connections) — `server/game/party_service.py`
- **.is_in_same_party()** (5 connections) — `server/game/party_service.py`
- **.is_leader()** (5 connections) — `server/game/party_service.py`
- **.get_party_members()** (4 connections) — `server/game/party_service.py`
- **Add a player to a party. Fails if party does not exist or player is already in…** (1 connections) — `server/game/party_service.py`
- **Normalize ID to string for dict keys and membership sets.** (1 connections) — `server/game/party_service.py`
- **Return the party the player is in, or None.** (1 connections) — `server/game/party_service.py`
- **Return True if the player is the leader of their current party.** (1 connections) — `server/game/party_service.py`
- **Return list of party member IDs for the given player (including themselves).…** (1 connections) — `server/game/party_service.py`
- **Return True if both players are in the same party. For combat/validator hook:…** (1 connections) — `server/game/party_service.py`
- **Remove player from any party and disband if they were leader. Cancel any…** (1 connections) — `server/game/party_service.py`

## Relationships

- [PartyService](PartyService.md) (15 shared connections)
- [Any](Any.md) (11 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [.__post_init__](__post_init__.md) (1 shared connections)

## Source Files

- `server/game/party_service.py`

## Audit Trail

- EXTRACTED: 73 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*