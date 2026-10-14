# NPCService

> 8 nodes

## Key Concepts

- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **.initialize()** (6 connections) — `server/container/bundles/npc.py`
- **._load_npc_definitions()** (4 connections) — `server/container/bundles/npc.py`
- **._start_npc_threads()** (2 connections) — `server/container/bundles/npc.py`
- **.__init__()** (2 connections) — `server/services/npc_service/__init__.py`
- **Initialize NPC services and load definitions.** (1 connections) — `server/container/bundles/npc.py`
- **Comprehensive NPC management service. Handles CRUD operations for NPC…** (1 connections) — `server/services/npc_service/__init__.py`
- **Initialize the NPC service.** (1 connections) — `server/services/npc_service/__init__.py`

## Relationships

- [test_npc_service.py](test_npc_service.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (2 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [NPCDefinitionCRUDMixin](NPCDefinitionCRUDMixin.md) (1 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (1 shared connections)
- [NPCPopulationController](NPCPopulationController.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [npc_database.py](npc_database.py.md) (1 shared connections)

## Source Files

- `server/container/bundles/npc.py`
- `server/services/npc_service/__init__.py`

## Audit Trail

- EXTRACTED: 24 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*