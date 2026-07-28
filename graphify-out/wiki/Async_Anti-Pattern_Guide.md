# Async Anti-Pattern Guide

> 16 nodes · cohesion 0.17

## Key Concepts

- **get_npc_name_from_instance()** (11 connections) — `server/realtime/connection_utils.py`
- **test_connection_utils.py** (9 connections) — `server/tests/unit/realtime/test_connection_utils.py`
- **test_get_npc_name_from_instance_handles_exception()** (4 connections) — `server/tests/unit/realtime/test_connection_utils.py`
- **test_get_npc_name_from_instance_no_lifecycle_manager()** (3 connections) — `server/tests/unit/realtime/test_connection_utils.py`
- **test_get_npc_name_from_instance_no_name()** (3 connections) — `server/tests/unit/realtime/test_connection_utils.py`
- **test_get_npc_name_from_instance_no_service()** (3 connections) — `server/tests/unit/realtime/test_connection_utils.py`
- **test_get_npc_name_from_instance_not_found()** (3 connections) — `server/tests/unit/realtime/test_connection_utils.py`
- **test_get_npc_name_from_instance_success()** (3 connections) — `server/tests/unit/realtime/test_connection_utils.py`
- **Get NPC name from the actual NPC instance, preserving original case from databas** (1 connections) — `server/realtime/connection_utils.py`
- **Unit tests for connection utils.  Tests the connection_utils module functions.** (1 connections) — `server/tests/unit/realtime/test_connection_utils.py`
- **Test get_npc_name_from_instance() returns NPC name when found.** (1 connections) — `server/tests/unit/realtime/test_connection_utils.py`
- **Test get_npc_name_from_instance() returns None when NPC not found.** (1 connections) — `server/tests/unit/realtime/test_connection_utils.py`
- **Test get_npc_name_from_instance() returns None when NPC has no name.** (1 connections) — `server/tests/unit/realtime/test_connection_utils.py`
- **Test get_npc_name_from_instance() returns None when service not available.** (1 connections) — `server/tests/unit/realtime/test_connection_utils.py`
- **Test get_npc_name_from_instance() returns None when no lifecycle manager.** (1 connections) — `server/tests/unit/realtime/test_connection_utils.py`
- **Test get_npc_name_from_instance() handles exceptions.** (1 connections) — `server/tests/unit/realtime/test_connection_utils.py`

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (3 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (1 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (1 shared connections)

## Source Files

- `server/realtime/connection_utils.py`
- `server/tests/unit/realtime/test_connection_utils.py`

## Audit Trail

- EXTRACTED: 46 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*