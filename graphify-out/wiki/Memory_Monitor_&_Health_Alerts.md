# Memory Monitor & Health Alerts

> 461 nodes

## Key Concepts

- **enhanced_logging_config.py** (507 connections) — `server/structured_logging/enhanced_logging_config.py`
- **get_logger()** (463 connections) — `server/structured_logging/enhanced_logging_config.py`
- **connection_manager.py** (129 connections) — `server/realtime/connection_manager.py`
- **time.py** (106 connections) — `server/container/bundles/time.py`
- **connection_manager_methods.py** (95 connections) — `server/realtime/connection_manager_methods.py`
- **asyncio.md** (58 connections) — `.claude/rules/asyncio.md`
- **RoomSubscriptionManager** (48 connections) — `server/realtime/room_subscription_manager.py`
- **threading.py** (45 connections) — `server/npc/threading.py`
- **connection_establishment.py** (42 connections) — `server/realtime/connection_establishment.py`
- **MemoryMonitor** (39 connections) — `server/realtime/memory_monitor.py`
- **nats_message_handler.py** (36 connections) — `server/realtime/nats_message_handler.py`
- **test_memory_monitor.py** (36 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **memory_monitor.py** (33 connections) — `server/realtime/memory_monitor.py`
- **ConnectionMetadata** (30 connections) — `server/realtime/connection_models.py`
- **test_hallucination_services.py** (27 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **connection_initialization.py** (26 connections) — `server/realtime/connection_initialization.py`
- **connection_session_management.py** (26 connections) — `server/realtime/connection_session_management.py`
- **statistics_aggregator.py** (26 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **schedule_service.py** (26 connections) — `server/services/schedule_service.py`
- **PerformanceTracker** (24 connections) — `server/realtime/monitoring/performance_tracker.py`
- **event_handlers.py** (24 connections) — `server/realtime/event_handlers.py`
- **nats_message_handler_processing.py** (24 connections) — `server/realtime/nats_message_handler_processing.py`
- **connection_cleaner.py** (23 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **connection_helpers.py** (22 connections) — `server/realtime/connection_helpers.py`
- **room_subscription_manager.py** (21 connections) — `server/realtime/room_subscription_manager.py`
- *... and 436 more nodes in this community*

## Relationships

- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (63 shared connections)
- [Connection Manager Methods](Connection_Manager_Methods.md) (53 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (43 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (36 shared connections)
- [NATS Messaging Config](NATS_Messaging_Config.md) (30 shared connections)
- [NPC Combat Integration](NPC_Combat_Integration.md) (29 shared connections)
- [Test Connection Disconnection](Test_Connection_Disconnection.md) (21 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (21 shared connections)
- [Chat Service & Channels](Chat_Service_&_Channels.md) (21 shared connections)
- [Room Subscription Manager](Room_Subscription_Manager.md) (20 shared connections)
- [Test Envelope](Test_Envelope.md) (20 shared connections)
- [Test Hallucination Services](Test_Hallucination_Services.md) (20 shared connections)

## Source Files

- `.claude/rules/asyncio.md`
- `monitoring/webhook-receiver.py`
- `scripts/run_test_ci.py`
- `server/app/tracked_task_manager.py`
- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/commands/container_helpers_inventory_logging.py`
- `server/commands/shutdown_process_termination.py`
- `server/config/models/_helpers.py`
- `server/config/models/nats.py`
- `server/container/bundles/time.py`
- `server/events/distributed_event_bus.py`
- `server/events/event_bus_lifecycle.py`
- `server/events/nats_event_bridge.py`
- `server/game/chat_moderation.py`
- `server/game/chat_pose_manager.py`
- `server/game/chat_whisper_tracker.py`
- `server/game/level_service.py`
- `server/game/mechanics.py`
- `server/game/player_search_service.py`

## Audit Trail

- EXTRACTED: 2693 (98%)
- INFERRED: 43 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*