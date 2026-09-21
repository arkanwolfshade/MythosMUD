# resolve_npc_attack_damage

> 19 nodes

## Key Concepts

- **resolve_npc_attack_damage()** (16 connections) — `server/game/npcs/attack_damage.py`
- **attack_damage.py** (12 connections) — `server/game/npcs/attack_damage.py`
- **test_attack_damage.py** (12 connections) — `server/tests/unit/game/npcs/test_attack_damage.py`
- **armor_points_from_base_stats()** (6 connections) — `server/game/npcs/attack_damage.py`
- **_damage_from_attack()** (6 connections) — `server/game/npcs/attack_damage.py`
- **Random** (4 connections)
- **_roll_int_bounds()** (3 connections) — `server/game/npcs/attack_damage.py`
- **_first_attack()** (2 connections) — `server/game/npcs/attack_damage.py`
- **_legacy_behavior_damage()** (2 connections) — `server/game/npcs/attack_damage.py`
- **test_apply_damage_subtracts_armor_points()** (2 connections) — `server/tests/unit/game/npcs/test_attack_damage.py`
- **test_armor_points_from_base_stats()** (2 connections) — `server/tests/unit/game/npcs/test_attack_damage.py`
- **test_resolve_falls_back_to_behavior_attack_damage()** (2 connections) — `server/tests/unit/game/npcs/test_attack_damage.py`
- **test_resolve_falls_back_to_min_max_without_expr()** (2 connections) — `server/tests/unit/game/npcs/test_attack_damage.py`
- **test_resolve_prefers_damage_expr()** (2 connections) — `server/tests/unit/game/npcs/test_attack_damage.py`
- **Resolve NPC outgoing attack damage from base_stats / behavior (ADR-027 Phase 3).** (1 connections) — `server/game/npcs/attack_damage.py`
- **Return damage from one attack entry, or None if it has no usable fields.** (1 connections) — `server/game/npcs/attack_damage.py`
- **Roll NPC damage: damage_expr if present, else min/max ints, else behavior, else…** (1 connections) — `server/game/npcs/attack_damage.py`
- **Return armor_points from nested base_stats.armor, or 0.** (1 connections) — `server/game/npcs/attack_damage.py`
- **Unit tests for NPC attack damage resolution (ADR-027 Phase 3).** (1 connections) — `server/tests/unit/game/npcs/test_attack_damage.py`

## Relationships

- [get_logger](get_logger.md) (5 shared connections)
- [damage_expr_to_min_max](damage_expr_to_min_max.md) (3 shared connections)
- [test_combat_flee_handler.py](test_combat_flee_handler.py.md) (2 shared connections)
- [CombatParticipant](CombatParticipant.md) (2 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (1 shared connections)
- [._attack_target_impl](_attack_target_impl.md) (1 shared connections)
- [CombatService](CombatService.md) (1 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)

## Source Files

- `server/game/npcs/attack_damage.py`
- `server/tests/unit/game/npcs/test_attack_damage.py`

## Audit Trail

- EXTRACTED: 47 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*