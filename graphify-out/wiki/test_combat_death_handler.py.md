# test_combat_death_handler.py

> 58 nodes

## Key Concepts

- **test_combat_death_handler.py** (30 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **CombatDeathHandler** (20 connections) — `server/services/combat_death_handler.py`
- **.connection_manager()** (16 connections) — `server/services/combat_messaging/base.py`
- **asyncio** (11 connections)
- **._create_corpse_on_death()** (9 connections) — `server/services/combat_death_handler.py`
- **patch** (9 connections)
- **._handle_npc_death()** (8 connections) — `server/services/combat_death_handler.py`
- **._handle_player_death_events()** (6 connections) — `server/services/combat_death_handler.py`
- **._log_room_subscribers_before_npc_death()** (6 connections) — `server/services/combat_death_handler.py`
- **._publish_npc_death_event()** (6 connections) — `server/services/combat_death_handler.py`
- **._resolve_original_npc_id()** (6 connections) — `server/services/combat_death_handler.py`
- **.handle_target_state_changes()** (5 connections) — `server/services/combat_death_handler.py`
- **._resolve_connection_manager_for_corpse_creation()** (5 connections) — `server/services/combat_death_handler.py`
- **._resolve_connection_manager_from_container()** (5 connections) — `server/services/combat_messaging/base.py`
- **fixture** (5 connections)
- **.check_connection_state()** (4 connections) — `server/services/combat_cleanup_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_death_handler.py`
- **handler()** (3 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **npc_target()** (3 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **player_target()** (3 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **test_create_corpse_service_error()** (3 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **test_create_corpse_skips_without_persistence()** (3 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **test_create_corpse_success()** (3 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **test_handle_npc_death()** (3 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **test_handle_player_death_events_broadcast_error()** (3 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- *... and 33 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (11 shared connections)
- [CombatParticipant](CombatParticipant.md) (9 shared connections)
- [CombatInstance](CombatInstance.md) (8 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [NPCStartupService](NPCStartupService.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (2 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (2 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (2 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [CombatAttackHandler](CombatAttackHandler.md) (1 shared connections)

## Source Files

- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_messaging/base.py`
- `server/tests/unit/services/test_combat_death_handler.py`

## Audit Trail

- EXTRACTED: 121 (87%)
- INFERRED: 18 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*