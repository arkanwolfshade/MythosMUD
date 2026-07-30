# look container

> 19 nodes

## Key Concepts

- **NPCCombatRewards** (18 connections) — `server/services/npc_combat_rewards.py`
- **.__init__()** (4 connections) — `server/services/npc_combat_rewards.py`
- **test_npc_combat_rewards.py** (4 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **.get_rewards_service()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.calculate_xp_reward()** (3 connections) — `server/services/npc_combat_rewards.py`
- **.award_xp_to_killer()** (3 connections) — `server/services/npc_combat_rewards.py`
- **._is_valid_uuid()** (3 connections) — `server/services/npc_combat_rewards.py`
- **.rewards_service()** (3 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **.test_init()** (3 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **Any** (2 connections)
- **Return rewards dependency for integration collaborators.** (1 connections) — `server/services/npc_combat_integration_service.py`
- **Manages XP rewards for NPC combat.** (1 connections) — `server/services/npc_combat_rewards.py`
- **Initialize the rewards manager.          Args:             async_persistence: As** (1 connections) — `server/services/npc_combat_rewards.py`
- **Calculate XP reward from NPC definition.          Args:             npc_definiti** (1 connections) — `server/services/npc_combat_rewards.py`
- **Award XP to the killer with defensive error handling.          Args:** (1 connections) — `server/services/npc_combat_rewards.py`
- **Check if a string is a valid UUID.** (1 connections) — `server/services/npc_combat_rewards.py`
- **Unit tests for NPC combat rewards.  Tests the NPCCombatRewards class for XP calc** (1 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **Create a NPCCombatRewards instance for testing.** (1 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **Test NPCCombatRewards initialization.** (1 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`

## Relationships

- [test npc combat rewards](test_npc_combat_rewards.md) (4 shared connections)
- [world](world.md) (3 shared connections)
- [NATSMessageSubscriptionMixin](NATSMessageSubscriptionMixin.md) (3 shared connections)
- [combat](combat.md) (2 shared connections)
- [src/**/*.spec](src-__-_.spec.md) (2 shared connections)
- [get health service()](get_health_service%28%29.md) (1 shared connections)
- [Test despawn npc handles NPC](Test_despawn_npc_handles_NPC.md) (1 shared connections)
- [real time](real_time.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_rewards.py`
- `server/tests/unit/services/test_npc_combat_rewards.py`

## Audit Trail

- EXTRACTED: 52 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*