# Community 840

> 19 nodes

## Key Concepts

- **resolve_npc_attack_damage()** (12 connections) — `server/game/npcs/attack_damage.py`
- **attack_damage.py** (12 connections) — `server/game/npcs/attack_damage.py`
- **test_attack_damage.py** (12 connections) — `server/tests/unit/game/npcs/test_attack_damage.py`
- **_damage_from_attack()** (6 connections) — `server/game/npcs/attack_damage.py`
- **armor_points_from_base_stats()** (4 connections) — `server/game/npcs/attack_damage.py`
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

- [Community 547](Community_547.md) (3 shared connections)
- [Combat Attack Execution](Combat_Attack_Execution.md) (3 shared connections)
- [NPC Behavior Engine](NPC_Behavior_Engine.md) (2 shared connections)
- [Combat Participants](Combat_Participants.md) (2 shared connections)

## Source Files

- `server/game/npcs/attack_damage.py`
- `server/tests/unit/game/npcs/test_attack_damage.py`

## Audit Trail

- EXTRACTED: 41 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*