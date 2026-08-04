# target resolution service

> 167 nodes

## Key Concepts

- **TargetResolutionService** (53 connections) — `server/services/target_resolution_service.py`
- **TargetResolutionResult** (42 connections) — `server/schemas/shared/target_resolution.py`
- **test_target_resolution_service.py** (40 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **TargetType** (39 connections) — `server/schemas/shared/target_resolution.py`
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
- *... and 142 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (34 shared connections)
- [spell game magic](spell_game_magic.md) (31 shared connections)
- [commands position system](commands_position_system.md) (10 shared connections)
- [models player related](models_player_related.md) (6 shared connections)
- [services ascii map](services_ascii_map.md) (5 shared connections)
- [game models player](game_models_player.md) (5 shared connections)
- [logging file setup](logging_file_setup.md) (4 shared connections)
- [uuid npc combat](uuid_npc_combat.md) (4 shared connections)
- [message filtering helpers](message_filtering_helpers.md) (3 shared connections)
- [party service game](party_service_game.md) (3 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)

## Source Files

- `server/schemas/shared/__init__.py`
- `server/schemas/shared/target_metadata.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/schemas/test_target_resolution.py`
- `server/tests/unit/services/test_target_resolution_service.py`

## Audit Trail

- EXTRACTED: 588 (94%)
- INFERRED: 35 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*