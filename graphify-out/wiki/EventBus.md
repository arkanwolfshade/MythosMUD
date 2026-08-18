# EventBus

> God node · 207 connections · `server/events/event_bus.py`

**Community:** [moduletype](moduletype.md)

## Connections by Relation

### calls
- _make_manager() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- ._publish_player_dp_correction_event() `EXTRACTED`
- ._publish_player_dp_update_event() `EXTRACTED`
- ._init_persistence_and_event_bus() `EXTRACTED`
- integration() `EXTRACTED`
- test_spawning_service_npc_room_event_handlers() `EXTRACTED`
- .__init__() `EXTRACTED`
- event_bus() `EXTRACTED`
- event_bus() `EXTRACTED`
- integration() `EXTRACTED`
- test_spawning_service_handle_player_entered_room() `EXTRACTED`
- test_spawning_service_maybe_add_required_npc_request() `EXTRACTED`
- test_spawning_service_process_spawn_queue_with_request() `EXTRACTED`
- test_spawning_service_queue_and_stats() `EXTRACTED`
- test_del_warns_when_running() `EXTRACTED`
- test_create_npc_instance_passive() `EXTRACTED`
- test_create_npc_instance_unknown_type() `EXTRACTED`

### contains
- event_bus.py `EXTRACTED`

### imports
- connection_manager.py `EXTRACTED`
- combat_service.py `EXTRACTED`
- async_persistence.py `EXTRACTED`
- test_population_control.py `EXTRACTED`
- test_event_bus.py `EXTRACTED`
- test_npc_instance_service.py `EXTRACTED`
- npc_combat_integration_service.py `EXTRACTED`
- lifecycle_manager.py `EXTRACTED`
- combat_handler.py `EXTRACTED`
- test_npc_combat_integration_class.py `EXTRACTED`
- npc_base.py `EXTRACTED`
- population_control.py `EXTRACTED`
- test_spawning_modules.py `EXTRACTED`
- spawning_service.py `EXTRACTED`
- memory_monitor.py `EXTRACTED`
- event_handler.py `EXTRACTED`
- movement_service.py `EXTRACTED`
- chat_npc_system.py `EXTRACTED`
- models/room.py `EXTRACTED`
- npc_instance_service.py `EXTRACTED`

### inherits
- DistributedEventBus `EXTRACTED`

### method
- ._handle_event_async() `EXTRACTED`
- ._stop_processing() `EXTRACTED`
- ._ensure_async_processing() `EXTRACTED`
- ._cancel_task_quietly() `EXTRACTED`
- ._abandon_pending_tasks() `EXTRACTED`
- ._cancel_and_wait_for_active_tasks() `EXTRACTED`
- ._create_async_subscriber_tasks() `EXTRACTED`
- ._process_events_async() `EXTRACTED`
- ._separate_subscribers() `EXTRACTED`
- ._process_sync_subscribers() `EXTRACTED`
- ._wait_for_async_subscribers() `EXTRACTED`
- .publish() `EXTRACTED`
- .inject() `EXTRACTED`
- .unsubscribe() `EXTRACTED`
- .unsubscribe_all_for_service() `EXTRACTED`
- .get_subscriber_stats() `EXTRACTED`
- .shutdown() `EXTRACTED`
- .set_main_loop() `EXTRACTED`
- ._ensure_processing_started() `EXTRACTED`
- ._signal_shutdown() `EXTRACTED`

### rationale_for
- Pure asyncio event bus for MythosMUD. This class provides a purely async… `EXTRACTED`

### references
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .event_bus() `EXTRACTED`
- .__init__() `EXTRACTED`
- subscribe_npc_spoke_to_chat() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- lifespan_event_bus() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`

### uses
- CombatService `INFERRED`
- BaseEvent `INFERRED`
- NPCLifecycleManager `INFERRED`
- NPCSpawningService `INFERRED`
- NPCPopulationController `INFERRED`
- CombatCommandHandler `INFERRED`
- FollowService `INFERRED`
- PartyService `INFERRED`
- MythosTickScheduler `INFERRED`
- MythosTimeEventConsumer `INFERRED`
- NPCInstanceService `INFERRED`
- create_npc_instance() `INFERRED`
- initialize_npc_instance_service() `INFERRED`
- _LifecycleManagerForDeath `INFERRED`
- _instantiate_by_type() `INFERRED`
- _build_aggressive() `INFERRED`
- _build_passive() `INFERRED`
- _build_shopkeeper() `INFERRED`
- test_handle_event_async_async_subscriber_error() `INFERRED`
- test_handle_event_async_sync_subscriber_error() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*