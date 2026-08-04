# target resolution service

> 165 nodes

## Key Concepts

- **TargetResolutionService** (53 connections) — `server/services/target_resolution_service.py`
- **TargetResolutionResult** (42 connections) — `server/schemas/shared/target_resolution.py`
- **test_target_resolution_service.py** (40 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **target_resolution_service.py** (27 connections) — `server/services/target_resolution_service.py`
- **TargetMetadata** (16 connections) — `server/schemas/shared/target_metadata.py`
- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **__init__.py** (12 connections) — `server/schemas/shared/__init__.py`
- **target_resolution.py** (11 connections) — `server/schemas/shared/target_resolution.py`
- **.resolve_target()** (9 connections) — `server/services/target_resolution_service.py`
- **._search_npcs_in_room()** (8 connections) — `server/services/target_resolution_service.py`
- **PersistenceProtocol** (7 connections) — `server/services/target_resolution_service.py`
- **._gather_room_target_matches()** (7 connections) — `server/services/target_resolution_service.py`
- **._search_players_in_room()** (7 connections) — `server/services/target_resolution_service.py`
- **._match_npcs_by_name()** (7 connections) — `server/services/target_resolution_service.py`
- **UUID** (6 connections)
- **.get_room_by_id()** (6 connections) — `server/services/target_resolution_service.py`
- **._get_player_from_persistence()** (6 connections) — `server/services/target_resolution_service.py`
- **._validate_player_and_room()** (6 connections) — `server/services/target_resolution_service.py`
- **._load_npc_ids_with_room_fallback()** (6 connections) — `server/services/target_resolution_service.py`
- **target_metadata.py** (5 connections) — `server/schemas/shared/target_metadata.py`
- **.get_player_by_id()** (5 connections) — `server/services/target_resolution_service.py`
- **Player** (5 connections)
- **PlayerServiceProtocol** (5 connections) — `server/services/target_resolution_service.py`
- **._build_target_result()** (5 connections) — `server/services/target_resolution_service.py`
- **._fetch_players_in_room()** (5 connections) — `server/services/target_resolution_service.py`
- *... and 140 more nodes in this community*

## Relationships

- [spell game magic](spell_game_magic.md) (31 shared connections)
- [NPC Combat](NPC_Combat.md) (24 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (13 shared connections)
- [commands position system](commands_position_system.md) (8 shared connections)
- [npc population stats](npc_population_stats.md) (4 shared connections)
- [models player related](models_player_related.md) (4 shared connections)
- [message filtering helpers](message_filtering_helpers.md) (3 shared connections)
- [services ascii map](services_ascii_map.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (3 shared connections)
- [commands npc admin](commands_npc_admin.md) (3 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (2 shared connections)
- [combat models rationale](combat_models_rationale.md) (2 shared connections)

## Source Files

- `server/schemas/shared/__init__.py`
- `server/schemas/shared/target_metadata.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/schemas/test_target_resolution.py`
- `server/tests/unit/services/test_target_resolution_service.py`

## Audit Trail

- EXTRACTED: 550 (94%)
- INFERRED: 34 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*