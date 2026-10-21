# PlayerEventHandlerUtils

> 131 nodes · cohesion 0.03

## Key Concepts

- **NPCCombatIntegration** (99 connections) — `server/npc/combat_integration.py`
- **test_npc_combat_integration_class.py** (46 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **combat_integration.py** (27 connections) — `server/npc/combat_integration.py`
- **test_combat_integration_base.py** (24 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **NPCAttacked** (14 connections) — `server/events/event_types.py`
- **asyncio** (13 connections)
- **asyncio** (11 connections)
- **._build_player_attacked_event()** (8 connections) — `server/npc/combat_integration.py`
- **_resolve_npc_combat_service_raw()** (7 connections) — `server/npc/combat_integration_base.py`
- **._calculate_max_dp()** (6 connections) — `server/npc/combat_integration.py`
- **._compute_dp_update_fields()** (6 connections) — `server/npc/combat_integration.py`
- **._get_int_stat()** (5 connections) — `server/npc/combat_integration.py`
- **._get_npc_display_name()** (5 connections) — `server/npc/combat_integration.py`
- **._get_npc_lifecycle_manager()** (5 connections) — `server/npc/combat_integration.py`
- **._publish_npc_attack_to_nats()** (5 connections) — `server/npc/combat_integration.py`
- **._publish_player_dp_updated_after_npc_damage()** (5 connections) — `server/npc/combat_integration.py`
- **._publish_player_dp_updated_event()** (5 connections) — `server/npc/combat_integration.py`
- **UUID** (5 connections)
- **test_apply_combat_effects_validation_error()** (5 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **integration()** (5 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **.get_combat_stats()** (4 connections) — `server/npc/combat_integration.py`
- **._get_npc_name_from_lifecycle()** (4 connections) — `server/npc/combat_integration.py`
- **._get_player_and_stats_for_nats()** (4 connections) — `server/npc/combat_integration.py`
- **._get_player_combat_stats()** (4 connections) — `server/npc/combat_integration.py`
- **._get_player_for_dp_update()** (4 connections) — `server/npc/combat_integration.py`
- *... and 106 more nodes in this community*

## Relationships

- [BaseEvent](BaseEvent.md) (16 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (8 shared connections)
- [get_username_from_user](get_username_from_user.md) (5 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (5 shared connections)
- [RoomLoader](RoomLoader.md) (5 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (4 shared connections)
- [utils/layout.ts](utils-layout.ts.md) (3 shared connections)
- [CombatInstance](CombatInstance.md) (3 shared connections)
- [Room](Room.md) (3 shared connections)
- [quest_rewards.py](quest_rewards.py.md) (2 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/npc/combat_integration.py`
- `server/npc/combat_integration_base.py`
- `server/npc/npc_base.py`
- `server/tests/unit/npc/test_combat_integration_base.py`
- `server/tests/unit/npc/test_npc_combat_integration_class.py`

## Audit Trail

- EXTRACTED: 238 (78%)
- INFERRED: 69 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*