# test_quest_start_by_trigger_then_abandon

> 9 nodes

## Key Concepts

- **test_quest_start_by_trigger_then_abandon()** (10 connections) — `server/tests/integration/test_quest_flow.py`
- **test_quest_start_log_abandon_flow()** (10 connections) — `server/tests/integration/test_quest_flow.py`
- **_make_shared_session_factory()** (4 connections) — `server/tests/integration/test_quest_flow.py`
- **integration** (2 connections)
- **asyncio** (2 connections)
- **serial** (2 connections)
- **Integration: start leave_the_tutorial, get_quest_log shows it, abandon, log…** (1 connections) — `server/tests/integration/test_quest_flow.py`
- **Start quest via start_quest_by_trigger(room), then abandon. Verifies trigger-…** (1 connections) — `server/tests/integration/test_quest_flow.py`
- **Return a callable that behaves like a session maker but always yields the same…** (1 connections) — `server/tests/integration/test_quest_flow.py`

## Relationships

- [get_logger](get_logger.md) (7 shared connections)
- [QuestService](QuestService.md) (2 shared connections)
- [fixtures/integration/__init__.py](fixtures-integration-__init__.py.md) (2 shared connections)

## Source Files

- `server/tests/integration/test_quest_flow.py`

## Audit Trail

- EXTRACTED: 16 (73%)
- INFERRED: 6 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*