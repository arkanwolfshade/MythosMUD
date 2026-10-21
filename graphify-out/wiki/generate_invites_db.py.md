# generate_invites_db.py

> 16 nodes · cohesion 0.28

## Key Concepts

- **_get_npc_occupants_in_room()** (16 connections) — `server/commands/look_npc.py`
- **test_look_npc_occupants.py** (13 connections) — `server/tests/unit/commands/test_look_npc_occupants.py`
- **test_an_unrecognised_type_is_listed_as_a_passive_mob()** (7 connections) — `server/tests/unit/commands/test_look_npc_occupants.py`
- **test_lists_each_live_npc_in_the_room_with_its_disposition()** (6 connections) — `server/tests/unit/commands/test_look_npc_occupants.py`
- **_get_npcs_in_room()** (5 connections) — `server/commands/look_npc.py`
- **_lifecycle()** (5 connections) — `server/tests/unit/commands/test_look_npc_occupants.py`
- **_npc()** (5 connections) — `server/tests/unit/commands/test_look_npc_occupants.py`
- **asyncio** (5 connections)
- **test_skips_the_dead_and_the_unnamed()** (5 connections) — `server/tests/unit/commands/test_look_npc_occupants.py`
- **test_the_names_helper_is_the_same_list_without_dispositions()** (5 connections) — `server/tests/unit/commands/test_look_npc_occupants.py`
- **test_no_lifecycle_manager_means_no_npcs()** (3 connections) — `server/tests/unit/commands/test_look_npc_occupants.py`
- **NpcOccupant** (1 connections)
- **Get list of NPC names in a room from lifecycle manager.** (1 connections) — `server/commands/look_npc.py`
- **The NPCs in a room as ``{name, disposition}``, from the lifecycle manager…** (1 connections) — `server/commands/look_npc.py`
- **`_get_npc_occupants_in_room`: the room's live NPCs as {name, disposition}…** (1 connections) — `server/tests/unit/commands/test_look_npc_occupants.py`
- **One bad definition row must not drop an NPC from the room.** (1 connections) — `server/tests/unit/commands/test_look_npc_occupants.py`

## Relationships

- [PlayerRepositoryProtocol](PlayerRepositoryProtocol.md) (4 shared connections)
- [look_container.py](look_container.py.md) (4 shared connections)
- [alias_storage.py](alias_storage.py.md) (2 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (1 shared connections)
- [Commands](Commands.md) (1 shared connections)
- [SystemAdminChannelStrategy](SystemAdminChannelStrategy.md) (1 shared connections)
- [player_presence_tracker.py](player_presence_tracker.py.md) (1 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/tests/unit/commands/test_look_npc_occupants.py`

## Audit Trail

- EXTRACTED: 43 (91%)
- INFERRED: 4 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*