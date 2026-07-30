# parse jsonb column()

> 247 nodes

## Key Concepts

- **NPCLifecycleManager** (76 connections) — `server/npc/lifecycle_manager.py`
- **lifecycle_manager.py** (48 connections) — `server/npc/lifecycle_manager.py`
- **ScheduleEntry** (28 connections) — `server/schemas/calendar/calendar.py`
- **ScheduleService** (28 connections) — `server/services/schedule_service.py`
- **NPCDied** (25 connections) — `server/events/event_types.py`
- **schedule_service.py** (25 connections) — `server/services/schedule_service.py`
- **time_event_consumer.py** (24 connections) — `server/time/time_event_consumer.py`
- **lifecycle_death.py** (23 connections) — `server/npc/lifecycle_death.py`
- **NPCThreadManager** (22 connections) — `server/npc/threading.py`
- **MythosTimeEventConsumer** (21 connections) — `server/time/time_event_consumer.py`
- **player_combat_service_support.py** (19 connections) — `server/services/player_combat_service_support.py`
- **_SpawnTrackedNPC** (17 connections) — `server/npc/lifecycle_manager.py`
- **NPCLifecycleRecord** (17 connections) — `server/npc/lifecycle_types.py`
- **_LifecycleManagerForDeath** (16 connections) — `server/npc/lifecycle_death.py`
- **_SpawningServiceProtocol** (16 connections) — `server/npc/lifecycle_manager.py`
- **RoomOccupantsRefreshRequested** (14 connections) — `server/events/event_types.py`
- **._spawn_npc_impl()** (14 connections) — `server/npc/lifecycle_manager.py`
- **TestScheduleService** (14 connections) — `server/tests/unit/services/test_schedule_service.py`
- **ChronicleLike** (13 connections) — `server/time/time_service.py`
- **MythosHourTickEvent** (12 connections) — `server/events/event_types.py`
- **lifecycle_types.py** (12 connections) — `server/npc/lifecycle_types.py`
- **NPCLifecycleState** (12 connections) — `server/npc/lifecycle_types.py`
- **NPCLifecycleEvent** (11 connections) — `server/npc/lifecycle_types.py`
- **lifecycle_despawn.py** (10 connections) — `server/npc/lifecycle_despawn.py`
- **handle_npc_died_impl()** (8 connections) — `server/npc/lifecycle_death.py`
- *... and 222 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (82 shared connections)
- [get current tick()](get_current_tick%28%29.md) (18 shared connections)
- [CombatService](CombatService.md) (17 shared connections)
- [HolidayCollection](HolidayCollection.md) (17 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (14 shared connections)
- [world](world.md) (14 shared connections)
- [test command parser](test_command_parser.md) (11 shared connections)
- [. init ()](_init_%28%29.md) (9 shared connections)
- [Test check all command blocks](Test_check_all_command_blocks.md) (9 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (9 shared connections)
- [movement monitor](movement_monitor.md) (6 shared connections)
- [Any](Any.md) (5 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/models/room.py`
- `server/npc/lifecycle_death.py`
- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/threading.py`
- `server/schemas/calendar/calendar.py`
- `server/services/player_combat_service_support.py`
- `server/services/schedule_service.py`
- `server/tests/unit/services/test_npc_instance_service.py`
- `server/tests/unit/services/test_schedule_service.py`
- `server/time/time_event_consumer.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 924 (88%)
- INFERRED: 132 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*