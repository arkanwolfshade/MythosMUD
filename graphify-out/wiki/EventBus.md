# EventBus

> God node · 203 connections · `server/events/event_bus.py`

**Community:** [[Distributed Event Bus]]

## Connections by Relation

### calls
- [[._publish_player_dp_correction_event()]] `EXTRACTED`
- [[._publish_player_dp_update_event()]] `EXTRACTED`
- [[integration()]] `EXTRACTED`
- [[event_bus()]] `EXTRACTED`
- [[event_bus()]] `EXTRACTED`

### contains
- [[event_bus.py]] `EXTRACTED`

### imports
- [[async_persistence.py]] `EXTRACTED`
- [[combat_service.py]] `EXTRACTED`
- [[test_population_control.py]] `EXTRACTED`
- [[test_npc_instance_service.py]] `EXTRACTED`
- [[test_event_bus.py]] `EXTRACTED`
- [[npc_combat_integration_service.py]] `EXTRACTED`
- [[lifecycle_manager.py]] `EXTRACTED`
- [[npc_base.py]] `EXTRACTED`
- [[event_handler.py]] `EXTRACTED`
- [[population_control.py]] `EXTRACTED`
- [[combat_handler.py]] `EXTRACTED`
- [[movement_service.py]] `EXTRACTED`
- [[event_reaction_system.py]] `EXTRACTED`
- [[spawning_service.py]] `EXTRACTED`
- [[room.py]] `EXTRACTED`
- [[npc_instance_service.py]] `EXTRACTED`
- [[test_npc_combat_integration_class.py]] `EXTRACTED`
- [[combat_integration_base.py]] `EXTRACTED`
- [[combat_loader.py]] `EXTRACTED`
- [[lifecycle_death.py]] `EXTRACTED`

### method
- [[._handle_event_async()]] `EXTRACTED`
- [[._stop_processing()]] `EXTRACTED`
- [[._create_async_subscriber_tasks()]] `EXTRACTED`
- [[._ensure_async_processing()]] `EXTRACTED`
- [[.inject()]] `EXTRACTED`
- [[._process_sync_subscribers()]] `EXTRACTED`
- [[.publish()]] `EXTRACTED`
- [[._separate_subscribers()]] `EXTRACTED`
- [[.unsubscribe()]] `EXTRACTED`
- [[._wait_for_async_subscribers()]] `EXTRACTED`
- [[.get_subscriber_stats()]] `EXTRACTED`
- [[._handle_task_result_async()]] `EXTRACTED`
- [[._process_events_async()]] `EXTRACTED`
- [[.shutdown()]] `EXTRACTED`
- [[.subscribe()]] `EXTRACTED`
- [[.unsubscribe_all_for_service()]] `EXTRACTED`
- [[._cancel_and_wait_for_active_tasks()]] `EXTRACTED`
- [[._cancel_processing_task()]] `EXTRACTED`
- [[._ensure_processing_started()]] `EXTRACTED`
- [[._finalize_shutdown()]] `EXTRACTED`

### rationale_for
- [[Pure asyncio event bus for MythosMUD.      This class provides a purely async pu]] `EXTRACTED`

### uses
- [[CombatService]] `INFERRED`
- [[NPCPopulationController]] `INFERRED`
- [[NPCLifecycleManager]] `INFERRED`
- [[BaseEvent]] `INFERRED`
- [[NPCSpawningService]] `INFERRED`
- [[CombatCommandHandler]] `INFERRED`
- [[UUID]] `INFERRED`
- [[FollowService]] `INFERRED`
- [[PartyService]] `INFERRED`
- [[CombatInstance]] `INFERRED`
- [[CombatParticipant]] `INFERRED`
- [[CombatCommandHandlerExtras]] `INFERRED`
- [[ZoneConfiguration]] `INFERRED`
- [[CombatResult]] `INFERRED`
- [[NPCInstanceService]] `INFERRED`
- [[PlayerCombatService]] `INFERRED`
- [[NPCDefinition]] `INFERRED`
- [[CombatParticipantData]] `INFERRED`
- [[CombatStartedEvent]] `INFERRED`
- [[EventBus]] `INFERRED`

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
