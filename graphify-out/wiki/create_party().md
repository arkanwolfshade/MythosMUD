# .create party()

> 17 nodes

## Key Concepts

- **Any** (10 connections)
- **._emit_party_updated()** (9 connections) — `server/game/party_service.py`
- **.disband_party()** (8 connections) — `server/game/party_service.py`
- **.remove_member()** (8 connections) — `server/game/party_service.py`
- **.kick_member()** (8 connections) — `server/game/party_service.py`
- **.create_party()** (7 connections) — `server/game/party_service.py`
- **._notify_player_removed_from_party()** (7 connections) — `server/game/party_service.py`
- **.__init__()** (6 connections) — `server/game/party_service.py`
- **._schedule_notification()** (6 connections) — `server/game/party_service.py`
- **Initialize empty party store. Optionally provide event_bus, connection_manager,** (1 connections) — `server/game/party_service.py`
- **Emit PartyUpdated event if event_bus is set.** (1 connections) — `server/game/party_service.py`
- **Create a new party with the given player as leader.          Returns dict with s** (1 connections) — `server/game/party_service.py`
- **Disband a party. If by_player_id is given, only the leader may disband.** (1 connections) — `server/game/party_service.py`
- **Safely schedule an async notification, handling cases where no event loop is run** (1 connections) — `server/game/party_service.py`
- **Notify a player they have been removed from a party. Resolves leader name.** (1 connections) — `server/game/party_service.py`
- **Remove a player from a party (leave or internal remove). If leader leaves,** (1 connections) — `server/game/party_service.py`
- **Remove a member from the party. Only the leader may kick.** (1 connections) — `server/game/party_service.py`

## Relationships

- [PartyService](PartyService.md) (24 shared connections)
- [.initialize()](initialize%28%29.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)
- [main()](main%28%29.md) (1 shared connections)
- [PartyUpdated](PartyUpdated.md) (1 shared connections)
- [Party](Party.md) (1 shared connections)

## Source Files

- `server/game/party_service.py`

## Audit Trail

- EXTRACTED: 77 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*