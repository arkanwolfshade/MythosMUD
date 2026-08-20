# subscribe_npc_spoke_to_chat

> 12 nodes

## Key Concepts

- **subscribe_npc_spoke_to_chat()** (9 connections) — `server/game/chat_npc_system.py`
- **set_chat_service_for_npc_system()** (8 connections) — `server/game/chat_npc_system.py`
- **.initialize()** (7 connections) — `server/container/bundles/chat.py`
- **subject_manager()** (7 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_npc_spoke_handler_schedules_room_speech()** (4 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_subscribe_npc_spoke_to_chat_once()** (3 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **Initialize chat service.** (1 connections) — `server/container/bundles/chat.py`
- **Subscribe once so NPCSpoke publishes become room chat lines.** (1 connections) — `server/game/chat_npc_system.py`
- **Wire ChatService once at app startup (optional for unit tests).** (1 connections) — `server/game/chat_npc_system.py`
- **NPCSpoke bridge schedules say-shaped room speech; skips whisper.** (1 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **NPCSpoke subscription is one-shot.** (1 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **Create NATSSubjectManager instance.** (1 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`

## Relationships

- [test_chat_npc_system.py](test_chat_npc_system.py.md) (10 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (5 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [test_manager.py](test_manager.py.md) (2 shared connections)
- [ChatService](ChatService.md) (1 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (1 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (1 shared connections)

## Source Files

- `server/container/bundles/chat.py`
- `server/game/chat_npc_system.py`
- `server/tests/unit/game/test_chat_npc_system.py`
- `server/tests/unit/services/nats_subject_manager/test_manager.py`

## Audit Trail

- EXTRACTED: 28 (85%)
- INFERRED: 5 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*