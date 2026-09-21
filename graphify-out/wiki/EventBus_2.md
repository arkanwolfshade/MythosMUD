# EventBus

> God node · 225 connections · `server/events/event_bus.py`

**Community:** [EventBus](EventBus.md)

## Connections by Relation

### calls
- _make_manager() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- ._publish_player_dp_correction_event() `EXTRACTED`
- test_greeting_respects_the_per_npc_per_event_cooldown() `EXTRACTED`
- test_no_reactions_registered_without_a_reaction_system() `EXTRACTED`
- .__init__() `EXTRACTED`
- ._init_persistence_and_event_bus() `EXTRACTED`
- integration() `EXTRACTED`
- test_greeting_does_not_fire_for_a_different_room() `EXTRACTED`
- test_player_entered_room_triggers_the_npcs_own_greeting() `EXTRACTED`
- test_player_left_room_triggers_the_npcs_own_farewell() `EXTRACTED`
- test_create_npc_instance_threads_event_reaction_system() `EXTRACTED`
- test_spawning_service_npc_room_event_handlers() `EXTRACTED`
- test_spawning_service_threads_event_reaction_system_to_created_npcs() `EXTRACTED`
- .__init__() `EXTRACTED`
- event_bus() `EXTRACTED`
- event_bus() `EXTRACTED`
- event_bus() `EXTRACTED`
- integration() `EXTRACTED`

### contains
- event_bus.py `EXTRACTED`

### imports
- [connection_manager.py](connection_manager.py.md) `EXTRACTED`
- [combat_service.py](combat_service.py.md) `EXTRACTED`
- [async_persistence.py](async_persistence.py.md) `EXTRACTED`
- test_population_control.py `EXTRACTED`
- test_event_bus.py `EXTRACTED`
- npc_combat_integration_service.py `EXTRACTED`
- test_npc_instance_service.py `EXTRACTED`
- lifecycle_manager.py `EXTRACTED`
- combat_handler.py `EXTRACTED`
- test_spawning_modules.py `EXTRACTED`
- test_npc_combat_integration_class.py `EXTRACTED`
- npc_base.py `EXTRACTED`
- population_control.py `EXTRACTED`
- event_handler.py `EXTRACTED`
- models/room.py `EXTRACTED`
- spawning_service.py `EXTRACTED`
- movement_service.py `EXTRACTED`
- memory_monitor.py `EXTRACTED`
- chat_npc_system.py `EXTRACTED`
- event_reaction_system.py `EXTRACTED`

### inherits
- DistributedEventBus `EXTRACTED`
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
- subscribe_npc_spoke_to_chat() `EXTRACTED`
- _shopkeeper() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- lifespan_event_bus() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- ._publish_correction_to_event_bus() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`

### uses
- [CombatService](CombatService.md) `INFERRED`
- BaseEvent `INFERRED`
- FollowService `INFERRED`
- NPCLifecycleManager `INFERRED`
- [NPCSpawningService](NPCSpawningService.md) `INFERRED`
- NPCPopulationController `INFERRED`
- [CombatCommandHandler](CombatCommandHandler.md) `INFERRED`
- [PartyService](PartyService.md) `INFERRED`
- [MythosTickScheduler](MythosTickScheduler.md) `INFERRED`
- NPCInstanceService `INFERRED`
- MythosTimeEventConsumer `INFERRED`
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