# TargetResolutionService

> 102 nodes

## Key Concepts

- **TargetResolutionService** (50 connections) — `server/services/target_resolution_service.py`
- **TargetType** (41 connections) — `server/schemas/shared/target_resolution.py`
- **target_resolution_service.py** (29 connections) — `server/services/target_resolution_service.py`
- **spell_targeting.py** (25 connections) — `server/game/magic/spell_targeting.py`
- **test_party_commands.py** (23 connections) — `server/tests/unit/commands/test_party_commands.py`
- **handle_party_command()** (21 connections) — `server/commands/party_commands.py`
- **party_commands.py** (21 connections) — `server/commands/party_commands.py`
- **follow_commands.py** (18 connections) — `server/commands/follow_commands.py`
- **schemas/shared/__init__.py** (16 connections) — `server/schemas/shared/__init__.py`
- **teach_command.py** (15 connections) — `server/commands/teach_command.py`
- **TargetMetadata** (14 connections) — `server/schemas/shared/target_metadata.py`
- **asyncio** (13 connections)
- **target_resolution.py** (12 connections) — `server/schemas/shared/target_resolution.py`
- **_party_request()** (11 connections) — `server/tests/unit/commands/test_party_commands.py`
- **Any** (9 connections)
- **._search_npcs_in_room()** (8 connections) — `server/services/target_resolution_service.py`
- **_handle_party_chat()** (7 connections) — `server/commands/party_commands.py`
- **._match_npcs_by_name()** (7 connections) — `server/services/target_resolution_service.py`
- **._search_players_in_room()** (7 connections) — `server/services/target_resolution_service.py`
- **_get_member_display()** (6 connections) — `server/commands/party_commands.py`
- **_get_party_command_context()** (6 connections) — `server/commands/party_commands.py`
- **.get_room_by_id()** (6 connections) — `server/services/target_resolution_service.py`
- **._load_npc_ids_with_room_fallback()** (6 connections) — `server/services/target_resolution_service.py`
- **target_metadata.py** (6 connections) — `server/schemas/shared/target_metadata.py`
- **_get_container()** (5 connections) — `server/commands/party_commands.py`
- *... and 77 more nodes in this community*

## Relationships

- [TargetResolutionResult](TargetResolutionResult.md) (24 shared connections)
- [AliasStorage](AliasStorage.md) (22 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (17 shared connections)
- [get_logger](get_logger.md) (15 shared connections)
- [TargetMatch](TargetMatch.md) (11 shared connections)
- [test_target_resolution_service.py](test_target_resolution_service.py.md) (10 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (9 shared connections)
- [handle_teach_command](handle_teach_command.md) (7 shared connections)
- [asyncio](asyncio.md) (5 shared connections)
- [DatabaseError](DatabaseError.md) (4 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (4 shared connections)
- [Spell](Spell.md) (3 shared connections)

## Source Files

- `server/commands/follow_commands.py`
- `server/commands/party_commands.py`
- `server/commands/teach_command.py`
- `server/game/magic/spell_targeting.py`
- `server/schemas/shared/__init__.py`
- `server/schemas/shared/target_metadata.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/commands/test_party_commands.py`

## Audit Trail

- EXTRACTED: 334 (91%)
- INFERRED: 32 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*