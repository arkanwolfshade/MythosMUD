# Cursor Plans Uvicorn

> 2 nodes · cohesion 0.05

## Key Concepts

- **UUID** (15 connections) — `server/services/npc_combat_integration_service.py`
- **AppWithState** (8 connections) — `server/commands/combat_taunt.py`

## Relationships

- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (1 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/services/npc_combat_integration_service.py`

## Audit Trail

- EXTRACTED: 6 (26%)
- INFERRED: 17 (74%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*