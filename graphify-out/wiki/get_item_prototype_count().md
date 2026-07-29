# get item prototype count()

> 11 nodes

## Key Concepts

- **_set_legacy_services()** (6 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_count()** (5 connections) — `server/app/lifespan_startup.py`
- **_legacy_service_bindings()** (5 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_entries()** (4 connections) — `server/app/lifespan_startup.py`
- **Any** (4 connections)
- **_log_npc_startup_errors()** (4 connections) — `server/app/lifespan_startup.py`
- **Return raw entries from the item prototype registry, or None on error.** (1 connections) — `server/app/lifespan_startup.py`
- **Get count of item prototypes from registry.** (1 connections) — `server/app/lifespan_startup.py`
- **Return (app.state attr, service value, display name) for legacy service bindings** (1 connections) — `server/app/lifespan_startup.py`
- **Set services on app.state for backward compatibility.** (1 connections) — `server/app/lifespan_startup.py`
- **Log any errors from NPC startup spawning results.** (1 connections) — `server/app/lifespan_startup.py`

## Relationships

- [.initialize()](initialize%28%29.md) (5 shared connections)
- [create npc services on app()](create_npc_services_on_app%28%29.md) (3 shared connections)
- [.shutdown()](shutdown%28%29.md) (2 shared connections)
- [lifespan](lifespan.md) (1 shared connections)

## Source Files

- `server/app/lifespan_startup.py`

## Audit Trail

- EXTRACTED: 33 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*