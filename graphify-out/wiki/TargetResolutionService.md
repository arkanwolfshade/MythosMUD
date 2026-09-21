# TargetResolutionService

> 131 nodes

## Key Concepts

- **TargetResolutionService** (50 connections) — `server/services/target_resolution_service.py`
- **test_target_resolution_service.py** (42 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **asyncio** (21 connections)
- **TargetMetadata** (15 connections) — `server/schemas/shared/target_metadata.py`
- **.resolve_target()** (9 connections) — `server/services/target_resolution_service.py`
- **._gather_room_target_matches()** (8 connections) — `server/services/target_resolution_service.py`
- **._search_npcs_in_room()** (8 connections) — `server/services/target_resolution_service.py`
- **PersistenceProtocol** (7 connections) — `server/services/target_resolution_service.py`
- **._match_npcs_by_name()** (7 connections) — `server/services/target_resolution_service.py`
- **._search_phantoms_in_room()** (7 connections) — `server/services/target_resolution_service.py`
- **._search_players_in_room()** (7 connections) — `server/services/target_resolution_service.py`
- **UUID** (7 connections)
- **.get_room_by_id()** (6 connections) — `server/services/target_resolution_service.py`
- **._get_player_from_persistence()** (6 connections) — `server/services/target_resolution_service.py`
- **._load_npc_ids_with_room_fallback()** (6 connections) — `server/services/target_resolution_service.py`
- **._validate_player_and_room()** (6 connections) — `server/services/target_resolution_service.py`
- **PlayerServiceProtocol** (5 connections) — `server/services/target_resolution_service.py`
- **._add_disambiguation_suffixes()** (5 connections) — `server/services/target_resolution_service.py`
- **._build_target_result()** (5 connections) — `server/services/target_resolution_service.py`
- **._fetch_players_in_room()** (5 connections) — `server/services/target_resolution_service.py`
- **._get_npcs_from_lifecycle_manager()** (5 connections) — `server/services/target_resolution_service.py`
- **test_add_disambiguation_suffixes()** (5 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_build_target_result_disambiguation_suffix_match()** (5 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_build_target_result_single_match()** (5 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **Player** (5 connections)
- *... and 106 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (12 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (9 shared connections)
- [TargetResolutionResult](TargetResolutionResult.md) (9 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (4 shared connections)
- [NPCBase](NPCBase.md) (3 shared connections)
- [test_party_commands.py](test_party_commands.py.md) (2 shared connections)
- [handle_teach_command](handle_teach_command.md) (2 shared connections)
- [get_config](get_config.md) (1 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (1 shared connections)
- [SpellTargetingService](SpellTargetingService.md) (1 shared connections)
- [CombatInstance](CombatInstance.md) (1 shared connections)

## Source Files

- `server/schemas/shared/target_metadata.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/services/test_target_resolution_service.py`

## Audit Trail

- EXTRACTED: 230 (90%)
- INFERRED: 26 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*