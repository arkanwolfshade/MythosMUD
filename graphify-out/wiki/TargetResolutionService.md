# TargetResolutionService

> 170 nodes

## Key Concepts

- **TargetResolutionService** (50 connections) — `server/services/target_resolution_service.py`
- **TargetType** (41 connections) — `server/schemas/shared/target_resolution.py`
- **test_target_resolution_service.py** (41 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **TargetResolutionResult** (34 connections) — `server/schemas/shared/target_resolution.py`
- **target_resolution_service.py** (29 connections) — `server/services/target_resolution_service.py`
- **asyncio** (21 connections)
- **schemas/shared/__init__.py** (16 connections) — `server/schemas/shared/__init__.py`
- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **teach_command.py** (15 connections) — `server/commands/teach_command.py`
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
- **.get_player_by_id()** (5 connections) — `server/services/target_resolution_service.py`
- *... and 145 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (29 shared connections)
- [get_username_from_user](get_username_from_user.md) (11 shared connections)
- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (9 shared connections)
- [SpellEffectType](SpellEffectType.md) (8 shared connections)
- [test_party_commands.py](test_party_commands.py.md) (7 shared connections)
- [handle_teach_command](handle_teach_command.md) (7 shared connections)
- [test_combat_handler.py](test_combat_handler.py.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (4 shared connections)
- [PlayerService](PlayerService.md) (4 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (4 shared connections)
- [run_flee_effect](run_flee_effect.md) (3 shared connections)

## Source Files

- `server/commands/teach_command.py`
- `server/schemas/shared/__init__.py`
- `server/schemas/shared/target_metadata.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/schemas/test_target_resolution.py`
- `server/tests/unit/services/test_target_resolution_service.py`

## Audit Trail

- EXTRACTED: 372 (91%)
- INFERRED: 38 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*