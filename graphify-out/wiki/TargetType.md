# TargetType

> 171 nodes

## Key Concepts

- **TargetType** (54 connections) — `server/schemas/shared/target_resolution.py`
- **TargetResolutionService** (52 connections) — `server/services/target_resolution_service.py`
- **test_target_resolution_service.py** (42 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **TargetResolutionResult** (38 connections) — `server/schemas/shared/target_resolution.py`
- **target_resolution_service.py** (29 connections) — `server/services/target_resolution_service.py`
- **asyncio** (21 connections)
- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **TargetMetadata** (15 connections) — `server/schemas/shared/target_metadata.py`
- **target_resolution.py** (14 connections) — `server/schemas/shared/target_resolution.py`
- **.resolve_target()** (9 connections) — `server/services/target_resolution_service.py`
- **._gather_room_target_matches()** (8 connections) — `server/services/target_resolution_service.py`
- **._search_npcs_in_room()** (8 connections) — `server/services/target_resolution_service.py`
- **PersistenceProtocol** (7 connections) — `server/services/target_resolution_service.py`
- **._match_npcs_by_name()** (7 connections) — `server/services/target_resolution_service.py`
- **._search_phantoms_in_room()** (7 connections) — `server/services/target_resolution_service.py`
- **._search_players_in_room()** (7 connections) — `server/services/target_resolution_service.py`
- **UUID** (7 connections)
- **._get_player_from_persistence()** (6 connections) — `server/services/target_resolution_service.py`
- **._load_npc_ids_with_room_fallback()** (6 connections) — `server/services/target_resolution_service.py`
- **._validate_player_and_room()** (6 connections) — `server/services/target_resolution_service.py`
- **PlayerServiceProtocol** (5 connections) — `server/services/target_resolution_service.py`
- **.get_room_by_id()** (5 connections) — `server/services/target_resolution_service.py`
- **._add_disambiguation_suffixes()** (5 connections) — `server/services/target_resolution_service.py`
- **._build_target_result()** (5 connections) — `server/services/target_resolution_service.py`
- **._fetch_players_in_room()** (5 connections) — `server/services/target_resolution_service.py`
- *... and 146 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (28 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (10 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (8 shared connections)
- [test_combat_handler.py](test_combat_handler.py.md) (8 shared connections)
- [party_commands.py](party_commands.py.md) (7 shared connections)
- [combat_assist.py](combat_assist.py.md) (7 shared connections)
- [handle_teach_command](handle_teach_command.md) (5 shared connections)
- [SpellEffects](SpellEffects.md) (5 shared connections)
- [SpellTargetingService](SpellTargetingService.md) (5 shared connections)
- [SpellEffectType](SpellEffectType.md) (4 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (4 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (4 shared connections)

## Source Files

- `server/schemas/shared/target_metadata.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/schemas/test_target_resolution.py`
- `server/tests/unit/services/test_target_resolution_service.py`

## Audit Trail

- EXTRACTED: 378 (92%)
- INFERRED: 33 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*