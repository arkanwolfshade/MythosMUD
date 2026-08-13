# fixture

> 24 nodes

## Key Concepts

- **fixture** (10 connections)
- **factory()** (8 connections) — `server/tests/unit/utils/test_command_factories.py`
- **async_session_factory()** (4 connections) — `server/tests/unit/services/test_rescue_service.py`
- **lucidity_service_factory()** (4 connections) — `server/tests/unit/services/test_rescue_service.py`
- **rescue_service()** (4 connections) — `server/tests/unit/services/test_rescue_service.py`
- **mock_event_dispatcher()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **mock_lucidity_service()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **mock_persistence()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **mock_session()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **sample_lucidity_record()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **sample_rescuer()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **sample_target()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **fixture** (1 connections)
- **Create a mock persistence layer.** (1 connections) — `server/tests/unit/services/test_rescue_service.py`
- **Create a mock async session.** (1 connections) — `server/tests/unit/services/test_rescue_service.py`
- **Create an async session factory.** (1 connections) — `server/tests/unit/services/test_rescue_service.py`
- **Create a mock lucidity service.** (1 connections) — `server/tests/unit/services/test_rescue_service.py`
- **Create a lucidity service factory.** (1 connections) — `server/tests/unit/services/test_rescue_service.py`
- **Create a mock event dispatcher.** (1 connections) — `server/tests/unit/services/test_rescue_service.py`
- **Create a RescueService instance.** (1 connections) — `server/tests/unit/services/test_rescue_service.py`
- **Create a sample rescuer player.** (1 connections) — `server/tests/unit/services/test_rescue_service.py`
- **Create a sample target player.** (1 connections) — `server/tests/unit/services/test_rescue_service.py`
- **Create a sample lucidity record.** (1 connections) — `server/tests/unit/services/test_rescue_service.py`
- **Create a CommandFactory instance.** (1 connections) — `server/tests/unit/utils/test_command_factories.py`

## Relationships

- [test_rescue_service.py](test_rescue_service.py.md) (10 shared connections)
- [rescue_service.py](rescue_service.py.md) (1 shared connections)
- [CommandFactory](CommandFactory.md) (1 shared connections)
- [test_command_factories.py](test_command_factories.py.md) (1 shared connections)
- [LRUCache](LRUCache.md) (1 shared connections)
- [test_quest_instance_repository.py](test_quest_instance_repository.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_rescue_service.py`
- `server/tests/unit/utils/test_command_factories.py`

## Audit Trail

- EXTRACTED: 35 (90%)
- INFERRED: 4 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*