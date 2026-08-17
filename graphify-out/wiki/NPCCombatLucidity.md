# NPCCombatLucidity

> 55 nodes

## Key Concepts

- **NPCCombatLucidity** (33 connections) — `server/services/npc_combat_lucidity.py`
- **ActiveLucidityService** (23 connections) — `server/services/active_lucidity_service.py`
- **TestNPCCombatLucidity** (17 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.apply_encounter_lucidity_effect()** (9 connections) — `server/services/npc_combat_lucidity.py`
- **._apply_loss_with_fallback()** (8 connections) — `server/services/npc_combat_lucidity.py`
- **_EncounterCtx** (7 connections) — `server/services/npc_combat_lucidity.py`
- **._apply_disturbing_fallback()** (7 connections) — `server/services/npc_combat_lucidity.py`
- **._commit_loss()** (7 connections) — `server/services/npc_combat_lucidity.py`
- **Any** (6 connections)
- **test_npc_combat_lucidity.py** (5 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **._archetype_from_definition()** (4 connections) — `server/services/npc_combat_lucidity.py`
- **._resolve_lucidity_category()** (4 connections) — `server/services/npc_combat_lucidity.py`
- **.test_apply_encounter_lucidity_effect_success()** (4 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.test_apply_encounter_lucidity_effect_with_npc_name()** (4 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.test_apply_encounter_lucidity_effect_without_npc_name()** (4 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.test_resolve_lucidity_category_get_behavior_config_exception()** (4 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.get_lucidity_service()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.test_init()** (3 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.test_resolve_lucidity_category_aggressive_mob()** (3 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.test_resolve_lucidity_category_default()** (3 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.test_resolve_lucidity_category_from_base_stats()** (3 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.test_resolve_lucidity_category_from_behavior_config()** (3 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.test_resolve_lucidity_category_from_mythos_tier()** (3 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.test_resolve_lucidity_category_get_base_stats_exception()** (3 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.test_resolve_lucidity_category_non_dict_stats()** (3 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- *... and 30 more nodes in this community*

## Relationships

- [DatabaseError](DatabaseError.md) (5 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [UnknownLucidityActionError](UnknownLucidityActionError.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (2 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [_NPCCombatIntegrationValidationDeps](_NPCCombatIntegrationValidationDeps.md) (2 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (2 shared connections)
- [active_lucidity_service](active_lucidity_service.md) (1 shared connections)
- [NPCCombatLifecycle](NPCCombatLifecycle.md) (1 shared connections)

## Source Files

- `server/services/active_lucidity_service.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_lucidity.py`
- `server/tests/unit/services/test_npc_combat_lucidity.py`

## Audit Trail

- EXTRACTED: 109 (91%)
- INFERRED: 11 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*