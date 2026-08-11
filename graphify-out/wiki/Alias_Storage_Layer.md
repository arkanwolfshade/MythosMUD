# Alias Storage Layer

> 52 nodes

## Key Concepts

- **NPCCombatLucidity** (34 connections) — `server/services/npc_combat_lucidity.py`
- **TestNPCCombatLucidity** (17 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **_EncounterCtx** (9 connections) — `server/services/npc_combat_lucidity.py`
- **.apply_encounter_lucidity_effect()** (9 connections) — `server/services/npc_combat_lucidity.py`
- **._apply_loss_with_fallback()** (8 connections) — `server/services/npc_combat_lucidity.py`
- **._commit_loss()** (7 connections) — `server/services/npc_combat_lucidity.py`
- **._apply_disturbing_fallback()** (7 connections) — `server/services/npc_combat_lucidity.py`
- **Any** (6 connections)
- **._archetype_from_definition()** (4 connections) — `server/services/npc_combat_lucidity.py`
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
- *... and 27 more nodes in this community*

## Relationships

- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (6 shared connections)
- [Container Open Events](Container_Open_Events.md) (6 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (4 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (2 shared connections)
- [Command Testing Guide](Command_Testing_Guide.md) (2 shared connections)
- [Playwright E2E Specs](Playwright_E2E_Specs.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_lucidity.py`
- `server/tests/unit/services/test_npc_combat_lucidity.py`

## Audit Trail

- EXTRACTED: 171 (94%)
- INFERRED: 10 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*