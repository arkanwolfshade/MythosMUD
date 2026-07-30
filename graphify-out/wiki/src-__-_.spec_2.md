# src/**/*.spec

> 15 nodes

## Key Concepts

- **NPCCombatHandlers** (16 connections) — `server/services/npc_combat_handlers.py`
- **.__init__()** (7 connections) — `server/services/npc_combat_handlers.py`
- **._handle_npc_death_on_combat_end()** (7 connections) — `server/services/npc_combat_handlers.py`
- **.handle_combat_result()** (4 connections) — `server/services/npc_combat_handlers.py`
- **Any** (3 connections)
- **._is_valid_uuid()** (3 connections) — `server/services/npc_combat_handlers.py`
- **npc_combat_handlers()** (3 connections) — `server/tests/unit/services/test_npc_combat_handlers.py`
- **.handle_npc_death()** (2 connections) — `server/services/npc_combat_handlers.py`
- **Handles combat result processing and NPC death operations.** (1 connections) — `server/services/npc_combat_handlers.py`
- **Initialize the combat handlers.          Args:             data_provider: NPC co** (1 connections) — `server/services/npc_combat_handlers.py`
- **Handle combat result, including broadcasting messages and handling NPC death.** (1 connections) — `server/services/npc_combat_handlers.py`
- **Handle NPC death when combat ends, with defensive exception handling.          A** (1 connections) — `server/services/npc_combat_handlers.py`
- **Handle NPC death and related effects.          Args:             npc_id: ID of t** (1 connections) — `server/services/npc_combat_handlers.py`
- **Check if a string is a valid UUID.** (1 connections) — `server/services/npc_combat_handlers.py`
- **Create NPCCombatHandlers instance.** (1 connections) — `server/tests/unit/services/test_npc_combat_handlers.py`

## Relationships

- [get health service()](get_health_service%28%29.md) (3 shared connections)
- [Test despawn npc handles NPC](Test_despawn_npc_handles_NPC.md) (2 shared connections)
- [communication commands support](communication_commands_support.md) (2 shared connections)
- [look container](look_container.md) (2 shared connections)
- [combat](combat.md) (2 shared connections)
- [test npc combat handlers](test_npc_combat_handlers.md) (2 shared connections)
- [NATSMessageSubscriptionMixin](NATSMessageSubscriptionMixin.md) (2 shared connections)
- [world](world.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_handlers.py`
- `server/tests/unit/services/test_npc_combat_handlers.py`

## Audit Trail

- EXTRACTED: 46 (88%)
- INFERRED: 6 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*