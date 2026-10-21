# Phase 3, Task 3.2: NATS Subject Manager Usage Review

> 36 nodes · cohesion 0.06

## Key Concepts

- **required** (8 connections) — `db/static/schemas/room.schema.json`
- **required** (8 connections) — `schemas/intersection_schema.json`
- **required** (8 connections) — `schemas/room_schema.json`
- **required** (8 connections) — `schemas/unified_room_schema.json`
- **required** (8 connections) — `tools/room_toolkit/room_validator/schemas/unified_room_schema.json`
- **required** (5 connections) — `tools/room_toolkit/room_validator/schemas/room_hierarchy_schema.json`
- **exits** (1 connections) — `db/static/schemas/room.schema.json`
- **id** (1 connections) — `db/static/schemas/room.schema.json`
- **name** (1 connections) — `db/static/schemas/room.schema.json`
- **plane** (1 connections) — `db/static/schemas/room.schema.json`
- **zone** (1 connections) — `db/static/schemas/room.schema.json`
- **exits** (1 connections) — `schemas/intersection_schema.json`
- **id** (1 connections) — `schemas/intersection_schema.json`
- **name** (1 connections) — `schemas/intersection_schema.json`
- **plane** (1 connections) — `schemas/intersection_schema.json`
- **zone** (1 connections) — `schemas/intersection_schema.json`
- **description** (1 connections) — `schemas/room_schema.json`
- **exits** (1 connections) — `schemas/room_schema.json`
- **id** (1 connections) — `schemas/room_schema.json`
- **name** (1 connections) — `schemas/room_schema.json`
- **plane** (1 connections) — `schemas/room_schema.json`
- **sub_zone** (1 connections) — `schemas/room_schema.json`
- **zone** (1 connections) — `schemas/room_schema.json`
- **exits** (1 connections) — `schemas/unified_room_schema.json`
- **id** (1 connections) — `schemas/unified_room_schema.json`
- *... and 11 more nodes in this community*

## Relationships

- [test_quality_fragmentation_guard.py](test_quality_fragmentation_guard.py.md) (1 shared connections)
- [NPCCommunicationIntegration](NPCCommunicationIntegration.md) (1 shared connections)
- [test_lifespan_shutdown.py](test_lifespan_shutdown.py.md) (1 shared connections)
- [DialogueEditorPage.tsx](DialogueEditorPage.tsx.md) (1 shared connections)
- [ProfessionCacheService](ProfessionCacheService.md) (1 shared connections)
- [GameTickService](GameTickService.md) (1 shared connections)

## Source Files

- `db/static/schemas/room.schema.json`
- `schemas/intersection_schema.json`
- `schemas/room_schema.json`
- `schemas/unified_room_schema.json`
- `tools/room_toolkit/room_validator/schemas/room_hierarchy_schema.json`
- `tools/room_toolkit/room_validator/schemas/unified_room_schema.json`

## Audit Trail

- EXTRACTED: 45 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*