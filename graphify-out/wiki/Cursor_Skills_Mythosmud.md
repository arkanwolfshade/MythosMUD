# Cursor Skills Mythosmud

> 6 nodes

## Key Concepts

- **.disconnect()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.unsubscribe()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._stop_health_monitoring()** (3 connections) — `server/infrastructure/nats_broker.py`
- **Disconnect from NATS server.** (1 connections) — `server/infrastructure/nats_broker.py`
- **Unsubscribe from NATS subject.          Args:             subscription_id: ID** (1 connections) — `server/infrastructure/nats_broker.py`
- **Stop health check monitoring task.** (1 connections) — `server/infrastructure/nats_broker.py`

## Relationships

- [Realtime Event Delegation](Realtime_Event_Delegation.md) (3 shared connections)
- [Multiplayer Browser Helpers](Multiplayer_Browser_Helpers.md) (2 shared connections)

## Source Files

- `server/infrastructure/nats_broker.py`

## Audit Trail

- EXTRACTED: 15 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*