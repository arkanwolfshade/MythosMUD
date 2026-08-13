# test_npc_combat_integration_class.py

> 36 nodes

## Key Concepts

- **test_npc_combat_integration_class.py** (23 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_combat_stats_for_player()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_combat_stats_npc_only_normalized()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_handle_npc_death_with_killer_applies_mechanics()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **mock_persistence()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_calculate_damage_physical_strength_bonus()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_calculate_damage_weapon_type_no_strength_bonus()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_calculate_max_dp_from_constitution_and_size()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_compute_dp_update_fields()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_derive_npc_name_from_id()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_int_stat_parses_numeric_string()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_name_from_lifecycle_reads_active_instance()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_name_from_lifecycle_returns_none_when_missing()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_stats_defaults()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_stats_preserves_values()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_normalize_npc_stats_adds_hp_from_determination_points()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_publish_attack_event_emits_npc_attacked()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **asyncio** (3 connections)
- **fixture** (2 connections)
- **Unit tests for server.npc.combat_integration.NPCCombatIntegration (helpers and…** (1 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **Invalid UUID with npc_stats returns normalized NPC stats.** (1 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **Killer path loads player and calls game mechanics helpers.** (1 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **After damage, old_dp reflects pre-hit value.** (1 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **Display name resolves from lifecycle_manager.active_npcs when present.** (1 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **When lifecycle manager is unavailable, display name lookup returns None.** (1 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- *... and 11 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (19 shared connections)
- [event_types.py](event_types.py.md) (3 shared connections)

## Source Files

- `server/tests/unit/npc/test_npc_combat_integration_class.py`

## Audit Trail

- EXTRACTED: 59 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*