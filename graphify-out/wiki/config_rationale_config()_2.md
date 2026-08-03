# config rationale config()

> 14 nodes

## Key Concepts

- **_get_npc_room_id()** (14 connections) — `server/commands/look_npc.py`
- **test_get_npc_room_id_from_current_room_id()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_get_npc_room_id_from_current_room()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_get_npc_room_id_none()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_get_npc_room_id_from_current_room_id()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_get_npc_room_id_from_current_room()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_get_npc_room_id_none()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Get the room ID from an NPC instance, checking both current_room and current_roo** (1 connections) — `server/commands/look_npc.py`
- **Test getting NPC room ID from current_room_id.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test getting NPC room ID from current_room when current_room_id is None.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test getting NPC room ID when both are None.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test _get_npc_room_id() returns current_room_id when available.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _get_npc_room_id() returns current_room when current_room_id is None.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _get_npc_room_id() returns None when both are None.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`

## Relationships

- [npc look commands](npc_look_commands.md) (4 shared connections)
- [schemas calendar rationale](schemas_calendar_rationale.md) (4 shared connections)
- [services service hallucination](services_service_hallucination.md) (2 shared connections)
- [commands quest rationale](commands_quest_rationale.md) (2 shared connections)
- [cache caching lru](cache_caching_lru.md) (1 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/tests/unit/commands/test_look_npc.py`
- `server/tests/unit/commands/test_look_npc_helpers.py`

## Audit Trail

- EXTRACTED: 39 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*