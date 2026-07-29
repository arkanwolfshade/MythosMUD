# NPCLifecycleManager

> 10 nodes

## Key Concepts

- **initialize_npc_instance_service()** (14 connections) — `server/services/npc_instance_service.py`
- **.__init__()** (6 connections) — `server/services/npc_instance_service.py`
- **test_initialize_npc_instance_service()** (4 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **NPCLifecycleManager** (2 connections)
- **NPCSpawningService** (2 connections)
- **NPCPopulationController** (2 connections)
- **EventBus** (2 connections)
- **Initialize the NPC instance service.          Args:             lifecycle_manage** (1 connections) — `server/services/npc_instance_service.py`
- **Initialize the global NPC instance service.** (1 connections) — `server/services/npc_instance_service.py`
- **Test initialize_npc_instance_service() initializes service.** (1 connections) — `server/tests/unit/services/test_npc_instance_service.py`

## Relationships

- [.initialize()](initialize%28%29.md) (4 shared connections)
- [NPCInstanceService](NPCInstanceService.md) (2 shared connections)
- [test npc instance service](test_npc_instance_service.md) (2 shared connections)
- [create npc services on app()](create_npc_services_on_app%28%29.md) (1 shared connections)
- [AbstractContextManager](AbstractContextManager.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)

## Source Files

- `server/services/npc_instance_service.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 35 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*