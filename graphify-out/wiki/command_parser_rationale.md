# command parser rationale

> 10 nodes

## Key Concepts

- **_get_lifecycle_manager()** (11 connections) — `server/commands/look_npc.py`
- **_get_npcs_in_room()** (7 connections) — `server/commands/look_npc.py`
- **test_get_lifecycle_manager_success()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_get_lifecycle_manager_no_service()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_get_lifecycle_manager_no_lifecycle_manager()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Get the lifecycle manager from the NPC instance service.** (1 connections) — `server/commands/look_npc.py`
- **Get list of NPC names in a room from lifecycle manager.** (1 connections) — `server/commands/look_npc.py`
- **Test getting lifecycle manager successfully.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test getting lifecycle manager when service not available.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test getting lifecycle manager when lifecycle_manager not available.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`

## Relationships

- [npc look commands](npc_look_commands.md) (7 shared connections)
- [commands quest rationale](commands_quest_rationale.md) (2 shared connections)
- [room look commands](room_look_commands.md) (2 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)
- [follow service game](follow_service_game.md) (1 shared connections)
- [models player related](models_player_related.md) (1 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/tests/unit/commands/test_look_npc.py`

## Audit Trail

- EXTRACTED: 32 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*