# Emote Schema Validator

> 98 nodes · cohesion 0.03

## Key Concepts

- **SchemaValidator** (30 connections) — `schemas/validator.py`
- **emote_service.py** (18 connections) — `server/game/emote_service.py`
- **validate_room_data()** (15 connections) — `server/world_loader.py`
- **world_loader.py** (14 connections) — `server/world_loader.py`
- **get_room_environment()** (13 connections) — `server/world_loader.py`
- **TestGetRoomEnvironment** (12 connections) — `server/tests/unit/test_world_loader.py`
- **TestValidateRoomData** (11 connections) — `server/tests/unit/test_world_loader.py`
- **create_validator()** (10 connections) — `schemas/validator.py`
- **test_world_loader.py** (10 connections) — `server/tests/unit/test_world_loader.py`
- **generate_room_id()** (9 connections) — `server/world_loader.py`
- **schema_validator.py** (8 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **_get_alias_validator()** (8 connections) — `server/alias_storage.py`
- **validator.py** (7 connections) — `schemas/validator.py`
- **Any** (7 connections) — `schemas/validator.py`
- **TestGenerateRoomId** (7 connections) — `server/tests/unit/test_world_loader.py`
- **.validate_data()** (6 connections) — `schemas/validator.py`
- **.validate_room()** (6 connections) — `schemas/validator.py`
- **EmoteDefinition** (5 connections) — `server/game/emote_service.py`
- **_EmoteLoadResult** (4 connections) — `server/game/emote_service.py`
- **_get_emote_validator()** (4 connections) — `server/game/emote_service.py`
- **.__init__()** (4 connections) — `schemas/validator.py`
- **.validate_alias_bundle()** (4 connections) — `schemas/validator.py`
- **.validate_emote_file()** (4 connections) — `schemas/validator.py`
- **.validate_room_database()** (4 connections) — `schemas/validator.py`
- **.validate_room_file()** (4 connections) — `schemas/validator.py`
- *... and 73 more nodes in this community*

## Relationships

- [[NPC Admin API]] (22 shared connections)
- [[Alias Expansion Logic]] (9 shared connections)
- [[Room Schema Validator]] (5 shared connections)
- [[Chat Message Helpers]] (3 shared connections)
- [[Dependency Risk Analyzer]] (3 shared connections)
- [[Alias Storage Layer]] (3 shared connections)
- [[Room Fixer Toolkit]] (2 shared connections)
- [[Lucidity Rate Overrides]] (2 shared connections)
- [[Hierarchical Schema Tests]] (1 shared connections)
- [[Command Input Utilities]] (1 shared connections)
- [[Game Emote Service]] (1 shared connections)
- [[Alias Storage]] (1 shared connections)

## Source Files

- `schemas/validator.py`
- `server/alias_storage.py`
- `server/game/emote_service.py`
- `server/tests/unit/test_world_loader.py`
- `server/world_loader.py`
- `tools/room_toolkit/room_validator/core/schema_validator.py`

## Audit Trail

- EXTRACTED: 336 (94%)
- INFERRED: 22 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
