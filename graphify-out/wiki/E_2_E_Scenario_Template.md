# E 2 E Scenario Template

> 2 nodes

## Key Concepts

- **test_subscribe_to_subject_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **Test _subscribe_to_subject() raises error on failure.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`

## Relationships

- [Inventory Command Models](Inventory_Command_Models.md) (1 shared connections)
- [SQLAlchemy Model Base](SQLAlchemy_Model_Base.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_message_handler.py`

## Audit Trail

- EXTRACTED: 3 (75%)
- INFERRED: 1 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*