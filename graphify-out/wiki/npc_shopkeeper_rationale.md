# npc shopkeeper rationale

> 48 nodes

## Key Concepts

- **NPCThreadManager** (29 connections) — `server/npc/threading.py`
- **test_npc_threading_messages.py** (23 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **NPCMessageQueue** (16 connections) — `server/npc/threading.py`
- **._npc_thread_worker()** (8 connections) — `server/npc/threading.py`
- **.start_npc_thread()** (5 connections) — `server/npc/threading.py`
- **._stop_npc_thread_internal()** (5 connections) — `server/npc/threading.py`
- **.restart_npc_thread()** (5 connections) — `server/npc/threading.py`
- **._execute_npc_behavior()** (5 connections) — `server/npc/threading.py`
- **.get_messages()** (4 connections) — `server/npc/threading.py`
- **.clear_messages()** (4 connections) — `server/npc/threading.py`
- **.__init__()** (4 connections) — `server/npc/threading.py`
- **.stop_npc_thread()** (4 connections) — `server/npc/threading.py`
- **.stop()** (3 connections) — `server/npc/threading.py`
- **.get_npc_definition()** (3 connections) — `server/npc/threading.py`
- **.__init__()** (2 connections) — `server/npc/threading.py`
- **.get_queue_size()** (2 connections) — `server/npc/threading.py`
- **.get_total_queue_size()** (2 connections) — `server/npc/threading.py`
- **.start()** (2 connections) — `server/npc/threading.py`
- **.get_active_npc_threads()** (2 connections) — `server/npc/threading.py`
- **test_npc_message_queue_add_get_clear()** (2 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_npc_message_queue_trims_oldest()** (2 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_npc_thread_manager_start_stop()** (2 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_npc_thread_manager_start_stop_npc_thread()** (2 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_npc_thread_manager_restart_npc_thread()** (2 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_npc_thread_manager_stop_cancels_running_task()** (2 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- *... and 23 more nodes in this community*

## Relationships

- [instance game manager](instance_game_manager.md) (9 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (8 shared connections)
- [models npc rationale](models_npc_rationale.md) (8 shared connections)
- [npc behavior engine](npc_behavior_engine.md) (4 shared connections)
- [idle movement npc](idle_movement_npc.md) (2 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (1 shared connections)
- [AppRouter main AppRouter()](AppRouter_main_AppRouter%28%29.md) (1 shared connections)

## Source Files

- `server/npc/threading.py`
- `server/tests/unit/npc/test_npc_threading_messages.py`

## Audit Trail

- EXTRACTED: 161 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*