# Test despawn npc handles NPC

> 34 nodes

## Key Concepts

- **NPCCombatLifecycle** (15 connections) — `server/services/npc_combat_lifecycle.py`
- **TestNPCCombatLifecycle** (12 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **._init_npc_submodules()** (9 connections) — `server/services/npc_combat_integration_service.py`
- **._despawn_npc()** (4 connections) — `server/services/npc_combat_lifecycle.py`
- **test_npc_combat_lifecycle.py** (4 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.__init__()** (3 connections) — `server/services/npc_combat_lifecycle.py`
- **.despawn_npc_safely()** (3 connections) — `server/services/npc_combat_lifecycle.py`
- **.get_npc_lifecycle_manager()** (3 connections) — `server/services/player_combat_service_support.py`
- **.lifecycle_service()** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_init()** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.mock_persistence()** (2 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_safely_success()** (2 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_safely_no_lifecycle_manager()** (2 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_safely_exception()** (2 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_safely_sqlalchemy_error()** (2 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_with_active_npcs()** (2 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_no_active_npcs()** (2 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **Any** (1 connections)
- **Manages NPC lifecycle operations during combat.** (1 connections) — `server/services/npc_combat_lifecycle.py`
- **Initialize the lifecycle manager.          Args:             async_persistence:** (1 connections) — `server/services/npc_combat_lifecycle.py`
- **Despawn NPC with defensive error handling.          Args:             npc_id: ID** (1 connections) — `server/services/npc_combat_lifecycle.py`
- **Despawn an NPC.          Args:             npc_id: ID of the NPC to despawn** (1 connections) — `server/services/npc_combat_lifecycle.py`
- **Return lifecycle manager (sync); may be wrapped by asyncio.to_thread.** (1 connections) — `server/services/player_combat_service_support.py`
- **Unit tests for NPC combat lifecycle.  Tests the NPCCombatLifecycle class for man** (1 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **Test suite for NPCCombatLifecycle class.** (1 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- *... and 9 more nodes in this community*

## Relationships

- [combat](combat.md) (3 shared connections)
- [world](world.md) (3 shared connections)
- [get health service()](get_health_service%28%29.md) (2 shared connections)
- [src/**/*.spec](src-__-_.spec.md) (2 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (1 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)
- [communication commands support](communication_commands_support.md) (1 shared connections)
- [look container](look_container.md) (1 shared connections)
- [Path](Path.md) (1 shared connections)
- [parse jsonb column()](parse_jsonb_column%28%29.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_lifecycle.py`
- `server/services/player_combat_service_support.py`
- `server/tests/unit/services/test_npc_combat_lifecycle.py`

## Audit Trail

- EXTRACTED: 84 (93%)
- INFERRED: 6 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*