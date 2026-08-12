# TargetResolutionService

> 98 nodes

## Key Concepts

- **TargetResolutionService** (53 connections) — `server/services/target_resolution_service.py`
- **test_target_resolution_service.py** (27 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **asyncio** (20 connections)
- **.resolve_target()** (9 connections) — `server/services/target_resolution_service.py`
- **._search_npcs_in_room()** (8 connections) — `server/services/target_resolution_service.py`
- **PersistenceProtocol** (7 connections) — `server/services/target_resolution_service.py`
- **._gather_room_target_matches()** (7 connections) — `server/services/target_resolution_service.py`
- **._search_players_in_room()** (7 connections) — `server/services/target_resolution_service.py`
- **.get_room_by_id()** (6 connections) — `server/services/target_resolution_service.py`
- **._get_player_from_persistence()** (6 connections) — `server/services/target_resolution_service.py`
- **._load_npc_ids_with_room_fallback()** (6 connections) — `server/services/target_resolution_service.py`
- **._validate_player_and_room()** (6 connections) — `server/services/target_resolution_service.py`
- **UUID** (6 connections)
- **PlayerServiceProtocol** (5 connections) — `server/services/target_resolution_service.py`
- **.__init__()** (5 connections) — `server/game/magic/spell_targeting.py`
- **.get_player_by_id()** (5 connections) — `server/services/target_resolution_service.py`
- **._add_disambiguation_suffixes()** (5 connections) — `server/services/target_resolution_service.py`
- **._fetch_players_in_room()** (5 connections) — `server/services/target_resolution_service.py`
- **._get_npcs_from_lifecycle_manager()** (5 connections) — `server/services/target_resolution_service.py`
- **Player** (5 connections)
- **.get_players_in_room()** (4 connections) — `server/services/target_resolution_service.py`
- **.__init__()** (4 connections) — `server/services/target_resolution_service.py`
- **._npc_ids_in_room_from_active_map()** (4 connections) — `server/services/target_resolution_service.py`
- **._validate_room_exists_async()** (4 connections) — `server/services/target_resolution_service.py`
- **target_service()** (4 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- *... and 73 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (18 shared connections)
- [magic_service.py](magic_service.py.md) (8 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (7 shared connections)
- [party_commands.py](party_commands.py.md) (3 shared connections)
- [get_username_from_user](get_username_from_user.md) (2 shared connections)
- [teach_command.py](teach_command.py.md) (2 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [CombatService](CombatService.md) (1 shared connections)
- [test_combat_flee_handler.py](test_combat_flee_handler.py.md) (1 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (1 shared connections)
- [Room](Room.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_targeting.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/services/test_target_resolution_service.py`

## Audit Trail

- EXTRACTED: 341 (95%)
- INFERRED: 18 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*