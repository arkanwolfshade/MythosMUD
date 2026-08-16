# TargetResolutionService

> 173 nodes

## Key Concepts

- **TargetResolutionService** (50 connections) — `server/services/target_resolution_service.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **TargetType** (41 connections) — `server/schemas/shared/target_resolution.py`
- **test_target_resolution_service.py** (41 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **TargetResolutionResult** (34 connections) — `server/schemas/shared/target_resolution.py`
- **target_resolution_service.py** (29 connections) — `server/services/target_resolution_service.py`
- **spell_targeting.py** (25 connections) — `server/game/magic/spell_targeting.py`
- **asyncio** (21 connections)
- **schemas/shared/__init__.py** (16 connections) — `server/schemas/shared/__init__.py`
- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **TargetMetadata** (14 connections) — `server/schemas/shared/target_metadata.py`
- **target_resolution.py** (12 connections) — `server/schemas/shared/target_resolution.py`
- **.resolve_target()** (9 connections) — `server/services/target_resolution_service.py`
- **._search_npcs_in_room()** (8 connections) — `server/services/target_resolution_service.py`
- **PersistenceProtocol** (7 connections) — `server/services/target_resolution_service.py`
- **._gather_room_target_matches()** (7 connections) — `server/services/target_resolution_service.py`
- **._match_npcs_by_name()** (7 connections) — `server/services/target_resolution_service.py`
- **._search_players_in_room()** (7 connections) — `server/services/target_resolution_service.py`
- **.get_room_by_id()** (6 connections) — `server/services/target_resolution_service.py`
- **._get_player_from_persistence()** (6 connections) — `server/services/target_resolution_service.py`
- **._load_npc_ids_with_room_fallback()** (6 connections) — `server/services/target_resolution_service.py`
- **._validate_player_and_room()** (6 connections) — `server/services/target_resolution_service.py`
- **target_metadata.py** (6 connections) — `server/schemas/shared/target_metadata.py`
- **UUID** (6 connections)
- **PlayerServiceProtocol** (5 connections) — `server/services/target_resolution_service.py`
- *... and 148 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (50 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (11 shared connections)
- [test_combat_handler.py](test_combat_handler.py.md) (7 shared connections)
- [test_party_commands.py](test_party_commands.py.md) (7 shared connections)
- [CombatInstance](CombatInstance.md) (7 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (6 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (6 shared connections)
- [handle_teach_command](handle_teach_command.md) (5 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (4 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (4 shared connections)
- [PlayerService](PlayerService.md) (4 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/game/magic/spell_targeting.py`
- `server/schemas/shared/__init__.py`
- `server/schemas/shared/target_metadata.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/schemas/test_target_resolution.py`
- `server/tests/unit/services/test_target_resolution_service.py`

## Audit Trail

- EXTRACTED: 423 (92%)
- INFERRED: 38 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*