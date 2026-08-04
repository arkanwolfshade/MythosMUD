# npc behavior engine

> 28 nodes

## Key Concepts

- **NPCActionMessage** (16 connections) — `server/npc/threading.py`
- **NPCActionType** (9 connections) — `server/npc/threading.py`
- **.wander()** (6 connections) — `server/npc/passive_mob_npc.py`
- **.schedule_idle_movement()** (6 connections) — `server/npc/passive_mob_npc.py`
- **.from_dict()** (6 connections) — `server/npc/threading.py`
- **._queue_wander_action()** (5 connections) — `server/npc/passive_mob_npc.py`
- **._create_wander_action()** (4 connections) — `server/npc/passive_mob_npc.py`
- **.to_dict()** (4 connections) — `server/npc/threading.py`
- **.from_json()** (4 connections) — `server/npc/threading.py`
- **._should_schedule_movement()** (3 connections) — `server/npc/passive_mob_npc.py`
- **._handle_wander()** (3 connections) — `server/npc/passive_mob_npc.py`
- **.to_json()** (3 connections) — `server/npc/threading.py`
- **test_npc_action_message_round_trip()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_npc_action_message_json_round_trip()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **Enum** (2 connections)
- **test_npc_action_message_to_dict_uses_enum_value()** (2 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **Perform wandering behavior using idle movement system.** (1 connections) — `server/npc/passive_mob_npc.py`
- **Check if idle movement should be scheduled based on configuration and timing.** (1 connections) — `server/npc/passive_mob_npc.py`
- **Create a WANDER action message.          Args:             current_time: Curr** (1 connections) — `server/npc/passive_mob_npc.py`
- **Queue a WANDER action via the thread manager.          Args:             wand** (1 connections) — `server/npc/passive_mob_npc.py`
- **Schedule a WANDER action for idle movement if interval has elapsed.          T** (1 connections) — `server/npc/passive_mob_npc.py`
- **Handle wandering action.** (1 connections) — `server/npc/passive_mob_npc.py`
- **Enumeration of NPC action types.** (1 connections) — `server/npc/threading.py`
- **Message structure for NPC actions.      This class represents a single action th** (1 connections) — `server/npc/threading.py`
- **Convert message to dictionary for serialization.** (1 connections) — `server/npc/threading.py`
- *... and 3 more nodes in this community*

## Relationships

- [command input commands](command_input_commands.md) (10 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (5 shared connections)
- [idle movement npc](idle_movement_npc.md) (3 shared connections)
- [NPC Combat](NPC_Combat.md) (3 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (2 shared connections)
- [idle npc movement](idle_npc_movement.md) (2 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [logging setup structured](logging_setup_structured.md) (1 shared connections)

## Source Files

- `server/npc/passive_mob_npc.py`
- `server/npc/threading.py`
- `server/tests/unit/npc/test_npc_threading_messages.py`

## Audit Trail

- EXTRACTED: 87 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*