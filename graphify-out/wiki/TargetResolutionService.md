# TargetResolutionService

> 151 nodes

## Key Concepts

- **TargetResolutionService** (51 connections) — `server/services/target_resolution_service.py`
- **TargetType** (45 connections) — `server/schemas/shared/target_resolution.py`
- **test_target_resolution_service.py** (43 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **target_resolution_service.py** (29 connections) — `server/services/target_resolution_service.py`
- **asyncio** (21 connections)
- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **TargetMetadata** (15 connections) — `server/schemas/shared/target_metadata.py`
- **teach_command.py** (15 connections) — `server/commands/teach_command.py`
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
- **target_metadata.py** (6 connections) — `server/schemas/shared/target_metadata.py`
- **PlayerServiceProtocol** (5 connections) — `server/services/target_resolution_service.py`
- **.get_player_by_id()** (5 connections) — `server/services/target_resolution_service.py`
- **._add_disambiguation_suffixes()** (5 connections) — `server/services/target_resolution_service.py`
- **._build_target_result()** (5 connections) — `server/services/target_resolution_service.py`
- *... and 126 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (18 shared connections)
- [TargetResolutionResult](TargetResolutionResult.md) (14 shared connections)
- [handle_teach_command](handle_teach_command.md) (7 shared connections)
- [test_party_commands.py](test_party_commands.py.md) (6 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (5 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (5 shared connections)
- [Spell](Spell.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [event_types.py](event_types.py.md) (4 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (4 shared connections)
- [combat_attack.py](combat_attack.py.md) (3 shared connections)
- [run_flee_effect](run_flee_effect.md) (3 shared connections)

## Source Files

- `server/commands/teach_command.py`
- `server/schemas/shared/target_metadata.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/schemas/test_target_resolution.py`
- `server/tests/unit/services/test_target_resolution_service.py`

## Audit Trail

- EXTRACTED: 332 (92%)
- INFERRED: 28 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*