# NPCThreadManager

> 77 nodes

## Key Concepts

- **NPCThreadManager** (30 connections) — `server/npc/threading.py`
- **test_npc_threading_messages.py** (25 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **NPCMessageQueue** (15 connections) — `server/npc/threading.py`
- **Any** (14 connections)
- **NPCCommunicationBridge** (13 connections) — `server/npc/threading.py`
- **asyncio** (10 connections)
- **._execute_wander_movement()** (8 connections) — `server/npc/threading.py`
- **._npc_thread_worker()** (6 connections) — `server/npc/threading.py`
- **._process_wander_action()** (6 connections) — `server/npc/threading.py`
- **._execute_npc_behavior()** (5 connections) — `server/npc/threading.py`
- **._process_npc_message()** (5 connections) — `server/npc/threading.py`
- **._resolve_wander_npc()** (5 connections) — `server/npc/threading.py`
- **.restart_npc_thread()** (5 connections) — `server/npc/threading.py`
- **.start_npc_thread()** (5 connections) — `server/npc/threading.py`
- **.__init__()** (4 connections) — `server/npc/threading.py`
- **._parse_behavior_config()** (4 connections) — `server/npc/threading.py`
- **.stop_npc_thread()** (4 connections) — `server/npc/threading.py`
- **._stop_npc_thread_internal()** (4 connections) — `server/npc/threading.py`
- **.broadcast_to_all_npcs()** (3 connections) — `server/npc/threading.py`
- **.get_messages_for_npc()** (3 connections) — `server/npc/threading.py`
- **.get_pending_messages()** (3 connections) — `server/npc/threading.py`
- **.receive_message_from_npc()** (3 connections) — `server/npc/threading.py`
- **.send_message_to_npc()** (3 connections) — `server/npc/threading.py`
- **.add_message()** (3 connections) — `server/npc/threading.py`
- **.get_messages()** (3 connections) — `server/npc/threading.py`
- *... and 52 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (9 shared connections)
- [NPCActionMessage](NPCActionMessage.md) (7 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [EventBus](EventBus.md) (3 shared connections)
- [MetricsCollector](MetricsCollector.md) (2 shared connections)
- [IdleMovementHandler](IdleMovementHandler.md) (2 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (2 shared connections)
- [NPCStartupService](NPCStartupService.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/npc/threading.py`
- `server/tests/unit/npc/test_npc_threading_messages.py`

## Audit Trail

- EXTRACTED: 135 (89%)
- INFERRED: 17 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*