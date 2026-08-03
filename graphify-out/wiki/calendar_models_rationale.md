# calendar models rationale

> 11 nodes

## Key Concepts

- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **TargetMetadata** (12 connections) — `server/schemas/shared/target_metadata.py`
- **target_metadata.py** (5 connections) — `server/schemas/shared/target_metadata.py`
- **test_target_match()** (4 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **test_target_type_enum()** (2 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **BaseModel** (1 connections)
- **Target metadata schema for MythosMUD.  This module defines Pydantic models for t** (1 connections) — `server/schemas/shared/target_metadata.py`
- **Metadata about a target in target resolution.      This model represents additio** (1 connections) — `server/schemas/shared/target_metadata.py`
- **Unit tests for target_resolution schemas.  Tests the Pydantic models in target_r** (1 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **Test TargetType enum values.** (1 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **Test TargetMatch can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_target_resolution.py`

## Relationships

- [combat commands handler](combat_commands_handler.md) (9 shared connections)
- [Item Instances](Item_Instances.md) (4 shared connections)
- [spell game magic](spell_game_magic.md) (4 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [target resolution service](target_resolution_service.md) (2 shared connections)

## Source Files

- `server/schemas/shared/target_metadata.py`
- `server/tests/unit/schemas/test_target_resolution.py`

## Audit Trail

- EXTRACTED: 40 (89%)
- INFERRED: 5 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*