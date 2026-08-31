# PlayerCombatService

> 257 nodes

## Key Concepts

- **PlayerCombatService** (76 connections) — `server/services/player_combat_service.py`
- **test_movement_service.py** (52 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_player_combat_service.py** (38 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **movement_service.py** (36 connections) — `server/game/movement_service.py`
- **player_combat_service.py** (36 connections) — `server/services/player_combat_service.py`
- **spell_targeting.py** (25 connections) — `server/game/magic/spell_targeting.py`
- **asyncio** (22 connections)
- **player_combat_service_support.py** (20 connections) — `server/services/player_combat_service_support.py`
- **asyncio** (20 connections)
- **movement_helpers.py** (17 connections) — `server/game/movement_helpers.py`
- **UUID** (15 connections)
- **PlayerCombatState** (14 connections) — `server/services/player_combat_service.py`
- **validate_exit()** (11 connections) — `server/game/movement_helpers.py`
- **validate_player_room_membership()** (11 connections) — `server/game/movement_helpers.py`
- **check_combat_state()** (10 connections) — `server/game/movement_helpers.py`
- **check_player_posture()** (8 connections) — `server/game/movement_helpers.py`
- **NPCCombatIntegrationReadApi** (7 connections) — `server/services/player_combat_service_support.py`
- **._award_xp_via_persistence_fallback()** (7 connections) — `server/services/player_combat_service.py`
- **player_combat_service()** (7 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **EventBusPublish** (6 connections) — `server/services/player_combat_service_support.py`
- **PlayerXpLike** (6 connections) — `server/services/player_combat_service_support.py`
- **extract_player_id()** (6 connections) — `server/game/movement_helpers.py`
- **.award_xp_on_npc_death()** (6 connections) — `server/services/player_combat_service.py`
- **Protocol** (6 connections)
- **NPCCombatRewardsLike** (5 connections) — `server/services/player_combat_service_support.py`
- *... and 232 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (14 shared connections)
- [event_types.py](event_types.py.md) (12 shared connections)
- [MovementService](MovementService.md) (11 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (9 shared connections)
- [CombatService](CombatService.md) (8 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (7 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (6 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (6 shared connections)
- [ValidationError](ValidationError.md) (6 shared connections)
- [SpellTargetingService](SpellTargetingService.md) (4 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)

## Source Files

- `server/game/magic/spell_targeting.py`
- `server/game/movement_helpers.py`
- `server/game/movement_service.py`
- `server/services/combat_service.py`
- `server/services/player_combat_service.py`
- `server/services/player_combat_service_support.py`
- `server/tests/unit/game/test_movement_service.py`
- `server/tests/unit/services/test_player_combat_service.py`

## Audit Trail

- EXTRACTED: 496 (91%)
- INFERRED: 52 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*