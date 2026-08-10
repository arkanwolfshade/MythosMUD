# Npc Behavior Engine

> 17 nodes

## Key Concepts

- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- **Any** (4 connections)
- **.test_emit_container_opened_events_success()** (3 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_no_connection_manager()** (3 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_no_room_id()** (3 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_validation_error()** (3 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_emission_error()** (3 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_missing_mutation_token()** (3 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_container_opened_events_room_emission_error()** (3 connections) — `server/tests/unit/api/test_container_events.py`
- **Emit WebSocket events for container opening.      Args:         connection_manag** (1 connections) — `server/api/container_events.py`
- **Test emit_container_opened_events successfully emits events.** (1 connections) — `server/tests/unit/api/test_container_events.py`
- **Test emit_container_opened_events handles None connection_manager.** (1 connections) — `server/tests/unit/api/test_container_events.py`
- **Test emit_container_opened_events handles container without room_id.** (1 connections) — `server/tests/unit/api/test_container_events.py`
- **Test emit_container_opened_events handles validation errors gracefully.** (1 connections) — `server/tests/unit/api/test_container_events.py`
- **Test emit_container_opened_events handles emission errors gracefully.** (1 connections) — `server/tests/unit/api/test_container_events.py`
- **Test emit_container_opened_events handles missing mutation_token gracefully.** (1 connections) — `server/tests/unit/api/test_container_events.py`
- **Test emit_container_opened_events handles room emission errors separately.** (1 connections) — `server/tests/unit/api/test_container_events.py`

## Relationships

- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (12 shared connections)
- [E 2 E Cleanup Troubleshooting](E_2_E_Cleanup_Troubleshooting.md) (2 shared connections)
- [E 2 E Testing Guide](E_2_E_Testing_Guide.md) (2 shared connections)
- [Product Requirements Document](Product_Requirements_Document.md) (1 shared connections)

## Source Files

- `server/api/container_events.py`
- `server/tests/unit/api/test_container_events.py`

## Audit Trail

- EXTRACTED: 49 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*