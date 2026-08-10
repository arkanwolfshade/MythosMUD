# E 2 E Cleanup Troubleshooting

> 15 nodes

## Key Concepts

- **_emit_close_container_event()** (14 connections) — `server/api/container_events.py`
- **UUID** (5 connections)
- **.test_emit_close_container_event_success()** (3 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_close_container_event_no_connection_manager()** (3 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_close_container_event_no_container_data()** (3 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_close_container_event_no_room_id()** (3 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_close_container_event_persistence_error()** (3 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_close_container_event_emission_error()** (3 connections) — `server/tests/unit/api/test_container_events.py`
- **Emit WebSocket event for container closing.      Args:         connection_manage** (1 connections) — `server/api/container_events.py`
- **Test _emit_close_container_event successfully emits event.** (1 connections) — `server/tests/unit/api/test_container_events.py`
- **Test _emit_close_container_event handles None connection_manager.** (1 connections) — `server/tests/unit/api/test_container_events.py`
- **Test _emit_close_container_event handles None container data.** (1 connections) — `server/tests/unit/api/test_container_events.py`
- **Test _emit_close_container_event handles container without room_id.** (1 connections) — `server/tests/unit/api/test_container_events.py`
- **Test _emit_close_container_event handles persistence errors gracefully.** (1 connections) — `server/tests/unit/api/test_container_events.py`
- **Test _emit_close_container_event handles emission errors gracefully.** (1 connections) — `server/tests/unit/api/test_container_events.py`

## Relationships

- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (12 shared connections)
- [Npc Behavior Engine](Npc_Behavior_Engine.md) (2 shared connections)
- [Product Requirements Document](Product_Requirements_Document.md) (1 shared connections)
- [E 2 E Testing Guide](E_2_E_Testing_Guide.md) (1 shared connections)

## Source Files

- `server/api/container_events.py`
- `server/tests/unit/api/test_container_events.py`

## Audit Trail

- EXTRACTED: 44 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*