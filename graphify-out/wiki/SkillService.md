# SkillService

> 38 nodes

## Key Concepts

- **spell_effects_support.py** (20 connections) — `server/game/magic/spell_effects_support.py`
- **test_spell_effects_support.py** (14 connections) — `server/tests/unit/game/magic/test_spell_effects_support.py`
- **process_create_object_effect()** (11 connections) — `server/game/magic/spell_effects_support.py`
- **process_stat_modify_effect()** (11 connections) — `server/game/magic/spell_effects_support.py`
- **apply_stat_modifications()** (10 connections) — `server/game/magic/spell_effects_stats.py`
- **_apply_stat_modify_to_player()** (8 connections) — `server/game/magic/spell_effects_support.py`
- **_spell()** (8 connections) — `server/tests/unit/game/magic/test_spell_effects_support.py`
- **test_spell_effects_stats.py** (8 connections) — `server/tests/unit/game/magic/test_spell_effects_stats.py`
- **_build_stat_modifications()** (7 connections) — `server/game/magic/spell_effects_support.py`
- **_create_object_for_room()** (7 connections) — `server/game/magic/spell_effects_support.py`
- **_target()** (7 connections) — `server/tests/unit/game/magic/test_spell_effects_support.py`
- **spell_effects_stats.py** (6 connections) — `server/game/magic/spell_effects_stats.py`
- **Any** (6 connections)
- **_create_object_for_player()** (5 connections) — `server/game/magic/spell_effects_support.py`
- **test_process_create_object_for_player()** (5 connections) — `server/tests/unit/game/magic/test_spell_effects_support.py`
- **test_process_create_object_missing_prototype()** (5 connections) — `server/tests/unit/game/magic/test_spell_effects_support.py`
- **test_process_stat_modify_rejects_non_player()** (5 connections) — `server/tests/unit/game/magic/test_spell_effects_support.py`
- **test_process_stat_modify_success()** (5 connections) — `server/tests/unit/game/magic/test_spell_effects_support.py`
- **test_create_object_for_room_placeholder()** (4 connections) — `server/tests/unit/game/magic/test_spell_effects_support.py`
- **asyncio** (4 connections)
- **test_build_stat_modifications_missing()** (3 connections) — `server/tests/unit/game/magic/test_spell_effects_support.py`
- **test_build_stat_modifications_shorthand()** (3 connections) — `server/tests/unit/game/magic/test_spell_effects_support.py`
- **test_apply_stat_modifications_bad_string_skipped()** (2 connections) — `server/tests/unit/game/magic/test_spell_effects_stats.py`
- **test_apply_stat_modifications_basic()** (2 connections) — `server/tests/unit/game/magic/test_spell_effects_stats.py`
- **test_apply_stat_modifications_clamps_to_bounds()** (2 connections) — `server/tests/unit/game/magic/test_spell_effects_stats.py`
- *... and 13 more nodes in this community*

## Relationships

- [connection_manager_methods.py](connection_manager_methods.py.md) (13 shared connections)
- [eventHandlers/types.ts](eventHandlers-types.ts.md) (7 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (4 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (2 shared connections)
- [NATSError](NATSError.md) (2 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)
- [extract_player_name](extract_player_name.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effects_stats.py`
- `server/game/magic/spell_effects_support.py`
- `server/tests/unit/game/magic/test_spell_effects_stats.py`
- `server/tests/unit/game/magic/test_spell_effects_support.py`

## Audit Trail

- EXTRACTED: 102 (95%)
- INFERRED: 5 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*