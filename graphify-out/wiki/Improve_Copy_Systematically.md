# Improve Copy Systematically

> 15 nodes · cohesion 0.13

## Key Concepts

- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **npc_service()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **fixture** (4 connections)
- **test_npc_service_init()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **mock_session()** (3 connections) — `server/tests/unit/services/test_npc_service.py`
- **sample_npc_definition()** (3 connections) — `server/tests/unit/services/test_npc_service.py`
- **sample_spawn_rule()** (3 connections) — `server/tests/unit/services/test_npc_service.py`
- **.__init__()** (2 connections) — `server/services/npc_service/__init__.py`
- **Comprehensive NPC management service. Handles CRUD operations for NPC…** (1 connections) — `server/services/npc_service/__init__.py`
- **Initialize the NPC service.** (1 connections) — `server/services/npc_service/__init__.py`
- **Test NPCService initialization.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Create a mock AsyncSession.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Create NPCService instance.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Create a sample NPC definition.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Create a sample spawn rule.** (1 connections) — `server/tests/unit/services/test_npc_service.py`

## Relationships

- [cross-env](cross-env.md) (6 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (2 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [ErrorType](ErrorType.md) (2 shared connections)
- [TargetMatch](TargetMatch.md) (1 shared connections)
- [fix_markdown_common_issues.py](fix_markdown_common_issues.py.md) (1 shared connections)

## Source Files

- `server/services/npc_service/__init__.py`
- `server/tests/unit/services/test_npc_service.py`

## Audit Trail

- EXTRACTED: 30 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*