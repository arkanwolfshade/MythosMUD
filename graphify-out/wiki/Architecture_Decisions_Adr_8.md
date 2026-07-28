# Architecture Decisions Adr

> 2 nodes · cohesion 1.00

## Key Concepts

- **test_get_behavior_config_from_instance_none()** (2 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`
- **Test _get_behavior_config_from_instance() when config is not found.** (1 connections) — `server/tests/unit/realtime/test_npc_event_handlers.py`

## Relationships

- [Investigations Sessions Session](Investigations_Sessions_Session.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_npc_event_handlers.py`

## Audit Trail

- EXTRACTED: 3 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*