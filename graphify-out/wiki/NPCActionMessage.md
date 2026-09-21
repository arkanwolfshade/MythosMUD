# NPCActionMessage

> 28 nodes

## Key Concepts

- **NPCActionMessage** (12 connections) — `server/npc/threading_messages.py`
- **.from_dict()** (8 connections) — `server/npc/threading_messages.py`
- **.wander()** (7 connections) — `server/npc/passive_mob_npc.py`
- **.schedule_idle_movement()** (6 connections) — `server/npc/passive_mob_npc.py`
- **._queue_wander_action()** (5 connections) — `server/npc/passive_mob_npc.py`
- **._create_wander_action()** (4 connections) — `server/npc/passive_mob_npc.py`
- **.from_json()** (4 connections) — `server/npc/threading_messages.py`
- **._handle_wander()** (3 connections) — `server/npc/passive_mob_npc.py`
- **._should_schedule_movement()** (3 connections) — `server/npc/passive_mob_npc.py`
- **.to_dict()** (3 connections) — `server/npc/threading_messages.py`
- **.to_json()** (3 connections) — `server/npc/threading_messages.py`
- **test_npc_action_message_json_round_trip()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_npc_action_message_round_trip()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **_float_field()** (2 connections) — `server/npc/threading_messages.py`
- **_optional_int_field()** (2 connections) — `server/npc/threading_messages.py`
- **_optional_str_field()** (2 connections) — `server/npc/threading_messages.py`
- **test_npc_action_message_to_dict_uses_enum_value()** (2 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **Check if idle movement should be scheduled based on configuration and timing.…** (1 connections) — `server/npc/passive_mob_npc.py`
- **Create a WANDER action message. Args: current_time: Current timestamp Returns:…** (1 connections) — `server/npc/passive_mob_npc.py`
- **Queue a WANDER action via the thread manager. Args: wander_action: The wander…** (1 connections) — `server/npc/passive_mob_npc.py`
- **Schedule a WANDER action for idle movement if interval has elapsed. This method…** (1 connections) — `server/npc/passive_mob_npc.py`
- **Handle wandering action.** (1 connections) — `server/npc/passive_mob_npc.py`
- **Perform wandering behavior using idle movement system.** (1 connections) — `server/npc/passive_mob_npc.py`
- **Convert message to JSON string.** (1 connections) — `server/npc/threading_messages.py`
- **Create message from JSON string.** (1 connections) — `server/npc/threading_messages.py`
- *... and 3 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (6 shared connections)
- [PassiveMobNPC](PassiveMobNPC.md) (6 shared connections)
- [test_npc_threading_messages.py](test_npc_threading_messages.py.md) (3 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [IdleMovementHandler](IdleMovementHandler.md) (1 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)

## Source Files

- `server/npc/passive_mob_npc.py`
- `server/npc/threading_messages.py`
- `server/tests/unit/npc/test_npc_threading_messages.py`

## Audit Trail

- EXTRACTED: 47 (92%)
- INFERRED: 4 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*