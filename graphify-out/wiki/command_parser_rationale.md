# command parser rationale

> 20 nodes

## Key Concepts

- **test_combat_integration_base.py** (24 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **_resolve_npc_combat_service_raw()** (7 connections) — `server/npc/combat_integration_base.py`
- **integration()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_combat_effects_attribute_error_raises()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_resolve_npc_combat_service_from_container()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_calculate_damage_minimum_on_bad_stats()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_combat_effects_npc_target()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_combat_effects_invalid_uuid_raises()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_combat_effects_player()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_convert_target_id_to_uuid()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_handle_unexpected_error_logs()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_is_target_in_login_grace_period_false()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_combat_effects_grace_period_blocks_damage()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_mental_effects_occult()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_handle_npc_attack_direct_path()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_calculate_damage_with_stats()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_perform_direct_npc_attack()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_handle_npc_attack_delegated()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **Return the live NPC combat integration service for delegation.      Prefer ``C** (1 connections) — `server/npc/combat_integration_base.py`
- **Unit tests for NPCCombatIntegrationBase helpers.** (1 connections) — `server/tests/unit/npc/test_combat_integration_base.py`

## Relationships

- [services nats service](services_nats_service.md) (16 shared connections)
- [Error Conversion](Error_Conversion.md) (5 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (1 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (1 shared connections)
- [tsconfig src/**/* spec](tsconfig_src-__-__spec.md) (1 shared connections)
- [add used user](add_used_user.md) (1 shared connections)
- [payload realtime optimizer](payload_realtime_optimizer.md) (1 shared connections)
- [room sync service](room_sync_service.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration_base.py`
- `server/tests/unit/npc/test_combat_integration_base.py`

## Audit Trail

- EXTRACTED: 64 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*