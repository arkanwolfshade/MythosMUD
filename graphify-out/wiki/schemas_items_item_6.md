# schemas items item

> 8 nodes

## Key Concepts

- **._get_npc_display_name()** (5 connections) — `server/npc/combat_integration.py`
- **._get_npc_lifecycle_manager()** (5 connections) — `server/npc/combat_integration.py`
- **._get_npc_name_from_lifecycle()** (4 connections) — `server/npc/combat_integration.py`
- **._derive_npc_name_from_id()** (3 connections) — `server/npc/combat_integration.py`
- **Resolve NPC instance display name from lifecycle manager, or derive from npc_id.** (1 connections) — `server/npc/combat_integration.py`
- **Best-effort lookup of NPC name from the lifecycle manager.** (1 connections) — `server/npc/combat_integration.py`
- **Resolve the NPC lifecycle manager from the app state, if available.** (1 connections) — `server/npc/combat_integration.py`
- **Fallback name derivation: first segment of npc_id (e.g. nightgaunt_limbo_... ->** (1 connections) — `server/npc/combat_integration.py`

## Relationships

- [room conftest toolkit](room_conftest_toolkit.md) (4 shared connections)
- [memory lifespan app](memory_lifespan_app.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [nats services metrics](nats_services_metrics.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration.py`

## Audit Trail

- EXTRACTED: 20 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*