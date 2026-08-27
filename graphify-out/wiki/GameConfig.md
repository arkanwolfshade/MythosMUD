# GameConfig

> 42 nodes

## Key Concepts

- **NPCCombatIntegrationBase** (25 connections) — `server/npc/combat_integration_base.py`
- **._perform_direct_npc_attack()** (10 connections) — `server/npc/combat_integration_base.py`
- **.apply_combat_effects()** (8 connections) — `server/npc/combat_integration_base.py`
- **._apply_player_combat_effects()** (8 connections) — `server/npc/combat_integration_base.py`
- **._is_target_in_login_grace_period()** (7 connections) — `server/npc/combat_integration_base.py`
- **._convert_target_id_to_uuid()** (6 connections) — `server/npc/combat_integration_base.py`
- **._handle_npc_attack_core()** (6 connections) — `server/npc/combat_integration_base.py`
- **._try_delegate_npc_attack_to_combat_service()** (5 connections) — `server/npc/combat_integration_base.py`
- **._handle_attribute_error()** (4 connections) — `server/npc/combat_integration_base.py`
- **._handle_unexpected_error()** (4 connections) — `server/npc/combat_integration_base.py`
- **._handle_validation_error()** (4 connections) — `server/npc/combat_integration_base.py`
- **._apply_mental_effects()** (3 connections) — `server/npc/combat_integration_base.py`
- **.calculate_damage()** (3 connections) — `server/npc/combat_integration_base.py`
- **._get_npc_stats()** (3 connections) — `server/npc/combat_integration_base.py`
- **._get_target_stats()** (3 connections) — `server/npc/combat_integration_base.py`
- **.handle_npc_attack()** (3 connections) — `server/npc/combat_integration_base.py`
- **._publish_attack_event()** (3 connections) — `server/npc/combat_integration_base.py`
- **._publish_npc_attack_to_nats()** (3 connections) — `server/npc/combat_integration_base.py`
- **._publish_player_dp_updated_after_npc_damage()** (3 connections) — `server/npc/combat_integration_base.py`
- **ABC** (2 connections)
- **UUID** (2 connections)
- **Exception** (1 connections)
- **ValidationError** (1 connections)
- **Apply combat effects to a target (player or NPC). Args: target_id: ID of the…** (1 connections) — `server/npc/combat_integration_base.py`
- **Convert target_id to UUID, accepting either string or UUID input.** (1 connections) — `server/npc/combat_integration_base.py`
- *... and 17 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (6 shared connections)
- [test_container_persistence_extended_crud.py](test_container_persistence_extended_crud.py.md) (2 shared connections)
- [MemoryProfiler](MemoryProfiler.md) (2 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)
- [test_movement_monitor.py](test_movement_monitor.py.md) (1 shared connections)
- [playerHandlers.ts](playerHandlers.ts.md) (1 shared connections)
- [🔴 CRITICAL ISSUES](🔴_CRITICAL_ISSUES.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [PostgresCursor](PostgresCursor.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration_base.py`

## Audit Trail

- EXTRACTED: 73 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*