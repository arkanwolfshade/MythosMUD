# npc shopkeeper rationale

> 52 nodes

## Key Concepts

- **NPCThreadManager** (29 connections) — `server/npc/threading.py`
- **test_npc_threading_messages.py** (23 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **NPCMessageQueue** (16 connections) — `server/npc/threading.py`
- **._npc_thread_worker()** (8 connections) — `server/npc/threading.py`
- **._process_wander_action()** (8 connections) — `server/npc/threading.py`
- **.start_npc_thread()** (5 connections) — `server/npc/threading.py`
- **._stop_npc_thread_internal()** (5 connections) — `server/npc/threading.py`
- **.restart_npc_thread()** (5 connections) — `server/npc/threading.py`
- **._process_npc_message()** (5 connections) — `server/npc/threading.py`
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
- *... and 27 more nodes in this community*

## Relationships

- [effect player repository](effect_player_repository.md) (9 shared connections)
- [room look commands](room_look_commands.md) (5 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (4 shared connections)
- [services npc startup](services_npc_startup.md) (4 shared connections)
- [idle movement npc](idle_movement_npc.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)
- [services nats service](services_nats_service.md) (2 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (2 shared connections)
- [tick game processing](tick_game_processing.md) (2 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [lucidity event services](lucidity_event_services.md) (1 shared connections)

## Source Files

- `server/npc/threading.py`
- `server/tests/unit/npc/test_npc_threading_messages.py`

## Audit Trail

- EXTRACTED: 175 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*