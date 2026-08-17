# NPCActionMessage

> 28 nodes

## Key Concepts

- **NPCActionMessage** (15 connections) — `server/npc/threading.py`
- **NPCActionType** (11 connections) — `server/npc/threading.py`
- **.schedule_idle_movement()** (6 connections) — `server/npc/passive_mob_npc.py`
- **.wander()** (6 connections) — `server/npc/passive_mob_npc.py`
- **.from_dict()** (6 connections) — `server/npc/threading.py`
- **._queue_wander_action()** (5 connections) — `server/npc/passive_mob_npc.py`
- **._create_wander_action()** (4 connections) — `server/npc/passive_mob_npc.py`
- **.from_json()** (4 connections) — `server/npc/threading.py`
- **.to_dict()** (4 connections) — `server/npc/threading.py`
- **test_npc_action_message_json_round_trip()** (4 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_npc_action_message_round_trip()** (4 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **._handle_wander()** (3 connections) — `server/npc/passive_mob_npc.py`
- **._should_schedule_movement()** (3 connections) — `server/npc/passive_mob_npc.py`
- **.to_json()** (3 connections) — `server/npc/threading.py`
- **test_npc_action_message_to_dict_uses_enum_value()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **Enum** (2 connections)
- **Check if idle movement should be scheduled based on configuration and timing.…** (1 connections) — `server/npc/passive_mob_npc.py`
- **Create a WANDER action message. Args: current_time: Current timestamp Returns:…** (1 connections) — `server/npc/passive_mob_npc.py`
- **Queue a WANDER action via the thread manager. Args: wander_action: The wander…** (1 connections) — `server/npc/passive_mob_npc.py`
- **Schedule a WANDER action for idle movement if interval has elapsed. This method…** (1 connections) — `server/npc/passive_mob_npc.py`
- **Handle wandering action.** (1 connections) — `server/npc/passive_mob_npc.py`
- **Perform wandering behavior using idle movement system.** (1 connections) — `server/npc/passive_mob_npc.py`
- **Enumeration of NPC action types.** (1 connections) — `server/npc/threading.py`
- **Message structure for NPC actions. This class represents a single action that…** (1 connections) — `server/npc/threading.py`
- **Convert message to dictionary for serialization.** (1 connections) — `server/npc/threading.py`
- *... and 3 more nodes in this community*

## Relationships

- [PassiveMobNPC](PassiveMobNPC.md) (8 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (7 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [NPCDefinition](NPCDefinition.md) (2 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (1 shared connections)
- [NPCStartupService](NPCStartupService.md) (1 shared connections)
- [IdleMovementHandler](IdleMovementHandler.md) (1 shared connections)

## Source Files

- `server/npc/passive_mob_npc.py`
- `server/npc/threading.py`
- `server/tests/unit/npc/test_npc_threading_messages.py`

## Audit Trail

- EXTRACTED: 52 (87%)
- INFERRED: 8 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*