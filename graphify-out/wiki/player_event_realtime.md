# player event realtime

> 110 nodes

## Key Concepts

- **NPCCombatIntegrationService** (90 connections) — `server/services/npc_combat_integration_service.py`
- **npc_combat_integration_service.py** (50 connections) — `server/services/npc_combat_integration_service.py`
- **NPCCombatMemory** (28 connections) — `server/services/npc_combat_memory.py`
- **NPCCombatRewards** (18 connections) — `server/services/npc_combat_rewards.py`
- **NPCCombatHandlers** (16 connections) — `server/services/npc_combat_handlers.py`
- **TestNPCCombatMemory** (16 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **npc_combat_handlers.py** (15 connections) — `server/services/npc_combat_handlers.py`
- **NPCCombatLifecycle** (15 connections) — `server/services/npc_combat_lifecycle.py`
- **.__init__()** (12 connections) — `server/services/npc_combat_integration_service.py`
- **npc_combat_rewards.py** (10 connections) — `server/services/npc_combat_rewards.py`
- **._init_npc_submodules()** (9 connections) — `server/services/npc_combat_integration_service.py`
- **.__init__()** (7 connections) — `server/services/npc_combat_handlers.py`
- **._handle_npc_death_on_combat_end()** (7 connections) — `server/services/npc_combat_handlers.py`
- **npc_combat_lifecycle.py** (7 connections) — `server/services/npc_combat_lifecycle.py`
- **npc_combat_memory.py** (7 connections) — `server/services/npc_combat_memory.py`
- **._init_messaging_handlers_and_publisher()** (6 connections) — `server/services/npc_combat_integration_service.py`
- **.handle_npc_attack_on_player()** (6 connections) — `server/services/npc_combat_integration_service.py`
- **.check_player_connection_state()** (6 connections) — `server/services/npc_combat_rewards.py`
- **._init_persistence_and_event_bus()** (5 connections) — `server/services/npc_combat_integration_service.py`
- **.handle_combat_result()** (4 connections) — `server/services/npc_combat_handlers.py`
- **._init_combat_service()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **._run_npc_attack_on_player_after_grace()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **test_npc_combat_lifecycle.py** (4 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **test_npc_combat_memory.py** (4 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **test_npc_combat_rewards.py** (4 connections) — `server/tests/unit/services/test_npc_combat_rewards.py`
- *... and 85 more nodes in this community*

## Relationships

- [grace period login](grace_period_login.md) (38 shared connections)
- [Error Conversion](Error_Conversion.md) (20 shared connections)
- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (10 shared connections)
- [rate limiter realtime](rate_limiter_realtime.md) (7 shared connections)
- [lucidity event services](lucidity_event_services.md) (7 shared connections)
- [casting game magic](casting_game_magic.md) (6 shared connections)
- [game models player](game_models_player.md) (6 shared connections)
- [add used user](add_used_user.md) (5 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (5 shared connections)
- [combat commands handler](combat_commands_handler.md) (5 shared connections)
- [player event handlers](player_event_handlers.md) (4 shared connections)
- [room renderer functions](room_renderer_functions.md) (4 shared connections)

## Source Files

- `server/services/npc_combat_handlers.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_lifecycle.py`
- `server/services/npc_combat_memory.py`
- `server/services/npc_combat_rewards.py`
- `server/tests/unit/services/test_npc_combat_lifecycle.py`
- `server/tests/unit/services/test_npc_combat_memory.py`
- `server/tests/unit/services/test_npc_combat_rewards.py`

## Audit Trail

- EXTRACTED: 458 (92%)
- INFERRED: 38 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*