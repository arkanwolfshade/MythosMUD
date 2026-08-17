# add_npc_occupants_to_list

> 8 nodes

## Key Concepts

- **add_npc_occupants_to_list()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **test_add_npc_occupants_to_list_filters_dead_npcs()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_add_npc_occupants_to_list_no_app()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_add_npc_occupants_to_list_success()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Add NPC occupants to the occupant names list.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Test add_npc_occupants_to_list() adds NPC names to list.** (1 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Test add_npc_occupants_to_list() does nothing when no app.** (1 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Test add_npc_occupants_to_list() includes all NPCs (code doesn't filter dead).** (1 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`

## Relationships

- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (4 shared connections)
- [asyncio](asyncio.md) (3 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [send_initial_room_state](send_initial_room_state.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 17 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*