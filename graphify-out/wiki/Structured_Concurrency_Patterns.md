# Structured Concurrency Patterns

> 13 nodes

## Key Concepts

- **NPCActionMessage** (12 connections) — `server/npc/threading.py`
- **NPCActionType** (8 connections) — `server/npc/threading.py`
- **.from_dict()** (5 connections) — `server/npc/threading.py`
- **.to_dict()** (4 connections) — `server/npc/threading.py`
- **.to_json()** (3 connections) — `server/npc/threading.py`
- **.from_json()** (3 connections) — `server/npc/threading.py`
- **Enum** (2 connections)
- **Enumeration of NPC action types.** (1 connections) — `server/npc/threading.py`
- **Message structure for NPC actions.      This class represents a single action th** (1 connections) — `server/npc/threading.py`
- **Convert message to dictionary for serialization.** (1 connections) — `server/npc/threading.py`
- **Create message from dictionary.** (1 connections) — `server/npc/threading.py`
- **Convert message to JSON string.** (1 connections) — `server/npc/threading.py`
- **Create message from JSON string.** (1 connections) — `server/npc/threading.py`

## Relationships

- [Client Event Store](Client_Event_Store.md) (9 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (4 shared connections)
- [NPC Movement Integration](NPC_Movement_Integration.md) (2 shared connections)

## Source Files

- `server/npc/threading.py`

## Audit Trail

- EXTRACTED: 39 (91%)
- INFERRED: 4 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*