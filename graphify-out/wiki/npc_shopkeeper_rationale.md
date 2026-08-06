# npc shopkeeper rationale

> 85 nodes

## Key Concepts

- **NPCThreadManager** (29 connections) — `server/npc/threading.py`
- **test_npc_threading_messages.py** (23 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **NPCActionMessage** (16 connections) — `server/npc/threading.py`
- **NPCMessageQueue** (16 connections) — `server/npc/threading.py`
- **NPCCommunicationBridge** (14 connections) — `server/npc/threading.py`
- **Any** (11 connections)
- **._npc_thread_worker()** (8 connections) — `server/npc/threading.py`
- **._process_wander_action()** (8 connections) — `server/npc/threading.py`
- **.from_dict()** (6 connections) — `server/npc/threading.py`
- **._queue_wander_action()** (5 connections) — `server/npc/passive_mob_npc.py`
- **.start_npc_thread()** (5 connections) — `server/npc/threading.py`
- **._stop_npc_thread_internal()** (5 connections) — `server/npc/threading.py`
- **.restart_npc_thread()** (5 connections) — `server/npc/threading.py`
- **._process_npc_message()** (5 connections) — `server/npc/threading.py`
- **._execute_npc_behavior()** (5 connections) — `server/npc/threading.py`
- **.to_dict()** (4 connections) — `server/npc/threading.py`
- **.from_json()** (4 connections) — `server/npc/threading.py`
- **.get_messages()** (4 connections) — `server/npc/threading.py`
- **.clear_messages()** (4 connections) — `server/npc/threading.py`
- **.__init__()** (4 connections) — `server/npc/threading.py`
- **.stop_npc_thread()** (4 connections) — `server/npc/threading.py`
- **.to_json()** (3 connections) — `server/npc/threading.py`
- **.add_message()** (3 connections) — `server/npc/threading.py`
- **.stop()** (3 connections) — `server/npc/threading.py`
- **.get_npc_definition()** (3 connections) — `server/npc/threading.py`
- *... and 60 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (17 shared connections)
- [idle movement npc](idle_movement_npc.md) (5 shared connections)
- [room look commands](room_look_commands.md) (5 shared connections)
- [commands npc admin](commands_npc_admin.md) (3 shared connections)
- [command input commands](command_input_commands.md) (2 shared connections)
- [npc behavior engine](npc_behavior_engine.md) (2 shared connections)
- [event connection helpers](event_connection_helpers.md) (2 shared connections)
- [realtime player connection](realtime_player_connection.md) (1 shared connections)
- [lucidity event services](lucidity_event_services.md) (1 shared connections)

## Source Files

- `server/npc/passive_mob_npc.py`
- `server/npc/threading.py`
- `server/tests/unit/npc/test_npc_threading_messages.py`

## Audit Trail

- EXTRACTED: 280 (97%)
- INFERRED: 10 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*