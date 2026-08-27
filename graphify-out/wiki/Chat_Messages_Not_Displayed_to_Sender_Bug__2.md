# Chat Messages Not Displayed to Sender (Bug #2)

> 3 nodes

## Key Concepts

- **.__init__()** (6 connections) — `server/game/party_service.py`
- **ConnectionManager** (1 connections)
- **Initialize empty party store. Optionally provide event_bus, connection_manager,…** (1 connections) — `server/game/party_service.py`

## Relationships

- [WebSocket Best Practices](WebSocket_Best_Practices.md) (2 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (1 shared connections)

## Source Files

- `server/game/party_service.py`

## Audit Trail

- EXTRACTED: 6 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*