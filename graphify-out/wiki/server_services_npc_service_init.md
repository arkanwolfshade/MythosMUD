# server services npc service init

> 15 nodes

## Key Concepts

- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
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

- [server tests unit services test](server_tests_unit_services_test.md) (7 shared connections)
- [draft7validator](draft7validator.md) (4 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (2 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (2 shared connections)
- [abstractcontextmanager](abstractcontextmanager.md) (1 shared connections)

## Source Files

- `server/services/npc_service/__init__.py`
- `server/tests/unit/services/test_npc_service.py`

## Audit Trail

- EXTRACTED: 27 (90%)
- INFERRED: 3 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*