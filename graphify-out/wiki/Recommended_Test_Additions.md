# Recommended Test Additions

> 15 nodes

## Key Concepts

- **NPCService** (10 connections) — `server/services/npc_service/__init__.py`
- **npc_service()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_npc_service_init()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **fixture** (4 connections)
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

- [item_instance_persistence_async.py](item_instance_persistence_async.py.md) (7 shared connections)
- [NPCDefinition](NPCDefinition.md) (3 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)
- [MetricsCollector](MetricsCollector.md) (1 shared connections)

## Source Files

- `server/services/npc_service/__init__.py`
- `server/tests/unit/services/test_npc_service.py`

## Audit Trail

- EXTRACTED: 26 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*