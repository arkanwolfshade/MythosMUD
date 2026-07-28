# Server Npc (6)

> 93 nodes

## Key Concepts

- **threading.py** (45 connections) — `server/npc/threading.py`
- **PassiveMobNPC** (29 connections) — `server/npc/passive_mob_npc.py`
- **passive_mob_npc.py** (18 connections) — `server/npc/passive_mob_npc.py`
- **NPCActionMessage** (12 connections) — `server/npc/threading.py`
- **Any** (11 connections)
- **NPCMessageQueue** (11 connections) — `server/npc/threading.py`
- **NPCCommunicationBridge** (10 connections) — `server/npc/threading.py`
- **NPCActionType** (8 connections) — `server/npc/threading.py`
- **._process_wander_action()** (8 connections) — `server/npc/threading.py`
- **test_npc_base.py** (8 connections) — `server/tests/unit/npc/test_npc_base.py`
- **.wander()** (6 connections) — `server/npc/passive_mob_npc.py`
- **.schedule_idle_movement()** (6 connections) — `server/npc/passive_mob_npc.py`
- **.__init__()** (5 connections) — `server/npc/passive_mob_npc.py`
- **._queue_wander_action()** (5 connections) — `server/npc/passive_mob_npc.py`
- **.from_dict()** (5 connections) — `server/npc/threading.py`
- **._process_npc_message()** (5 connections) — `server/npc/threading.py`
- **exception_metrics.py** (4 connections) — `server/monitoring/exception_metrics.py`
- **._create_wander_action()** (4 connections) — `server/npc/passive_mob_npc.py`
- **.to_dict()** (4 connections) — `server/npc/threading.py`
- **.get_messages()** (4 connections) — `server/npc/threading.py`
- **.__init__()** (4 connections) — `server/npc/threading.py`
- **get_summary()** (3 connections) — `server/monitoring/exception_metrics.py`
- **._setup_passive_mob_behavior_rules()** (3 connections) — `server/npc/passive_mob_npc.py`
- **._should_schedule_movement()** (3 connections) — `server/npc/passive_mob_npc.py`
- **.respond_to_player()** (3 connections) — `server/npc/passive_mob_npc.py`
- *... and 68 more nodes in this community*

## Relationships

- [Server Commands](Server_Commands.md) (12 shared connections)
- [Server Events](Server_Events.md) (12 shared connections)
- [Server Npc](Server_Npc.md) (11 shared connections)
- [Server Npc (5)](Server_Npc_%285%29.md) (9 shared connections)
- [Server Npc (2)](Server_Npc_%282%29.md) (6 shared connections)
- [Server App](Server_App.md) (5 shared connections)
- [Server Services (22)](Server_Services_%2822%29.md) (3 shared connections)
- [Server Npc (3)](Server_Npc_%283%29.md) (2 shared connections)
- [Server Services (7)](Server_Services_%287%29.md) (2 shared connections)
- [Server Game](Server_Game.md) (1 shared connections)
- [Scripts Utils (2)](Scripts_Utils_%282%29.md) (1 shared connections)
- [Server Config (2)](Server_Config_%282%29.md) (1 shared connections)

## Source Files

- `server/monitoring/exception_metrics.py`
- `server/npc/passive_mob_npc.py`
- `server/npc/threading.py`
- `server/tests/unit/npc/test_npc_base.py`

## Audit Trail

- EXTRACTED: 315 (95%)
- INFERRED: 15 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*