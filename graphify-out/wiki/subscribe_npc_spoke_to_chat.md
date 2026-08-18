# subscribe_npc_spoke_to_chat

> 8 nodes

## Key Concepts

- **subscribe_npc_spoke_to_chat()** (9 connections) — `server/game/chat_npc_system.py`
- **.initialize()** (7 connections) — `server/container/bundles/chat.py`
- **test_npc_spoke_handler_schedules_room_speech()** (4 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **test_subscribe_npc_spoke_to_chat_once()** (3 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **Initialize chat service.** (1 connections) — `server/container/bundles/chat.py`
- **Subscribe once so NPCSpoke publishes become room chat lines.** (1 connections) — `server/game/chat_npc_system.py`
- **NPCSpoke bridge schedules say-shaped room speech; skips whisper.** (1 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **NPCSpoke subscription is one-shot.** (1 connections) — `server/tests/unit/game/test_chat_npc_system.py`

## Relationships

- [test_chat_npc_system.py](test_chat_npc_system.py.md) (6 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [ChatService](ChatService.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [test_manager.py](test_manager.py.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)

## Source Files

- `server/container/bundles/chat.py`
- `server/game/chat_npc_system.py`
- `server/tests/unit/game/test_chat_npc_system.py`

## Audit Trail

- EXTRACTED: 18 (90%)
- INFERRED: 2 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*