# room conftest toolkit

> 22 nodes

## Key Concepts

- **NPCCombatIntegration** (103 connections) — `server/npc/combat_integration.py`
- **test_combat_integration_base.py** (24 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **_resolve_npc_combat_service_raw()** (7 connections) — `server/npc/combat_integration_base.py`
- **integration()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_combat_effects_validation_error()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
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
- **Integrates NPCs with the existing combat and game mechanics systems.      Extend** (1 connections) — `server/npc/combat_integration.py`
- **Return the live NPC combat integration service for delegation.      Prefer ``C** (1 connections) — `server/npc/combat_integration_base.py`
- **Unit tests for NPCCombatIntegrationBase helpers.** (1 connections) — `server/tests/unit/npc/test_combat_integration_base.py`

## Relationships

- [services nats service](services_nats_service.md) (26 shared connections)
- [models npc rationale](models_npc_rationale.md) (9 shared connections)
- [message queue realtime](message_queue_realtime.md) (7 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (6 shared connections)
- [memory lifespan app](memory_lifespan_app.md) (5 shared connections)
- [schemas items item](schemas_items_item.md) (4 shared connections)
- [event bus events](event_bus_events.md) (4 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (3 shared connections)
- [npc aggressive mob](npc_aggressive_mob.md) (3 shared connections)
- [player death service](player_death_service.md) (2 shared connections)
- [attack combat commands](attack_combat_commands.md) (2 shared connections)
- [lucidity event services](lucidity_event_services.md) (2 shared connections)

## Source Files

- `server/npc/combat_integration.py`
- `server/npc/combat_integration_base.py`
- `server/tests/unit/npc/test_combat_integration_base.py`

## Audit Trail

- EXTRACTED: 160 (94%)
- INFERRED: 11 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*