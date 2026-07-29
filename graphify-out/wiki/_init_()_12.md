# . init ()

> 16 nodes

## Key Concepts

- **QuestInstanceRepository** (19 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **QuestDefinitionRepository** (17 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **test_quest_flow.py** (15 connections) — `server/tests/integration/test_quest_flow.py`
- **test_quest_start_log_abandon_flow()** (7 connections) — `server/tests/integration/test_quest_flow.py`
- **test_quest_start_by_trigger_then_abandon()** (7 connections) — `server/tests/integration/test_quest_flow.py`
- **_make_shared_session_factory()** (5 connections) — `server/tests/integration/test_quest_flow.py`
- **quest_instance_repository()** (3 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **.__init__()** (2 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **.__init__()** (2 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **Repository for quest_definitions and quest_offers (read-only for offers).** (1 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **Repository for quest_instances table.** (1 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **Integration tests for quest subsystem: start, quest log, abandon flow.  Uses rea** (1 connections) — `server/tests/integration/test_quest_flow.py`
- **Return a callable that behaves like a session maker but always yields the same** (1 connections) — `server/tests/integration/test_quest_flow.py`
- **Integration: start leave_the_tutorial, get_quest_log shows it, abandon, log empt** (1 connections) — `server/tests/integration/test_quest_flow.py`
- **Start quest via start_quest_by_trigger(room), then abandon.     Verifies trigger** (1 connections) — `server/tests/integration/test_quest_flow.py`
- **Create a QuestInstanceRepository instance.** (1 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`

## Relationships

- [main()](main%28%29.md) (18 shared connections)
- [Any](Any.md) (6 shared connections)
- [Base](Base.md) (4 shared connections)
- [QuestCompleted](QuestCompleted.md) (4 shared connections)
- [test quest definition repository](test_quest_definition_repository.md) (2 shared connections)
- [test quest instance repository](test_quest_instance_repository.md) (2 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)
- [async sessionmaker](async_sessionmaker.md) (2 shared connections)
- [APIRouter](APIRouter.md) (1 shared connections)
- [AsyncSessionFactory](AsyncSessionFactory.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/quest_definition_repository.py`
- `server/persistence/repositories/quest_instance_repository.py`
- `server/tests/integration/test_quest_flow.py`
- `server/tests/unit/persistence/test_quest_instance_repository.py`

## Audit Trail

- EXTRACTED: 75 (89%)
- INFERRED: 9 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*