# test_combat_death_handler.py

> 69 nodes

## Key Concepts

- **test_combat_death_handler.py** (31 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **CombatDeathHandler** (22 connections) — `server/services/combat_death_handler.py`
- **asyncio** (11 connections)
- **._create_corpse_on_death()** (9 connections) — `server/services/combat_death_handler.py`
- **patch** (9 connections)
- **_CombatServiceDeps** (8 connections) — `server/services/combat_death_handler.py`
- **._handle_npc_death()** (8 connections) — `server/services/combat_death_handler.py`
- **._handle_player_death_events()** (7 connections) — `server/services/combat_death_handler.py`
- **.handle_target_state_changes()** (6 connections) — `server/services/combat_death_handler.py`
- **._log_room_subscribers_before_npc_death()** (6 connections) — `server/services/combat_death_handler.py`
- **._publish_npc_death_event()** (6 connections) — `server/services/combat_death_handler.py`
- **._resolve_original_npc_id()** (6 connections) — `server/services/combat_death_handler.py`
- **_ConnectionManagerLike** (5 connections) — `server/services/combat_death_handler.py`
- **._resolve_connection_manager_for_corpse_creation()** (5 connections) — `server/services/combat_death_handler.py`
- **fixture** (5 connections)
- **_NPCCombatIntegrationLike** (4 connections) — `server/services/combat_death_handler.py`
- **.get_original_string_id()** (4 connections) — `server/services/combat_death_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_death_handler.py`
- **handler()** (3 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **npc_target()** (3 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **player_target()** (3 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **test_create_corpse_service_error()** (3 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **test_create_corpse_skips_without_persistence()** (3 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **test_create_corpse_success()** (3 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **test_handle_npc_death()** (3 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- *... and 44 more nodes in this community*

## Relationships

- [CombatParticipant](CombatParticipant.md) (11 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (10 shared connections)
- [CombatInstance](CombatInstance.md) (8 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [event_types.py](event_types.py.md) (2 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [CombatMessagingService](CombatMessagingService.md) (2 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (2 shared connections)
- [NATSError](NATSError.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)

## Source Files

- `server/services/combat_death_handler.py`
- `server/tests/unit/services/test_combat_death_handler.py`

## Audit Trail

- EXTRACTED: 133 (92%)
- INFERRED: 12 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*