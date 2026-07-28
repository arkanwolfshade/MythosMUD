# Server Realtime (19)

> 75 nodes

## Key Concepts

- **NPCEventHandler** (25 connections) — `server/realtime/npc_event_handlers.py`
- **MessageBuilder** (22 connections) — `server/realtime/message_builders.py`
- **get_global_tracked_manager()** (18 connections) — `server/app/tracked_task_manager.py`
- **PeriodicOrphanAuditor** (9 connections) — `server/app/memory_lifespan_coordinator.py`
- **._get_next_sequence()** (8 connections) — `server/realtime/message_builders.py`
- **.handle_npc_entered()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._send_npc_left_message()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_spawn_message()** (7 connections) — `server/realtime/npc_event_handlers.py`
- **Any** (6 connections)
- **._send_room_message()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **.handle_npc_left()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **.create_player_entered_message()** (5 connections) — `server/realtime/message_builders.py`
- **.create_player_left_message()** (5 connections) — `server/realtime/message_builders.py`
- **.__init__()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **Any** (5 connections)
- **._get_npc_instance()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_name()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **.schedule_periodic_auditing()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **._background_audit_cycle()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **._do_full_cleanup_audit()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **.force_single_audit_cycle()** (4 connections) — `server/app/memory_lifespan_coordinator.py`
- **.build_occupants_update_message()** (4 connections) — `server/realtime/message_builders.py`
- **.build_room_update_message()** (4 connections) — `server/realtime/message_builders.py`
- **.build_room_state_message()** (4 connections) — `server/realtime/message_builders.py`
- **._get_behavior_config_from_instance()** (4 connections) — `server/realtime/npc_event_handlers.py`
- *... and 50 more nodes in this community*

## Relationships

- [Server Events](Server_Events.md) (18 shared connections)
- [Server Commands](Server_Commands.md) (9 shared connections)
- [Server Npc](Server_Npc.md) (3 shared connections)
- [Server App (5)](Server_App_%285%29.md) (2 shared connections)
- [Server Realtime (6)](Server_Realtime_%286%29.md) (2 shared connections)
- [Server Realtime (53)](Server_Realtime_%2853%29.md) (2 shared connections)
- [Server Realtime (22)](Server_Realtime_%2822%29.md) (2 shared connections)
- [Server Realtime (72)](Server_Realtime_%2872%29.md) (2 shared connections)
- [Server App (2)](Server_App_%282%29.md) (1 shared connections)
- [Server Realtime (28)](Server_Realtime_%2828%29.md) (1 shared connections)
- [Server Services (117)](Server_Services_%28117%29.md) (1 shared connections)
- [Server Realtime (2)](Server_Realtime_%282%29.md) (1 shared connections)

## Source Files

- `server/app/memory_lifespan_coordinator.py`
- `server/app/tracked_task_manager.py`
- `server/realtime/message_builders.py`
- `server/realtime/npc_event_handlers.py`
- `server/tests/unit/realtime/test_npc_event_handlers.py`

## Audit Trail

- EXTRACTED: 259 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*