# _str_id

> 33 nodes

## Key Concepts

- **_str_id()** (16 connections) — `server/game/party_service.py`
- **UUID** (15 connections)
- **Any** (10 connections)
- **._emit_party_updated()** (9 connections) — `server/game/party_service.py`
- **.disband_party()** (8 connections) — `server/game/party_service.py`
- **.get_party_for_player()** (8 connections) — `server/game/party_service.py`
- **.kick_member()** (8 connections) — `server/game/party_service.py`
- **.remove_member()** (8 connections) — `server/game/party_service.py`
- **.add_member()** (7 connections) — `server/game/party_service.py`
- **.create_party()** (7 connections) — `server/game/party_service.py`
- **.__init__()** (6 connections) — `server/game/party_service.py`
- **._notify_player_removed_from_party()** (6 connections) — `server/game/party_service.py`
- **.on_player_disconnect()** (6 connections) — `server/game/party_service.py`
- **._schedule_notification()** (6 connections) — `server/game/party_service.py`
- **.is_in_same_party()** (5 connections) — `server/game/party_service.py`
- **.is_leader()** (5 connections) — `server/game/party_service.py`
- **.get_party_members()** (4 connections) — `server/game/party_service.py`
- **ConnectionManager** (1 connections)
- **Create a new party with the given player as leader. Returns dict with success…** (1 connections) — `server/game/party_service.py`
- **Disband a party. If by_player_id is given, only the leader may disband. If…** (1 connections) — `server/game/party_service.py`
- **Add a player to a party. Fails if party does not exist or player is already in…** (1 connections) — `server/game/party_service.py`
- **Safely schedule an async notification, handling cases where no event loop is…** (1 connections) — `server/game/party_service.py`
- **Notify a player they have been removed from a party. Resolves leader name.** (1 connections) — `server/game/party_service.py`
- **Normalize ID to string for dict keys and membership sets.** (1 connections) — `server/game/party_service.py`
- **Remove a player from a party (leave or internal remove). If leader leaves,…** (1 connections) — `server/game/party_service.py`
- *... and 8 more nodes in this community*

## Relationships

- [PartyService](PartyService.md) (17 shared connections)
- [.accept_party_invite](accept_party_invite.md) (13 shared connections)
- [Party](Party.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)

## Source Files

- `server/game/party_service.py`

## Audit Trail

- EXTRACTED: 92 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*