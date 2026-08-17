# NPCCombatLifecycle

> 36 nodes

## Key Concepts

- **NPCCombatLifecycle** (15 connections) — `server/services/npc_combat_lifecycle.py`
- **TestNPCCombatLifecycle** (12 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **._init_npc_submodules()** (9 connections) — `server/services/npc_combat_integration_service.py`
- **asyncio** (6 connections)
- **test_npc_combat_lifecycle.py** (5 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **._despawn_npc()** (4 connections) — `server/services/npc_combat_lifecycle.py`
- **.lifecycle_service()** (4 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.despawn_npc_safely()** (3 connections) — `server/services/npc_combat_lifecycle.py`
- **.__init__()** (3 connections) — `server/services/npc_combat_lifecycle.py`
- **.get_npc_lifecycle_manager()** (3 connections) — `server/services/player_combat_service_support.py`
- **.mock_persistence()** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_no_active_npcs()** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_safely_exception()** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_safely_no_lifecycle_manager()** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_safely_sqlalchemy_error()** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_safely_success()** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_with_active_npcs()** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_init()** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **fixture** (2 connections)
- **Any** (1 connections)
- **Manages NPC lifecycle operations during combat.** (1 connections) — `server/services/npc_combat_lifecycle.py`
- **Initialize the lifecycle manager. Args: async_persistence: Async persistence…** (1 connections) — `server/services/npc_combat_lifecycle.py`
- **Despawn NPC with defensive error handling. Args: npc_id: ID of the NPC to…** (1 connections) — `server/services/npc_combat_lifecycle.py`
- **Despawn an NPC. Args: npc_id: ID of the NPC to despawn _room_id: ID of the room…** (1 connections) — `server/services/npc_combat_lifecycle.py`
- **Return lifecycle manager (sync); may be wrapped by asyncio.to_thread.** (1 connections) — `server/services/player_combat_service_support.py`
- *... and 11 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (4 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)
- [test_npc_combat_handlers.py](test_npc_combat_handlers.py.md) (2 shared connections)
- [NPCCombatMemory](NPCCombatMemory.md) (1 shared connections)
- [NPCCombatUUIDMapping](NPCCombatUUIDMapping.md) (1 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (1 shared connections)
- [NPCCombatLucidity](NPCCombatLucidity.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_lifecycle.py`
- `server/services/player_combat_service_support.py`
- `server/tests/unit/services/test_npc_combat_lifecycle.py`

## Audit Trail

- EXTRACTED: 58 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*