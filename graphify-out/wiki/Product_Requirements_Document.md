# Product Requirements Document

> 18 nodes

## Key Concepts

- **emit_transfer_event()** (17 connections) — `server/api/container_events.py`
- **.test_emit_transfer_event_success()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_no_connection_manager()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_no_container_in_result()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_no_room_id()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_validation_error()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_emission_error()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_to_player_direction()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_transfer_event_to_container_direction()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **Emit WebSocket event for transfer operation.      Args:         connection_manag** (1 connections) — `server/api/container_events.py`
- **Test emit_transfer_event successfully emits event.** (1 connections) — `server/tests/unit/api/test_container_events.py`
- **Test emit_transfer_event handles None connection_manager.** (1 connections) — `server/tests/unit/api/test_container_events.py`
- **Test emit_transfer_event handles missing container in result.** (1 connections) — `server/tests/unit/api/test_container_events.py`
- **Test emit_transfer_event handles container without room_id.** (1 connections) — `server/tests/unit/api/test_container_events.py`
- **Test emit_transfer_event handles validation errors gracefully.** (1 connections) — `server/tests/unit/api/test_container_events.py`
- **Test emit_transfer_event handles emission errors gracefully.** (1 connections) — `server/tests/unit/api/test_container_events.py`
- **Test emit_transfer_event with 'to_player' direction.** (1 connections) — `server/tests/unit/api/test_container_events.py`
- **Test emit_transfer_event with 'to_container' direction.** (1 connections) — `server/tests/unit/api/test_container_events.py`

## Relationships

- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (12 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (9 shared connections)
- [Npc Behavior Engine](Npc_Behavior_Engine.md) (1 shared connections)
- [E 2 E Cleanup Troubleshooting](E_2_E_Cleanup_Troubleshooting.md) (1 shared connections)
- [E 2 E Testing Guide](E_2_E_Testing_Guide.md) (1 shared connections)

## Source Files

- `server/api/container_events.py`
- `server/tests/unit/api/test_container_events.py`

## Audit Trail

- EXTRACTED: 58 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*