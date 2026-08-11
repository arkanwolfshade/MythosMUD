# NPC Occupants Verification

> 17 nodes

## Key Concepts

- **test_occupants.py** (14 connections) — `server/commands/npc_admin/test_occupants.py`
- **Any** (7 connections)
- **_resolve_room_and_handler_for_test_occupants()** (6 connections) — `server/commands/npc_admin/test_occupants.py`
- **_resolve_test_occupants_context()** (6 connections) — `server/commands/npc_admin/test_occupants.py`
- **_get_event_handler_for_test_occupants()** (5 connections) — `server/commands/npc_admin/test_occupants.py`
- **_resolve_app_and_player_for_test_occupants()** (5 connections) — `server/commands/npc_admin/test_occupants.py`
- **_get_room_id_for_test_occupants()** (4 connections) — `server/commands/npc_admin/test_occupants.py`
- **_separate_occupants()** (4 connections) — `server/commands/npc_admin/test_occupants.py`
- **_format_occupants_result()** (3 connections) — `server/commands/npc_admin/test_occupants.py`
- **NPC test-occupants command for debugging occupant queries.** (1 connections) — `server/commands/npc_admin/test_occupants.py`
- **Get room_id from args or current room. Returns (room_id, error_result).** (1 connections) — `server/commands/npc_admin/test_occupants.py`
- **Get event handler from app.state. Returns (event_handler, error_result).** (1 connections) — `server/commands/npc_admin/test_occupants.py`
- **Separate occupants into players and NPCs.** (1 connections) — `server/commands/npc_admin/test_occupants.py`
- **Format occupants result as a string.** (1 connections) — `server/commands/npc_admin/test_occupants.py`
- **Resolve application and player object for NPC test occupants command.** (1 connections) — `server/commands/npc_admin/test_occupants.py`
- **Resolve room_id and event handler for NPC test occupants command.** (1 connections) — `server/commands/npc_admin/test_occupants.py`
- **Resolve application, player, room_id, and event handler for NPC test occupants c** (1 connections) — `server/commands/npc_admin/test_occupants.py`

## Relationships

- [Player Schema Converter](Player_Schema_Converter.md) (7 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)
- [Command Factory Creators](Command_Factory_Creators.md) (1 shared connections)

## Source Files

- `server/commands/npc_admin/test_occupants.py`

## Audit Trail

- EXTRACTED: 60 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*