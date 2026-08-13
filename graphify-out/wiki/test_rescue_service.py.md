# test_rescue_service.py

> 83 nodes

## Key Concepts

- **test_rescue_service.py** (32 connections) — `server/tests/unit/services/test_rescue_service.py`
- **rescue_service.py** (19 connections) — `server/services/rescue_service.py`
- **asyncio** (17 connections)
- **RescueService** (12 connections) — `server/services/rescue_service.py`
- **fixture** (10 connections)
- **.rescue()** (8 connections) — `server/services/rescue_service.py`
- **factory()** (8 connections) — `server/tests/unit/utils/test_command_factories.py`
- **Any** (7 connections)
- **_load_rescue_participants()** (6 connections) — `server/services/rescue_service.py`
- **.__init__()** (6 connections) — `server/services/rescue_service.py`
- **_ensure_uuid()** (5 connections) — `server/services/rescue_service.py`
- **._apply_rescue_adjustment()** (5 connections) — `server/services/rescue_service.py`
- **_dispatch_rescue_events()** (4 connections) — `server/services/rescue_service.py`
- **_maybe_await()** (4 connections) — `server/services/rescue_service.py`
- **async_session_factory()** (4 connections) — `server/tests/unit/services/test_rescue_service.py`
- **lucidity_service_factory()** (4 connections) — `server/tests/unit/services/test_rescue_service.py`
- **rescue_service()** (4 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_no_persistence()** (4 connections) — `server/tests/unit/services/test_rescue_service.py`
- **_rescue_success_payload()** (3 connections) — `server/services/rescue_service.py`
- **mock_event_dispatcher()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **mock_lucidity_service()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **mock_persistence()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **mock_session()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **sample_lucidity_record()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **sample_rescuer()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- *... and 58 more nodes in this community*

## Relationships

- [LucidityService](LucidityService.md) (10 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (3 shared connections)
- [BaseCommand](BaseCommand.md) (2 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [test_command_factories.py](test_command_factories.py.md) (1 shared connections)
- [LRUCache](LRUCache.md) (1 shared connections)
- [test_quest_instance_repository.py](test_quest_instance_repository.py.md) (1 shared connections)

## Source Files

- `server/services/rescue_service.py`
- `server/tests/unit/services/test_rescue_service.py`
- `server/tests/unit/utils/test_command_factories.py`

## Audit Trail

- EXTRACTED: 142 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*