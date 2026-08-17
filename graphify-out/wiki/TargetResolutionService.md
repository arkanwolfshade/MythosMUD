# TargetResolutionService

> 125 nodes

## Key Concepts

- **TargetResolutionService** (50 connections) — `server/services/target_resolution_service.py`
- **test_target_resolution_service.py** (41 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **asyncio** (21 connections)
- **TargetMetadata** (14 connections) — `server/schemas/shared/target_metadata.py`
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
- **UUID** (6 connections)
- **PlayerServiceProtocol** (5 connections) — `server/services/target_resolution_service.py`
- **.get_player_by_id()** (5 connections) — `server/services/target_resolution_service.py`
- **._add_disambiguation_suffixes()** (5 connections) — `server/services/target_resolution_service.py`
- **._build_target_result()** (5 connections) — `server/services/target_resolution_service.py`
- **._fetch_players_in_room()** (5 connections) — `server/services/target_resolution_service.py`
- **._get_npc_instance()** (5 connections) — `server/services/target_resolution_service.py`
- **._get_npcs_from_lifecycle_manager()** (5 connections) — `server/services/target_resolution_service.py`
- **test_add_disambiguation_suffixes()** (5 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_build_target_result_disambiguation_suffix_match()** (5 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_build_target_result_single_match()** (5 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- *... and 100 more nodes in this community*

## Relationships

- [TargetType](TargetType.md) (14 shared connections)
- [TargetMatch](TargetMatch.md) (11 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [test_party_commands.py](test_party_commands.py.md) (3 shared connections)
- [PlayerService](PlayerService.md) (2 shared connections)
- [handle_teach_command](handle_teach_command.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [SpellTargetingService](SpellTargetingService.md) (2 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (2 shared connections)
- [NPCBase](NPCBase.md) (2 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (1 shared connections)
- [CombatValidator](CombatValidator.md) (1 shared connections)

## Source Files

- `server/schemas/shared/target_metadata.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/services/test_target_resolution_service.py`

## Audit Trail

- EXTRACTED: 214 (86%)
- INFERRED: 34 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*