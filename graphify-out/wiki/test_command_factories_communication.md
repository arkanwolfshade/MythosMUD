# test command factories communication

> 6 nodes

## Key Concepts

- **factory()** (7 connections) — `server/tests/unit/utils/test_command_factories.py`
- **async_session_factory()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **lucidity_service_factory()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **Create an async session factory.** (1 connections) — `server/tests/unit/services/test_rescue_service.py`
- **Create a lucidity service factory.** (1 connections) — `server/tests/unit/services/test_rescue_service.py`
- **Create a CommandFactory instance.** (1 connections) — `server/tests/unit/utils/test_command_factories.py`

## Relationships

- [main()](main%28%29.md) (2 shared connections)
- [world](world.md) (1 shared connections)
- [bench cache npc](bench_cache_npc.md) (1 shared connections)
- [test command factories](test_command_factories.md) (1 shared connections)
- [Spell Targeting](Spell_Targeting.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_rescue_service.py`
- `server/tests/unit/utils/test_command_factories.py`

## Audit Trail

- EXTRACTED: 10 (62%)
- INFERRED: 6 (38%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*