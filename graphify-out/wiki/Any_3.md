# Any

> 18 nodes

## Key Concepts

- **Any** (10 connections)
- **._emit_party_updated()** (9 connections) — `server/game/party_service.py`
- **.disband_party()** (8 connections) — `server/game/party_service.py`
- **.kick_member()** (8 connections) — `server/game/party_service.py`
- **.remove_member()** (8 connections) — `server/game/party_service.py`
- **.create_party()** (7 connections) — `server/game/party_service.py`
- **.__init__()** (6 connections) — `server/game/party_service.py`
- **._notify_player_removed_from_party()** (6 connections) — `server/game/party_service.py`
- **._schedule_notification()** (6 connections) — `server/game/party_service.py`
- **ConnectionManager** (1 connections)
- **Create a new party with the given player as leader. Returns dict with success…** (1 connections) — `server/game/party_service.py`
- **Disband a party. If by_player_id is given, only the leader may disband. If…** (1 connections) — `server/game/party_service.py`
- **Safely schedule an async notification, handling cases where no event loop is…** (1 connections) — `server/game/party_service.py`
- **Notify a player they have been removed from a party. Resolves leader name.** (1 connections) — `server/game/party_service.py`
- **Remove a player from a party (leave or internal remove). If leader leaves,…** (1 connections) — `server/game/party_service.py`
- **Remove a member from the party. Only the leader may kick.** (1 connections) — `server/game/party_service.py`
- **Initialize empty party store. Optionally provide event_bus, connection_manager,…** (1 connections) — `server/game/party_service.py`
- **Emit PartyUpdated event if event_bus is set.** (1 connections) — `server/game/party_service.py`

## Relationships

- [PartyService](PartyService.md) (23 shared connections)
- [Party](Party.md) (1 shared connections)
- [test_party_flow.py](test_party_flow.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)

## Source Files

- `server/game/party_service.py`

## Audit Trail

- EXTRACTED: 52 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*