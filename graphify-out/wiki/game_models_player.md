# game models player

> 56 nodes

## Key Concepts

- **NPCCombatLucidity** (30 connections) — `server/services/npc_combat_lucidity.py`
- **ActiveLucidityService** (20 connections) — `server/services/active_lucidity_service.py`
- **npc_combat_integration_validation_mixin.py** (20 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **TestNPCCombatLucidity** (17 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **npc_combat_lucidity.py** (12 connections) — `server/services/npc_combat_lucidity.py`
- **UnknownEncounterCategoryError** (10 connections) — `server/services/active_lucidity_service.py`
- **.apply_encounter_lucidity_effect()** (6 connections) — `server/services/npc_combat_lucidity.py`
- **.apply_encounter_lucidity_loss()** (5 connections) — `server/services/active_lucidity_service.py`
- **UUID** (4 connections)
- **.get_action_cooldown()** (4 connections) — `server/services/active_lucidity_service.py`
- **._resolve_lucidity_category()** (4 connections) — `server/services/npc_combat_lucidity.py`
- **test_npc_combat_lucidity.py** (4 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.test_resolve_lucidity_category_get_behavior_config_exception()** (4 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **Any** (3 connections)
- **.get_lucidity_service()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.test_init()** (3 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.test_resolve_lucidity_category_none_npc()** (3 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.test_resolve_lucidity_category_from_base_stats()** (3 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.test_resolve_lucidity_category_from_mythos_tier()** (3 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.test_resolve_lucidity_category_from_behavior_config()** (3 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.test_resolve_lucidity_category_aggressive_mob()** (3 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.test_resolve_lucidity_category_passive_mob()** (3 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.test_resolve_lucidity_category_default()** (3 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.test_resolve_lucidity_category_get_base_stats_exception()** (3 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.test_resolve_lucidity_category_non_dict_stats()** (3 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- *... and 31 more nodes in this community*

## Relationships

- [auth endpoints rationale](auth_endpoints_rationale.md) (8 shared connections)
- [Error Conversion](Error_Conversion.md) (8 shared connections)
- [models player rationale](models_player_rationale.md) (8 shared connections)
- [npc population control](npc_population_control.md) (7 shared connections)
- [player event realtime](player_event_realtime.md) (6 shared connections)
- [realtime real time](realtime_real_time.md) (5 shared connections)
- [player room realtime](player_room_realtime.md) (3 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (3 shared connections)
- [combat commands handler](combat_commands_handler.md) (2 shared connections)
- [subject admin controller](subject_admin_controller.md) (1 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (1 shared connections)
- [rate limiter realtime](rate_limiter_realtime.md) (1 shared connections)

## Source Files

- `server/services/active_lucidity_service.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_integration_validation_mixin.py`
- `server/services/npc_combat_lucidity.py`
- `server/tests/unit/services/test_npc_combat_lucidity.py`

## Audit Trail

- EXTRACTED: 202 (94%)
- INFERRED: 13 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*