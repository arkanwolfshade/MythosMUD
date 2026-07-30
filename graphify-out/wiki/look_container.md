# look container

> 30 nodes

## Key Concepts

- **NPCCombatRewards** (18 connections) — `server/services/npc_combat_rewards.py`
- **NPCCombatHandlers** (16 connections) — `server/services/npc_combat_handlers.py`
- **.__init__()** (7 connections) — `server/services/npc_combat_handlers.py`
- **._handle_npc_death_on_combat_end()** (7 connections) — `server/services/npc_combat_handlers.py`
- **.handle_combat_result()** (4 connections) — `server/services/npc_combat_handlers.py`
- **.__init__()** (4 connections) — `server/services/npc_combat_rewards.py`
- **Any** (3 connections)
- **._is_valid_uuid()** (3 connections) — `server/services/npc_combat_handlers.py`
- **.get_rewards_service()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.calculate_xp_reward()** (3 connections) — `server/services/npc_combat_rewards.py`
- **.award_xp_to_killer()** (3 connections) — `server/services/npc_combat_rewards.py`
- **._is_valid_uuid()** (3 connections) — `server/services/npc_combat_rewards.py`
- **npc_combat_handlers()** (3 connections) — `server/tests/unit/services/test_npc_combat_handlers.py`
- **.test_init()** (3 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **.handle_npc_death()** (2 connections) — `server/services/npc_combat_handlers.py`
- **Any** (2 connections)
- **Handles combat result processing and NPC death operations.** (1 connections) — `server/services/npc_combat_handlers.py`
- **Initialize the combat handlers.          Args:             data_provider: NPC co** (1 connections) — `server/services/npc_combat_handlers.py`
- **Handle combat result, including broadcasting messages and handling NPC death.** (1 connections) — `server/services/npc_combat_handlers.py`
- **Handle NPC death when combat ends, with defensive exception handling.          A** (1 connections) — `server/services/npc_combat_handlers.py`
- **Handle NPC death and related effects.          Args:             npc_id: ID of t** (1 connections) — `server/services/npc_combat_handlers.py`
- **Check if a string is a valid UUID.** (1 connections) — `server/services/npc_combat_handlers.py`
- **Return rewards dependency for integration collaborators.** (1 connections) — `server/services/npc_combat_integration_service.py`
- **Manages XP rewards for NPC combat.** (1 connections) — `server/services/npc_combat_rewards.py`
- **Initialize the rewards manager.          Args:             async_persistence: As** (1 connections) — `server/services/npc_combat_rewards.py`
- *... and 5 more nodes in this community*

## Relationships

- [Any](Any.md) (7 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (5 shared connections)
- [combat](combat.md) (4 shared connections)
- [test npc combat rewards](test_npc_combat_rewards.md) (4 shared connections)
- [Test despawn npc handles NPC](Test_despawn_npc_handles_NPC.md) (3 shared connections)
- [communication commands support](communication_commands_support.md) (2 shared connections)
- [test npc combat handlers](test_npc_combat_handlers.md) (2 shared connections)
- [.initialize()](initialize%28%29.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_handlers.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_rewards.py`
- `server/tests/unit/services/test_npc_combat_handlers.py`
- `server/tests/unit/services/test_npc_combat_rewards.py`

## Audit Trail

- EXTRACTED: 89 (91%)
- INFERRED: 9 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*