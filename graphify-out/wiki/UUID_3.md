# UUID

> 15 nodes · cohesion 0.21

## Key Concepts

- **UUID** (17 connections)
- **_str_id()** (16 connections) — `server/game/party_service.py`
- **.get_party_for_player()** (8 connections) — `server/game/party_service.py`
- **.add_member()** (7 connections) — `server/game/party_service.py`
- **.on_player_disconnect()** (6 connections) — `server/game/party_service.py`
- **.is_in_same_party()** (5 connections) — `server/game/party_service.py`
- **.is_leader()** (5 connections) — `server/game/party_service.py`
- **.get_party_members()** (4 connections) — `server/game/party_service.py`
- **Add a player to a party. Fails if party does not exist or player is already in a** (1 connections) — `server/game/party_service.py`
- **Normalize ID to string for dict keys and membership sets.** (1 connections) — `server/game/party_service.py`
- **Return the party the player is in, or None.** (1 connections) — `server/game/party_service.py`
- **Return True if the player is the leader of their current party.** (1 connections) — `server/game/party_service.py`
- **Return list of party member IDs for the given player (including themselves).** (1 connections) — `server/game/party_service.py`
- **Return True if both players are in the same party. For combat/validator hook:** (1 connections) — `server/game/party_service.py`
- **Remove player from any party and disband if they were leader.         Cancel any** (1 connections) — `server/game/party_service.py`

## Relationships

- [PartyService](PartyService.md) (16 shared connections)
- [Any](Any.md) (12 shared connections)
- [get_logger](get_logger.md) (3 shared connections)

## Source Files

- `server/game/party_service.py`

## Audit Trail

- EXTRACTED: 75 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*