# dependencies

> 32 nodes · cohesion 0.08

## Key Concepts

- **NPCActionMessage** (12 connections) — `server/npc/threading_messages.py`
- **threading_messages.py** (11 connections) — `server/npc/threading_messages.py`
- **.from_dict()** (8 connections) — `server/npc/threading_messages.py`
- **.schedule_idle_movement()** (6 connections) — `server/npc/passive_mob_npc.py`
- **.wander()** (6 connections) — `server/npc/passive_mob_npc.py`
- **NPCActionType** (6 connections) — `server/npc/threading_messages.py`
- **._queue_wander_action()** (5 connections) — `server/npc/passive_mob_npc.py`
- **.from_json()** (5 connections) — `server/npc/threading_messages.py`
- **._create_wander_action()** (4 connections) — `server/npc/passive_mob_npc.py`
- **._handle_wander()** (3 connections) — `server/npc/passive_mob_npc.py`
- **._should_schedule_movement()** (3 connections) — `server/npc/passive_mob_npc.py`
- **.to_dict()** (3 connections) — `server/npc/threading_messages.py`
- **.to_json()** (3 connections) — `server/npc/threading_messages.py`
- **test_npc_action_message_json_round_trip()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_npc_action_message_round_trip()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **_float_field()** (2 connections) — `server/npc/threading_messages.py`
- **_optional_int_field()** (2 connections) — `server/npc/threading_messages.py`
- **_optional_str_field()** (2 connections) — `server/npc/threading_messages.py`
- **Enum** (2 connections)
- **test_npc_action_message_to_dict_uses_enum_value()** (2 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **Check if idle movement should be scheduled based on configuration and timing.…** (1 connections) — `server/npc/passive_mob_npc.py`
- **Create a WANDER action message. Args: current_time: Current timestamp Returns:…** (1 connections) — `server/npc/passive_mob_npc.py`
- **Queue a WANDER action via the thread manager. Args: wander_action: The wander…** (1 connections) — `server/npc/passive_mob_npc.py`
- **Schedule a WANDER action for idle movement if interval has elapsed. This method…** (1 connections) — `server/npc/passive_mob_npc.py`
- **Handle wandering action.** (1 connections) — `server/npc/passive_mob_npc.py`
- *... and 7 more nodes in this community*

## Relationships

- [executeCommand](executeCommand.md) (6 shared connections)
- [Room](Room.md) (5 shared connections)
- [StatisticsAggregator](StatisticsAggregator.md) (4 shared connections)
- [command_parser.py](command_parser.py.md) (1 shared connections)
- [websocket_integration.py](websocket_integration.py.md) (1 shared connections)
- [admin_setstat_command.py](admin_setstat_command.py.md) (1 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (1 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (1 shared connections)

## Source Files

- `server/npc/passive_mob_npc.py`
- `server/npc/threading_messages.py`
- `server/tests/unit/npc/test_npc_threading_messages.py`

## Audit Trail

- EXTRACTED: 57 (92%)
- INFERRED: 5 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*