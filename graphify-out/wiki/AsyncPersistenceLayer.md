# AsyncPersistenceLayer

> 746 nodes

## Key Concepts

- **AsyncPersistenceLayer** (167 connections) — `server/async_persistence.py`
- **CombatService** (165 connections) — `server/services/combat_service.py`
- **get_config()** (105 connections) — `server/config/__init__.py`
- **combat_service.py** (99 connections) — `server/services/combat_service.py`
- **async_persistence.py** (84 connections) — `server/async_persistence.py`
- **PlayerCombatService** (76 connections) — `server/services/player_combat_service.py`
- **Room** (73 connections) — `server/models/room.py`
- **api/monitoring.py** (64 connections) — `server/api/monitoring.py`
- **models/combat.py** (58 connections) — `server/models/combat.py`
- **npc_combat_integration_service.py** (53 connections) — `server/services/npc_combat_integration_service.py`
- **test_movement_service.py** (52 connections) — `server/tests/unit/game/test_movement_service.py`
- **CombatCommandHandler** (51 connections) — `server/commands/combat_handler.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **combat_turn_participant_actions.py** (47 connections) — `server/services/combat_turn_participant_actions.py`
- **CombatParticipantType** (44 connections) — `server/models/combat.py`
- **CombatParticipantData** (37 connections) — `server/services/combat_types.py`
- **player_combat_service.py** (36 connections) — `server/services/player_combat_service.py`
- **movement_service.py** (35 connections) — `server/game/movement_service.py`
- **models/room.py** (32 connections) — `server/models/room.py`
- **test_room_class.py** (30 connections) — `server/tests/unit/models/test_room_class.py`
- **player_disconnect_handlers.py** (29 connections) — `server/realtime/player_disconnect_handlers.py`
- **combat_service_start.py** (28 connections) — `server/services/combat_service_start.py`
- **monitoring_models.py** (23 connections) — `server/api/monitoring_models.py`
- **combat_event_publisher.py** (23 connections) — `server/services/combat_event_publisher.py`
- **combat_death_handler.py** (22 connections) — `server/services/combat_death_handler.py`
- *... and 721 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (144 shared connections)
- [ConnectionManager](ConnectionManager.md) (102 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (74 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (60 shared connections)
- [DatabaseError](DatabaseError.md) (51 shared connections)
- [UUID](UUID.md) (47 shared connections)
- [test_monitoring_endpoints.py](test_monitoring_endpoints.py.md) (44 shared connections)
- [AliasStorage](AliasStorage.md) (42 shared connections)
- [CombatParticipant](CombatParticipant.md) (42 shared connections)
- [CombatInstance](CombatInstance.md) (40 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (30 shared connections)
- [combat_service_npc.py](combat_service_npc.py.md) (25 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/api/monitoring_models.py`
- `server/app/game_tick_counter.py`
- `server/async_persistence.py`
- `server/commands/combat_handler.py`
- `server/config/__init__.py`
- `server/constants/spawn_defaults.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/events/combat_events.py`
- `server/game/instance_manager.py`
- `server/game/magic/spell_targeting.py`
- `server/game/movement_helpers.py`
- `server/game/movement_monitor.py`
- `server/game/movement_service.py`
- `server/models/combat.py`
- `server/models/room.py`
- `server/npc/combat_integration_protocols.py`
- `server/npc/movement_integration.py`
- `server/npc/spawning_request_execution.py`

## Audit Trail

- EXTRACTED: 2273 (88%)
- INFERRED: 303 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*