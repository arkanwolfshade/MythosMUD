# test_publish_attack_event_emits_npc_attacked

> 12 nodes

## Key Concepts

- **test_publish_attack_event_emits_npc_attacked()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_calculate_max_dp_from_constitution_and_size()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_derive_npc_name_from_id()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_stats_defaults()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_stats_preserves_values()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_normalize_npc_stats_adds_hp_from_determination_points()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **_publish_attack_event forwards to event bus when configured.** (1 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **Empty npc_stats yields default strength/constitution.** (1 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **Provided npc_stats are returned as-is.** (1 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **First underscore segment title-cased.** (1 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **Fallback max_dp uses (con+siz)//5.** (1 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **hp alias filled from determination_points.** (1 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`

## Relationships

- [test_npc_combat_integration_class.py](test_npc_combat_integration_class.py.md) (6 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (6 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/tests/unit/npc/test_npc_combat_integration_class.py`

## Audit Trail

- EXTRACTED: 12 (63%)
- INFERRED: 7 (37%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*