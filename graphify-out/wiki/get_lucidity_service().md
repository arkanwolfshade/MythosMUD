# .get lucidity service()

> 39 nodes

## Key Concepts

- **NPCCombatLucidity** (30 connections) — `server/services/npc_combat_lucidity.py`
- **TestNPCCombatLucidity** (17 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.apply_encounter_lucidity_effect()** (6 connections) — `server/services/npc_combat_lucidity.py`
- **._resolve_lucidity_category()** (4 connections) — `server/services/npc_combat_lucidity.py`
- **test_npc_combat_lucidity.py** (4 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.test_resolve_lucidity_category_get_behavior_config_exception()** (4 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
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
- **.test_apply_encounter_lucidity_effect_success()** (3 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.test_apply_encounter_lucidity_effect_with_npc_name()** (3 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **.test_apply_encounter_lucidity_effect_without_npc_name()** (3 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **Test _resolve_lucidity_category gets category from base_stats.** (3 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **Any** (2 connections)
- **Return lucidity dependency for integration collaborators.** (1 connections) — `server/services/npc_combat_integration_service.py`
- **Manages lucidity effects for NPC encounters.** (1 connections) — `server/services/npc_combat_lucidity.py`
- **Apply lucidity loss when a player engages an eldritch entity.          Args:** (1 connections) — `server/services/npc_combat_lucidity.py`
- *... and 14 more nodes in this community*

## Relationships

- [Any](Any.md) (3 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (3 shared connections)
- [main()](main%28%29.md) (3 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (2 shared connections)
- [.store npc xp mapping for](store_npc_xp_mapping_for.md) (2 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_lucidity.py`
- `server/tests/unit/services/test_npc_combat_lucidity.py`

## Audit Trail

- EXTRACTED: 121 (94%)
- INFERRED: 8 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*