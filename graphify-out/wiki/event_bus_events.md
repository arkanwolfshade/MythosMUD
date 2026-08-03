# event bus events

> 16 nodes

## Key Concepts

- **NPCOccupantProcessor** (31 connections) — `server/realtime/npc_occupant_processor.py`
- **test_npc_occupant_processor.py** (17 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **processor()** (3 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_get_npc_room_id_prefers_current_room()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_should_include_npc_dead()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_should_include_npc_matching_room()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_scan_active_npcs_for_room()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_query_npcs_for_room_uses_lifecycle_manager()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_query_npcs_fallback_to_room()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_process_npcs_for_occupants()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_filter_fallback_npcs_dead()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_get_npc_lifecycle_manager_unavailable()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_get_npc_lifecycle_manager_no_active_npcs()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **test_query_npcs_handles_exception()** (2 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`
- **Processes NPC occupants for rooms.** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Unit tests for NPCOccupantProcessor.** (1 connections) — `server/tests/unit/realtime/test_npc_occupant_processor.py`

## Relationships

- [message realtime messaging](message_realtime_messaging.md) (9 shared connections)
- [magic healing game](magic_healing_game.md) (6 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (3 shared connections)
- [look helpers commands](look_helpers_commands.md) (2 shared connections)
- [NATS Messaging](NATS_Messaging.md) (1 shared connections)

## Source Files

- `server/realtime/npc_occupant_processor.py`
- `server/tests/unit/realtime/test_npc_occupant_processor.py`

## Audit Trail

- EXTRACTED: 73 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*