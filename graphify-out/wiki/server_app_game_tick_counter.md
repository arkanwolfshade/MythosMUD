# server app game tick counter

> 235 nodes

## Key Concepts

- **get_config()** (101 connections) — `server/config/__init__.py`
- **combat_service.py** (99 connections) — `server/services/combat_service.py`
- **models/combat.py** (58 connections) — `server/models/combat.py`
- **CombatParticipantType** (40 connections) — `server/models/combat.py`
- **magic_service.py** (30 connections) — `server/game/magic/magic_service.py`
- **combat_service_start.py** (28 connections) — `server/services/combat_service_start.py`
- **test_damage_grace_period.py** (28 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **spell_targeting.py** (25 connections) — `server/game/magic/spell_targeting.py`
- **combat_death_handler.py** (22 connections) — `server/services/combat_death_handler.py`
- **CombatDeathHandler** (20 connections) — `server/services/combat_death_handler.py`
- **CombatAttackHandler** (19 connections) — `server/services/combat_attack_handler.py`
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **test_combat_cleanup_handler.py** (19 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **npc_combat_data_provider.py** (18 connections) — `server/services/npc_combat_data_provider.py`
- **combat_attack_handler.py** (17 connections) — `server/services/combat_attack_handler.py`
- **.connection_manager()** (15 connections) — `server/services/combat_messaging/base.py`
- **get_current_tick()** (14 connections) — `server/app/game_tick_counter.py`
- **.__init__()** (14 connections) — `server/services/combat_service.py`
- **test_aggro_flow.py** (14 connections) — `server/tests/integration/test_aggro_flow.py`
- **test_combat_turn_participant_actions.py** (13 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **CombatCleanupHandler** (12 connections) — `server/services/combat_cleanup_handler.py`
- **combat_service_end.py** (12 connections) — `server/services/combat_service_end.py`
- **npc_combat_integration_combat_mixin.py** (12 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **combat_cleanup_handler.py** (11 connections) — `server/services/combat_cleanup_handler.py`
- **combat_types.py** (11 connections) — `server/services/combat_types.py`
- *... and 210 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (53 shared connections)
- [server services aggro threat](server_services_aggro_threat.md) (42 shared connections)
- [server models combat combataction](server_models_combat_combataction.md) (37 shared connections)
- [server models combat combatinstance](server_models_combat_combatinstance.md) (35 shared connections)
- [server container bundles combat combatbundle](server_container_bundles_combat_combatbundle.md) (32 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (25 shared connections)
- [server events combat events](server_events_combat_events.md) (20 shared connections)
- [server services combat initialization](server_services_combat_initialization.md) (20 shared connections)
- [combatdpsync](combatdpsync.md) (16 shared connections)
- [server tests unit services test](server_tests_unit_services_test.md) (12 shared connections)
- [server commands combat taunt rationale](server_commands_combat_taunt_rationale.md) (10 shared connections)
- [server realtime message formatters](server_realtime_message_formatters.md) (9 shared connections)

## Source Files

- `server/app/game_tick_counter.py`
- `server/config/__init__.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/spell_targeting.py`
- `server/models/combat.py`
- `server/services/aggro_threat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_service.py`
- `server/services/combat_service_end.py`
- `server/services/combat_service_start.py`
- `server/services/combat_turn_processor.py`
- `server/services/combat_types.py`
- `server/services/npc_combat_data_provider.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/tests/integration/test_aggro_flow.py`
- `server/tests/unit/config/test_config.py`
- `server/tests/unit/config/test_config_init.py`

## Audit Trail

- EXTRACTED: 813 (95%)
- INFERRED: 44 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*