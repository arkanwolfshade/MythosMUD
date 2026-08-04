# models npc rationale

> 525 nodes

## Key Concepts

- **CombatInstance** (186 connections) — `server/models/combat.py`
- **CombatService** (181 connections) — `server/services/combat_service.py`
- **get_config()** (105 connections) — `server/config/__init__.py`
- **combat_service.py** (99 connections) — `server/services/combat_service.py`
- **test_combat.py** (60 connections) — `server/tests/unit/models/test_combat.py`
- **combat.py** (56 connections) — `server/models/combat.py`
- **CombatParticipantType** (44 connections) — `server/models/combat.py`
- **test_combat_attack_handler.py** (37 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_combat_service.py** (37 connections) — `server/tests/unit/services/test_combat_service.py`
- **combat_service_start.py** (28 connections) — `server/services/combat_service_start.py`
- **_make_service()** (28 connections) — `server/tests/unit/services/test_combat_service.py`
- **combat_service_attack.py** (27 connections) — `server/services/combat_service_attack.py`
- **CombatResult** (23 connections) — `server/models/combat.py`
- **CorpseLifecycleService** (23 connections) — `server/services/corpse_lifecycle_service.py`
- **combat_death_handler.py** (22 connections) — `server/services/combat_death_handler.py`
- **CombatDeathHandler** (20 connections) — `server/services/combat_death_handler.py`
- **UUID** (20 connections)
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **npc_combat_data_provider.py** (18 connections) — `server/services/npc_combat_data_provider.py`
- **test_combat_cleanup_handler.py** (18 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **combat_attack_handler.py** (17 connections) — `server/services/combat_attack_handler.py`
- **CombatAttackHandler** (17 connections) — `server/services/combat_attack_handler.py`
- **get_current_tick()** (16 connections) — `server/app/game_tick_processing.py`
- **npc_combat_integration_combat_mixin.py** (16 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.connection_manager()** (15 connections) — `server/services/combat_messaging/base.py`
- *... and 500 more nodes in this community*

## Relationships

- [Item Instances](Item_Instances.md) (126 shared connections)
- [NPC Combat](NPC_Combat.md) (81 shared connections)
- [services combat sync](services_combat_sync.md) (45 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (43 shared connections)
- [player look commands](player_look_commands.md) (38 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (37 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (37 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (26 shared connections)
- [nats services service](nats_services_service.md) (24 shared connections)
- [command factories exploration](command_factories_exploration.md) (21 shared connections)
- [commands communication say](commands_communication_say.md) (20 shared connections)
- [retry nats handler](retry_nats_handler.md) (17 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/config/__init__.py`
- `server/container/bundles/combat.py`
- `server/game/player_service.py`
- `server/models/combat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_start.py`
- `server/services/combat_service_state.py`
- `server/services/combat_service_types.py`
- `server/services/combat_turn_processor.py`
- `server/services/corpse_lifecycle_service.py`
- `server/services/npc_combat_data_provider.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 2327 (94%)
- INFERRED: 149 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*