# test command factories communication

> 70 nodes

## Key Concepts

- **test_rescue_service.py** (32 connections) — `server/tests/unit/services/test_rescue_service.py`
- **RescueService** (11 connections) — `server/services/rescue_service.py`
- **.rescue()** (7 connections) — `server/services/rescue_service.py`
- **factory()** (7 connections) — `server/tests/unit/utils/test_command_factories.py`
- **.__init__()** (6 connections) — `server/services/rescue_service.py`
- **_ensure_uuid()** (5 connections) — `server/services/rescue_service.py`
- **Any** (4 connections)
- **_maybe_await()** (4 connections) — `server/services/rescue_service.py`
- **async_session_factory()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **lucidity_service_factory()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **rescue_service()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_no_persistence()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **UUID** (2 connections)
- **mock_persistence()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **mock_session()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **mock_lucidity_service()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **mock_event_dispatcher()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **sample_rescuer()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **sample_target()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_rescuer_not_found()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_target_not_found()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_different_rooms()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_lucidity_record_not_found()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_not_catatonic()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_success()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- *... and 45 more nodes in this community*

## Relationships

- [LiabilityStackEntry](LiabilityStackEntry.md) (6 shared connections)
- [test rate limiter utils](test_rate_limiter_utils.md) (4 shared connections)
- [UUID](UUID.md) (2 shared connections)
- [Send a system message to](Send_a_system_message_to.md) (1 shared connections)
- [. get persistence from app()](_get_persistence_from_app%28%29.md) (1 shared connections)
- [map helpers](map_helpers.md) (1 shared connections)
- [init](init.md) (1 shared connections)
- [bench cache npc](bench_cache_npc.md) (1 shared connections)
- [test command factories](test_command_factories.md) (1 shared connections)
- [Spell Targeting](Spell_Targeting.md) (1 shared connections)

## Source Files

- `server/services/rescue_service.py`
- `server/tests/unit/services/test_rescue_service.py`
- `server/tests/unit/utils/test_command_factories.py`

## Audit Trail

- EXTRACTED: 159 (94%)
- INFERRED: 10 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*