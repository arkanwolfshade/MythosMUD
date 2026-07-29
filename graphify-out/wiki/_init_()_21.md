# . init ()

> 79 nodes

## Key Concepts

- **NPCCombatMemory** (28 connections) — `server/services/npc_combat_memory.py`
- **NPCCombatRewards** (18 connections) — `server/services/npc_combat_rewards.py`
- **NPCCombatHandlers** (16 connections) — `server/services/npc_combat_handlers.py`
- **TestNPCCombatMemory** (16 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **npc_combat_handlers.py** (15 connections) — `server/services/npc_combat_handlers.py`
- **NPCCombatLifecycle** (15 connections) — `server/services/npc_combat_lifecycle.py`
- **._init_npc_submodules()** (9 connections) — `server/services/npc_combat_integration_service.py`
- **.__init__()** (7 connections) — `server/services/npc_combat_handlers.py`
- **._handle_npc_death_on_combat_end()** (7 connections) — `server/services/npc_combat_handlers.py`
- **npc_combat_lifecycle.py** (7 connections) — `server/services/npc_combat_lifecycle.py`
- **npc_combat_memory.py** (7 connections) — `server/services/npc_combat_memory.py`
- **.check_player_connection_state()** (6 connections) — `server/services/npc_combat_rewards.py`
- **.handle_combat_result()** (4 connections) — `server/services/npc_combat_handlers.py`
- **test_npc_combat_lifecycle.py** (4 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **test_npc_combat_memory.py** (4 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **Any** (3 connections)
- **._is_valid_uuid()** (3 connections) — `server/services/npc_combat_handlers.py`
- **.get_rewards_service()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.__init__()** (3 connections) — `server/services/npc_combat_lifecycle.py`
- **.award_xp_to_killer()** (3 connections) — `server/services/npc_combat_rewards.py`
- **._is_valid_uuid()** (3 connections) — `server/services/npc_combat_rewards.py`
- **.test_init()** (3 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **.test_get_attacker_not_found()** (3 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **.test_get_attacker_found()** (3 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **.test_record_attack_first_engagement()** (3 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- *... and 54 more nodes in this community*

## Relationships

- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (14 shared connections)
- [main()](main%28%29.md) (8 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (8 shared connections)
- [Test despawn npc handles NPC](Test_despawn_npc_handles_NPC.md) (4 shared connections)
- [test npc combat rewards](test_npc_combat_rewards.md) (4 shared connections)
- [test npc combat handlers](test_npc_combat_handlers.md) (3 shared connections)
- [.get instance()](get_instance%28%29.md) (2 shared connections)
- [. despawn npc()](_despawn_npc%28%29.md) (2 shared connections)
- [.calculate xp reward()](calculate_xp_reward%28%29.md) (2 shared connections)
- [.shutdown()](shutdown%28%29.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [.get lucidity service()](get_lucidity_service%28%29.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_handlers.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_lifecycle.py`
- `server/services/npc_combat_memory.py`
- `server/services/npc_combat_rewards.py`
- `server/tests/unit/services/test_npc_combat_lifecycle.py`
- `server/tests/unit/services/test_npc_combat_memory.py`

## Audit Trail

- EXTRACTED: 254 (94%)
- INFERRED: 17 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*