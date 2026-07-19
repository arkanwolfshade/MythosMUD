# Realtime Connection

> 15 nodes · cohesion 0.20

## Key Concepts

- **get_npc_name_from_instance()** (11 connections) — `server/realtime/connection_utils.py`
- **test_connection_utils.py** (8 connections) — `server/tests/unit/realtime/test_connection_utils.py`
- **test_get_npc_name_from_instance_handles_exception()** (4 connections) — `server/tests/unit/realtime/test_connection_utils.py`
- **test_get_npc_name_from_instance_no_lifecycle_manager()** (3 connections) — `server/tests/unit/realtime/test_connection_utils.py`
- **test_get_npc_name_from_instance_no_name()** (3 connections) — `server/tests/unit/realtime/test_connection_utils.py`
- **test_get_npc_name_from_instance_no_service()** (3 connections) — `server/tests/unit/realtime/test_connection_utils.py`
- **test_get_npc_name_from_instance_not_found()** (3 connections) — `server/tests/unit/realtime/test_connection_utils.py`
- **test_get_npc_name_from_instance_success()** (3 connections) — `server/tests/unit/realtime/test_connection_utils.py`
- **Test get_npc_name_from_instance() returns NPC name when found.** (2 connections) — `server/tests/unit/realtime/test_connection_utils.py`
- **Get NPC name from the actual NPC instance, preserving original case from databas** (1 connections) — `server/realtime/connection_utils.py`
- **Unit tests for connection utils.  Tests the connection_utils module functions.** (1 connections) — `server/tests/unit/realtime/test_connection_utils.py`
- **Test get_npc_name_from_instance() returns None when NPC has no name.** (1 connections) — `server/tests/unit/realtime/test_connection_utils.py`
- **Test get_npc_name_from_instance() returns None when service not available.** (1 connections) — `server/tests/unit/realtime/test_connection_utils.py`
- **Test get_npc_name_from_instance() returns None when no lifecycle manager.** (1 connections) — `server/tests/unit/realtime/test_connection_utils.py`
- **Test get_npc_name_from_instance() handles exceptions.** (1 connections) — `server/tests/unit/realtime/test_connection_utils.py`

## Relationships

- [[Room Occupant Events]] (1 shared connections)
- [[NPC Admin API]] (1 shared connections)
- [[NPC Occupant Verification]] (1 shared connections)
- [[Services Service Room]] (1 shared connections)

## Source Files

- `server/realtime/connection_utils.py`
- `server/tests/unit/realtime/test_connection_utils.py`

## Audit Trail

- EXTRACTED: 45 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
