# EventBus

> God node · 208 connections · `server/events/event_bus.py`

**Community:** [NPCLifecycleManager](NPCLifecycleManager.md)

## Connections by Relation

### calls
- _make_manager() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- ._init_persistence_and_event_bus() `EXTRACTED`
- integration() `EXTRACTED`
- test_spawning_service_npc_room_event_handlers() `EXTRACTED`
- .__init__() `EXTRACTED`
- ._publish_player_dp_correction_event() `EXTRACTED`
- event_bus() `EXTRACTED`
- event_bus() `EXTRACTED`
- event_bus() `EXTRACTED`
- integration() `EXTRACTED`
- test_spawning_service_handle_player_entered_room() `EXTRACTED`
- test_spawning_service_maybe_add_required_npc_request() `EXTRACTED`
- test_spawning_service_process_spawn_queue_with_request() `EXTRACTED`
- test_spawning_service_queue_and_stats() `EXTRACTED`
- test_create_npc_instance_passive() `EXTRACTED`
- test_create_npc_instance_unknown_type() `EXTRACTED`
- test_spawning_service_calculate_priority_required() `EXTRACTED`

### contains
- event_bus.py `EXTRACTED`

### imports
- [connection_manager.py](connection_manager.py.md) `EXTRACTED`
- combat_service.py `EXTRACTED`
- [test_population_control.py](test_population_control.py.md) `EXTRACTED`
- test_event_bus.py `EXTRACTED`
- test_npc_instance_service.py `EXTRACTED`
- npc_combat_integration_service.py `EXTRACTED`
- [lifecycle_manager.py](lifecycle_manager.py.md) `EXTRACTED`
- test_npc_combat_integration_class.py `EXTRACTED`
- npc_base.py `EXTRACTED`
- [population_control.py](population_control.py.md) `EXTRACTED`
- test_spawning_modules.py `EXTRACTED`
- spawning_service.py `EXTRACTED`
- combat_handler.py `EXTRACTED`
- event_handler.py `EXTRACTED`
- movement_service.py `EXTRACTED`
- memory_monitor.py `EXTRACTED`
- chat_npc_system.py `EXTRACTED`
- models/room.py `EXTRACTED`
- npc_instance_service.py `EXTRACTED`
- event_reaction_system.py `EXTRACTED`

### inherits
- [DistributedEventBus](DistributedEventBus.md) `EXTRACTED`
- [EventBusLifecycleMixin](EventBusLifecycleMixin.md) `EXTRACTED`
- EventBusProcessingMixin `EXTRACTED`

### method
- .unsubscribe() `EXTRACTED`
- .get_subscriber_stats() `EXTRACTED`
- .set_main_loop() `EXTRACTED`
- .subscribe() `EXTRACTED`
- .get_subscriber_count() `EXTRACTED`
- .get_all_subscriber_counts() `EXTRACTED`
- .get_subscriber_lifecycle_metrics() `EXTRACTED`
- .unsubscribe_all_for_service() `EXTRACTED`
- .__init__() `EXTRACTED`
- ._ensure_processing_started() `EXTRACTED`
- .get_active_task_count() `EXTRACTED`
- .get_queue_depth() `EXTRACTED`
- .get_active_task_details() `EXTRACTED`

### rationale_for
- Pure asyncio event bus for MythosMUD. This class provides a purely async… `EXTRACTED`

### references
- .event_bus() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- subscribe_npc_spoke_to_chat() `EXTRACTED`
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
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`

### uses
- [CombatService](CombatService.md) `INFERRED`
- [NPCLifecycleManager](NPCLifecycleManager.md) `INFERRED`
- [NPCSpawningService](NPCSpawningService.md) `INFERRED`
- NPCPopulationController `INFERRED`
- [CombatCommandHandler](CombatCommandHandler.md) `INFERRED`
- FollowService `INFERRED`
- [PartyService](PartyService.md) `INFERRED`
- [MythosTickScheduler](MythosTickScheduler.md) `INFERRED`
- NPCInstanceService `INFERRED`
- MythosTimeEventConsumer `INFERRED`
- create_npc_instance() `INFERRED`
- _LifecycleManagerForDeath `INFERRED`
- _instantiate_by_type() `INFERRED`
- initialize_npc_instance_service() `INFERRED`
- _build_aggressive() `INFERRED`
- _build_passive() `INFERRED`
- _build_shopkeeper() `INFERRED`
- party_events() `INFERRED`
- party_service() `INFERRED`
- test_event_bus_inject_dispatches_to_subscribers() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*