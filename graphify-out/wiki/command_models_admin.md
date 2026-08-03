# command models admin

> 66 nodes

## Key Concepts

- **CombatResult** (23 connections) — `server/models/combat.py`
- **test_combat_service.py** (18 connections) — `server/tests/unit/services/test_combat_service.py`
- **.connection_manager()** (15 connections) — `server/services/combat_messaging/base.py`
- **_NPCCombatIntegrationDeps** (14 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **_make_participant()** (10 connections) — `server/tests/unit/services/test_combat_service.py`
- **_make_combat_instance()** (9 connections) — `server/tests/unit/services/test_combat_service.py`
- **_make_service()** (9 connections) — `server/tests/unit/services/test_combat_service.py`
- **._process_combat_attack()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.start_new_combat_for_mixin()** (8 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._handle_npc_death_on_combat_end()** (7 connections) — `server/services/npc_combat_handlers.py`
- **._apply_npc_attack_damage_for_npc_initiated_combat()** (7 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._broadcast_room_after_npc_death()** (7 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.get_combat_service()** (6 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **UUID** (6 connections)
- **.check_player_connection_state()** (6 connections) — `server/services/npc_combat_rewards.py`
- **test_validate_melee_or_end_combat_ends_combat_on_invalid()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_apply_damage_and_check_involuntary_flee_returns_early_result_on_flee()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_finalize_attack_result_awards_xp_and_completes_combat()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_process_attack_returns_melee_validation_early_result()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_process_attack_happy_path_calls_helpers_and_returns_final_result()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **.check_connection_state()** (5 connections) — `server/services/combat_cleanup_handler.py`
- **._resolve_connection_manager_from_container()** (5 connections) — `server/services/combat_messaging/base.py`
- **.get_data_provider()** (5 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **test_validate_melee_or_end_combat_returns_none_on_valid()** (5 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_apply_damage_and_check_involuntary_flee_no_flee_for_npc()** (5 connections) — `server/tests/unit/services/test_combat_service.py`
- *... and 41 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (33 shared connections)
- [Item Instances](Item_Instances.md) (15 shared connections)
- [Error Conversion](Error_Conversion.md) (4 shared connections)
- [combat services messaging](combat_services_messaging.md) (4 shared connections)
- [tick game processing](tick_game_processing.md) (2 shared connections)
- [nats exceptions services](nats_exceptions_services.md) (1 shared connections)
- [room realtime rationale](room_realtime_rationale.md) (1 shared connections)
- [room websocket updates](room_websocket_updates.md) (1 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_service.py`
- `server/services/npc_combat_handlers.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/services/npc_combat_rewards.py`
- `server/tests/unit/services/test_combat_service.py`

## Audit Trail

- EXTRACTED: 248 (91%)
- INFERRED: 25 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*