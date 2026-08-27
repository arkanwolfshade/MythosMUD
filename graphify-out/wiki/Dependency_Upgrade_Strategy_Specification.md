# Dependency Upgrade Strategy Specification

> 25 nodes

## Key Concepts

- **enum** (8 connections) — `schemas/items/item_prototype.schema.json`
- **subzone_schema.json** (7 connections) — `tools/room_toolkit/room_validator/schemas/subzone_schema.json`
- **zone_schema.json** (7 connections) — `tools/room_toolkit/room_validator/schemas/zone_schema.json`
- **item_type** (3 connections) — `schemas/items/item_prototype.schema.json`
- **required** (3 connections) — `tools/room_toolkit/room_validator/schemas/zone_schema.json`
- **environment** (3 connections) — `schemas/items/item_prototype.schema.json`
- **required** (2 connections) — `tools/room_toolkit/room_validator/schemas/subzone_schema.json`
- **consumable** (2 connections) — `schemas/items/item_prototype.schema.json`
- **type** (1 connections) — `schemas/items/item_prototype.schema.json`
- **additionalProperties** (1 connections) — `tools/room_toolkit/room_validator/schemas/subzone_schema.json`
- **description** (1 connections) — `tools/room_toolkit/room_validator/schemas/subzone_schema.json`
- **$schema** (1 connections) — `tools/room_toolkit/room_validator/schemas/subzone_schema.json`
- **title** (1 connections) — `tools/room_toolkit/room_validator/schemas/subzone_schema.json`
- **type** (1 connections) — `tools/room_toolkit/room_validator/schemas/subzone_schema.json`
- **additionalProperties** (1 connections) — `tools/room_toolkit/room_validator/schemas/zone_schema.json`
- **description** (1 connections) — `tools/room_toolkit/room_validator/schemas/zone_schema.json`
- **$schema** (1 connections) — `tools/room_toolkit/room_validator/schemas/zone_schema.json`
- **title** (1 connections) — `tools/room_toolkit/room_validator/schemas/zone_schema.json`
- **type** (1 connections) — `tools/room_toolkit/room_validator/schemas/zone_schema.json`
- **artifact** (1 connections) — `schemas/items/item_prototype.schema.json`
- **container** (1 connections) — `schemas/items/item_prototype.schema.json`
- **currency** (1 connections) — `schemas/items/item_prototype.schema.json`
- **equipment** (1 connections) — `schemas/items/item_prototype.schema.json`
- **quest** (1 connections) — `schemas/items/item_prototype.schema.json`
- **zone_type** (1 connections) — `tools/room_toolkit/room_validator/schemas/zone_schema.json`

## Relationships

- [Critical Coverage Gaps](Critical_Coverage_Gaps.md) (1 shared connections)
- [CommandRateLimiter](CommandRateLimiter.md) (1 shared connections)
- [_make_session_context](_make_session_context.md) (1 shared connections)
- [enum](enum.md) (1 shared connections)

## Source Files

- `schemas/items/item_prototype.schema.json`
- `tools/room_toolkit/room_validator/schemas/subzone_schema.json`
- `tools/room_toolkit/room_validator/schemas/zone_schema.json`

## Audit Trail

- EXTRACTED: 28 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*