# Community 1297

> 8 nodes

## Key Concepts

- **._get_npc_display_name()** (5 connections) — `server/npc/combat_integration.py`
- **._get_npc_lifecycle_manager()** (5 connections) — `server/npc/combat_integration.py`
- **._get_npc_name_from_lifecycle()** (4 connections) — `server/npc/combat_integration.py`
- **._derive_npc_name_from_id()** (3 connections) — `server/npc/combat_integration.py`
- **Resolve NPC instance display name from lifecycle manager, or derive from npc_id.** (1 connections) — `server/npc/combat_integration.py`
- **Best-effort lookup of NPC name from the lifecycle manager.** (1 connections) — `server/npc/combat_integration.py`
- **Resolve the NPC lifecycle manager from the app state, if available.** (1 connections) — `server/npc/combat_integration.py`
- **Fallback name derivation: first segment of npc_id (e.g. nightgaunt_limbo_... ->…** (1 connections) — `server/npc/combat_integration.py`

## Relationships

- [Community 231](Community_231.md) (4 shared connections)
- [Community 785](Community_785.md) (1 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (1 shared connections)
- [Community 218](Community_218.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration.py`

## Audit Trail

- EXTRACTED: 13 (93%)
- INFERRED: 1 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*