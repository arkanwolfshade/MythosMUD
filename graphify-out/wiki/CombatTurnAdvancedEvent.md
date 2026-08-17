# CombatTurnAdvancedEvent

> 4 nodes

## Key Concepts

- **CombatTurnAdvancedEvent** (8 connections) — `server/events/combat_events.py`
- **test_publish_combat_turn_advanced_success()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Event fired when combat turn advances.** (1 connections) — `server/events/combat_events.py`
- **Test publish_combat_turn_advanced() successfully publishes.** (1 connections) — `server/tests/unit/services/test_combat_event_publisher.py`

## Relationships

- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (3 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [CombatEventPublisher](CombatEventPublisher.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [asyncio](asyncio.md) (1 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 8 (73%)
- INFERRED: 3 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*