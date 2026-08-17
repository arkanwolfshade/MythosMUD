# NPCCombatRewards

> 19 nodes

## Key Concepts

- **NPCCombatRewards** (18 connections) — `server/services/npc_combat_rewards.py`
- **.check_player_connection_state()** (6 connections) — `server/services/npc_combat_rewards.py`
- **test_npc_combat_rewards.py** (5 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **.__init__()** (4 connections) — `server/services/npc_combat_rewards.py`
- **.get_rewards_service()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.award_xp_to_killer()** (3 connections) — `server/services/npc_combat_rewards.py`
- **.calculate_xp_reward()** (3 connections) — `server/services/npc_combat_rewards.py`
- **._is_valid_uuid()** (3 connections) — `server/services/npc_combat_rewards.py`
- **.test_init()** (3 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **Any** (2 connections)
- **Return rewards dependency for integration collaborators.** (1 connections) — `server/services/npc_combat_integration_service.py`
- **Check if a string is a valid UUID.** (1 connections) — `server/services/npc_combat_rewards.py`
- **Manages XP rewards for NPC combat.** (1 connections) — `server/services/npc_combat_rewards.py`
- **Initialize the rewards manager. Args: async_persistence: Async persistence…** (1 connections) — `server/services/npc_combat_rewards.py`
- **Calculate XP reward from NPC definition. Args: npc_definition: NPC definition…** (1 connections) — `server/services/npc_combat_rewards.py`
- **Check and log player connection state before operations. Args: player_id: ID of…** (1 connections) — `server/services/npc_combat_rewards.py`
- **Award XP to the killer with defensive error handling. Args: killer_id: ID of…** (1 connections) — `server/services/npc_combat_rewards.py`
- **Unit tests for NPC combat rewards. Tests the NPCCombatRewards class for XP…** (1 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- **Test NPCCombatRewards initialization.** (1 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`

## Relationships

- [TestNPCCombatRewards](TestNPCCombatRewards.md) (4 shared connections)
- [test_npc_combat_handlers.py](test_npc_combat_handlers.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (2 shared connections)
- [NPCCombatLifecycle](NPCCombatLifecycle.md) (1 shared connections)
- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (1 shared connections)
- [._handle_npc_death_on_combat_end](_handle_npc_death_on_combat_end.md) (1 shared connections)
- [NPCStartupService](NPCStartupService.md) (1 shared connections)
- [.connection_manager](connection_manager.md) (1 shared connections)
- [GameMechanicsService](GameMechanicsService.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_rewards.py`
- `server/tests/unit/services/test_npc_combat_rewards.py`

## Audit Trail

- EXTRACTED: 34 (89%)
- INFERRED: 4 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*