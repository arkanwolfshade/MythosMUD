# Server Services (27)

> 70 nodes

## Key Concepts

- **NPCCombatMemory** (28 connections) — `server/services/npc_combat_memory.py`
- **NPCCombatRewards** (18 connections) — `server/services/npc_combat_rewards.py`
- **NPCCombatHandlers** (16 connections) — `server/services/npc_combat_handlers.py`
- **TestNPCCombatMemory** (16 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **.__init__()** (7 connections) — `server/services/npc_combat_handlers.py`
- **._handle_npc_death_on_combat_end()** (7 connections) — `server/services/npc_combat_handlers.py`
- **.check_player_connection_state()** (6 connections) — `server/services/npc_combat_rewards.py`
- **.handle_combat_result()** (4 connections) — `server/services/npc_combat_handlers.py`
- **.__init__()** (4 connections) — `server/services/npc_combat_rewards.py`
- **test_npc_combat_memory.py** (4 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **Any** (3 connections)
- **._is_valid_uuid()** (3 connections) — `server/services/npc_combat_handlers.py`
- **.get_rewards_service()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.calculate_xp_reward()** (3 connections) — `server/services/npc_combat_rewards.py`
- **.award_xp_to_killer()** (3 connections) — `server/services/npc_combat_rewards.py`
- **._is_valid_uuid()** (3 connections) — `server/services/npc_combat_rewards.py`
- **.test_init()** (3 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **.test_get_attacker_not_found()** (3 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **.test_get_attacker_found()** (3 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **.test_record_attack_first_engagement()** (3 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **.test_record_attack_subsequent_engagement()** (3 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **.test_record_attack_overwrites_previous()** (3 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **.test_clear_memory_exists()** (3 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **.test_clear_memory_not_exists()** (3 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **.test_has_memory_true()** (3 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- *... and 45 more nodes in this community*

## Relationships

- [Server Services (4)](Server_Services_%284%29.md) (12 shared connections)
- [Server Services (11)](Server_Services_%2811%29.md) (9 shared connections)
- [Server Services (51)](Server_Services_%2851%29.md) (4 shared connections)
- [Server Services (47)](Server_Services_%2847%29.md) (2 shared connections)
- [Server App](Server_App.md) (2 shared connections)
- [Server Services (5)](Server_Services_%285%29.md) (2 shared connections)

## Source Files

- `server/services/npc_combat_handlers.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_memory.py`
- `server/services/npc_combat_rewards.py`
- `server/tests/unit/services/test_npc_combat_memory.py`

## Audit Trail

- EXTRACTED: 201 (93%)
- INFERRED: 14 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*