# . init ()

> 41 nodes

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
- **Any** (2 connections)
- **Return lucidity dependency for integration collaborators.** (1 connections) — `server/services/npc_combat_integration_service.py`
- **Manages lucidity effects for NPC encounters.** (1 connections) — `server/services/npc_combat_lucidity.py`
- **Apply lucidity loss when a player engages an eldritch entity.          Args:** (1 connections) — `server/services/npc_combat_lucidity.py`
- **Determine encounter category based on NPC definition metadata.          Args:** (1 connections) — `server/services/npc_combat_lucidity.py`
- *... and 16 more nodes in this community*

## Relationships

- [UUID](UUID.md) (4 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (4 shared connections)
- [combat](combat.md) (2 shared connections)
- [Return stats\[key\] as int, or](Return_stats%5Bkey%5D_as_int%2C_or.md) (2 shared connections)
- [Test despawn npc handles NPC](Test_despawn_npc_handles_NPC.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)
- [test player preferences service](test_player_preferences_service.md) (1 shared connections)

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