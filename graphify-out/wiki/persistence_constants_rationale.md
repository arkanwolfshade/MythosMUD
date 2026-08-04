# persistence constants rationale

> 2 nodes

## Key Concepts

- **._normalize_npc_stats()** (3 connections) — `server/npc/combat_integration.py`
- **Normalize NPC stats to include 'hp' for backward compatibility.** (1 connections) — `server/npc/combat_integration.py`

## Relationships

- [room conftest toolkit](room_conftest_toolkit.md) (1 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration.py`

## Audit Trail

- EXTRACTED: 4 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*