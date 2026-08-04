# models npc rationale

> 334 nodes

## Key Concepts

- **get_config()** (105 connections) — `server/config/__init__.py`
- **combat_service.py** (99 connections) — `server/services/combat_service.py`
- **combat.py** (56 connections) — `server/models/combat.py`
- **npc_combat_integration_service.py** (50 connections) — `server/services/npc_combat_integration_service.py`
- **CombatParticipantType** (44 connections) — `server/models/combat.py`
- **NPCCombatDataProvider** (39 connections) — `server/services/npc_combat_data_provider.py`
- **CombatParticipantData** (37 connections) — `server/services/combat_types.py`
- **combat_service_start.py** (28 connections) — `server/services/combat_service_start.py`
- **NPCCombatMemory** (28 connections) — `server/services/npc_combat_memory.py`
- **combat_death_handler.py** (22 connections) — `server/services/combat_death_handler.py`
- **npc_combat_integration_validation_mixin.py** (20 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **npc_combat_data_provider.py** (18 connections) — `server/services/npc_combat_data_provider.py`
- **NPCCombatRewards** (18 connections) — `server/services/npc_combat_rewards.py`
- **test_combat_cleanup_handler.py** (18 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **combat_attack_handler.py** (17 connections) — `server/services/combat_attack_handler.py`
- **.create_combat_instance()** (17 connections) — `server/services/combat_initialization.py`
- **test_npc_combat_data_provider.py** (17 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **NPCCombatHandlers** (16 connections) — `server/services/npc_combat_handlers.py`
- **npc_combat_integration_combat_mixin.py** (16 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **TestNPCCombatMemory** (16 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **combat_initialization.py** (15 connections) — `server/services/combat_initialization.py`
- **.connection_manager()** (15 connections) — `server/services/combat_messaging/base.py`
- **npc_combat_handlers.py** (15 connections) — `server/services/npc_combat_handlers.py`
- **NPCCombatIntegrationValidationMixin** (15 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **NPCCombatLifecycle** (15 connections) — `server/services/npc_combat_lifecycle.py`
- *... and 309 more nodes in this community*

## Relationships

- [Loot Generation](Loot_Generation.md) (39 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (38 shared connections)
- [services combat sync](services_combat_sync.md) (35 shared connections)
- [command factories exploration](command_factories_exploration.md) (33 shared connections)
- [NPC Combat](NPC_Combat.md) (26 shared connections)
- [Item Instances](Item_Instances.md) (23 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (21 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (19 shared connections)
- [movement monitor game](movement_monitor_game.md) (18 shared connections)
- [command player state](command_player_state.md) (16 shared connections)
- [nats services service](nats_services_service.md) (14 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (10 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/models/combat.py`
- `server/services/aggro_threat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_initialization.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_service.py`
- `server/services/combat_service_end.py`
- `server/services/combat_service_start.py`
- `server/services/combat_types.py`
- `server/services/npc_combat_data_provider.py`
- `server/services/npc_combat_handlers.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_integration_validation_mixin.py`
- `server/services/npc_combat_lifecycle.py`
- `server/services/npc_combat_memory.py`
- `server/services/npc_combat_rewards.py`

## Audit Trail

- EXTRACTED: 1493 (95%)
- INFERRED: 74 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*