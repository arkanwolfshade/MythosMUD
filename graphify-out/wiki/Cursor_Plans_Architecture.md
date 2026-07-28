# Cursor Plans Architecture

> 2 nodes · cohesion 1.00

## Key Concepts

- **test_handle_npc_left_room()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Test handle_npc_left_room() processes event.** (1 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_npc_event_handlers.py`

## Audit Trail

- EXTRACTED: 4 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*