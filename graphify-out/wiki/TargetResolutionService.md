# TargetResolutionService

> 142 nodes

## Key Concepts

- **TargetResolutionService** (50 connections) — `server/services/target_resolution_service.py`
- **TargetType** (41 connections) — `server/schemas/shared/target_resolution.py`
- **test_target_resolution_service.py** (40 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **target_resolution_service.py** (28 connections) — `server/services/target_resolution_service.py`
- **asyncio** (21 connections)
- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **TargetMetadata** (14 connections) — `server/schemas/shared/target_metadata.py`
- **target_resolution.py** (11 connections) — `server/schemas/shared/target_resolution.py`
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
- **._get_npcs_from_lifecycle_manager()** (5 connections) — `server/services/target_resolution_service.py`
- *... and 117 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (19 shared connections)
- [TargetResolutionResult](TargetResolutionResult.md) (19 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [test_party_commands.py](test_party_commands.py.md) (6 shared connections)
- [magic_service.py](magic_service.py.md) (6 shared connections)
- [handle_teach_command](handle_teach_command.md) (5 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (4 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (3 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (3 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (3 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (3 shared connections)
- [magic_service_completion.py](magic_service_completion.py.md) (2 shared connections)

## Source Files

- `server/schemas/shared/target_metadata.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/schemas/test_target_resolution.py`
- `server/tests/unit/services/test_target_resolution_service.py`

## Audit Trail

- EXTRACTED: 299 (90%)
- INFERRED: 34 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*