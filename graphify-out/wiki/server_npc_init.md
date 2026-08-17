# server npc init

> 97 nodes

## Key Concepts

- **NPCThreadManager** (30 connections) — `server/npc/threading.py`
- **test_npc_threading_messages.py** (25 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **server/npc/__init__.py** (22 connections) — `server/npc/__init__.py`
- **passive_mob_npc.py** (20 connections) — `server/npc/passive_mob_npc.py`
- **NPCActionMessage** (15 connections) — `server/npc/threading.py`
- **NPCMessageQueue** (15 connections) — `server/npc/threading.py`
- **Any** (14 connections)
- **NPCCommunicationBridge** (13 connections) — `server/npc/threading.py`
- **NPCActionType** (11 connections) — `server/npc/threading.py`
- **asyncio** (10 connections)
- **._execute_wander_movement()** (8 connections) — `server/npc/threading.py`
- **.from_dict()** (6 connections) — `server/npc/threading.py`
- **._npc_thread_worker()** (6 connections) — `server/npc/threading.py`
- **._process_wander_action()** (6 connections) — `server/npc/threading.py`
- **._execute_npc_behavior()** (5 connections) — `server/npc/threading.py`
- **._process_npc_message()** (5 connections) — `server/npc/threading.py`
- **._resolve_wander_npc()** (5 connections) — `server/npc/threading.py`
- **.restart_npc_thread()** (5 connections) — `server/npc/threading.py`
- **.start_npc_thread()** (5 connections) — `server/npc/threading.py`
- **.from_json()** (4 connections) — `server/npc/threading.py`
- **.to_dict()** (4 connections) — `server/npc/threading.py`
- **.__init__()** (4 connections) — `server/npc/threading.py`
- **._parse_behavior_config()** (4 connections) — `server/npc/threading.py`
- **.stop_npc_thread()** (4 connections) — `server/npc/threading.py`
- **._stop_npc_thread_internal()** (4 connections) — `server/npc/threading.py`
- *... and 72 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (13 shared connections)
- [server events event bus](server_events_event_bus.md) (8 shared connections)
- [server npc passive mob npc](server_npc_passive_mob_npc.md) (7 shared connections)
- [draft7validator](draft7validator.md) (5 shared connections)
- [server app lifespan startup create](server_app_lifespan_startup_create.md) (4 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (4 shared connections)
- [server events event types playerenteredroom](server_events_event_types_playerenteredroom.md) (4 shared connections)
- [server npc idle movement](server_npc_idle_movement.md) (3 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (3 shared connections)
- [lock](lock.md) (2 shared connections)
- [server container main applicationcontainer get](server_container_main_applicationcontainer_get.md) (1 shared connections)
- [eventbus](eventbus.md) (1 shared connections)

## Source Files

- `server/npc/__init__.py`
- `server/npc/passive_mob_npc.py`
- `server/npc/threading.py`
- `server/tests/unit/npc/test_npc_threading_messages.py`

## Audit Trail

- EXTRACTED: 195 (89%)
- INFERRED: 25 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*