# player persistence repository

> 2 nodes

## Key Concepts

- **test_broadcast_combat_start()** (3 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **Test broadcast_combat_start broadcasts combat start event.** (1 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`

## Relationships

- [NATS Messaging](NATS_Messaging.md) (1 shared connections)
- [combat messaging services](combat_messaging_services.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_combat_messaging_integration.py`

## Audit Trail

- EXTRACTED: 4 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*