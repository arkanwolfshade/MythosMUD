# test_npc_combat_handlers.py

> 61 nodes

## Key Concepts

- **test_npc_combat_handlers.py** (22 connections) — `server/tests/unit/services/test_npc_combat_handlers.py`
- **NPCCombatHandlers** (18 connections) — `server/services/npc_combat_handlers.py`
- **CombatResultCtx** (16 connections) — `server/services/npc_combat_handlers.py`
- **asyncio** (9 connections)
- **fixture** (8 connections)
- **._handle_npc_death_on_combat_end()** (7 connections) — `server/services/npc_combat_handlers.py`
- **.__init__()** (7 connections) — `server/services/npc_combat_handlers.py`
- **.handle_combat_result()** (5 connections) — `server/services/npc_combat_handlers.py`
- **._complete_player_attack_on_npc_after_grace()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **.handle_player_attack_on_npc()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **npc_combat_handlers()** (4 connections) — `server/tests/unit/services/test_npc_combat_handlers.py`
- **test_handle_combat_result_broadcast_error()** (4 connections) — `server/tests/unit/services/test_npc_combat_handlers.py`
- **test_handle_combat_result_combat_ended()** (4 connections) — `server/tests/unit/services/test_npc_combat_handlers.py`
- **test_handle_combat_result_success()** (4 connections) — `server/tests/unit/services/test_npc_combat_handlers.py`
- **test_handle_combat_result_unsuccessful()** (4 connections) — `server/tests/unit/services/test_npc_combat_handlers.py`
- **._broadcast_combat_success()** (3 connections) — `server/services/npc_combat_handlers.py`
- **.handle_npc_death()** (3 connections) — `server/services/npc_combat_handlers.py`
- **._is_valid_uuid()** (3 connections) — `server/services/npc_combat_handlers.py`
- **mock_combat_memory()** (3 connections) — `server/tests/unit/services/test_npc_combat_handlers.py`
- **mock_combat_result()** (3 connections) — `server/tests/unit/services/test_npc_combat_handlers.py`
- **mock_data_provider()** (3 connections) — `server/tests/unit/services/test_npc_combat_handlers.py`
- **mock_lifecycle()** (3 connections) — `server/tests/unit/services/test_npc_combat_handlers.py`
- **mock_messaging_integration()** (3 connections) — `server/tests/unit/services/test_npc_combat_handlers.py`
- **mock_npc_instance()** (3 connections) — `server/tests/unit/services/test_npc_combat_handlers.py`
- **mock_rewards()** (3 connections) — `server/tests/unit/services/test_npc_combat_handlers.py`
- *... and 36 more nodes in this community*

## Relationships

- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (8 shared connections)
- [CombatService](CombatService.md) (5 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [NPCCombatMemory](NPCCombatMemory.md) (3 shared connections)
- [NPCCombatRewards](NPCCombatRewards.md) (3 shared connections)
- [NPCStartupService](NPCStartupService.md) (1 shared connections)
- [test_combat_death_handler.py](test_combat_death_handler.py.md) (1 shared connections)
- [npc_combat_grace.py](npc_combat_grace.py.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_handlers.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/services/test_npc_combat_handlers.py`

## Audit Trail

- EXTRACTED: 101 (90%)
- INFERRED: 11 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*