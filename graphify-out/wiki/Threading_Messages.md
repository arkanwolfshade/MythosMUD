# Threading Messages

> 20 nodes

## Key Concepts

- **threading_messages.py** (11 connections) — `server/npc/threading_messages.py`
- **NPCActionMessage** (10 connections) — `server/npc/threading_messages.py`
- **.from_dict()** (8 connections) — `server/npc/threading_messages.py`
- **NPCActionType** (6 connections) — `server/npc/threading_messages.py`
- **.from_json()** (4 connections) — `server/npc/threading_messages.py`
- **.to_dict()** (3 connections) — `server/npc/threading_messages.py`
- **.to_json()** (3 connections) — `server/npc/threading_messages.py`
- **test_npc_action_message_json_round_trip()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_npc_action_message_round_trip()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **_float_field()** (2 connections) — `server/npc/threading_messages.py`
- **_optional_int_field()** (2 connections) — `server/npc/threading_messages.py`
- **_optional_str_field()** (2 connections) — `server/npc/threading_messages.py`
- **test_npc_action_message_to_dict_uses_enum_value()** (2 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **Enum** (2 connections)
- **Convert message to JSON string.** (1 connections) — `server/npc/threading_messages.py`
- **Create message from JSON string.** (1 connections) — `server/npc/threading_messages.py`
- **Enumeration of NPC action types.** (1 connections) — `server/npc/threading_messages.py`
- **Message structure for NPC actions. This class represents a single action that…** (1 connections) — `server/npc/threading_messages.py`
- **Convert message to dictionary for serialization.** (1 connections) — `server/npc/threading_messages.py`
- **Create message from dictionary.** (1 connections) — `server/npc/threading_messages.py`

## Relationships

- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (6 shared connections)
- [Test Npc Threading Messages](Test_Npc_Threading_Messages.md) (4 shared connections)
- [Test Npc Thread Manager Internals](Test_Npc_Thread_Manager_Internals.md) (1 shared connections)

## Source Files

- `server/npc/threading_messages.py`
- `server/tests/unit/npc/test_npc_threading_messages.py`

## Audit Trail

- EXTRACTED: 35 (90%)
- INFERRED: 4 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*