# NPCActionMessage

> 13 nodes

## Key Concepts

- **NPCActionMessage** (16 connections) — `server/npc/threading.py`
- **.from_dict()** (6 connections) — `server/npc/threading.py`
- **.from_json()** (4 connections) — `server/npc/threading.py`
- **.to_dict()** (4 connections) — `server/npc/threading.py`
- **.to_json()** (3 connections) — `server/npc/threading.py`
- **test_npc_action_message_json_round_trip()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_npc_action_message_round_trip()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_npc_action_message_to_dict_uses_enum_value()** (2 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **Message structure for NPC actions. This class represents a single action that…** (1 connections) — `server/npc/threading.py`
- **Convert message to dictionary for serialization.** (1 connections) — `server/npc/threading.py`
- **Create message from dictionary.** (1 connections) — `server/npc/threading.py`
- **Convert message to JSON string.** (1 connections) — `server/npc/threading.py`
- **Create message from JSON string.** (1 connections) — `server/npc/threading.py`

## Relationships

- [NPCThreadManager](NPCThreadManager.md) (6 shared connections)
- [PassiveMobNPC](PassiveMobNPC.md) (3 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [IdleMovementHandler](IdleMovementHandler.md) (1 shared connections)

## Source Files

- `server/npc/threading.py`
- `server/tests/unit/npc/test_npc_threading_messages.py`

## Audit Trail

- EXTRACTED: 28 (93%)
- INFERRED: 2 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*