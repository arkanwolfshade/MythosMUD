# player_combat_service.py

> 68 nodes

## Key Concepts

- **player_combat_service.py** (35 connections) — `server/services/player_combat_service.py`
- **movement_service.py** (34 connections) — `server/game/movement_service.py`
- **player_combat_service_support.py** (19 connections) — `server/services/player_combat_service_support.py`
- **movement_helpers.py** (16 connections) — `server/game/movement_helpers.py`
- **NPCCombatIntegrationReadApi** (10 connections) — `server/services/player_combat_service_support.py`
- **EventBusPublish** (9 connections) — `server/services/player_combat_service_support.py`
- **PlayerXpLike** (9 connections) — `server/services/player_combat_service_support.py`
- **validate_player_room_membership()** (8 connections) — `server/game/movement_helpers.py`
- **._validate_movement()** (8 connections) — `server/game/movement_service.py`
- **check_combat_state()** (7 connections) — `server/game/movement_helpers.py`
- **validate_exit()** (7 connections) — `server/game/movement_helpers.py`
- **NPCCombatRewardsLike** (6 connections) — `server/services/player_combat_service_support.py`
- **UUIDMappingXP** (6 connections) — `server/services/player_combat_service_support.py`
- **check_player_posture()** (6 connections) — `server/game/movement_helpers.py`
- **extract_player_id()** (6 connections) — `server/game/movement_helpers.py`
- **._validate_movement_rooms()** (6 connections) — `server/game/movement_service.py`
- **Protocol** (6 connections)
- **PersistenceWithNpcLifecycleManager** (5 connections) — `server/services/player_combat_service_support.py`
- **lifecycle_lookup_id()** (5 connections) — `server/services/player_combat_service_support.py`
- **log_missing_lifecycle_npc()** (5 connections) — `server/services/player_combat_service_support.py`
- **original_string_id_for_npc()** (5 connections) — `server/services/player_combat_service_support.py`
- **Any** (5 connections)
- **UUID** (5 connections)
- **._despawn_npc()** (4 connections) — `server/services/npc_combat_lifecycle.py`
- **async_load_lifecycle_manager()** (4 connections) — `server/services/player_combat_service_support.py`
- *... and 43 more nodes in this community*

## Relationships

- [get_npc_instance_service](get_npc_instance_service.md) (18 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (14 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (8 shared connections)
- [MovementService](MovementService.md) (7 shared connections)
- [ConnectionManager](ConnectionManager.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [BaseEvent](BaseEvent.md) (2 shared connections)

## Source Files

- `server/game/movement_helpers.py`
- `server/game/movement_service.py`
- `server/services/npc_combat_lifecycle.py`
- `server/services/player_combat_service.py`
- `server/services/player_combat_service_support.py`

## Audit Trail

- EXTRACTED: 283 (94%)
- INFERRED: 17 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*