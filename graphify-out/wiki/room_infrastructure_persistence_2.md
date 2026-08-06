# room infrastructure persistence

> 9 nodes

## Key Concepts

- **get_nats_message_handler()** (8 connections) — `server/dependencies.py`
- **TestGetNatsMessageHandler** (5 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_nats_message_handler_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_nats_message_handler_none_returns_none()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Any** (2 connections)
- **Get NATS message handler from container with dependency injection.      Args:** (1 connections) — `server/dependencies.py`
- **Tests for get_nats_message_handler dependency function.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_nats_message_handler returns handler when present.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_nats_message_handler returns None when handler is None (NATS disabled).** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`

## Relationships

- [NPC Definitions Admin](NPC_Definitions_Admin.md) (5 shared connections)
- [player event handlers](player_event_handlers.md) (1 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (1 shared connections)

## Source Files

- `server/dependencies.py`
- `server/tests/unit/infrastructure/test_dependencies.py`

## Audit Trail

- EXTRACTED: 23 (92%)
- INFERRED: 2 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*