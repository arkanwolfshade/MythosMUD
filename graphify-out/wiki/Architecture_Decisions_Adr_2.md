# Architecture Decisions Adr

> 6 nodes · cohesion 0.33

## Key Concepts

- **items** (5 connections) — `db/static/schemas/npc_schedules.schema.json`
- **schedules** (4 connections) — `db/static/schemas/npc_schedules.schema.json`
- **properties** (2 connections) — `db/static/schemas/npc_schedules.schema.json`
- **additionalProperties** (1 connections) — `db/static/schemas/npc_schedules.schema.json`
- **minItems** (1 connections) — `db/static/schemas/npc_schedules.schema.json`
- **type** (1 connections) — `db/static/schemas/npc_schedules.schema.json`

## Relationships

- [Command Factories Combat](Command_Factories_Combat.md) (1 shared connections)
- [Caching Lru Cache](Caching_Lru_Cache.md) (1 shared connections)
- [Mythosmud Obsidian Raw](Mythosmud_Obsidian_Raw.md) (1 shared connections)
- [Combat Services Messaging](Combat_Services_Messaging.md) (1 shared connections)

## Source Files

- `db/static/schemas/npc_schedules.schema.json`

## Audit Trail

- EXTRACTED: 14 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*