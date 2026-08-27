# NPCCombatIntegration

> 140 nodes

## Key Concepts

- **NPCCombatIntegration** (99 connections) — `server/npc/combat_integration.py`
- **test_npc_combat_integration_class.py** (47 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **combat_integration.py** (27 connections) — `server/npc/combat_integration.py`
- **test_combat_integration_base.py** (25 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **aggressive_mob_npc.py** (19 connections) — `server/npc/aggressive_mob_npc.py`
- **NPCAttacked** (14 connections) — `server/events/event_types.py`
- **asyncio** (13 connections)
- **asyncio** (11 connections)
- **._build_player_attacked_event()** (8 connections) — `server/npc/combat_integration.py`
- **_resolve_npc_combat_service_raw()** (7 connections) — `server/npc/combat_integration_base.py`
- **._calculate_max_dp()** (6 connections) — `server/npc/combat_integration.py`
- **._compute_dp_update_fields()** (6 connections) — `server/npc/combat_integration.py`
- **._get_combat_event_publisher()** (6 connections) — `server/npc/combat_integration.py`
- **._get_int_stat()** (5 connections) — `server/npc/combat_integration.py`
- **._get_npc_display_name()** (5 connections) — `server/npc/combat_integration.py`
- **._get_npc_lifecycle_manager()** (5 connections) — `server/npc/combat_integration.py`
- **._publish_npc_attack_to_nats()** (5 connections) — `server/npc/combat_integration.py`
- **._publish_player_dp_updated_after_npc_damage()** (5 connections) — `server/npc/combat_integration.py`
- **._publish_player_dp_updated_event()** (5 connections) — `server/npc/combat_integration.py`
- **test_apply_combat_effects_validation_error()** (5 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **integration()** (5 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **UUID** (5 connections)
- **_RoomPersistence** (4 connections) — `server/npc/aggressive_mob_npc.py`
- **.get_combat_stats()** (4 connections) — `server/npc/combat_integration.py`
- **._get_npc_name_from_lifecycle()** (4 connections) — `server/npc/combat_integration.py`
- *... and 115 more nodes in this community*

## Relationships

- [NPCBase](NPCBase.md) (12 shared connections)
- [time.py](time.py.md) (8 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (7 shared connections)
- [EventBus](EventBus.md) (6 shared connections)
- [AggressiveMobNPC](AggressiveMobNPC.md) (4 shared connections)
- [event_types.py](event_types.py.md) (4 shared connections)
- [ValidationError](ValidationError.md) (4 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (3 shared connections)
- [get_username_from_user](get_username_from_user.md) (3 shared connections)
- [SpellEffects](SpellEffects.md) (3 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (3 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/npc/aggressive_mob_npc.py`
- `server/npc/combat_integration.py`
- `server/npc/combat_integration_base.py`
- `server/npc/npc_base.py`
- `server/tests/unit/npc/test_combat_integration_base.py`
- `server/tests/unit/npc/test_npc_combat_integration_class.py`

## Audit Trail

- EXTRACTED: 263 (79%)
- INFERRED: 70 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*