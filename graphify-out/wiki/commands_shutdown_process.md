# commands shutdown process

> 6 nodes

## Key Concepts

- **._get_lifecycle_manager_for_filtering()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._filter_fallback_npcs()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._filter_single_fallback_npc()** (4 connections) — `server/realtime/npc_occupant_processor.py`
- **Get lifecycle manager for filtering fallback NPCs.          Returns:** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Check if a single fallback NPC should be included.          Args:             np** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Filter fallback NPCs to only include those in active_npcs and alive.          Ar** (1 connections) — `server/realtime/npc_occupant_processor.py`

## Relationships

- [event bus events](event_bus_events.md) (3 shared connections)
- [message realtime messaging](message_realtime_messaging.md) (3 shared connections)
- [AppRouter main AppRouter()](AppRouter_main_AppRouter%28%29.md) (1 shared connections)

## Source Files

- `server/realtime/npc_occupant_processor.py`

## Audit Trail

- EXTRACTED: 17 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*